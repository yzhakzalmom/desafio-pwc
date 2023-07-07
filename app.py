import os
import shutil
from collections import Counter

# OK
def reverter(input_string):
    
    # Divide a frase em palavras, as armazena numa lista e reverte a ordem
    palavras = input_string.split()[::-1]
    
    # Une as palavras com um espaço
    frase_invertida = ' '.join(palavras)
    return frase_invertida

# OK
def remover_duplicados(input_string):
    caracteres_unicos = []
    
    # Percorre a string para checar os caracteres únicos e os coloca num array, mantendo os espaços
    for char in input_string:
        if char == ' ' or char not in caracteres_unicos:
            caracteres_unicos.append(char)
    
    # Une os caracteres únicos  
    texto_sem_duplicados = ''.join(caracteres_unicos)
    
    return texto_sem_duplicados

# OK
def substring_palindroma(input_string):
    tamanho = len(input_string)

    # Cria uma matriz quadrada [tamanho][tamanho] para indicar se a substring entre as posições [i][j] é palíndroma
    matriz = [[False] * tamanho for _ in range(tamanho)]

    # Inicializa todas as substrings de tamanho 1 como palíndromas
    for i in range(tamanho):
        matriz[i][i] = True

    # Até esse ponto, considera-se a primeira letra maior substring palíndroma, pois trata-se de apenas uma letra
    inicio_palindromo = 0
    tamanho_palindromo = 1

    # Inicializa substrings de tamanho 2 se os caracteres extremos forem iguais
    for i in range(tamanho - 1):
        if input_string[i] == input_string[i + 1]:
            matriz[i][i + 1] = True
            inicio_palindromo = i
            tamanho_palindromo = 2

    # Verificar substrings de tamanho maior que 2
    for tamanho_atual in range(3, tamanho + 1):
        for i in range(tamanho - tamanho_atual + 1):
            
            # Indica a última posição da substring
            j = i + tamanho_atual - 1
            
            # Checa se os caracteres extremos são iguais e se a substring interna é um palíndromo
            if input_string[i] == input_string[j] and matriz[i + 1][j - 1]:
                matriz[i][j] = True
                inicio_palindromo = i
                tamanho_palindromo = tamanho_atual

    # Retorna a maior substring palíndroma encontrada
    return input_string[inicio_palindromo:inicio_palindromo + tamanho_palindromo]

# OK
def primeira_maiuscula(input_string):
    return input_string.title()
    
def anagrama_palindromo(input_string):
    
    # Contabiliza a frequência de cada caractere na entrada
    frequencia = Counter(input_string)

    # Checa a contagem dos caracteres
    count_impar = 0
    for count in frequencia.values():
        if count % 2 != 0:
            count_impar += 1
            
        # Caso haja mais de um caractere com número de aparições ímpares, a string não será palíndroma
        if count_impar > 1:
            return False
    
    return True

# Exibe um menu para permitir a escolhe do usuário entre as opções
def exibir_menu():
    print('OPÇÕES:')
    print('1. Reverter ordem')
    print('2. Remover caracteres duplicados')
    print('3. Encontrar substring palíndroma mais longa')
    print('4. Primeiras letras maiúscula')
    print('5. Verificar anagrama de palíndromo')
    print('A. ENTRAR COM OUTRA STRING')
    print('X. FINALIZAR PROGRAMA\n')

# Garante que o número da opção escolhida é valida
def obter_opcao():
    while True:
        opcao = input('Digite a opção desejada: ')
        
        # Checa se a entrada é int e está entre as opções
        if opcao.isdigit() and 1 <= int(opcao) <= 5:
            return int(opcao)
        
        # Checa se a entrada é X, usada para terminar a execução
        elif opcao.upper() == 'X' or opcao.upper() == 'A':
            return opcao
        
        print('Opção inválida. Tente novamente.')

def limpar_terminal():
    
    # Verifica se o SO é Windows
    if os.name == 'nt':
        os.system('cls')
        
    # Verifica se o SO é baseado em Unix
    else:
        os.system('clear')

# Linha de separação a ser usada no terminal para separar diferentes outputs
def imprimir_linha_separadora(caractere='-', tamanho=None):
    if tamanho is None:
        # Estabelece tamanho padrão de (80, 20) caso não consiga encontrar essa informação
        tamanho_terminal = shutil.get_terminal_size((80, 20)).columns
        tamanho = tamanho_terminal

    linha = caractere * tamanho
    print(linha)

# Dicionário para basear a escolha do usuário entre as funções
funcoes = {
    1: reverter,
    2: remover_duplicados,
    3: substring_palindroma,
    4: primeira_maiuscula,
    5: anagrama_palindromo
}

def main():
    # Pedir ao usuário uma string
    input_string = input('Entre com uma string: ')
    limpar_terminal()
    
    while True:
        imprimir_linha_separadora()
        print()
        
        # Sempre relembrar ao usuário a sua entrada
        print('INPUT: ', input_string)
        print()
        
        # Pedir ao usuário que escolha uma função no menu
        exibir_menu()
        opcao = obter_opcao()
        print()
        
        # Checa se usuário escolheu finalizar o programa
        if str(opcao).upper() == 'X':
            break
        elif str(opcao).upper() == 'A':
            limpar_terminal()
            input_string = input('Entre com uma string: ')
            limpar_terminal()
            continue
        
        # Executa a função escolhida e imprime o resultado
        funcao_escolhida = funcoes.get(opcao)
        print('OUTPUT: ', funcao_escolhida(input_string), '\n')

if __name__ == '__main__':
    main()