🏦 Sistema Bancário em Python

Feito por: Victor Vicente  

Um sistema bancário simples desenvolvido em **Python**, projetado para simular as principais operações de uma conta corrente: **depósito**, **saque** e **extrato**.  
Este projeto foi feito para fins de aprendizado e prática de lógica de programação, estruturas condicionais e laços de repetição.

---

🚀 Funcionalidades

O sistema permite ao usuário:

- **[d] Depositar:** adicionar dinheiro à conta.
- **[s] Sacar:** retirar dinheiro respeitando o limite de saque.
- **[e] Extrato:** visualizar o histórico de movimentações e o saldo atual.
- **[q] Sair:** encerrar o programa.

---

⚙️ Regras do Sistema

- O **limite máximo por operação** é de **R$ 500,00**.  
- O **número máximo de saques diários** é **3**.  
- Não é permitido realizar **depósitos ou saques com valores negativos ou zero**.  
- O **extrato** exibe todas as movimentações realizadas (depósitos e saques).  
- Caso nenhuma movimentação tenha sido feita, o sistema informa que **nenhuma operação foi registrada**.

---

💻 Como Executar o Programa

Pré-requisitos
- Ter o **Python 3** instalado em sua máquina.

Passos
1. Baixe ou copie o código para um arquivo chamado `sistema_bancario.py`
2. Abra o terminal (ou prompt de comando) no diretório onde o arquivo está salvo.
3. Execute o comando:
   ```bash
   python sistema_bancario.py
O menu principal será exibido:

csharp
Copiar código
======= Selecione a opção desejada =======

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==========================================
=> 
Digite a letra correspondente à operação desejada e siga as instruções.

🧠 Exemplo de Uso
ruby
Copiar código
======= Selecione a opção desejada =======

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==========================================

=> d
Digite um valor para depósito: 200
Depósito realizado com sucesso!

=> s
Informe o valor para saque: 100
Saque realizado com sucesso!

=> e

=============== Extrato ===============
Depósito: R$ 200.00
Saque: R$ 100.00

Saldo: R$ 100.00
=======================================

🧩 Tecnologias Utilizadas
Python 3

input() para interação com o usuário

Estruturas condicionais (if, elif, else)

Laço while

Variáveis numéricas e strings

📚 Aprendizados
Durante o desenvolvimento deste projeto, foram praticados:

Estrutura de repetição com controle de saída (while True)

Manipulação de variáveis numéricas e strings

Validação de entradas do usuário

Criação de mensagens dinâmicas e personalizadas

Lógica de negócio simples com condições compostas

🧑‍💻 Autor
Projeto desenvolvido por Victor Vicente.
💬 Caso queira trocar ideias sobre programação ou Python, entre em contato!

📝 Licença
Este projeto é de uso livre para fins educacionais.
Sinta-se à vontade para modificar e aprimorar o código!


Quer que eu adicione uma **seção de melhorias futuras**, como “fazer login com usuário e senha”, “armazenar dados em arquivo” ou “adicionar interface gráfica”? Posso incluir isso no README também.
