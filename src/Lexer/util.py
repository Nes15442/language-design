'''
*************************************************
Universidad del Valle de Guatemala
Diseño de Lenguajes de Programación

util.py
- funciones auxiliares

Autor: Diego Cordova - 20212
*************************************************
'''

from .Automata import AFD

class SubState:
  ''' Objecto para stack de estados (Dstates) '''
  def __init__(self, states) -> None:
    self.states = states
    self.marked = False

def get_unmarked(Dstates:list[SubState]) -> list:
    ''' Devuelve el primer estado sin marcar en Dstates '''
    for state in Dstates:
        if state.marked == False:
            return state
    
    return False

def getDState(DStates:list[SubState], U:list[int]) -> SubState:
    ''' Devuelve el Substate que contine U en Dstates '''
    for state in DStates:
        if state.states == U:
            return state

def enumStates(
    estados:list[SubState],
    symbols:list,
    initial:SubState,
    finals:list[SubState],
    transitions:dict
) -> AFD:
    '''
        Devuelve un AFD con estados como numeros
        utilzando como base estados de SubStates (objetos)
    '''

    # Llave para transformar estados de objeto a numeros
    # Y estados
    states_dict = {}
    actual_states = []

    for index, state in enumerate(estados):
        states_dict[state] = index
        actual_states.append(index)

    # Transiciones
    actual_trans = {}
    for key in transitions.keys():
        actual_trans[(states_dict[key[0]], key[1])] = states_dict[transitions[key]]

    # Estado inicial y estados finales
    actual_initial = states_dict[initial]
    actual_finals = [ states_dict[q] for q in finals ]
    
    return AFD(
        estados=actual_states,
        symbols=symbols,
        initial=actual_initial,
        finals=actual_finals,
        transitions=actual_trans
    )