from outer_class import outer_class

if __name__ == "__main__":
    # El objetivo es crear un objeto de la clase inner_class

    X = outer_class.inner_class()

    print(X.a)

    #Y = outer_class.__inner_class_private()
    #Y = outer_class.instanciador()

    O = outer_class(5)
    Y = O.instanciador()

    print(Y.a)