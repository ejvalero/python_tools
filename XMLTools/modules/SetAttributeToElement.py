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
                 outputFile = None, position = 'All'):

    # Define input and output directories, and typefile
    inputDir  = '../inputs/'
    outputDir = '../outputs/setAttributeToElement/'
    typefile = type( filename )
    position = str(position)

    try:
        # Import .xml file and get root of the tree
        if typefile is str and filename.count('\n') is 0:
            tree = ET.parse(inputDir + filename)
        
        elif 'xml.etree.ElementTree' in str( typefile ):
            tree = filename


        # Define node path for edit
        nodepath = './/' + parent + '/' + nodename

        if position is not 'All':
            nodepath = nodepath + '[' + position + ']'


        # Setting attributes
        parentElement = tree.findall( nodepath )

        for child in parentElement:
            child.set('completed', value)


        # Display message to console
        message = str( len(parentElement) ) + ' nodes assigned with attr ' + \
                  attribute + '="' + value + '" inside ' + '<' + parent + '>'

        if position is not 'All':
            message = message + ', position ' + position
        
        print('---', 'MESSAGE: ' + message, '---')


        # Save updated xml files
        if outputFile is None or outputFile is '':
            output = outputDir + str(uuid.uuid4()) + '.xml'
        
        else:
            output = outputDir + outputFile

        tree.write(output, encoding='utf-8')


    except Exception as e:
        print('ERROR:', e)
        sys.exit(1)
  

"""
Implementation
"""

xmlfile = 'xml/Bland_MesoAmericaReef_2017.xml'
setAttribute(xmlfile, 'authors', 'author', 
             'completed', 'yes', position = 1, 
             outputFile='Bland_MesoAmericaReef_2017.xml')
