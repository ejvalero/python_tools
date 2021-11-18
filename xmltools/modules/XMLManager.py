#!/usr/bin/env python3
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
    def filterElements( self, parameters, verbose = True):

        # Define initial parameters
        parent     = parameters['parent']
        nodename   = parameters['nodename']
        position   = parameters['position']
        attributes = parameters['attributes']
        pathcomponents  = ' '.join( [ parent, nodename ] ).split()
        components      = len( pathcomponents )
        self.parameters = parameters


        # Filtered element is main tree by default
        self.element = self.tree


        # Functions for build xpath based on parent, nodename, position and attributes
        def includeAttributes( basepath ):
            if len(attributes) > 0:
                attrpath = ''

                for attr in attributes:
                    attrpath = attrpath + '[@' + attr[ 0 ] + '="' + attr[ 1 ]+ '"]'

                return basepath + attrpath
            
            else:
                return basepath

        def buildXpath():
            if components is  0:
                xpath = './/*'

            if components is 1:
                xpath = './/' + pathcomponents[0]

            if components is 2:
                xpath = './/' + parameters['parent'] + '/' + nodename

            if position not in [ 'All', '' ]:
                xpath = xpath + '[' + str(position) + ']'

            return includeAttributes( xpath )


        # Display output messages to console
        def displayMessages():
            nodes = len( self.element )

            if nodes is not 0:
                elem   = 'elements' if position in ['All', ''] else 'element'
                nodes  = str(nodes) + ' ' if position in ['All', ''] else ''
                posmsg = ' in position ' + str(position) if position not in ['All', ''] else ''


                if components is 1:
                    info = nodes \
                         + '<' + pathcomponents[0] + '> ' + elem \
                         + posmsg \
                         + ' from all of its parents'

                if components is 2:
                    info = nodes \
                         + '<' + nodename + '>' + ' ' + elem \
                         + posmsg \
                         + ' from parent ' + '<' + parameters['parent'] + '>'


                print( '---', 'SUCCESS: Selected ' + info, '---' )
            
            else:
                print( '---', 'WARNING: No element matching your parameters')


        # Select element using xpath and display outputs to console
        nodepath =  buildXpath()

        if nodepath is not None:
            self.element = self.tree.findall( nodepath )
            if verbose: 
                displayMessages()
                print( *self.element, sep='\n' )


        return self.element



    """
    Set attribute(s) to element
    """
    def setAttributeToElement(self, element, attribute, value):


        try:
            # Setting attributes
            parentElement = tree.findall( nodepath )

            for child in parentElement:
                child.set( attribute[ 0 ], attribute[ 1 ] )


        except Exception as e:
            print(e)
            sys.exit(1)

    
    
    """
    def exportOutput():
        return
    """

filename = 'DT00/dummy.xml'

# parameters = {
#     "parent": 'book', 
#     "nodename" : '', 
#     "position" : 'All',
#     "attributes": [
#         ['completed', 'yes'],
#         ['verified', 'false']
#     ]
# }

parameters = {
    "parent": '', 
    "nodename" : 'book', 
    "position" : '2',
    "attributes": [

    ]
}

node = XMLFileManager( filename ).filterElements( parameters )