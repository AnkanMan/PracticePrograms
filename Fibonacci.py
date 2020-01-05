class Fibonacci():
    a,b = 0,1
    l = [0,1]

    def __init__(self):
        pass

    def loop(self,n):
        for x in range(n-2):
            f=self.a+self.b
            self.l.append(f)
            a=self.b
            b=f
        return self.l

    def recursion(self,n):
        if n>2:
            f = self.a + self.b
            self.a = self.b
            self.b = f
            self.l.append(f)
            return self.recursion(n-1)
        else :
            return self.l
