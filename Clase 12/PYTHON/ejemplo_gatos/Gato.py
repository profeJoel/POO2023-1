class Gato:
    # Los atributos no son necesarios de declarar

    #metodos
    #Constructor que en python se llama __init__() y requiere del componente self que hace referencia al objeto mismo (todos los metodos tienen que agregar el self para pertenecer a la clase)
    def __init__(self, name:str, sex:str, age:int, weight:int, color:str, texture:str):
         # tipo de dato None, o nulo, hace referencia a que es una variable opcional
        self.name = name
        self.sex = sex
        self.age = age
        self.weight = weight
        self.color = color
        self.texture = texture
    
    def eat(self):
        print(f"{self.name} esta comiendo...")
    
    def move(self):
        print(f"{self.name} se esta moviendo...")
    
    def meow(self):
        print(f"{self.name} hace miauuuuuu...")
    
    def purr(self):
        print(f"{self.name} esta ronrroneando...")

    def hunt_mice(self):
        print(f"{self.name} esta capturando ratoncillos...")