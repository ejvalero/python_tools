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


def setAttribute(
        filename, 
        node      = { "parent": '', "name": '', "position": 'All' },
        attribute = ['', ''],
        output    = { "folder": None, "name": None }
    ):


    # Define input and output directories, and typefile
    inputDir  = '../inputs/'
    typefile = type( filename )
    node['position'] = str( node['position'] )

    try:
        # Import .xml file and get root of the tree
        if typefile is str and filename.count('\n') is 0:
            tree = ET.parse(inputDir + filename)
        
        if 'xml.etree.ElementTree' in str( typefile ):
            tree = filename


        # Define node path for edit
        nodepath = './/' + node['parent'] + '/' + node['name']

        if node['position'] is not 'All':
            nodepath = nodepath + '[' + node['position'] + ']'


        # Setting attributes
        parentElement = tree.findall( nodepath )

        for child in parentElement:
            child.set( attribute[ 0 ], attribute[ 1 ] )


        # Display message to console
        message = str( len(parentElement) ) + ' nodes assigned with attr ' + \
                  attribute[ 0 ] + '="' + attribute[ 1 ] + '" inside ' + \
                  '<' + node['parent'] + '>'

        if node['position'] is not 'All':
            message = message + ', position ' + node['position']
        
        print('---', 'MESSAGE: ' + message, '---')


        # Save updated xml files
        outdir  = output.get('folder')
        outname = output.get('name')

        if outdir is None:
            outdir = 'XML'

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
xmlfile = ET.parse('../inputs/xml/Bland_MesoAmericaReef_2017.xml')

setAttribute(
    xmlfile,
    node      = { "parent" : 'authors', "name": 'author', "position": 2 },
    attribute = [ 'completed', 'yes' ],
    output    = { 'folder': 'xml', 'name': 'Bland_MesoAmericaReef_2017.xml'}
)


# Using data from .xml file directly

## Example 1
xmlfile = 'DT00/dummy.xml'

setAttribute(
    xmlfile,
    node      = { "parent" : 'catalog', "name": 'book', "position": 1 },
    attribute = [ 'completed', 'yes' ],
    output    = { "folder": 'DT00', "name": 'dummy.xml'}
)

## Example 2
xmlfile = 'xml/Keith_Foundations_2013.xml'

setAttribute(
    xmlfile, 
    node = { 
        "parent" : 'cited-references', 
        "name": 'cited', 
        "position": 'All' 
    },
    attribute = [ 'verified-node', 'no']
)