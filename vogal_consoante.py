def vogal_consoante(letra):
  
  if letra.isalpha():  
    letra = letra.lower()  
    if letra in "aeiou":  
      return "Vogal"
    else:
      return "Consoante"
  else:
    return "Erro"  


letra_usuario = input("Digite uma letra: ")


resultado = vogal_consoante(letra_usuario)
print(f"A letra '{letra_usuario}' é {resultado}.")
