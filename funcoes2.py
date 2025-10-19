"""
demonstra a declaração e chamada de funções com a utilização de parâmetros
verificando se o perfil do usuário que está logando é o administrador
para imprimir "Bem-vindo, Administrador" no console,
senão imprimirá "Bem-vindo, Usuário"
"""

# função que imprime "Bem-vindo, Administrador", caso o perfil seja admin
# senão será impresso "Bem-vindo, Usuário"
def loginUsuario(perfil):
    if perfil.lower() == "admin":
        print("Bem-vindo, Administrador")
    else:
        print("Bem-vindo, Usuário")

# faz chamadas a função para imprimir o bem-vindo passando como argumento o perfil do usuário
loginUsuario("Admin")
loginUsuario("admin")
loginUsuario("User")
loginUsuario("usuário")
loginUsuario("etc.")