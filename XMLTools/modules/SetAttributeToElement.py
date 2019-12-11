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

def setAttrbute(filename, parent, attribute):

    # Define structure of input and output directories
    inputDir  = 'inputs/'
    outputDir = 'outputs/'

    # Import .xml file and get root of the tree
    tree = ET.parse(inputDir + filename)