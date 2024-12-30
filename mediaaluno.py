def calcular_media():
  
  
  nota1 = float(input("Digite a primeira nota: "))
  nota2 = float(input("Digite a segunda nota: "))

  
  media = (nota1 + nota2) / 2

  
  if media >= 7.0:
    mensagem = "Aprovado!"
  else:
    mensagem = "Reprovado."

  return mensagem


mensagem = calcular_media()
print(mensagem)