# Desafio Python

Foram repassadas **três** questões para o desafio de Python, porém, além das três questões, o **desafio de Excel** também foi resolvido em Python de forma extra. Sendo assim, neste repositório estão contidas as três questões obrigatórias e o trabalho extra realizado.

As possibilidades de execução e a divisão do código serão explicadas separadamente a seguir.
* **
## Preparação do ambiente

Para a execução dos programas em Python pode ser necessário a instalação de alguns pacotes, caso ainda não estejam instalados:

### Instalação dos pacotes necessários

Os pacotes que devem ser instalados para a execução dos programas são os seguintes:

 * numpy
 * pandas

sendo que apenas o `numpy` é necessário nos testes obrigatórios, sendo utilizado na questão 3

Uma das possibilidade para instalação dos pacotes é via via pip3. Portanto, o passo a passo para preparação do ambiente, partindo do princípio de que a máquina já possua o `python3` instalado seria:

 1. Execute o comando

        sudo apt updtate

 1. Instale o `pip3`, caso ainda não tenha instalado, utilizando o comando:

        sudo apt install python3-pip

 3. Instale o `numpy`, caso ainda não tenha instalado, utilizando o comando:

        pip3 install numpy

 4. Instale o `pandas`, caso ainda não tenha instalado, utilizando o comando:

        pip3 install pandas

Caso nenhuma mensagem de erro apareça seu ambiente estará pronto para executar todas as funcionalidades da aplicação.

* **
## Possibilidades de execução

Os arquivos `question_1.py`, `question_2.py` e `question_3.py`, corrrespondem, respectivamente, à **resolução das questões 1, 2 e 3** que foram propostas. Todos os arquivos relacionados ao código extra, que reproduz o desafio de Excel, estão armazenados na pasta `ex2python`. As instruções a seguir pressupõem que esta pasta já está sendo acessada via terminal ou interface gráfica do sistema operacional

### 1 - Execução da Questão 1

Para executar a aplicação utilizando o terminal, basta abrir o terminal na pasta onde se localiza o arquivo `question_1.py` e executar o seguinte comando:

    python3 question_1.py

Ao fim da execução do programa, é impressa na tela do terminal a resposta referente à pergunta proposta.

### 1 - Execução da Questão 1

Para executar a aplicação utilizando o terminal, basta abrir o terminal na pasta onde se localiza o arquivo `question_2.py` e executar o seguinte comando:

    python3 question_2.py

Ao fim da execução do programa, é impressa na tela do terminal a resposta referente à pergunta proposta.

### 1 - Execução da Questão 3

Para executar a aplicação utilizando o terminal, basta abrir o terminal na pasta onde se localiza o arquivo `question_3.py` e executar o seguinte comando:

    python3 question_3.py

Será solicitado ao usuário que insira, via terminal, a quantidade de alunos que deseja inserir, após isso serão solicitadas as inserções do nome e da nota de cada aluno.

Ao fim da execução do programa, é impressa na tela do terminal a resposta referente à pergunta proposta.

### 4 - Execução da Questão Extra (Teste de Excel)

Para executar a aplicação utilizando o terminal, basta abrir o terminal na pasta `ex2python/src` e executar o seguinte comando:

    python3 principal.py

Ao fim da execução do programa, são impressas na tela do terminal as respostas referentes a todas as perguntas propostas no teste de Excel


## Divisão do código da pasta ex2python
Arquivo onde estão escritos os testes relacionados as funções responsáveis por saídas de dados
para o usuário que estão escritas no arquivo src/saidas.py
A pasta raiz contém três diretórios distintos:

 * **dados**: Diretório onde está o arquivo `Dados.xlsx`, onde são armazenados os dados utilizados pelo programa.

 * **src**: Diretório onde estão armazenados os arquivos Python relativos ao código fonte do programa desenvolvido.
    - [principal.py](./code/src/principal.py): Programa principal que faz a leitura do banco de dados dos aquivos e imprime os resultados desejados.
    - [saidas.py](./code/src/saidas.py): Arquivo onde estão escritas as funções relacionadas a geração de informações de saida para o usuário.
    - [funcs.py](./code/src/tratamento.py): Arquivo onde estão escritas as funções relacionadas a manipulação dos dataframes utilizados no programa
