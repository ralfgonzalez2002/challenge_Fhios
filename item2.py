'''Escribir una función poker que reciba cinco cartas de la baraja francesa e informe
(devuelva el valor lógico correspondiente) si esas cartas forman o no un poker (es decir
que hay 4 cartas con el mismo número).'''


def poker(*_poker):
  tupla=_poker
  counter=0
  counter2=0
  devolver_si_poker='poker'
  no_poker='No hay un poker'

  for j in range(5):
      carta=tupla[j][0]
      for i in range(counter2,5):
          if carta==tupla[i][0]:
             counter +=1
      if counter==4:
          return devolver_si_poker
      else :
           return no_poker


      counter=0
      counter2 +=1
print(poker('4h','8s','4d','4p','4s'))