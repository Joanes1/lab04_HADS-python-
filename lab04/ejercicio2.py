class Mochila: 
    def __init__(self):
        self.objetos = []
    
    def __str__(self):
        for objeto in self.objetos:
            print(objeto)
        return ""

    def introducir_objeto(self, a):
        self.objetos.append(a)
    
    


#Programa

def main():
    m2 = Mochila()
    m3 = Mochila()
    m2.introducir_objeto('bocadillo')
    m2.introducir_objeto('juego de llaves')
    print("mochila 2:")
    print(m2)
    print("mochila 3:")
    print(m3)

if __name__== "__main__":
    main()


