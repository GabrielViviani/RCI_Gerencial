import pandas as pd

df = pd.read_excel(r"C:\Users\55219\Desktop\Temporario MesaRV\mock_data.xlsx", usecols=[0,1,2])  
menu = int(input("O que gostaria de fazer? \n 1 - Pesquisar um código de cliente \n 2 - Adicionar um novo cliente \n 3 - Visualizar tabela de dados \n 4 - Encerrar o programa \n Selecione uma alternativa válida: "))

if menu == 1:
    
    code = int(input("Insira o código do cliente: "))
    filtered_df = df.loc[df['Cliente'] == code]
    
    if not filtered_df.empty:
        
        nome = filtered_df['Nome'].values[0]
        cliente = filtered_df['Cliente'].values[0]
        patrimonio = filtered_df['Patrimônio'].values[0]
        
        print(f"O cliente de código {code} possui as seguintes informações: \n\n Nome: {nome}\n Patrimônio: {patrimonio} \n")
    else:
        print("Nenhum cliente com o código fornecido foi encontrado.")

elif menu == 2:
    new_code = int(input("Por favor, insira o código do novo cliente: "))
    new_name = str(input("Agora insira o nome do cliente, por favor: "))
    new_networth = float(input("Qual o patrimônio atual do cliente? "))
    
    new_client = pd.DataFrame({'Cliente': [new_code],
                            'Nome': [new_name],
                            'Patrimônio': [new_networth]})
    
    df = pd.concat([df, new_client], ignore_index=True)
    
    df.to_excel(r"C:\Users\55219\Desktop\Temporario MesaRV\mock_data.xlsx", index=False)
    
elif menu == 3:
    print(df)
    
elif menu == 4:
    print("Programa encerrado.")
