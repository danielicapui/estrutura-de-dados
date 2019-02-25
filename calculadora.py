from calc import *
is_game_over=False
while not is_game_over:
   
   op=int(input("Digite a operação desejada 1 para soma,"
   	"2 subtração, 3 para multiplicação,"
   	"4 para divisão:\n"))
   a=int(input("Digite o valor do primeiro número:\n"))
   b=int(input("Digite o valor do segundo número:\n"))
   
   c=Calc(a,b)
   if op==1:
       print("Soma :{}".format(c.sum()))
   if op==2:
       print("Subtração :{}".format(c.subtraction()))
   if op==3:
       print("Multiplicação :{}".format(c.multiplication()))
   if op==4:
       print("Divisão :{}".format(c.division()))
   
   choice=input("Deseja continuar?Y ou N \n")
   if choice=='y' or choice=='Y':
      print("Retornando...")
   else:
      print("Ate mais")
      is_game_over=True

