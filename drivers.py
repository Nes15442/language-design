from src import *

def createAFN(r:str) -> None:
    '''Crea un AFN a partir de una regex'''
    r_ = toPostfix(r)
    r_tree = SyntaxTree(r_)
    r_tree.showTree()
    afn = createAFN_thompson(r_tree)
    afn.drawAutomata()

def AFN_to_AFD(r:str) -> None:
    '''Crea un AFN a partir de una regex'''
    r_ = toPostfix(r)
    r_tree = SyntaxTree(r_)
    r_tree.showTree()

    afn = createAFN_thompson(r_tree)
    afn.drawAutomata()

    afd = subconjuntos(afn)
    afd.drawAutomata()

