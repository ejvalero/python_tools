#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AUTHOR: 
    Emanuel Valero - Provita

LATEST UPDATE:
    2019-12-14
"""

import os, sys, uuid
import xml.etree.ElementTree as ET

def exportXML(xmlfile, outputname, outputdirs = ['..', 'outputs']):

    outputdir = ''

    for directory in outputdirs:
        outputdir = os.path.join(outputdir, directory)

    if not os.path.exists(outputdir):
        os.makedirs( outputdir )

    output = os.path.join( outputdir, outputname)

    xmlfile.write( output, encoding = 'utf-8')

    return xmlfile


"""
Implementation
"""

#xmlfile = ET.parse('../inputs/DT00/dummy.xml')

#exportXML(xmlfile, 'filename.xml', outputdirs = ['..', 'outputs', 'anotherdir'])