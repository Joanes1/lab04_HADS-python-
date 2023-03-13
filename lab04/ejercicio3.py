class Diccionario:

    def __init__(self):
        self.dictionary = {}

    def __str__(self):
        for palabra in self.dictionary:
            print(palabra)
        return ""

    def cargar(self, fichero, origen):
        g = open(fichero, "r")
        if(origen == "eu"):
            
          
        