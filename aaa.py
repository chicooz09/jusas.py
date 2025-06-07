def analisar_pesquisa():
    """
    Coleta dados de salário e número de filhos de uma pesquisa,
    e calcula:
    a) média do salário da população;
    b) média do número de filhos;
    c) maior salário;
    d) percentual de pessoas com salário até R$100,00.
    A leitura de dados termina com a entrada da informação "final".
    """

    salarios = []
    filhos = []
    salarios_ate_100 = 0

    print("Digite o salário e o número de filhos (ou 'final' para terminar):")

    while True:
        entrada_salario = input("Salário: ")
        if entrada_salario.lower() == "final":
            break
        
        try:
            salario = float(entrada_salario)
            salarios.append(salario)
            if salario <= 100.00:
                salarios_ate_100 += 1
        except ValueError:
            print("Entrada inválida para salário. Por favor, digite um número ou 'final'.")
            continue

        entrada_filhos = input("Número de filhos: ")
        try:
            num_filhos = int(entrada_filhos)
            filhos.append(num_filhos)
        except ValueError:
            print("Entrada inválida para número de filhos. Por favor, digite um número inteiro.")
            # Remove o salário adicionado se o número de filhos for inválido para manter a consistência
            if salarios:
                salarios.pop()
            if salario <= 100.00:
                salarios_ate_100 -= 1
            continue

    total_pessoas = len(salarios)

    if total_pessoas == 0:
        print("\nNenhum dado foi inserido para análise.")
        return

    # a) Média do salário da população
    media_salario = sum(salarios) / total_pessoas

    # b) Média do número de filhos
    media_filhos = sum(filhos) / total_pessoas

    # c) Maior salário
    maior_salario = max(salarios)

    # d) Percentual de pessoas com salário até R$100,00
    percentual_salario_ate_100 = (salarios_ate_100 / total_pessoas) * 100

    print("\n--- Resultados da Pesquisa ---")
    print(f"a) Média do salário da população: R$ {media_salario:.2f}")
    print(f"b) Média do número de filhos: {media_filhos:.2f}")
    print(f"c) Maior salário: R$ {maior_salario:.2f}")
    print(f"d) Percentual de pessoas com salário até R$100,00: {percentual_salario_ate_100:.2f}%")

if __name__ == "__main__":
    analisar_pesquisa()