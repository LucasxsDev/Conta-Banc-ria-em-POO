# Conta Bancária 🏦

Um projeto de terminal feito em Python para praticar programação orientada a objetos e organização de código em módulos.

## O projeto

O programa permite cadastrar os dados de uma conta e realizar operações básicas pelo menu. A interface fica separada da classe `Conta`, para deixar cada parte do projeto com uma responsabilidade clara.

## Funcionalidades

- Cadastrar nome, número da conta e saldo inicial
- Consultar os dados da conta
- Fazer depósitos
- Fazer saques
- Validar opções e entradas numéricas no menu

## Estrutura

```text
ex-1/
├── conta Bancária.py       # Menu e fluxo principal
└── utils/
    ├── classes/
    │   └── dados.py        # Classe Conta
    └── interface/
        └── visual.py      # Elementos visuais do terminal
```

## Como executar

É necessário ter Python 3 instalado. O projeto não usa bibliotecas externas.

Abra o terminal na pasta do projeto e execute:

```bash
python "conta Bancária.py"
```

No Windows, também pode funcionar com:

```powershell
py "conta Bancária.py"
```

## Observação

Os dados da conta ficam apenas na memória enquanto o programa está aberto. Ao encerrar, eles não são salvos.

## Ideias para evoluir

- Impedir depósitos e saques com valores negativos
- Verificar se há saldo suficiente para o saque
- Salvar os dados para reutilizá-los em outra execução

Feito como exercício de estudo de Python e POO.
