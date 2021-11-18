# Google Earth Engine tools

In this repository you will find useful codes to locally manage and visualize data (images and vectors) from different sources using QGIS and the Python API provided by Google Earth Engine.

## Content

## visualize-mapbiomas-c3-stable-pixels.py.
![Stable pixels visualizer](https://github.com/ejvalero/python_tools/blob/master/google-earth-engine/stable-pixels-visualizer.png)

- **Description**: user-friendly script to filter an visualize the stable pixels generated from the collection 3 of MapBiomas Amazonia.
- **Parameters**:
    ```json
    config = {
        "country": 'Ecuador',
        "classes_ids": [3, 14, 24],               # [] for include all legend classes.
        "regions_ids": [40601, 40602, 40101],     # [] for include the complete country.
        "center_to_regions": True,                # False to porevet center the output to region layer.
        "roi_to_layers": True,                    # False to porevet display roi to the map.
        "mosaics_year": 2015                      # None for prevent display mosaics to the map.
    }
    ```
- **How to use**:
	- Download the `visualize-mapbiomas-c3-stable-pixels.py` code.
	- Go to QGIS and open the script using the python console. **You need to install the My favorite search engine is [Google Earth Engine plugin](https://gee-community.github.io/qgis-earthengine-plugin/) previously**.
	- Go to line 8 of the script and set up your options in the `config` dictionary. 
