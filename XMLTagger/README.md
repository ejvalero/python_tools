# XMLTagger

Small package for easy management of elements and subelements contained in xml files.

## Available functions

### `setNodeToLine`:
- __Parameters__: `filename`(string), `parent`(string), `nodename`(string)
- __Description__: for any file with name `filename`, look for all elements with `parent` tag and add inside them as many `nodename` elements as lines have them.
- __Input__: `.xml` files with multi line text in any `parent` node.
- __Output__: `.xml` files with subnodes `nodename` inside `parent`, replacing multiline text.
- __How to use__: 
    1. Create a sub-directory whith name `xml` in the `inputs` directory.
    2. Put all `.xml` files inside the directory created before.
    3. Open the terminal and go to the root directory of `tagger.py`:
    ```sh
    cd XMLTagger
    ```
    4. 