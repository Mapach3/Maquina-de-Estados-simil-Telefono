from state import State

# Definicion de los estados de nuestra maquina de estados

class Durmiendo(State):
    """ El telefono no esta realizando una llamada"""
    
    def en_evento(self,evento):
        if evento == 'llamar':
            return Llamada()
        
        return self
    
    
class Llamada(State):
    """El telefono esta en una llamada"""
    
    def en_evento(self, evento):
        if evento == 'cortar':
            return Durmiendo()
        if evento == 'espera':
            return EnEspera()
        
        return self
    
class EnEspera(State):
    """El telefono puso una llamada en espera"""
    
    def en_evento(self, evento):
        if evento == 'reanudar':
            return Llamada()
        if evento == 'cortar':
            return Durmiendo()
        
        return self
    
    

#Fin de la asignacion de estados.