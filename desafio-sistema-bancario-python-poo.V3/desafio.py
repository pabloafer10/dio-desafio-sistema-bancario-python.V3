from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
import textwrap

# Para V3 a classe Cliente representa um cliente bancário, armazenando endereço e contas associadas.
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    # Método para realizar uma transação vinculada a uma conta específica.
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    # Método para associar uma nova conta ao cliente.
    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Para V3 a classe PessoaFisica herda de Cliente e adiciona informações pessoais (CPF, nome, data de nascimento).
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento 

# Para V3 a classe Conta representa uma conta bancária, armazenando saldo, número da conta, agência e histórico de transações.  
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente  
        self._historico = Historico()
    
    # Método de classe para criar uma nova conta associada a um cliente específico.
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    # Propriedades para acessar atributos protegidos.
    @property  
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    # Método para realizar saques, respeitando saldo disponível. 
    # Em caso de exceder o saldo, exibir mensagem "Saldo insuficiente, retorne ao menu e tente novamente."
    # Em caso valor inválido, exibir mensagem "Valor de saque inválido, retorne ao menu e tente novamente."
    # Em caso saque realizado, exibir mensagem "Saque realizado com sucesso!."
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\n@@@ Saldo insuficiente, retorne ao menu e tente novamente. @@@")
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Valor de saque inválido, retorne ao menu e tente novamente. @@@")
            
        return False
    
    # Método para realizar depósitos, aceitando apenas valores positivos.  
    # Em caso de exceder o saldo, exibir mensagem "Saldo insuficiente, retorne ao menu e tente novamente."
    # Em caso valor inválido, exibir mensagem "Valor de depósito inválido, retorne ao menu e tente novamente."
    # Em caso saque realizado, exibir mensagem "Depósito realizado com sucesso!."    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")     
        else:
            print("\n@@@ Valor de deposito inválido, retorne ao menu e tente novamente. @@@")
            return False
         
        return True
   
# Para V3 a classe Conta Corrente herda de Conta e adiciona limites de saque diário e valores máximos permitidos.
# Em caso de exceder o limite de valor do saque, exibir mensagem "Valor excede o limite de saque, retorne ao menu e tente novamente.".
# Em caso de exceder o limite diário de saque, exibir mensagem "Limite de saques diário excedido, retorne ao menu e tente novamente.".
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saque = limite_saques
    
    # Sobrescreve o método sacar para aplicar as regras de limite de saque   
    def sacar(self, valor):
        numero_saque = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saque >= self._limite_saque
        
        if excedeu_limite:
            print("\n@@@ Valor excede o limite de saque, retorne ao menu e tente novamente. @@@")
        
        elif excedeu_saques:
            print("\n@@@ Limite de saques diário excedido, retorne ao menu e tente novamente mais tarde.  @@@")
            
        else:
            return super().sacar(valor)
        
        return False
    
    # Representação em string da conta corrente.
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            Saldo:\t{self.saldo:.2f}
        =======================================
        """
            
# Para V3 a classe Histórico armazena todas as transações realizadas em uma conta.   
class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes

    # Método para registrar uma nova transação.
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )

# Para V3 a classe(interface) abstrata Transação abstrata Transacao serve como interface para transações financeiras.          
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass

# Para V3 a classe Saque representa uma operação de saque
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
           
# Para V3 a classe Depósito representa uma operação de depósito.              
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            
# Menu de opções de operações bancárias com opções de 0-6.
def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tCriar Cliente
    [5]\tCriar Conta
    [6]\tListar Contas
    [0]\tSair
    =======================================
    Por favor, selecione a opção desejada (0-6): 
    => """
    return input(textwrap.dedent(menu))

# Para V3 o método de filtrar usuário passou por uma refatoração, passou a chamar filtrar cliente e deverá filtrar cliente pelo cpf e retornar se foi ou não localizado o cliente filtrato.
def filtrar_cliente(cpf, clientes):
        clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None

# Para V3 o novo método de recuperar a conta do cliente deverá filtrar cliente e retornar se o cliente possui ou não conta existente.
# Em caso de não localizar cliente, exibir mensagem "Cliente não possui conta cadastrada, retorne ao menu e tente novamente."
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta cadastrada, retorne ao menu e tente novamente. @@@")
        return

      # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

