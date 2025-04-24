"""
    Summary
"""
class Node:
    """
    Clase Node que representa un nodo con un atributo 'x'.
    
    Métodos:
    - __init__(x): Constructor que inicializa el nodo con un valor 'x'.
    - getter_x(): Devuelve el valor de 'x'.
    - setter_x(x): Establece un nuevo valor para 'x'.
    """
    def __init__(self,x):
        self._x = x
        self._left = None
        self._right = None
        self._parent =None
        self._height = 1
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,x):
        self._x = x
    @property
    def left(self):
        return self._left
    @left.setter
    def left(self,node):
        self._left = node
    @property
    def right(self):
        return self._right
    @right.setter
    def right(self,node):
        self._right = node
    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self,node):
        self._parent = node
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,height):
        self._height = height
