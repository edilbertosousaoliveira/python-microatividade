"""
demonstra como utilizar as estruturas de condição if, else if e else
avaliando o nível de conhecimento com base no tempo de experiência
"""

# atribuição do tempo de experiência para ser avaliado
tempoExperiencia = 5 # primeira opção de valor
#tempoExperiencia = 1 # segunda opção de valor
#tempoExperiencia = 3 # terceira opção de valor

# verifica o tempo de experiência para definir o nível de conhecimento
if tempoExperiencia < 2:
    print("Nível de conhecimento júnior.")
elif tempoExperiencia > 2 and tempoExperiencia < 5:
    print("Nível de conhecimento pleno.")
else:
    print("Nível de conhecimento sênior.")
