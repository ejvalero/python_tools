#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
path_modules = os.path.abspath('modules')
sys.path.append( path_modules )


"""
Implementation 'setNodeToLine'
"""

def implementSetNodeToLine():

    from SetElementFromLine import setNodeToLine
    
    datafolder = 'xml'
    xmlspath = os.path.join('inputs', datafolder)
    xmls = os.listdir( xmlspath )


    for xmlfile in xmls:
        filepath = os.path.join(datafolder, xmlfile)

        setNodeToLine(
            filepath,
            node      = { "parent" : 'cited-references', "name": 'cited-reference' },
            output    = { "folder": 'xml', "name": xmlfile}
        )

    print(
        '---',
        'SUCCESS: ' + str( len(xmls) ) + ' .xml files processed and outputs saved in outputs/xml',
        '---'
    )



"""
Implementation of setAttribute
"""

def implementSetAttributeToElement():

    from SetAttributeToElement import setAttribute

    xmlfile = os.path.join('xml', 'Keith_Foundations_2013.xml')

    setAttribute(
        xmlfile, 
        node = { 
            "parent" : 'cited-references', 
            "name": 'cited', 
            "position": 'All' 
        },
        attribute = [ 'verified-node', 'no']
    )

implementSetAttributeToElement()