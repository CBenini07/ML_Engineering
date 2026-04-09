'''
O interpretador Python pode executar em modo que possibilite o dev a 
escrever código, e ver o resultado na hora.

Para iniciar, há duas formas:
* Digitar no terminal "python" para chamar o interpretador
* Executar o script com a flag -i "python -i app.py"
----------------------------------------------------------------------
Função dir:

Sem arg, retorna a lista de nome no escopo local. Com um arg, retorna uma
lista de atributos válidos para o objeto. Exemplo:

dir()
dir(100) -> Traz os métodos que podem ser usados com número inteiro
dir(True) -> Traz os métodos que podem ser usados com o booleano True
----------------------------------------------------------------------
Função help

Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo
ou informar por parâmetro qual o nome do módulo, func, classe, método ou variável.
Exemplo:

help()
help(100) ou help (int) -> traz informações sobre a classe int

'''