def fahrenheit_para_celsius(fahrenheit):
  """Converte uma temperatura de Fahrenheit para Celsius.

  Args:
    fahrenheit: Temperatura em Fahrenheit.

  Returns:
    Temperatura em Celsius.
  """

  celsius = (fahrenheit - 32) * 5/9
  return celsius

# Pedindo a temperatura ao usuário
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

# Convertendo para Celsius
celsius = fahrenheit_para_celsius(fahrenheit)

# Imprimindo o resultado
print(f"{fahrenheit}°F equivalem a {celsius:.2f}°C")