class Heroi:
    def __init__(self, nome, idade, tipo):
        self.__nome = nome    
        self.__idade = idade  
        self.__tipo = tipo    

    def atacar(self):
        ataque = self.__determinar_ataque()
        print(f"O {self.__tipo} atacou usando {ataque}")

    def __determinar_ataque(self):
        if self.__tipo.lower() == 'mago':
            return 'magia'
        elif self.__tipo.lower() == 'guerreiro':
            return 'espada'
        elif self.__tipo.lower() == 'monge':
            return 'artes marciais'
        elif self.__tipo.lower() == 'ninja':
            return 'shuriken'
        else:
            return 'não tem ataque definido'

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_tipo(self):
        return self.__tipo

heroi1 = Heroi("Arthas", 30, "guerreiro")
heroi2 = Heroi("Jaina", 28, "mago")
heroi3 = Heroi("Zed", 25, "ninja")

heroi1.atacar()  
heroi2.atacar()  
heroi3.atacar()  
