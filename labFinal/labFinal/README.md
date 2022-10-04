# CGr-P
Materiais das práticas

Livro: 

Stemkoski, L., & Pascale, M. (2021). Developing Graphics Frameworks with Python and OpenGL (p. 344). Taylor & Francis by CRC Press.
ISBN 9780367721800

## Diretoria
Código final em labFinal

### Preparação do ambiente de trabalho

1. Instalar o Python
2. Instalar os pacotes (`requirements.txt`)
```
    mkdir C:\Users\xxxxx\venvs
    py -m venv C:\Users\xxxxx\venvs\CGr
    C:\Users\xxxxx\venvs\CGr\Scripts\activate
    py -m pip install -r requirements.txt
```
3. Instalar um editor (`VSCode` ou `Sublime Text`)

### Ativar o ambiente virtual

C:\Users\xxxxx\venvs\CGr\Scripts\activate

### Testar o ambiente de trabalho

Abrir uma janela

### Execução dos programas

	Abrir uma janela cmd na pasta CGr criada
	Scripts\activate
	cd labFinal
	py basic_scene.py

### É necessário ter as seguintes pastas na mesma diretoria que o programa (basic_scene.py) para o conseguir interpretar o programa:
# "core"
# "core_ext"
# "geometry"
# "material" 
# "extras"
# "images"

### Jogo desenvolvido

# Projeto Final (basic_scene.py)

## LabFinal contem:
- Pasta core para conseguir interpretar os programas pedidos.
- Pasta core_ext para conseguir interpretar o objeto 3D da secretária.
- Pasta geometry com ficheiros que interpretam diversas figuras geométricas.
- Pasta material com ficheiros que interpretam diversas texturas. 
- Pasta images com ficheiros .png e .jpg que interpretam imagens para definir as
texturas dos objetos.
- basic scene.py programa que interpreta os vários objetos para formar o ambiente do jogo.
- Outros ficheiros .py onde constam em objetos feitos pelo grupo para formar o jogo


### Objetivo do jogo

O jogo consiste numa aranha a andar por um quarto (para movimentar utilizar as setas up, down, 
left, right) com o objetivo de combater com as outras aranhas. 

Existem 3 aranhas npcs (azul, verde, vermelha) que estão espalhadas pelo quarto. Quando estivermos frente a frente com uma 
aranha inimiga, ao clicar na tecla "p" vamos entrar em duelo com essa aranha. O duelo consiste em 
selecionar um dos 3 elementos (fogo, água e erva) vísiveis no ecrã e a aranha inimiga também vai 
escolher um dos elementos para atacar/defender.

Durante o combate podemos escolher um dos 3 elementos:
- Para selecionar o fogo pressione a tecla "j"
- Para selecionar o água pressione a tecla "k"
- Para selecionar o erva pressione a tecla "l"

Ordem dos elementos:
- Fogo derrota Erva
- Erva derrota Água
- Água derrota Fogo.

O objetivo de cada duelo é ganhar 3 vezes à aranha inimiga. Perdemos caso sejamos derrotados 3 vezes.

No fim do combate, para voltarmos ao quarto basta pressionar a tecla "m"

Finalmente, o objetivo final do jogo é derrotar as 3 aranhas inimigas, coletando assim os 
3 elementos.

### Trabalho desenvolvido por:
# Rúben Martins a64566
# Pedro Gonçalves a64644
# Hugo Sá a61269
# Mouna Altahhan a77568