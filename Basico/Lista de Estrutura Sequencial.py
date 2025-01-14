# %% [markdown]
# # Lista de Estrutura Sequencial

# %% [markdown]
# #### 1. Faça um Programa que mostre a mensagem (print) "Alo mundo" na tela.

# %%
# Programa para exibir a mensagem "Alo mundo" na tela
def exibir_mensagem():
    """
    Função que exibe a mensagem 'Alo mundo' na tela.
    """
    print("Alo mundo")

# Chamada da função
exibir_mensagem()


# %% [markdown]
# #### 2. Faça um Programa que peça um número (input) e então mostre a mensagem: "O número informado foi [número]."

# %%
def numero():
    """
    Função que solicita ao usuário um número ou comando de saída e exibe o número informado.
    Exibe uma mensagem de encerramento quando o comando de saída é inserido.
    
    A função continua a solicitar a entrada até que 'sair' ou 'exit' seja digitado.
    """
    while True:
        try:
            # Solicitar entrada do usuário
            numeros = input("Informe o número ou digite 'sair' ou 'exit': ").strip().lower()
            
            # Verificar se o comando de saída foi inserido
            if numeros in ["sair", "exit"]:
                print("Encerrando o programa. Até logo!")
                break

            # Tentar converter a entrada em um número
            convert = float(numeros)
            print(f"O número informado foi: {convert}")
                
        except ValueError:
            # Tratamento para entradas inválidas
            print("Entrada inválida, favor digitar um número.")

# Chamada da função
numero()


# %% [markdown]
# #### 3. Faça um Programa que peça dois números e imprima a soma.

# %%
def soma():
    """
    Função que solicita ao usuário dois números e imprime a soma.
    A função lida com entradas inválidas e pede novamente até receber dois números válidos.
    """
    lista_soma = []
    
    # Continuar solicitando números até que dois números válidos sejam inseridos
    while len(lista_soma) < 2:
        try:
            # Solicitar número
            numero = float(input(f"Informe o número {len(lista_soma) + 1}: "))
            lista_soma.append(numero)
        except ValueError:
            # Tratamento para entradas inválidas
            print("Entrada inválida, favor digitar um número.")

    # Calcular e exibir a soma
    resultado = sum(lista_soma)
    print(f"A soma dos números é {resultado}")

# Chamada da função
soma()


# %% [markdown]
# #### 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.

# %%
def media_notas(user):
    """
    Função que solicita ao usuário uma quantidade específica de notas e calcula a média.
    Lida com entradas inválidas e garante que as notas estejam entre 0 e 10.
    
    Parâmetros:
    user (int): O número de notas que o usuário deseja fornecer.
    
    Retorna:
    float: A média das notas fornecidas.
    """
    lista_notas = []
    
    # Solicita notas até que a quantidade desejada seja atingida
    while len(lista_notas) < user:
        try:
            nota1 = float(input(f"Passa a nota {len(lista_notas)+1} (de 0 a 10): "))
            
            # Verifica se a nota está no intervalo permitido
            if 0 <= nota1 <= 10:
                lista_notas.append(nota1)
            else:
                print("Uma nota de 0 a 10")
        except ValueError:
            # Trata entradas que não podem ser convertidas para número
            print("Entrada inválida, favor digitar um número")
    
    # Calcula e exibe a média das notas
    media = sum(lista_notas) / len(lista_notas)
    print("A média das notas é", media)
    return media

def pede_quantidade():
    """
    Função que solicita ao usuário a quantidade de notas que deseja inserir para o cálculo da média.
    Permite encerrar o programa digitando 'sair' ou 'exit'.
    """
    while True:
        try:
            # Solicita a quantidade de notas ou permite sair do programa
            user = input("Qual a quantidade de notas para média? (ou digite 'sair' para encerrar): ").strip().lower()
            
            # Verifica se o usuário deseja encerrar o programa
            if user in ["sair", "exit"]:
                print("Encerrando o programa. Até logo!")
                break
            
            # Verifica se a entrada é um número inteiro
            if user.isdigit():
                user = int(user)
                media_notas(user)
            else:
                print("Digite um número inteiro por favor")
        except ValueError:
            # Trata entradas inválidas
            print("Entrada inválida, favor digitar um número inteiro")

# Chamada da função principal
pede_quantidade()


# %% [markdown]
# #### 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).

