# XMLTagger

Small package for easy management of elements and subelements contained in xml files.

## Available functions
- `setNodeToLine`:
    - Parameters: __filename__(string), __parent__(string), __nodename__(string)
    - Description: for any file with name __filename__, look for all elements with __parent__ tag and add inside them as many __nodename__ elements as lines have them.