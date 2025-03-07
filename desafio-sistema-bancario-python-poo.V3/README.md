# 🏦 <u>Projeto Bootcamp DIO - Sistema Bancário - V3</u>

### <u>Objetivo geral</u>
##### **Manter toda regra de negócio já existente na V1 e V2, e implementar o novo conceito de POO e as novas regras para V3. Para V3 iremos implementar classes, remodelar as funções existentes de saque, depósito, extrato, criar conta, listar conta, e implementar novas funções de criar cliente(no lugar de usuário), filtrar cliente e recuperar conta cliente.**

### <u>Desafio</u>
##### **Nosso desafio consiste em modelar nosso sistema bancário com POO, onde adicionaremos classes para os clientes e as operações bancárias de depósito e saque, atualizando o sitema bancário para armazenar os dados do cliente e das operações bancárias em objetos e não mais em dicionários. Para isso iremos utilizar a modelagem UML como pré requisito, onde foi definido os métodos públicos e os métodos privados.**

### <u>Separação Classes, Funções e Métodos</u>
##### **Devemos criar classes e refatorar as funções e métodos para todas as operações do sistema, mantendo as regras de negócio atuais e implementando novas funcionalidades para nova versão.** 

## <u>Explicando o projeto</u>
##### **Este projeto é a versão 3 de um sistema bancário simples desenvolvido em Python, com funcionalidades básicas de operações financeiras como:**  
✔ <u>Existentes da V1:</u>  
✅ **Função de depósito**   
✅ **Função de saque**   
✅ **Função de extrato**  

✔✔ <u>Implementação da V2</u>  
✅✅ **Função de criar_usuário**  (deixará de existir dando lugar função criar_cliente Cliente)  
✅✅ **Função de criar_conta**  

✔✔✔ <u>Implementação da V3</u>  
✅✅✅ _**Criação de classe Cliente**_   
✅✅✅ _**Criação de classe PessoaFisica**_    
✅✅✅ _**Criação de classe Conta**_  
✅✅✅ _**Criação de classe ContaCorrente**_  
✅✅✅ _**Criação de classe Historico**_  
✅✅✅ _**Criação de classe Transacao**_  
✅✅✅ _**Criação de classe SaqueTransacao**_            
✅✅✅ _**Criação de classe DepositoTransacao**_       
✅✅✅ _**Criação de função realizar_transação**_  
✅✅✅ _**Criação de função adicionar_conta**_  
✅✅✅ _**Criação de função nova_conta**_   
✅✅✅ _**Criação de função sacar**_   
✅✅✅ _**Criação de função depositar**_  
✅✅✅ _**Criação de função adicionar_transacao**_  
✅✅✅ _**Criação de função registrar**_  
✅✅✅ _**Criação de função filtar_cliente**_  
✅✅✅ _**Criação de função recuperar_conta_cliente**_  
✅✅✅ _**Criação de função criar_cliente**_  
✅✅✅ _**Refatoração de função menu**_   
✅✅✅ _**Refatoração de função depositar**_  
✅✅✅ _**Refatoração de função sacar**_  
✅✅✅ _**Refatoração de função exibir_extrato**_  
✅✅✅ _**Refatoração de função listar_contas**_  
✅✅✅ _**Refatoração de função main**_

📌 **Regras de Negócio:**  
🔹 **Depósitos:**  
✔ V1 - Apenas valores positivos são permitidos.  
✔ V1 - Em caso de valor inválido deve ser exibido a mensagem: "Valor inválido, tente novamente."  
✔ V1 - Todos os depósitos devem ser armazenados e exibidos na consulta de extrato.  

✔✔ <u>Para V2:</u>  
✔✔ V2 - A função depósito deve receber os argumentos apenas por posição (positional only). 
✔✔ V2 - Sugestão de argumentos: saldo, valor, extrato.  
✔✔ V2 - Sugestão de retorno: saldo e extrato.  

✔✔✔ <u>Para V3 foi implemantado:</u>  
✔✔✔ **V3 - Deverá ser informado um CPF de cliente ao invés de usuário**
✔✔✔ **V3 - Deverá ser informado um CPF apenas com números**   
✔✔✔ **V3 - Em caso CPF não cadastrado, retorno de mensagem "Cliente não localizado! Informe um CPF cadastrado."**   
✔✔✔ **V3 - Em caso CPF cadastrado, aí poderá solicitar o valor e exibir mensagem "Informe o valor do depósito: "**  

🔹 **Saques:**  
✔ V1 - Limite diário de 3 saques.  
✔ V1 - Caso o limite diário de saque seja maior do que permitido, deve ser exibido a mensagem: "Limite de saques diário excedido! Por favor, tente novamente."  
✔ V1 - Valor máximo de R$ 500,00 por saque.  
✔ V1 - Caso o saldo seja insuficiente, deve ser exibido a mensagem: "Saldo insuficiente! Por favor, tente novamente."  
✔ V1 - Caso o valor do saque seja inválido, deve ser exibido a mensagem: "Valor informado inválido, tente novamente."  
✔ V1 - Todos os saques devem ser armazenados e exibidos na consulta de extrato.  

