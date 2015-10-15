#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.width = ""
        self.height = ""
        self.background-color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = "" 
        self.right = "" 
        self.src = ""
        self.region = ""  
        self.begin = ""
        self.dur = ""  

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.width = attrs.get('width',"")
            self.height = attrs.get('heigth',"")
            self.background-color = attrs.get('background-color',"")

    def get_tags(self):
        """
        Metodo llamado get_tags que devolvera una lista con las etiquetas encontradas, 
        sus atributos y el contenido de los atributos. 
        """
        # self.tags = 
        return self.tags


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = ChistesHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    My_List = get_tags(cHandler)
    print(cHandler)
