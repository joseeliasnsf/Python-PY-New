def verificar_par_impar(numero):
  
  if numero % 2 == 0:
    mensagem = "Par"
  else:
    mensagem = "Ímpar"
  return mensagem

numero = int(input("Digite um número inteiro: "))
mensagem = verificar_par_impar(numero)
print(f"O número {numero} é {mensagem}.")
