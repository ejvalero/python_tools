# XMLTagger

Small package for easy management of elements and subelements contained in xml files.

## Available functions

### `setNodeToLine`:
- Parameters: `filename`(string), `parent`(string), `nodename`(string)
- Description: for any file with name `filename`, look for all elements with `parent` tag and add inside them as many `nodename` elements as lines have them.
- Input: `.xml` files with multi line text in any `parent` node.
- Output: `.xml` files with subnodes `nodename` inside `parent`, replacing multiline text.
- How to use: 
    - Create a directory whith name `xml`.
    - Put all `.xml` files inside the directory created before.
    - Open the terminal (command prompt in Windows) and navigate to the root directory of `tagger.py` (`cd path-to-tagger.py-dir`)
    - Run `python3 tagger.py`.