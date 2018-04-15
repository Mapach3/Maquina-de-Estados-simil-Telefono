class State(object):
    """
    Usamos la clase State para definir algunas caracteristicas de los
    estados de nuestra maquina de estados.
    """

    def __init__(self):
        print 'Estado actual del telefono:', str(self)

    def en_evento(self, evento):
        """
        Encargarse de los eventos que sean delegados a este estado
        """
        pass

    def __repr__(self):
        """
        Ni idea que hace pero sino no te imprime el nombre del estado asi que no tocarlo
        """
        return self.__str__()

    def __str__(self):
        """
        Devuelve el nombre del estado
        """
        return self.__class__.__name__