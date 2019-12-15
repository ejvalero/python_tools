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
from SaveXML import exportXML


def setAttribute(filename, 
                 attribute, value,
                 parent = { "name": '', "children": '', "nodeposition": 'All' },
                 output = { 'directory': None, 'name': None }):


    # Define input and output directories, and typefile
    inputDir  = '../inputs/'
    typefile = type( filename )
    parent['nodeposition'] = str( parent['nodeposition'] )

    try:
        # Import .xml file and get root of the tree
        if typefile is str and filename.count('\n') is 0:
            tree = ET.parse(inputDir + filename)
        
        if 'xml.etree.ElementTree' in str( typefile ):
            tree = filename


        # Define node path for edit
        nodepath = './/' + parent['name'] + '/' + parent['children']

        if parent['nodeposition'] is not 'All':
            nodepath = nodepath + '[' + parent['nodeposition'] + ']'


        # Setting attributes
        parentElement = tree.findall( nodepath )

        for child in parentElement:
            child.set( attribute, value)


        # Display message to console
        message = str( len(parentElement) ) + ' nodes assigned with attr ' + \
                  attribute + '="' + value + '" inside ' + '<' + parent['name'] + '>'

        if parent['nodeposition'] is not 'All':
            message = message + ', position ' + parent['nodeposition']
        
        print('---', 'MESSAGE: ' + message, '---')


        # Save updated xml files
        outdir  = output.get('directory')
        outname = output.get('name')

        if outdir is None:
            outdir = uuid.uuid4().hex[:5]

        if outname is None:
            outname = uuid.uuid4().hex + '.xml'


        exportXML(
            tree, outname, outputdirs = [
                '..', 'outputs', 'setAttributeToElement', outdir
            ]
        )
        

        return tree


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

setAttribute(xmlfile,
             'completed', 'yes',
             parent = { 'name' : 'catalog', 'children': 'book', 'nodeposition': 1 },
             output= { 'directory': 'DT00', 'name': 'dummy.xml'}
             )

## Example 2
xmlfile = 'xml/Keith_Foundations_2013.xml'

setAttribute(xmlfile, 
             'verified-node', 'no',
             parent = { 
                 "name" : 'cited-references', 
                 "children": 'cited', 
                 "nodeposition": 'All' },
             )