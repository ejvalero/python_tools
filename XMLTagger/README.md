# XMLTagger

Small package for easy management of elements and subelements contained in xml files.

## Available functions
- `setNodeToLine`:
    - Parameters: `filename`(string), `parent`(string), `nodename`(string)
    - Description: for any file with name `filename`, look for all elements with `parent` tag and add inside them as many `nodename` elements as lines have them.