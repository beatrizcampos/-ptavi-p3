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
        #self.background-color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = "" 
        self.right = "" 
        self.src = ""
        self.region = ""  
        self.begin = ""
        self.dur = "" 
        self.list = [] 

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.width = attrs.get('width',"")
            self.height = attrs.get('heigth',"")
            #self.background-color = attrs.get('background-color',"")
            self.list.append([name, attrs])

        elif name == 'region':
            self.id = attrs.get('width',"")
            self.top = attrs.get('heigth',"")
            self.bottom = attrs.get('background-color',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('rigth',"")
            self.list.append([name, attrs])

        if name == 'img':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            self.list.append([name, attrs])

        if name == 'audio':
            self.src = attrs.get('src',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            self.list.append([name, attrs])

        if name == 'textstream':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.list.append([name, attrs])

    def get_tags(self):
        """
        Metodo llamado get_tags que devolvera una lista con las etiquetas encontradas, 
        sus atributos y el contenido de los atributos. 
        """
        return self.list


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    My_List = cHandler.get_tags()
    print(My_List)
