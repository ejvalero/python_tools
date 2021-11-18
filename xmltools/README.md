# XMLTools

Small package for easy management of elements and subelements contained in xml files.


## Available functions

### `setElementFromLine`:
- __Parameters__: 
    - `filename`: (*string*). Name of the input xml file. 
    - `parent`(*string*). Parent node containing text whose items are separated with line break. 
    - `nodename`(string). Name of the node to be assigned to each line of text contained inside `parent`.
- __Description__: function that looks for all elements with `parent` tag, and add inside them as many `nodename` elements as lines have them.
- __Input__: `.xml` file(s) with multi line text in `parent` nodes.
- __Output__: `.xml` file(s) with subnodes `nodename` inside `parent`, replacing multiline text.
- __How to use__: 

    1. Clone or download Python Tools repository. For cloning you can run

    ```sh
    git clone https://github.com/ejvalero/python.git
    ```

    2. Open the terminal and go to the XMLTools directory:

    ```sh
    cd python_tools/XMLTools
    ```

    3. Put all your `.xml` files inside the `xml` directory located in `inputs`.

    4. Run the following:

    ```sh
    python3 processFromXMLdir.py
    ```

    Your output files will be stored in `outputs/setElementFromLine` with the same name of the inputs.


## Python Compatibility

XMLTools is compatible only with Python 3. Python 2 is not supported.