#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AUTHOR:
    Emanuel Valero - Provita

LATEST UPDATE:
    2019-12-03
"""


import os, io
import xml.etree.ElementTree as ET
from SaveXML import exportXML


def setNodeToLine(
        filename, 
        node   = { "parent": '', "name": ''},
        output = { "folder": None, "name": None }
    ):
        
    # Define structure of input and output directories
    inputfile  = os.path.join('inputs', filename)
    pathfile  = filename.split('/')   ## TODO: implement auto detetc filename


    # Import .xml file and get root of the tree
    tree = ET.parse(inputfile)


    # Find all containers whose tags matches with 'parent' parameter. 
    # Then, for each text line in them, assign node with name equals to 'nodename'
    for child in tree.findall('.//' + node['parent']):

        # Detect and rename existent nodes
        if len(child) > 0:
            childName = child[0].tag
            childrenCount = str( len(child.getchildren()) )
            print( 
                '---',
                'WARNING: ' + childrenCount + ' <'+ childName + '> nodes in "' + 
                pathfile[1] + '" were changed to <' + node['name'] + '>',
                '---'
            )

            for cited in child:
                cited.tag = node['name']

        # Set nodename to each text line inside 'parent'
        childText = child.text

        if childText is not None:
            childText = ' '.join(filter(None, childText.split(' ')))
            childText = childText.replace('\n ', '\n')

            countLines = childText.count('\n')
            lines = childText.split('\n')

            for counter in range( countLines ):
                line = lines[ counter ]
                line = ' '.join(line.split())

                if line is not '':
                    ct = ET.Element(node['name'])
                    ct.text = line
                    child.text = ''
                    child.insert(1, ct)


    # Export xml outputs to root path defined in 'outputDir'
    outdir  = output.get('folder')
    outname = output.get('name')

    if outdir is None:
        outdir = 'XML'

    if outname is None:
        outname = uuid.uuid4().hex + '.xml'

    root = tree.getroot()
    indent(root)

    exportXML(
        tree, outname, outputdirs = [
            'outputs', 'setElementFromLine', outdir
        ]
    )


    return tree


"""
Formatear identación de los archivos, de acuerdo con su estructura
"""
def indent(element, level = 0, more_sibs = False):
    i = "\n"
    
    if level: i += (level-1) * '  '
    
    childs = len(element)
    
    if childs:
        if not element.text or not element.text.strip():
            element.text = i + '  '
            if level:
                element.text += '  '
        count = 0
    
        for children in element:
            indent(children, level+1, count < childs - 1)
            count += 1
    
        if not element.tail or not element.tail.strip():
            element.tail = i
            if more_sibs: element.tail += '  '
    
    else:
        if level and (not element.tail or not element.tail.strip()):
            element.tail = i
            if more_sibs: element.tail += '  '


"""
Implementation
"""

# xmlfile = 'DT00/dummy.xml'

# setNodeToLine(
#     xmlfile,
#     node      = { "parent" : 'description', "name": 'desc' },
#     output    = { "folder": 'DT00', "name": 'dummy.xml'}
# )