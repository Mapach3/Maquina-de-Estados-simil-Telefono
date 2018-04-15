# simple_device.py

from my_states import Durmiendo

class MaquinaEstados(object):
    """ 
    Una maquina de estados simple que simula ser un telefono
    """

    def __init__(self):
        """ Inicializar maquina de estados. """

        # Definir esta de inicio
        self.estado = Durmiendo()

    def en_evento(self, evento):
        """
        Este metodo se encarga de gestionar el evento entrante, entonces en base
        a este obtenemos un nuevo estado.
        """

        # The next state will be the result of the on_event function.
        self.estado = self.estado.en_evento(evento)