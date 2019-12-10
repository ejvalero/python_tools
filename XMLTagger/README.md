# XMLTagger

Small package for easy management of elements and subelements contained in xml files.


## Available functions

### `setNodeToLine`:
- __Parameters__: 
 - `filename`(string) 
 - `parent`(string)
 - `nodename`(string)
- __Description__: for any file with name `filename`, look for all elements with `parent` tag and add inside them as many `nodename` elements as lines have them.
- __Input__: `.xml` files with multi line text in any `parent` node.
- __Output__: `.xml` files with subnodes `nodename` inside `parent`, replacing multiline text.
- __How to use__: 

1. Clone or download Python Tools repository. For cloning you can run

```sh
git clone https://github.com/ejvalero/python.git
```

2. Open the terminal and go to the XMLTagger directory:

```sh
cd XMLTagger
```

3. Put all your `.xml` files inside the `xml` directory located inside `inputs`.

4. Run the following:

```sh
python3 processFromXMLdir.py
```


## Python Compatibility

XMLTager is compatible only with Python 3. Python 2 is not supported.