# %%
def metros():
    """
    Função que converte metros para centímetros.
    Solicita ao usuário uma quantidade de metros e exibe a conversão correspondente.
    Permite encerrar o programa digitando 'sair' ou 'exit'.
    """
    while True:
        try:
            # Solicita a quantidade de metros ou permite sair do programa
            user = input("Qual a quantidade de metros? (ou digite 'sair' para encerrar): ").strip().lower()
            
            # Verifica se o usuário deseja encerrar o programa
            if user in ["sair", "exit"]:
                print("Encerrando o programa. Até logo!")
                break  
            
            # Converte a entrada para float e calcula a conversão para centímetros
            converte = float(user)
            centimentro = converte * 100
            print(f"A conversão de {converte} metros para centímetros é: {centimentro}")
            
        except ValueError:
            # Trata entradas inválidas
            print("Entrada inválida, favor digitar a metragem")

# Chamada da função
metros()

        

# %% [markdown]
# #### 6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.

# %%
def calcula_area():
    """
    Função que calcula a área de um retângulo com base no comprimento e na largura fornecidos pelo usuário.
    Lida com entradas inválidas e solicita novamente até receber números válidos.
    
    Retorna:
    float: A área calculada.
    """
    comprimento = None
    largura = None

    # Continua solicitando valores até que ambos comprimento e largura sejam fornecidos corretamente
    while comprimento is None or largura is None:
        try:
            if comprimento is None:
                comprimento = float(input("Informe o comprimento: "))
            if largura is None:
                largura = float(input("Informe a largura: "))
        except ValueError:
            # Tratamento de entradas inválidas
            print("Entrada inválida, favor digitar um número válido.")
            if comprimento is not None and largura is None:
                continue  # Continua pedindo a largura se o comprimento já foi inserido
            else:
                comprimento = None  # Reseta ambos os valores em caso de erro

    # Calcula e exibe a área do retângulo
    area = comprimento * largura
    print("A área é:", area)
    return area

# Chamada da função
calcula_area()


# %% [markdown]
# #### 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# %%
def calcula_salario():
    """
    Função que calcula o salário mensal com base no valor ganho por hora e no número de horas trabalhadas.
    Lida com entradas inválidas e solicita novamente até receber números válidos.
    
    Retorna:
    float: O salário total do mês.
    """
    dinheiro = None
    hora = None

    # Continua solicitando os valores até que ambos (dinheiro e horas) sejam fornecidos corretamente
    while dinheiro is None or hora is None:
        try:
            if dinheiro is None:
                dinheiro = float(input("Informe o dinheiro ganhado por hora: "))
            if hora is None:
                hora = float(input("Informe a quantidade de horas trabalhadas por mês: "))
        except ValueError:
            # Tratamento de entradas inválidas
            print("Entrada inválida, favor digitar um número válido.")
            if dinheiro is not None and hora is None:
                continue  # Continua pedindo as horas se o valor por hora já foi inserido
            else:
                dinheiro = None  # Reseta ambos os valores em caso de erro

    # Calcula e exibe o salário mensal
    tutu = dinheiro * hora
    print("O salário do mês será:", tutu)
    return tutu

# Chamada da função
calcula_salario()


# %% [markdown]
# #### 8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# $C = \frac{5}{9}(F-32)$

# %%
def fah_para_cel():
    """
    Função que converte uma temperatura fornecida em Fahrenheit para Celsius.
    Lida com entradas inválidas e solicita novamente até receber um número válido.
    
    Retorna:
    tuple: Temperatura em Celsius (precisa e arredondada).
    """
    while True:
        try:
            # Solicita a temperatura em Fahrenheit
            fah = float(input("Informe a temperatura em Fahrenheit: "))

        except ValueError: 
            # Trata entradas inválidas
            print("Entrada inválida, favor digitar um número")

        # Converte para Celsius
        c = ((5/9) * (fah - 32))
        c_arredondado = round(c, 2)  # Arredonda o valor para 2 casas decimais

        # Exibe os resultados
        print("A temperatura em graus Celsius será:", c)
        print("A temperatura em graus Celsius arredondado será:", c_arredondado)
        
        return c, c_arredondado

# Chamada da função
fah_para_cel()
 

# %% [markdown]
# #### 9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# $F = \frac{9}{5}C + 32$

