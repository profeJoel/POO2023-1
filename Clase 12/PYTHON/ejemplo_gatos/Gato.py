class Gato:
    # Los atributos no son necesarios de declarar

    #metodos
    #Constructor que en python se llama __init__() y requiere del componente self que hace referencia al objeto mismo (todos los metodos tienen que agregar el self para pertenecer a la clase)
    def __init__(self, name:str, sex:str, age:int, weight:int, color:str, texture:str):
         # tipo de dato None, o nulo, hace referencia a que es una variable opcional
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__weight = weight
        self.__color = color
        self.__texture = texture
    
    def eat(self):
        print(f"{self.__name} esta comiendo...")
    
    def move(self):
        print(f"{self.__name} se esta moviendo...")
    
    def meow(self):
        print(f"{self.__name} hace miauuuuuu...")
    
    def purr(self):
        print(f"{self.__name} esta ronrroneando...")

    def hunt_mice(self):
        print(f"{self.__name} esta capturando ratoncillos...")

    # Getters y Setters

    def get_name(self):
        return self.__name
    
    def get_sex(self):
        return self.__sex
    
    def get_age(self):
        return self.__age
    
    def get_weight(self):
        return self.__weight

    def get_color(self):
        return self.__color

    def get_texture(self):
        return self.__texture

    #Setters
    def set_age(self, new_age:int):
        if new_age >= 0 and new_age >= self.__age:
            self.__age = new_age

    def happy_birthday(self):
        self.set_age(self.__age + 1)

    def set_weight(self, new_weight:int):
        if new_weight >= 0 and new_weight >= self.__weight/2 and new_weight <= self.__weight*2:
            self.__weight = new_weight

    def set_color(self, new_color:str):
        if new_color in ["gris", "blanco"]:
            self.__color = new_color
        else:
            print("No se permite el cambio de color")