from .binary_operation import BinaryOperation

class ModuleOperation(BinaryOperation):
    """ 
    Операция остатка от деления
    """
  
    def calculate(self):
      """
      Метод вычисляет численное значение выражения
      :return: значение выражения как вещественное число
      """
      # raises ZeroDivisionError automatically
      return self._left.calculate() % self._right.calculate()
