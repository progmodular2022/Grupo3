# Jogo das palavras - Grupo 3

É necessário que o pygame esteja instalado para rodar a aplicação. É possível instalar utilizando o gerenciador de pacotes pip com o seguinte comando: `pip install pygame`

## Descrição
O objetivo do jogo é formar palavras clicando nas letras presentes na tela. Caso a sua palavra formada seja válida a cor da palavra mudará para verde. Caso a palavra que você esteja tentando formar não seja válida, a cor da palavra mudará para vermelha.

O jogo está dividido por "contextos", sendo eles "frutas", "animais" e "fixo", para frutas e animais é utilizado uma lista de palavras específicas para cada caso. Uma lista contendo as possíveis frutas a serem formadas no jogo está presente em src/frutas.txt, e para animais src/animais.txt. As listas são extensas para tentar cobrir a maior quantidade de frutas e animais possíveis, porém é possível que alguma palavra "exótica" não possa ser formada no jogo. A aplicação garante que pelo menos uma palavra da lista de palavras estará presente no tabuleiro do jogo. Já o "fixo" possui uma palavra fixa que estará presente sempre, sendo neste caso a palavra "lixeira".

Para selecionar uma letra é necessário clicar em cima da mesma, e para "desselecionar" é possível tanto clicar novamente em cima da última letra marcada, ou clicar no botão "limpar" que irá desfazer todas as seleções de uma única vez.

### Estrutura de arquivos

* Os arquivos da aplicação se encontram na pasta `src/`, e os testes em `test/`. 

Para rodar o jogo execute o arquivo `main.py`

