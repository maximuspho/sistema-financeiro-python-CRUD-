import json

def salvar_dados():
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(base, arquivo, indent= 4, ensure_ascii=False)
    print("Dados salvos com sucesso!")

def carregar_dados():
    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def entrada(tipo):
    print(f"\n--- Registrando {tipo.upper()} ---")
    desc = input("Descrição: ").strip().lower()
    valor_str = input("Valor: ").replace(",", ".")
    
    try:
        valor_n = float(valor_str)
    except ValueError:
        print('Erro: valor digitado não é um número válido.')
        return 

    if tipo == 'despesa' and valor_n > 0:
        valor_n = -valor_n

    elif tipo == 'receita' and valor_n < 0:
        valor_n = abs(valor_n)

    base.append({"desc": desc, "valor": valor_n})
    salvar_dados()
    print(f"{tipo.capitalize()} adicionada com sucesso!")

def apagar():
    
    if not base:
        print("A base está vazia! Não há nada para apagar.")
        return

    for i, item in enumerate(base):
        cor = "🟢" if item['valor'] > 0 else "🔴"
        print(f"{cor}:Indice: {i} - {item['desc']:.<20} - {item['valor']:>8.2f}")
        
    while True:
        try:
           num = int(input("Apagar indice: (-1 para voltar): "))
           if num == -1:
               print("Operação cancelada. Voltando ao menu...")
               break 

           if num >= 0 and num < len(base):
                base.pop(num)
                salvar_dados()
                print(f'Indice: {num} Apagado com Sucesso!!')
                break 
           else:
                print(f"Indice {num} não localizado! Tente novamente.")
                break
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.") 

def exibir():
    print("\n" + "="*50)
    print(f"{'DESCRIÇÃO':<20} | {'VALOR':>10} | {'TOTAL':>10}")
    print("-" * 50)
    saldo = 0
    cor_item = "⚪"      

    for i in base:
        saldo += i['valor']
        cor_item = "🟢" if i["valor"] >= 0 else "🔴" 
        
        print(f"{cor_item}:{i['desc']:.<20} | R$ {i['valor']:>8.2f} | R$ {saldo:>8.2f}") 
          
    print("="*50 + "")
    cor_final = "🟢" if saldo >= 0 else "🔴"
    print(f"{cor_final}:{'SALDO EM CONTA:':.<20} R$ {saldo:>8.2f}\n") 

def menu():
    while True:
        print("--- Sistema Finaceiro ---")
        print("Selecione uma opão no MENU:")
        print(f"| {'1-Adicionar Receita':<20} | {'2 - Adicionar Despesa':<20} | {'3 - Exibir Extrato':<20} | {'4 - Apagar':<10} | {'0 - Sair':<10} |")
        try:
            opcao = int(input("Digite: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue
        match opcao:
            case 1:
                entrada("receita")
            case 2:
                entrada("despesa")
            case 3:
                exibir()
            case 4:
                apagar()    
            case 0:
                break
    
base = carregar_dados()
menu()