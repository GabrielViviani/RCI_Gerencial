import pandas as pd

# Function to display the menu options
def display_menu():
    print("Sistema de Cadastro de Usuários")
    print("1 - Procurar usuário")
    print("2 - Adicionar usuário")
    print("3 - Ver todos os usuários")
    print("4 - Encerrar programa.")

# Function to search for a user by code
def search_user(df):
    code = int(input("Insira o código do usuário: "))
    filtered_df = df.loc[df['Code'] == code]
    
    if not filtered_df.empty:
        name = filtered_df['Name'].values[0]
        email = filtered_df['Email'].values[0]
        patrimonio = filtered_df['Net Worth'].values[0]
        
        print(f"Usuário do código {code} encontrado:\n")
        print(f"Nome: {name}")
        print(f"Email: {email}")
        print(f"Patrimônio: {patrimonio}\n")
    else:
        print("Nenhum usuário encontrado com o código informado.")

# Function to add a new user
def add_user(df):
    new_code = int(input("Insira o código do usuário: "))
    new_name = str(input("Insira o nome do usuário: "))
    new_email = str(input("Insira o email do usuário: "))
    new_patrimonio = float(input("Qual o patrimônio do cliente? "))
    
    new_user = pd.DataFrame({'Code': [new_code],
                             'Name': [new_name],
                             'Email': [new_email],
                             'Net Worth': [new_patrimonio]})
    
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_excel(data_path, index=False)
    
    print("Novo usuário adicionado com sucesso.")

# Function to view all users
def view_all_users(df):
    print("Todos os usuários:")
    print(df)
    print()

# Main program
def main():
    df = pd.read_excel(data_path, usecols=[0, 1, 2, 3])
    
    while True:
        display_menu()
        menu = int(input("Selecione uma opção: "))
        
        if menu == 1:
            search_user(df)
        elif menu == 2:
            add_user(df)
        elif menu == 3:
            view_all_users(df)
        elif menu == 4:
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida, tente novamente.\n")

if __name__ == '__main__':
    data_path = r"C:\Users\55219\Desktop\Temporario MesaRV\user_data.xlsx"
    main()
