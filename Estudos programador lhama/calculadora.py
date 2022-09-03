# aula video3 

class Calculadora:

    def calcular(self, op, num1, num2):
        if op == "+":
            return self.__adicionar(num1, num2)
        if op == '-':
            return self.__subtrair(num1, num2)

        else: print ('Operação inválida')

    def __adicionar(self, num1, num2): 
        return num1 + num2

    def __subtrair(self, num1, num2):
        return num1 - num2


calculadora = Calculadora() # sem metodo constrututor, basta estanciar.
calculo = calculadora.calcular('*', 2, 5)
print(calculo)