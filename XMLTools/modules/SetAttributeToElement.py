#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AUTHOR: 
    Emanuel Valero - Provita

LATEST UPDATE:
    2019-12-10
"""

import os, sys, uuid
import xml.etree.ElementTree as ET

def setAttribute(filename, parent, nodename, attribute, value, 
                 nodeposition = 'All'):


    # Define input and output directories, and typefile
    inputDir  = '../inputs/'
    outputDir = '../outputs/setAttributeToElement/'
    typefile = type( filename )
    nodeposition = str(nodeposition)

    try:
        # Import .xml file and get root of the tree
        if typefile is str and filename.count('\n') is 0:
            tree = ET.parse(inputDir + filename)
        
        if 'xml.etree.ElementTree' in str( typefile ):
            tree = filename


        # Define node path for edit
        nodepath = './/' + parent + '/' + nodename

        if nodeposition is not 'All':
            nodepath = nodepath + '[' + nodeposition + ']'


        # Setting attributes
        parentElement = tree.findall( nodepath )

        for child in parentElement:
            child.set( attribute, value)


        # Display message to console
        message = str( len(parentElement) ) + ' nodes assigned with attr ' + \
                  attribute + '="' + value + '" inside ' + '<' + parent + '>'

        if nodeposition is not 'All':
            message = message + ', position ' + nodeposition
        
        print('---', 'MESSAGE: ' + message, '---')


        # Save updated xml files
        if not os.path.exists( outputDir ):
            os.makedirs( outputDir )

        if typefile is str and filename.count('\n') is 0:
            pathfile  = filename.split('/')

            if not os.path.exists( outputDir + pathfile[0] ):
                os.makedirs( outputDir + pathfile[0] )

            output = outputDir + filename

        else:
            output = outputDir + str(uuid.uuid4()) + '.xml'


        tree.write(output, encoding='utf-8')


    except Exception as e:
        print('ERROR:', e)
        sys.exit(1)
  

"""
Implementation
"""

# Using parsed xml file as object
# xmlfile = ET.parse('../inputs/xml/Bland_MesoAmericaReef_2017.xml')

# setAttribute(xmlfile, 'authors', 'author', 
#              'completed', 'yes', nodeposition = 2)


# Using data from .xml file directly

## Example 1
xmlfile = 'DT00/dummy.xml'

setAttribute(xmlfile, 'catalog', 'book', 
             'completed', 'yes', nodeposition = 4)

## Example 2
xmlfile = 'xml/Keith_Foundations_2013.xml'

setAttribute(xmlfile, 'cited-references', 'cited', 
             'verified-node', 'no', nodeposition = 'All')