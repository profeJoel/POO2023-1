class outer_class:

    def __init__(self, id):
        self.id = id

    def instanciador(self):
        return self.__inner_class_private()

    class inner_class:
        def __init__(self):
            self.a = 10

    class __inner_class_private:
        def __init__(self):
            self.a = 100