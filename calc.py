
class Calc:

   def __init__(self,a,b):
       self.a = a 
       self.b = b

   def sum(self):
       return self.a+self.b
   
   def subtraction(self):
       return self.a-self.b
   
   def multiplication(self):
       return self.a*self.b

   def division(self):
       if self.b==0:
           return False
       else:
           return self.a/ self.b
   def potencia(self):
      return self.a**self.b
   def raiz_quadrada(self):
      return self.a**(1/b)
if __name__=='__calc__':
    Calc()
