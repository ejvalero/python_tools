# XMLTagger

Small package for easy management of elements and subelements contained in xml files.

## Available functions

### `setNodeToLine`:
- Parameters: `filename`(string), `parent`(string), `nodename`(string)
- Description: for any file with name `filename`, look for all elements with `parent` tag and add inside them as many `nodename` elements as lines have them.
- Input: `.xml` files with multi line text in any `parent` node.
- Output: `.xml` files with subnodes `nodename` inside `parent`, replacing multiline text.
- How to use: 
    1. Create a directory whith name `xml`.
    2. Put all `.xml` files inside the directory created before.
    3. Open the terminal and go to the root directory of `tagger.py` (`cd path-to-tagger.py-dir`)
    4. Run `python3 tagger.py`.