try: # TENTE ALGO
    numero = int(input("Digite um número inteiro: "))
    resultado = 100 / numero
    print(f"O resultado de 100 dividido por {numero} é: {resultado}")
except ZeroDivisionError: # EXCETO
    print("Erro: não é possível dividir por zero.")
except ValueError:
    print("Erro: entrada inválida. Por favor, digite um número inteiro.")

    
# ESTRUTURAS DE CONDIÇÃO -> IF, ELIF E ELSE
# ESTRUTURAS DE REPETIÇÃO -> FOR E WHILE
# ESTRUTURA DE EXCESSÃO DE ERROS -> TRY/EXCEPT

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print(err)
