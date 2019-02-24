is_game_over=False
class calculadora:

   def __init__(self,a,b):
       self.a = a 
       self.b = b

   def soma(self,a,b):
       return a+b
   
   def subtração(self,a,b):
       return a-b
   
   def multiplicação(self,a,b):
       return a*b

   def divisão(self,a,b):
       if b==0:
           return False
       else:
           return a/b

while not is_game_over:
   
   op=int(input("Digite a operação desejada 1 para soma,"
   	"2 subtração, 3 para multiplicação,"
   	"4 para divisão:\n"))
   a=int(input("Digite o valor do primeiro número:\n"))
   b=int(input("Digite o valor do segundo número:\n"))
   
   c=calculadora(a,b)
   if op==1:
       print("Soma :{}".format(c.soma(a,b)))
   if op==2:
       print("Subtração :{}".format(c.subtração(a,b)))
   if op==3:
       print("Multiplicação :{}".format(c.multiplicação(a,b)))
   if op==4:
       print("Divisão :{}".format(c.divisão(a,b)))
   
   escolha=input("Deseja continuar?Y ou N \n")
   if escolha=='y' or escolha=='Y':
      print("Retornando...")
   else:
      print("Ate mais")
      is_game_over=True