# %%
def cel_para_fah():
    """
    Função que converte uma temperatura fornecida em Celsius para Fahrenheit.
    Lida com entradas inválidas e solicita novamente até receber um número válido.
    
    Retorna:
    tuple: Temperatura em Fahrenheit (precisa e arredondada).
    """
    while True:
        try:
            # Solicita a temperatura em Celsius
            cel = float(input("Informe a temperatura em Celsius: "))

        except ValueError: 
            # Trata entradas inválidas
            print("Entrada inválida, favor digitar um número")

        # Converte para Fahrenheit
        f = (((9/5) * cel) + 32)
        f_arredondado = round(f, 2)  # Arredonda o valor para 2 casas decimais

        # Exibe os resultados
        print("A temperatura em graus Fahrenheit será:", f)
        print("A temperatura em graus Fahrenheit arredondado será:", f_arredondado)
        
        return f, f_arredondado

# Chamada da função
cel_para_fah()


# %% [markdown]
# #### 10. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# $P = 72,7h - 58$

# %%
def peso_ideal():
    """
    Função que calcula o peso ideal com base na altura fornecida pelo usuário, utilizando a fórmula de Peso Ideal de Hélio Gracie.
    Lida com entradas inválidas e solicita novamente até receber um número válido.
    
    Retorna:
    tuple: Peso ideal (preciso e arredondado).
    """
    while True:
        try:
            # Solicita a altura do usuário em metros
            altura = float(input("Informe a sua altura em METROS: "))

        except ValueError: 
            # Trata entradas inválidas
            print("Entrada inválida, favor digitar um número")

        # Calcula o peso ideal usando a fórmula de Hélio Gracie
        calculo = ((72.7 * altura) - 58)
        calculo_arredondado = round(calculo, 2)  # Arredonda o resultado para 2 casas decimais

        # Exibe os resultados
        print(f"O seu peso ideal será: {calculo} KG ")
        print(f"O seu peso ideal arredondado será: {calculo_arredondado} KG ")
        
        return calculo, calculo_arredondado

# Chamada da função
peso_ideal()


# %% [markdown]
# #### 11. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# ##### a. Para homens: $P = 72,7h - 58$
# ##### b. Para mulheres: $P = 62,1h - 44,7$

# %%
def pede_escolha():
    """
    Função que solicita ao usuário o sexo (H ou M) e retorna a escolha.
    A função lida com entradas inválidas e continua pedindo até receber uma resposta válida.
    
    Retorna:
    str: O sexo do usuário ('h' ou 'm').
    """
    while True: 
        try:
            # Solicita o sexo do usuário (H ou M)
            sexo = input("Qual o seu sexo? (H ou M): ").lower()
            if sexo in ("h", "m"):
                return sexo
        except ValueError: 
            # Trata entradas inválidas
            print("Entrada inválida, favor digitar um número")

def pede_altura():
    """
    Função que solicita a altura do usuário em metros e retorna o valor.
    Lida com entradas inválidas e continua pedindo até receber um número válido.
    
    Retorna:
    float: A altura do usuário em metros.
    """
    while True: 
        try:
            # Solicita a altura do usuário em metros
            altura = float(input("Informe a sua altura em METROS: "))
            return altura
        except ValueError: 
            # Trata entradas inválidas
            print("Entrada inválida, favor digitar sua altura em METROS.")

def calcula():
    """
    Função que calcula o peso ideal com base no sexo e altura fornecidos.
    Utiliza fórmulas diferentes dependendo do sexo (masculino ou feminino).
    Lida com entradas inválidas e exibe o peso ideal do usuário.
    
    Retorna:
    float: O peso ideal calculado.
    """
    while True:
        try:
            # Solicita o sexo e a altura
            sexo = pede_escolha()
            altura = pede_altura()

            # Calcula o peso ideal dependendo do sexo
            if sexo == "m":
                calculo = ((62.1 * altura) - 44.7)  # Fórmula para mulheres
            else:
                calculo = ((72.7 * altura) - 58)   # Fórmula para homens

            # Exibe o peso ideal calculado
            print(f"O seu peso ideal será: {calculo} KG ")
            break
        except ValueError: 
            # Trata qualquer erro inesperado
            print("Erro")

    return calculo

# Chamada da função
calcula()


# %% [markdown]
# #### 12. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