✔✔ <u>Para V2:</u>  
✔✔ V2 - A função saque deve receber os argumentos apenas por nome (keyword only).  
✔✔ V2 - Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.  
✔✔ V2 - Sugestão de retorno: saldo e extrato.  

✔✔✔ <u>Para V3 foi implemantado:</u>  
✔✔✔ **V3 - Deverá ser informado um CPF de cliente ao invés de usuário**
✔✔✔ **V3 - Deverá ser informado um CPF apenas com números**   
✔✔✔ **V3 - Em caso CPF não cadastrado, retorno de mensagem "Cliente não localizado! Informe um CPF cadastrado."**   
✔✔✔ **V3 - Em caso CPF cadastrado, aí poderá solicitar o valor e exibir mensagem "Informe o valor doe saque: "**

🔹 **Extrato:**  
✔ V1 - Deve listar todos os depósitos e saques realizados.  
✔ V1 - No final, exibe o saldo disponível no formato: R$ xxx.xx.                    

✔✔ <u>Para V2 incluiremos:</u>  
✔ V2 - A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).  
✔ V2 - Argumentos posicionais: saldo.  
✔ V2 - Argumentos nomeados: extrato.

✔✔✔ <u>Para V3 foi implemantado:</u>  
✔✔✔ **V3 - Deverá ser informado um CPF de cliente ao invés de usuário**
✔✔✔ **V3 - Deverá ser informado um CPF apenas com números**   
✔✔✔ **V3 - Em caso CPF não cadastrado, retorno de mensagem "Cliente não localizado! Informe um CPF cadastrado."**   
✔✔✔ **V3 - Em caso CPF cadastrado, deverá ser exibido extrato**
✔✔✔ **V3 - Em caso extrato sem movimentações, deverá ser exibido mensagem "Não foram realizado movimentações."**

🔹 **Criar Usuário**  
✔✔ V2 - Criar novos usuários:**  
✔✔ V2 - Armazenar os usuários em uma lista.**  
✔✔ V2 - Um usuário é composto por: nome, data de nascimento, cpf e endereço.**  
✔✔ V2 - O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado.**  
✔✔ V2 - Deve ser armazenado somente os números do CPF.**  
✔✔ V2 - Não podemos cadastrar 2 usuários com o mesmo CPF.**  

✔✔✔ <u>Para V3 foi implemantado:</u> 
✔✔✔ **V3 - Criar novos cliente(deixará de existir novos usuários):**  
✔✔✔ **V3 - Deverá ser informado um CPF de cliente ao invés de usuário**
✔✔✔ **V3 - Deverá ser informado um CPF apenas com números**  
✔✔✔ **V3 - Em caso de CPF já cadastrado, deve ser exibido mensagem "Já existe cliente cadastrado para o CPF, tente novamente com outro CPF."**
✔✔✔ **V3 - Em caso de CPF não cadastrado, deve ser informado exibido mensagens "Informe o nome completo: ", "Informe a data de nascimento com (dd-mm-aaaa): " , "Informe o endereço completo com (logradouro, número, bairro, cidade/sigla do estado): " e criar o cliente exibindo mensagem "Cliente criado com sucesso!"**

🔹 **Criar Conta**   
✔✔ V2 - Deve armazenar contas em uma lista.  
✔✔ V2 - Uma conta é composta por: agência, número da conta e usuário.  
✔✔ V2 - O número da conta é sequencial, iniciando em 1.  
✔✔ V2 - O número da agência é fixo: "0001".  
✔✔ V2 - O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.  

✔✔✔ <u>Para V3 foi implemantado:</u>
✔✔✔ **V3 - Deverá ser informado um CPF de cliente ao invés de usuário**
✔✔✔ **V3 - Deverá ser informado um CPF apenas com números**  
✔✔✔ **V3 - Em caso de CPF não ter conta cadastrada, deve ser exibido mensagem "Cliente não localizado, não foi possível criar conta.**
✔✔✔ **V3 - Em caso de CPF ter conta cadastrada, deve ser exibido mensagem "Conta criada com sucesso!**

🔹 **Listar Contas**
✔✔✔ **V3 - Em caso de digitar um CPf de cliente sem conta cadastrada, deve ser exibida mensagem "Nenhuma conta cadastrada."**
✔✔✔ **V3 - Em caso de digitar um CPf de cliente com conta cadastrada, deve ser exibida lista de conta cadastrada para CPF do cliente."**

🔹 **Outras regras:**  
✔ V1 - O usuário pode optar por sair do sistema a qualquer momento.  
✔ V1 - Se a entrada do usuário for inválida (não estiver no menu de opções), deve ser exibido a mensagem: "Opção inválida, por favor seleciona novamente a operação desejada."
