"""
demonstra a utilização da estrutura de repetição while
imprimindo no console a idade informada até que digite zero para finalizar o programa
"""

# valor inicial da idade
entrada_idade = ""

# fica em loop solicitando a idade até que digite zero para sair
while entrada_idade != str(0):
    entrada_idade = input("Digite um número qualquer ou 0 para sair:")
    print(f"Número digitado: {entrada_idade}")
