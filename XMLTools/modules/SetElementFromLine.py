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


def setNodeToLine(filename, parent, nodename):
        
    # Define structure of input and output directories
    inputDir  = 'inputs/'
    outputDir = 'outputs/'
    pathfile  = filename.split('/')


    # Import .xml file and get root of the tree
    tree = ET.parse(inputDir + filename)


    # Find all containers whose tags matches with 'parent' parameter. 
    # Then, for each text line in them, assign node with name equals to 'nodename'
    for child in tree.findall('.//' + parent):

        # Detect and rename existent nodes
        if len(child) > 0:
            childName = child[0].tag
            childrenCount = str( len(child.getchildren()) )
            print( 
                '---',
                'WARNING: ' + childrenCount + ' <'+ childName + '> nodes in "' + 
                pathfile[1] + '" were changed to <' + nodename + '>',
                '---'
            )

            for cited in child:
                cited.tag = nodename

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
                    ct = ET.Element(nodename)
                    ct.text = line
                    child.text = ''
                    child.insert(1, ct)


    # Export xml outputs to root path defined in 'outputDir'
    if not os.path.exists(outputDir):
        
        if pathfile[0] is not None:
            os.makedirs(outputDir + 'setElementFromLine/')
        else:
            os.makedirs(outputDir)

    output = outputDir + 'setElementFromLine/' + pathfile[1]

    root = tree.getroot()
    indent(root)
    tree.write(output, encoding='utf-8')

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