# %%
def pergunta():
    """
    Função que solicita ao usuário o valor do dinheiro ganho por hora e a quantidade de horas trabalhadas por mês.
    Lida com entradas inválidas e solicita novamente até que ambos os valores sejam válidos.
    
    Retorna:
    list: Uma lista contendo o valor ganho por hora e a quantidade de horas trabalhadas no mês.
    """
    horas = None
    numero_hora = None

    while horas is None or numero_hora is None:
        try:
            # Solicita o valor do dinheiro ganho por hora
            if horas is None:
                horas = float(input("Informe o dinheiro ganhado por hora: "))
            # Solicita a quantidade de horas trabalhadas por mês
            if numero_hora is None:
                numero_hora = float(input("Informe a quantidade de horas trabalhadas por mês: "))
        except ValueError:
            # Trata entradas inválidas e solicita novamente
            print("Entrada inválida, favor digitar um número válido.")
            # Continua pedindo a quantidade de horas trabalhadas até receber um valor válido
            if horas is not None and numero_hora is None:
                continue
            else:
                horas = None
                numero_hora = None

    return [horas, numero_hora]

# Chamada da função
pergunta()


# %% [markdown]
# #####  Calcule o salário bruto (horas * salario por hora)

# %%
def salario_bruto():
    """
    Função que calcula o salário bruto com base no valor do dinheiro ganho por hora e na quantidade de horas trabalhadas por mês.
    Utiliza os dados obtidos pela função 'pergunta' para calcular o salário bruto.
    
    Retorna:
    float: O salário bruto calculado.
    """
    # Obtém os dados (horas e salário por hora) chamando a função 'pergunta'
    pega_dados = pergunta()
    horas = pega_dados[0]  # Valor ganho por hora
    salario = pega_dados[1]  # Quantidade de horas trabalhadas por mês
    
    # Calcula o salário bruto multiplicando as horas pelo salário
    bruto = horas * salario
    
    return bruto

# Chamada da função
salario_bruto()


# %% [markdown]
# ##### Calcule o desconto do IR (11% do salário bruto)

# %%
def desconto_IR(bruto):
    """
    Função que calcula o desconto de imposto de renda sobre o salário bruto.
    O cálculo é feito com base em uma alíquota de 11%.
    
    Parâmetros:
    bruto (float): O valor do salário bruto a ser calculado.
    
    Retorna:
    float: O valor do imposto de renda a ser descontado.
    """
    # Calcula o imposto de renda com base no salário bruto (11%)
    imposto = bruto * (11 / 100)
    
    return imposto

# Chamada da função
desconto_IR(3000)  # Exemplo de chamada com salário bruto de 3000


# %% [markdown]
# ##### Calcule o desconto do INSS (8% do salário bruto)

# %%
def desconto_inss(bruto):
    """
    Função que calcula o desconto de INSS sobre o salário bruto.
    O cálculo é feito com base em uma alíquota de 8%.
    
    Parâmetros:
    bruto (float): O valor do salário bruto a ser calculado.
    
    Retorna:
    float: O valor do desconto de INSS a ser aplicado.
    """
    # Calcula o desconto do INSS com base no salário bruto (8%)
    imposto = bruto * (8 / 100)
    
    return imposto

# Chamada da função
desconto_inss(3000)  # Exemplo de chamada com salário bruto de 3000


# %% [markdown]
# ##### Calcule o desconto do sindicato (5% do salário bruto)

# %%
def desconto_sindicato(bruto):
    """
    Função que calcula o desconto para o sindicato sobre o salário bruto.
    O cálculo é feito com base em uma alíquota de 5%.
    
    Parâmetros:
    bruto (float): O valor do salário bruto a ser calculado.
    
    Retorna:
    float: O valor do desconto para o sindicato a ser aplicado.
    """
    # Calcula o desconto do sindicato com base no salário bruto (5%)
    imposto = bruto * (5 / 100)
    
    return imposto

# Chamada da função
desconto_sindicato(3000)  # Exemplo de chamada com salário bruto de 3000


# %% [markdown]
# ##### Calcule o salário líquido (salário bruto - descontos)