# Para V3 a função de depositar passou por uma refatoração, porém deverá a continuar recebendo somente valores positivos, todos depósitos deve ser armazenados agora não mais em uma variavel, e sim numa classe e exibir e ser armazenada na classe Histórico. 
# Em caso de não localizar o cliente deve ser exibido a mensagem: "Cliente não localizado, retorne ao menu e tente novamente.".
def depositar(clientes):
    cpf = input("Informe o número do CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não localizado, retorne ao menu e tente novamente. @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


# Para V3 a função de sacar passou por uma refatoração,função Sacar deve continuar recebendo limite e limite diário. 
# Em caso de não localizar o cliente deve ser exibido a mensagem: "Cliente não localizado, retorne ao menu e tente novamente.".
def sacar(clientes):
    cpf = input("Informe o número do CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não localizado, retorne ao menu e tente novamente. @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)
 
# Para V3 a função de exibir extrato passou por uma refatoração,função exibir extrato, deve exibir o extrato da conta corrente com todos os depósitos e saques realizados, No final, exibe o saldo disponível no formato: R$ xxx.xx.". 
# Em caso de não localizar o cliente deve ser exibido a mensagem: "Cliente não localizado, retorne ao menu e tente novamente.".
# Em caso de não haver movimentação deve ser exibido a mensagem: "Não foram realizado movimentações.".  
def exibir_extrato(clientes):
    cpf = input("Informe o número do CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n@@@ Cliente não localizado, retorne ao menu e tente novamente. @@@")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n==================== EXTRATO ====================")
    transacoes = conta.historico.transacoes
    
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizado movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
            
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("\n=================================================")

# Para V3 a função de criar usuário passou por uma refatoração, passou a chamar criar cliente.
# Em caso de cliente já cadastrado deve ser exibido a mensagem: "Já existe cliente cadastrado para o CPF, retorne ao menu e tente novamente com outro CPF.".
# Em caso de cliente ainda não cadastrado, deve ser exibido as mensagens "Informe o nome completo: ", "Informe a data de nascimento com (dd-mm-aaaa): " , "Informe o endereço completo com (logradouro, número, bairro, cidade/sigla do estado): "  
# Em caso de cliente cadastrado, deve ser exibida a mensagem "Cliente criado com sucesso!".    
def criar_cliente(clientes):
    cpf = input("Informe o número do CPF do cliente (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("\n@@@ Já existe cliente cadastrado para o CPF, retorne ao menu e tente novamente com outro CPF. @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento com (dd-mm-aaaa): ")
    endereco = input("Informe o endereço completo com (logradouro, número, bairro, cidade/sigla do estado): ")
    
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    
    clientes.append(cliente)
    
    print("\n=== Cliente criado com sucesso! ===")
    
# Função para criar uma conta com agência, número da conta e usuário, implemantada na V2 somente.
# Em caso de cliente não localizado deve ser exibido a mensagem: "Cliente não localizado, retorne ao menu e tente novamente.". 
# Em caso de conta criada, deve ser exibida mensagem "Conta criada com sucesso!".
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o número do CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n@@@ Cliente não localizado, retorne ao menu e tente novamente. @@@")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente,numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")

# Função para listar todas as contas cadastradas.
# Em caso de conta não localizada, deve ser exibida a mensagem "Nenhuma conta cadastrada."
# Em caso de conta localizada, deve ser exibida a lista de contas para o CPF informado.
def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return

    print("\n=========== Contas Cadastradas ============")
             
    for conta in contas:
        print(conta)
        
# Função principal (main) que controla o fluxo do programa
def main():
    clientes = []
    contas = []

# Laço de repetição para exibir o menu de opções    
    while True:
        opcao = menu()
        
# Menu de opções de operações bancárias inputadas pelo usuário ma opção 1 - Depositar         
        if opcao == "1":
            depositar(clientes)
            
# Menu de opções de operações bancárias inputadas pelo usuário ma opção 2 - Sacar             
        elif opcao == "2":
            sacar(clientes)

# Menu de opções de operações bancárias inputadas pelo usuário ma opção 3 - Extrato       
        elif opcao == "3":
            exibir_extrato(clientes)
# Menu de opções de operações bancárias inputadas pelo usuário ma opção 4 - Criar Cliente        
        elif opcao == "4":
            criar_cliente(clientes)

# Menu de opções de operações bancárias inputadas pelo usuário ma opção 5 - Criar Conta        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

# Menu de opções de operações bancárias inputadas pelo usuário ma opção 6 - Listar Contas criadas           
        elif opcao == "6":
            listar_contas(contas)

# Menu de opções de operações bancárias inputadas pelo usuário ma opção 0 - Sair       
        elif opcao == "0":
            break

# Menu de opções de operações bancárias inputadas pelo usuário ma opção != 0-6 - inválida        
        else:
            print("\n@@@ Operação inválida, por favor tente novamente a opção desejada. @@@")
            
main()     

        
    

            

    