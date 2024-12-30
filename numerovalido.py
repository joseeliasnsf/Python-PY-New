def solicitar_numero_valido():
  
  
  while True:
    try:
      numero = int(input("Digite um número entre 0 e 10: "))
      if 0 <= numero <= 10:
        return numero
      else:
        print("Valor inválido. Digite um número entre 0 e 10.")
    except ValueError:
      print("Entrada inválida. Digite um número inteiro.")

numero_valido = solicitar_numero_valido()
print(f"Você digitou um número válido e ele é: {numero_valido}.")