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

```
# Load `easyDict.py`
execfile('easyDict.py')

# Create dictionary from tab or comma delimited data
mtc = easyDict("data.csv", sep=",", subset=[1, 3]), display=False)
```
