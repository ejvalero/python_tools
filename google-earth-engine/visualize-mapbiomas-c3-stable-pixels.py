import ee
from ee_plugin import Map


"""
0.- User parameters
"""
config = {
    "country": 'Ecuador',
    "classes_ids": [3, 14, 24],               # [] for include all legend classes.
    "regions_ids": [40601, 40602, 40101],     # [] for include the complete country.
    "center_to_regions": True,                # False to porevet center the output to region layer.
    "roi_to_layers": True,                    # False to porevet display roi to the map.
    "mosaics_year": 2015                      # None for prevent display mosaics to the map.
}


"""
1.- select classes from image
"""


def get_classes(image, classes):
    number_of_classes = len(classes)

    try:
        if number_of_classes:
            classes_mask = image.remap(classes, [1] * number_of_classes, 0)
            new_image = image.updateMask(classes_mask.eq(1))

        else:
            new_image = image

        return new_image

    except Exception as e:
        print("SOMETHING WENT WRONG GETTING THE IMAGE OF CLASSES. \n", e)



"""
2.- Clip image by region
"""


def clip_region(image, country, regions, regions_ids):
    number_of_regions = len(regions_ids)

    try:
        main_roi = regions.filter(ee.Filter.eq('pais', country))
        
        if number_of_regions:
            roi = main_roi.filter(
                ee.Filter.inList('id_regionC', regions_ids)
            )

        else:
            roi = main_roi

        return {
            "image": image.clip(roi),
            "roi": roi
        }

    except Exception as e:
        print("SOMETHING WENT WRONG WHEN CLIPPING THE OUTPUT IMAGE. \n", e)



"""
3.- Set up layer names based on custom regions ids
"""


def set_layer_name(ids):
    number_of_regions = len(ids)

    try:
        if number_of_regions:
            str_ids = [str(id) for id in ids]
            str_names = ', '.join(str_ids)
            layer_name = "STABLES FOR REGIONS " + str_names

        else:
            layer_name = "STABLES FOR REGIONS FOR ALL REGIONS"

        return layer_name

    except Exception as e:
        print("SOMETHING WENT WRONG SETTING UP THE LAYER NAME. \n", e)



"""
4.- Get filtered stable pixels and display them to map
"""


def get_stables(_config):
    # configurations    
    country = config["country"]
    regions_ids = config["regions_ids"]
    classes_ids = config["classes_ids"]
    center_to_roi = config["center_to_regions"]
    roi_to_layers = config["roi_to_layers"]
    mosaics_year = config["mosaics_year"]

    # load data    
    image_path = 'projects/mapbiomas-raisg/DATOS_AUXILIARES/RASTERS/stables-3'
    regions_path = 'projects/mapbiomas-raisg/DATOS_AUXILIARES/VECTORES/clasificacion-regiones-3'

    main_image = ee.Image(image_path)
    regions_layer = ee.FeatureCollection(regions_path)
    
    mosaics_path = 'projects/mapbiomas-raisg/MOSAICOS/workspace-c3-v2'
    mosaics = ee.ImageCollection(mosaics_path)

    # getting the output image
    stables = get_classes(main_image, classes_ids)
    clipped = clip_region(stables, country, regions_layer, regions_ids)

    # define stables layer name
    if center_to_roi:
        Map.centerObject(clipped["roi"].geometry(), 10)
    
    # Mosaic visualization based on custom year
    if mosaics_year:
        mosaic = mosaics.filterMetadata('year', 'equals', mosaics_year)
        mosaic = mosaics.mosaic().clip(clipped["roi"])
        
        Map.addLayer(
            mosaic,
            {
                'bands': [
                    'swir1_median',
                    'nir_median',
                    'red_median'
                ],
                'min': 200,
                'max': 5000
            },
            "MOSAIC " + str(mosaics_year),
            True
        )
        
    # Stables pixels visualization
    Map.addLayer(
        clipped["image"],
        {
            'palette':
                [
                    'ffffff', '129912', '1f4423', '006400', '00ff00', '687537',
                    '76a5af', '29eee4', '77a605', '935132', 'bbfcac', '45c2a5',
                    'b8af4f', 'f1c232', 'ffffb2', 'ffd966', 'f6b26b', 'f99f40',
                    'e974ed', 'd5a6bd', 'c27ba0', 'fff3bf', 'ea9999', 'dd7e6b',
                    'aa0000', 'ff99ff', '0000ff', 'd5d5e5', 'dd497f', 'b2ae7c',
                    'ff02eb', '8a2be2', '968c46', '0000ff', '4fd3ff'
                ],
            'min': 0,
            'max': 34
        },
        set_layer_name(regions_ids)
    )
    
    # ROI visualization
    Map.addLayer(
        clipped["roi"].style(color='cyan', fillColor='00000000', width=1.5),
        {},
        'ROI BOUNDARY',
        True if roi_to_layers else False
    )


"""
5.- Run the code
"""


get_stables(config)
