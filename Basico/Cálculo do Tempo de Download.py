#1. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

#Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. Um megabit é 1/8 de um megabyte. 

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
