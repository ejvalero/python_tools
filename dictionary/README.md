##Dictionary

**Description**: easy-and-smart dictionary with interesting display options
**Content**:
- data: directory containing data sets to be used on implementation and examples.
- `easyDict.py`: main Python dictionary function
- `examples.py`: some implementations of `easyDict` applied to datasets in __data__

**Usage**
- Run Python on your computer
- Load `easyDict.py` using `execfile`:
- Create dictionary from tab/comma delimited data

**Example**

```python
# Load `easyDict.py`
execfile('easyDict.py')

# Create dictionary from tab or comma delimited data and display it
mtc = easyDict("data/data.csv", sep=",", display=True)
```
```
Mazda RX4: 21
Pontiac Firebird: 19.2
Ferrari Dino: 19.7
Ford Pantera L: 15.8
Hornet Sportabout: 18.7
Toyota Corolla: 33.9
Lincoln Continental: 10.4
AMC Javelin: 15.2
Chrysler Imperial: 14.7
Merc 280C: 17.8
Maserati Bora: 15
Toyota Corona: 21.5
Hornet 4 Drive: 21.4
Camaro Z28: 13.3
Merc 280: 19.2
Cadillac Fleetwood: 10.4
Fiat X1-9: 27.3
Duster 360: 14.3
Merc 450SLC: 15.2
Lotus Europa: 30.4
Volvo 142E: 21.4
car: mpg
Merc 230: 22.8
Merc 240D: 24.4
Honda Civic: 30.4
Merc 450SE: 16.4
Dodge Challenger: 15.5
Valiant: 18.1
Fiat 128: 32.4
Datsun 710: 22.8
Porsche 914-2: 26
Merc 450SL: 17.3
Mazda RX4 Wag: 21
```
```
# select rows from 2 to 5
mtc = easyDict("data/data.csv", sep=",", subset=[2, 5], display=True)
```

```
Mazda_RX4_Wag: 21
Hornet_4_Drive: 21.4
Datsun_710: 22.8
Mazda_RX4: 21
```
