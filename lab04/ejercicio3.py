class Diccionario:

    def __init__(self):
        self.dictionary = {}

    def __str__(self):
        for palabra in self.dictionary:
            print(palabra, ":", self.dictionary[palabra])
        return ""

    def cargar(self, fichero, origen):
        g = open(fichero, "r")

        if(origen == "eu"):
            for l in g:
                lerroa = l.strip()
                clave = l.rsplit()[0]
                valor = l.rsplit()[1]
                self.dictionary[clave] = valor
                
        elif(origen == "en"): 
            for l in g:
                lerroa = l.strip()
                clave = l.split()[1]
                valor = l.split()[0]
                self.dictionary[clave] = valor
        else:
            print("El diccionario tiene que ser eu/en o en/eu")
        g.close()

    def consultar(self, palabra):
        claves = self.dictionary.keys()
        if palabra in claves:
            print(self.dictionary.get(palabra))
            return self.dictionary.get(palabra)
        else:
            print(" ")
            return " "
            
        




#Programa

def main():
    hiztegia = Diccionario()
    hiztegia.cargar('.\diccionario_prueba.txt', 'eu')
    #Consulta
    hiztegia.consultar('Car')
    hiztegia.consultar("afdsfg")
    print(" ")
    print(" ")
    #El diccionario completo, para ver que funciona __str__
    print("El diccionario completo: ")
    print(hiztegia)

if __name__== "__main__":
    main()