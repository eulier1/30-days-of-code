class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        for i, element in enumerate(self.__elements):
            for num in self.__elements[++i:]:
                if self.maximumDifference < abs(element - num):
                    self.maximumDifference = abs(element - num)
