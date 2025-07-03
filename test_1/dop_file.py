class deistvie:
    def summ(self, number_1, number_2):
        return number_1 + number_2

    def proizv(self, number_1, number_2):
        return number_1 * number_2

    def minus(self, number_1, number_2):
        return number_1 - number_2

    def delenie(self, number_1, number_2):
        return number_1 / number_2

class Calculator(deistvie):
    def otvet(self, number_1, number_2):
        result = self.summ(number_1, number_2)  # вызываем summ через self
        return result

