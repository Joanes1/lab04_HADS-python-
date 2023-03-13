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
            while line.readline():
                lerroa = line.readline()
                clave = lerroa.split[0]
                valor = lerroa.split[1]
                self.dictionary[clave] = valor
        else: 
            while line.readline():
                lerroa = line.readline()
                clave = lerroa.split[1]
                valor = lerroa.split[0]
                self.dictionary[clave] = valor

        g.close()

        def consultar(self, palabra):
            if self.dictionary.has_key(palabra):
                return self.dictionary.get(palabra)
            else:
                return " "