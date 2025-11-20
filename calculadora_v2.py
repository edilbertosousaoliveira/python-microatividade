"""
Programa que efetua operações matemáticas: adição, subtração, multiplicação e divisão
que faz uso de recursos como declaração e atribuição de valores a variáveis,
estruturas de condição e repetição, input de dados, além de funções
"""

# variável que receberá o valor da pergunta: Deseja fazer outra operação matemática?(S/N)
saida = ''

# função que retorna a soma de dois números recebidos nos parâmetros
def adicao(numero1, numero2):
    return numero1 + numero2

# função que retorna a subtração de dois números recebidos nos parâmetros
def subracao(numero1, numero2):
    return numero1 - numero2

# função que retorna a multiplicação de dois números recebidos nos parâmetros
def multiplicacao(numero1, numero2):
    return numero1 * numero2

# função que retorna a divisão de dois números recebidos nos parâmetros
def divisao(numero1, numero2):
    if numero1 == 0 or numero2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return numero1 / numero2

# função que retorna o resultado da operação matemática de dois números.
# recebe como parâmetro os dois números e a operação que deseja fazer com os dois números.
def calculadora(numero1, numero2, operacao):
    if (operacao == '+' or
        str(operacao).lower() == 'soma' or
        str(operacao).lower() == 'adicao' or
        str(operacao).lower() == 'adição'
    ):
        resultado = adicao(numero1, numero2)
    elif (operacao == '-' or
          str(operacao).lower() == 'subtracao' or
          str(operacao).lower() == 'subtração'
    ):
        resultado = subracao(numero1, numero2)
    elif (operacao == '*' or
          str(operacao).lower() == 'multiplicacao' or
          str(operacao).lower() == 'multiplicação'
    ):
        resultado = multiplicacao(numero1, numero2)
    elif (operacao == '/' or
          str(operacao).lower() == 'divisao' or
          str(operacao).lower() == 'divisão'
    ):
        resultado = divisao(numero1, numero2)
    else:
        resultado = "Operação matemática inválida!"

    return resultado

# loop que executa as operações matemáticas,
# onde o usuário informa dois números e a operação que deseja fazer com eles.
# mostra na console o seu resultado.
# pergunta se deseja fazer outra operação matemática, caso seja diferente de n executa novamente os comandos do loop
print("=== Operações Matemáticas ===")
while str(saida).lower() != 'n':
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = str(input("Digite o símbolo ou nome da operação matemática: "))

    resultado = calculadora(numero1, numero2, operacao)
    print(f"Resultado da operação: {resultado}")

    saida = input("Deseja fazer outra operação matemática?(S/N) ")