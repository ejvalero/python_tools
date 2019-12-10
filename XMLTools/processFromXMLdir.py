#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
path_modules = os.path.abspath('modules')
sys.path.append( path_modules )
from SetElementFromLine import setNodeToLine


xmls = os.listdir('inputs/xml')

for xmlfile in xmls:
    xmlfile = 'xml/' + xmlfile
    setNodeToLine( xmlfile, 'cited-references', 'cited-reference' )

print(
    '---',
    'SUCCESS: ' + str( len(xmls) ) + ' .xml files processed and outputs saved in outputs/xml',
    '---'
)