# %%
def main():
    """
    Função principal que calcula o salário bruto, descontos de IR, INSS e sindicato, 
    e o salário líquido com base nos dados informados pelo usuário.
    
    Passos:
    1. Chama a função 'salario_bruto' para calcular o salário bruto.
    2. Chama as funções 'desconto_IR', 'desconto_inss' e 'desconto_sindicato' 
       para calcular os descontos sobre o salário bruto.
    3. Calcula o salário líquido subtraindo os descontos do salário bruto.
    4. Exibe um resumo do salário bruto, descontos e salário líquido.
    
    Retorna:
    float: O salário líquido calculado após os descontos.
    """
    # Calcula o salário bruto
    bruto = salario_bruto()

    # Calcula os descontos de IR, INSS e Sindicato
    ir = desconto_IR(bruto)
    inss = desconto_inss(bruto)
    sindicato = desconto_sindicato(bruto)

    # Calcula o salário líquido subtraindo os descontos do salário bruto
    salario_liquido = bruto - (ir + inss + sindicato)

    # Exibe o resumo do salário com os descontos
    print(f"\nResumo do salário:\n")
    print(f"Salário Bruto: R$ {bruto:.2f}")
    print(f"Desconto IR: R$ {ir:.2f}")
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Desconto Sindicato: R$ {sindicato:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

    return salario_liquido


# Chama a função principal
main()


# %% [markdown]
# #### 13. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# %%
def loja_tintas():
    """
    Função que calcula a quantidade de latas de tinta necessárias para pintar uma área 
    e o custo total, com base no tamanho da área fornecido pelo usuário.
    
    O cálculo assume que cada lata de tinta cobre 18 metros quadrados e que cada lata custa R$ 80,00.
    
    Passos:
    1. Solicita ao usuário a área a ser pintada (em metros quadrados).
    2. Calcula a quantidade de litros necessários, considerando que 1 litro cobre 3 metros quadrados.
    3. Determina o número de latas de tinta necessárias, arredondando para cima caso a quantidade de litros não seja um múltiplo exato de 18.
    4. Calcula o preço total com base no número de latas.
    5. Exibe a quantidade de latas e o custo total.
    """
    # Loop para garantir que a entrada seja válida
    while True:
        try:
            # Solicita a área a ser pintada
            area = float(input("Informe o tamanho da área a ser pintada (em metros quadrados): "))
        except ValueError:
            # Mensagem de erro caso o valor informado não seja válido
            print("Entrada inválida. Por favor, insira um número válido para a área.")
            continue

        # Calcula a quantidade de litros necessários
        litros = area / 3

        # Calcula o número de latas, arredondando para cima se necessário
        latas = int(litros / 18)
        if litros % 18 != 0:
            latas = latas + 1

        # Calcula o preço total
        preco = latas * 80
        
        # Exibe a quantidade de latas e o custo total
        print(f"A quantidade de latas a serem compradas é: {latas:.2f}")
        print(f"O custo total será: R$ {preco:.2f}")
        
        # Sai do loop após a execução bem-sucedida
        break

# Chama a função para executar
loja_tintas()


# %% [markdown]
# #### 14. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
# 
# Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. Um megabit é 1/8 de um megabyte. 

# %%
def dowload():
    """
    Função que calcula o tempo aproximado de download de um arquivo com base no tamanho do arquivo e na velocidade de conexão do usuário.
    
    Passos:
    1. Solicita ao usuário o tamanho do arquivo (em MB) e a velocidade da internet (em Mbps).
    2. Converte a velocidade de Mbps para MB por segundo, dividindo por 8.
    3. Calcula o tempo em segundos que levaria para baixar o arquivo e converte esse tempo para minutos.
    4. Exibe o tempo aproximado de download.
    """
    tamanho = None
    velocidade = None

    # Loop para garantir que as entradas sejam válidas
    while tamanho is None or velocidade is None:
        try:
            # Solicita o tamanho do arquivo
            if tamanho is None:
                tamanho = float(input("Informe o tamanho do arquivo (em MB): "))
            # Solicita a velocidade da internet
            if velocidade is None:
                velocidade = float(input("Informe a velocidade de sua internet (em Mbps): "))
        except ValueError:
            # Mensagem de erro caso o valor informado não seja válido
            print("Entrada inválida, favor digitar um número válido.")

        # Converte a velocidade de Mbps para MB por segundo
        converte_Mb_para_MB = velocidade / 8
        
        # Calcula o tempo de download em segundos e depois converte para minutos
        MB_em_segundos = tamanho / converte_Mb_para_MB
        MB_em_minutos = MB_em_segundos / 60
        
        # Exibe o tempo aproximado de download
        print(f"O tempo aproximado de download é: {MB_em_minutos:.2f} minutos.")

    # Retorna o tempo em minutos
    return MB_em_minutos

# Chama a função para executar
dowload()



