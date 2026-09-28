# PESQUISA DE OPINIÃO
# COMTAGEM
qtd_excelente = 0
qtd_ruim = 0

# REPETIÇÃO
for i in range(10): 
    print(f"\n--- Entrevistado {i + 1} ---")
    
    # ENTRADA DE INFORMAÇÕES 
    nome = input("Digite o nome do usuário: ").strip().capitalize()
    idade = int(input("Digite a idade do usuário: "))
    opiniao = input("Digite sua opinião sobre o atendimento (1: Excelente, 2: Bom ou 3: Ruim): ").strip()

    # PROCESSAMENTO 
    if opiniao == "1":
        qtd_excelente += 1
    elif opiniao == "3":
        qtd_ruim += 1

# RESULTADO 
print("\n=== RESULTADO DA PESQUISA ===")
print(f"Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"Quantidade de respostas 'RUIM': {qtd_ruim}")
