class Calculator(AdvancedArithmetic):
    def divisorSum(self, num):
        return sum([n for n in range(1,num+1) if(num%n==0)])
