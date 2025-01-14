# Lista de produtos vazia para armazenar os produtos cadastrados
produtos = [] 

# Função para cadastrar produtos
def cadastro_produto():
    """
    Função que solicita ao usuário o nome de um produto e o cadastra em uma lista,
    evitando duplicatas. O processo continua até que o usuário digite 'sair' para finalizar.
    
    A função também exibe mensagens de sucesso ou de erro caso o produto já exista.
    """
    while True:
        try:
            # Solicitar entrada do nome do produto
            user = input("Digite o nome do produto (ou 'sair' para finalizar): ").lower()
            
            # Verificar se o usuário deseja sair
            if user == 'sair': 
                break
            
            # Verificar se o produto já foi cadastrado
            elif user not in produtos:
                produtos.append(user)  
                print("Produto cadastrado com sucesso!")
            else:
                print("Produto já existe, tente novamente")
        
        except ValueError:
            print("Houve um erro inesperado, tente novamente")

# Chamada da função para iniciar o cadastro dos produtos
cadastro_produto()

print("Lista de produtos atualizada:", produtos)

