#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AUTOR: 
    Emanuel Valero - Provita

ÚLTIMA ACTUALIZACIÓN:
    2019-12-10
"""

import os, io
import xml.etree.ElementTree as ET

def setAttribute(filename, parent, nodename, attribute, value ):

    # Define structure of input and output directories
    inputDir  = '../inputs/'
    outputDir = 'outputs/'

    # Import .xml file and get root of the tree
    if type(filename) is str:
        tree = ET.parse(inputDir + filename)

        for child in tree.findall( parent + '//' + nodename ):
            child.set( attribute, value )

            print(child.get( attribute ))

"""
Implementation
"""

xmlfile = 'DT00/dummy.xml'
setAttribute(xmlfile, 'book', 'description', 'completed', 'yes')