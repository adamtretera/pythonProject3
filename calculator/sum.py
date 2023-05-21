



class Calculator:
    """
    Create a Calculator class with the following methods:
    add(a, b) - returns the sum of a and b
    subtract(a, b) - returns the difference of a and b
    multiply(a, b) - returns the product of a and b
    divide(a, b) - returns the quotient of a and b
    """


    def add(self, a, b):
        """
        Returns the sum of a and b
        :param a: first number
        :param b: second number
        :return: sum of a and b
        """
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")



