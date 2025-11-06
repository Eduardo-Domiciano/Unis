# Atividade 2

1. Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.
2. Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso os valores formem um triângulo, calcular e escrever a área deste triângulo. Se não formam triângulo escrever os valores lidos. (Se a > b + c não formam triângulo algum, se a é o maior).
3. Faça um programa que leia 3 números inteiros e mostre o menor deles.
4. Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.
5. Escreva uma função que:
Receba uma frase como parâmetro.
Retorne uma nova frase com cada palavra com as letras invertidas.

## Executavel
Empacotei um executavel Linux com o PyInstaller que esta na pasta Dist. Tentei empacotar pra windows em uma maquina virtual, mas nao conseguir corrigir um problema de OpenGL.

## Rodar Script
Se quiser rodar o codigo usei uma interface do kivy pra juntar tudo.
### Ambiente virtual
1. Instalar ambiente virtual Linux/Mac:
`python3 -m venv atividade` cria o ambiente com nome atividade
`source kivy_venv/bin/activate` Ativa o ambiente
2. Instalar ambiente virtual Windows:
`python -m venv atividade` cria o ambiente com nome atividade
`source atividade/Scripts/activate` Ativa usando o ==>"BASH"<==

### Kivi
1. Instalar o kivy no linux/Mac:
```
pip install --upgrade pip setuptools
pip install kivy[full]
```

2. Instalar o kivy no Windows:
`python.exe -m pip install --upgrade pip` atualiza o pip instaler
instala o kivy
```
pip install --upgrade pip setuptools wheel
pip install kivy[full]
```

### Modulo
Da pra fazer teste em cada modulo, mas fiz o kivy pq to apendendo como criar interface e to empolgado com isso por agora.