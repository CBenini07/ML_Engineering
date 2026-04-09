'''
Variáveis são valores que podem sofrer alterações no decorrer da execução 
do programa. 
'''
print('--- ESSES SÃO EXEMPLOS DE VARIÁVEIS ---')
age, name = 28, 'Guilherme' 

print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

age, name = 18, 'Giovanna'

print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

# ---------------------------------------------------------------------------------------------
'''
Constantes são valores imutáveis.

Em Python, não existe uma palavra reservada para informar ao interpretador
que o valor é cte (eg. const em C). Contudo, usamos a convenção que diz ao programador
que a var é uma cte. Para tal, deve-se criar a variável com o nome todo em maiúsculo.
'''
print('\n--- ESTE SÃO EXEMPLOS DE CONSTANTES ---')

ABS_PATH = r'C:\Users\cauab\OneDrive\Área de Trabalho\Data_Engineer' # prefixo 'r' indica raw string, ou seja, não considera \X um escape unicode
DEBUG = True
STATES = ['SP', 'RJ', 'MG']
AMOUNT = 30.2

print(f'Esse é o caminho para o documento atual: {ABS_PATH}')

