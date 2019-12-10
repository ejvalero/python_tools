#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DESCRIPCIÓN: 
    Script para asignar el nodo 'nodename' a los ítems contenidos en el container
    'parnt' de los archivo 'xml' (Lista Roja de Ecosistemas).

PARÁMETROS
    - filename: nombre del archivo de entrada. Ver el ítem USO para más información.

USO:
    - Crear un directorio 'xml' en la misma carpeta donde se donde se encuentra el script 
    'tagger.py'

    - Colocar los archivos originales en formata .xml en '/xml'

    - Ejecutar en una terminal: 
        > cd ruta-donde-se-ubica-tagger.py. 
        > tagger.py

    Los archivos resultantes se guardarán en el directorio 'outputs', con el mismo nombre de
    los archivos de entrada.

AUTOR: 
    Emanuel Valero - Provita

ÚLTIMA ACTUALIZACIÓN:
    2019-12-03

"""


import os, io
import xml.etree.ElementTree as ET


def setNodeToLine(filename, parent, nodename):
        
    # Definir estructura de los directorios de entrada y salida
    inputDir  = 'inputs/'
    outputDir = 'outputs/' 


    # Importar el o los archivos .xml y obtener la estructura raíz de los datos
    tree = ET.parse(inputDir + filename)


    # Encontrar todos los containers identificados con 'cited-references'. 
    # Luego, para cada línea de texto en ellos, asignar el nodo definido en 'nodename'
    for citedReferences in tree.findall('.//' + parent):

        # Detectar y renombrar nodos exitentes
        if len(citedReferences) > 0:
            childrenNames = citedReferences[0].tag
            childrenCount = str( len(citedReferences.getchildren()) )
            print( childrenCount + ' nodes named ' + childrenNames + ' changed to ' + nodename )

            for cited in citedReferences:
                cited.tag = nodename

        # Agregar nodename a cada línea de texto en cited-references
        childText = citedReferences.text

        if childText is not None:
            childText = ' '.join(filter(None, childText.split(' ')))
            childText = childText.replace('\n ', '\n')

            countLines = childText.count('\n')
            lines = childText.split('\n')

            for counter in range( countLines ):
                line = lines[ counter ]
                line = ' '.join(line.split())

                if line is not '':
                    ct = ET.Element(nodename)
                    ct.text = line
                    citedReferences.text = ''
                    citedReferences.insert(1, ct)


    # Exportar archivos con la nueva estructura a la ruta definida en la variable 'outputDir'
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    root = tree.getroot()
    indent(root)
    tree.write(outputDir + filename, encoding='utf-8')


"""
Formatear identación de los archivos, de acuerdo con su estructura
"""
def indent(element, level = 0, more_sibs = False):
    i = "\n"
    
    if level: i += (level-1) * '  '
    
    childs = len(element)
    
    if childs:
        if not element.text or not element.text.strip():
            element.text = i + '  '
            if level:
                element.text += '  '
        count = 0
    
        for children in element:
            indent(children, level+1, count < childs - 1)
            count += 1
    
        if not element.tail or not element.tail.strip():
            element.tail = i
            if more_sibs: element.tail += '  '
    
    else:
        if level and (not element.tail or not element.tail.strip()):
            element.tail = i
            if more_sibs: element.tail += '  '


"""
Ejemplo para todos los archivos en 'xml'


xmls = os.listdir('inputs/DT00')

for xmlfile in xmls:
    setNodeToLine( xmlfile, 'cited-references', 'cited-reference' )
"""