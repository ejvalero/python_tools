#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AUTHOR: 
    Emanuel Valero - Provita

LATEST UPDATE:
    2019-12-10
"""

import os, sys
import xml.etree.ElementTree as ET

def setAttribute(filename, parent, nodename, attribute, value, position = 'All'):

    # Define input and output directories, and typefile
    inputDir  = '../inputs/'
    outputDir = 'outputs/'
    typefile = type( filename )

    try:
        
        # Import .xml file and get root of the tree
        if typefile is str and filename.count('\n') is 0:
            tree = ET.parse(inputDir + filename)
        
        elif 'xml.etree.ElementTree' in str( typefile ):
            tree = filename


        # Define node path
        nodepath = './/' + parent + '/' + nodename

        if position is not 'All':
            nodepath = nodepath + '[' + str(position) + ']'


        # Setting attributes
        parentElement = tree.findall( nodepath )

        for child in parentElement:
            child.set('completed', value)

        # Diplay message to console
        message = str( len(parentElement) ) + ' nodes assigned with attr ' + \
                  attribute + '="' + value + '" inside ' + '<' + parent + '>'
        
        print('---', 'MESSAGE: ' + message, '---')

    
    except:
        print('ERROR: Invalid filename')
        sys.exit(1)
  

"""
Implementation
"""


xmlfile = '../inputs/DT00/dummy.xml'
setAttribute(xmlfile, 'catalog', 'book', 'completed', 'yes')
