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

class XMLFileManager():


    """
    Import or parameterse filename
    """
    def __init__(self, fiename):

        typefile = type( filename )

        if typefile is str and filename.count('\n') is 0:
            path = os.path.join('..', 'inputs', filename)
            tree = ET.parse(path)
        
        if 'xml.etree.ElementTree' in str( typefile ):
            tree = filename

        self.tree = tree


    """
    Filter element using parent, node name and node position
    """
    def filterElements( self, parameters):

        # Define initial parameters
        parent     = parameters['parent']
        nodename   = parameters['nodename']
        position   = parameters['position']
        attributes = parameters['attributes']
        self.parameters = parameters


        # Filtered element is main tree by default
        nodepath = None
        filtered = self.tree


        # Setting up nodepath by parent, nodename, position and attributes
        def includeAttributes( basepath ):

            if len(attributes) > 0:
                attrpath = ''

                for attr in attributes:
                    attrpath = attrpath + '[@' + attr[0] + '="' + attr[1]+ '"]'

                nodepath = basepath + attrpath

                return nodepath


        pathcomponents = [ parent, nodename ]
        pathcomponents  = ' '.join( pathcomponents ).split()
        components = len( pathcomponents )

        if components > 0:

            if components is 1:
                nodepath = './/' + pathcomponents[0]

            if components is 2:
                nodepath = './/' + parent + '/' + nodename

            if position is not 'All':
                nodepath = nodepath + '[' + str(position) + ']'


            nodepath = includeAttributes( nodepath )

        else:
            nodepath = includeAttributes( './/*' )
            

        print(nodepath)
        if nodepath is not None: filtered = self.tree.findall( nodepath )

        
        self.element = filtered
        return self.element



    """
    Set attribute(s) to element
    """
    def setAttributeToElement(self, element, attribute, value):

        try:
            all( [element, attribute, value] )


        except Exception as e:
            print(e)
            sys.exit(1)

            

    """
    def displayMessage():
        return
    
    def exportOutput():
        return
    """

filename = 'DT00/dummy.xml'

parameters = {
    "parent": 'book', 
    "nodename" : '', 
    "position" : 'All',
    "attributes": [
        ['completed', 'yes'],
        ['verified', 'false']
    ]
}

node = XMLFileManager( filename ).filterElements( parameters )
print(node)