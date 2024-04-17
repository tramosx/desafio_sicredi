# README

Este é um projeto relacionado ao desafio da SICREDI

## Requisitos

- Python 3.6.9

## Instalação de Requisitos

Para instalar as dependências do projeto, você pode usar o gerenciador de pacotes `pip`. Execute o seguinte comando no terminal:

```
pip install -r requirements.txt
```

Certifique-se de estar no diretório raiz do projeto ao executar este comando.

## Executando os Testes

Para executar os testes unitários, você pode usar o `make`. Certifique-se de ter o `make` instalado em seu sistema. Em seguida, execute o seguinte comando no terminal:

```
make test_all
```

Isso executará todos os testes unitários definidos nos arquivos `test_question1.py` e `test_question2.py`.

Se desejar executar apenas os testes relacionados à primeira questão, você pode usar o seguinte comando:

```
make test_question1
```

E para executar apenas os testes relacionados à segunda questão, você pode usar este comando:

```
make test_question2
```
