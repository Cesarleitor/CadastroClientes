from multiprocessing.util import close_all_fds_except


class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir_detalhes(self):
        """Método para exibir os detalhes do cliente"""
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')
        print(f'Telefone: {self.telefone}')
        print("-" * 30)

class Cadastro:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        """Método para adicionar um cliente ao cadastro"""
        self.clientes.append(cliente)

    def listar_clientes(self):
        """Método para listar todos os clientes cadastrados"""
        if not self.clientes:
            print('Nenhum cliente cadastrado.')
        else:
            print('Clientes cadastrados:')
            for cliente in self.clientes:
                cliente.exibir_detalhes()


cadastro = Cadastro()

while True:
    print("1. Cadastrar novo cliente")
    print("2. Listar todos os clientes")
    print("3. Sair")

    opcao = input('Escolha uma opção:')

    if opcao == "1":
        nome = input('Digite o nome do cliente')
        email = input('Digite o email do cliente')
        telefone = input('Digite o telefone do cliente')

        cliente = Cliente(nome, email, telefone)
        cadastro.adicionar_cliente(cliente)
        print('Cliente cadastrado com sucesso!\n')

    elif opcao == "2":
        cadastro.listar_clientes()

    elif opcao == "3":
        print('Saindo do sistema')
        break

    else:
        print('Opção invalida, tente novamente.\n')

