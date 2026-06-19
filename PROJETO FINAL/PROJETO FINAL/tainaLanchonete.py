cardapioItens=["Coxinha", "Pastel de Carne", "Fatia de Bolo", "Suco natural", "Paçoca"]
cardapioValores=[6.0, 8.0, 6.0, 5.0, 0.5]

pedidoNome=[]
pedidoValor=[]
total= 0
opcao = 0
escolha = -1

while escolha != 0:
    print("-"*20)
    print(f"Bem-vind@s a lanchonete, selecione o que deseja fazer: ")
    print("-"*20)
    print(f"1 - Exibir cardápio ---------------------------------- ")
    print(f"2 - Adicionar item ao pedido ------------------------- ")
    print(f"3 - Remover item do pedido --------------------------- ")
    print(f"4 - Listar itens do pedido --------------------------- ")
    print(f"5 - Total da conta ----------------------------------- ")
    print(f"0 - Sair --------------------------------------------- ")
    print("-"*20)
    
    escolha = int(input("Qual a sua escolha? "))

    if escolha == 0:
        print("Encerrado, volte sempre!")
        break

    elif escolha == 1:
        print("-"*20)
        print("--- CARDÁPIO ---")
        for i in range(len(cardapioItens)):
            print(f"[{i + 1}] {cardapioItens[i]} ------ R$ {cardapioValores[i]:.2f}")

    elif escolha == 2:
        print("Escolha o item a ser adicionado informando o número dele: ")
        numLanche = int(input("Número do item: "))
        
        if numLanche == 1 or numLanche == 2 or numLanche == 3 or numLanche == 4 or numLanche == 5:        
            opcaoEscolhida = int(numLanche) - 1 #posicao no array começa em 0 e aqui to traduzindo pro sistema
            lanche = cardapioItens[opcaoEscolhida]
            preco = cardapioValores[opcaoEscolhida]    
            pedidoNome.append(lanche)
            pedidoValor.append(preco)    
            print(f"Seu item {lanche} foi adicionado. ")
        else:
            print("Opção inválida ")
    
    elif escolha == 3:
        print("Selecione o item a ser removido: ")
        
        if len(pedidoNome) == 0:
            print("Seu pedido está vazio atualmente. ")
        else:
            print("Aqui está seu pedido atual: ")
            
            for i in range(len(pedidoNome)):
                print(f"[{i + 1}] {pedidoNome[i]} R$ {pedidoValor[i]:.2f}") 
            
            removePedido = input("Digite o número do item que quer excluir do pedido: ")
            
            itemValido = []
            for i in range(len(pedidoNome)):
                itemValido.append(str(i + 1)) 
            
            if removePedido in itemValido:
                indiceReal = int(removePedido) - 1
                
                itemRemovido = pedidoNome.pop(indiceReal)
                valorRemovido = pedidoValor.pop(indiceReal)
                print(f"{itemRemovido} foi removido do seu pedido.")
            else:
                print("Opção inválida - o item informado não existe em seu pedido. ")
        
    elif escolha == 4:
        print("\n--- SEU PEDIDO ATUAL ---")
        if len(pedidoNome) == 0:
            print("Pedido vazio. ")
        else:
            for i in range(len(pedidoNome)):
                print(f"- {pedidoNome[i]}: R$ {pedidoValor[i]:.2f}")
    
    elif escolha == 5:
        print("\n")
        print("-"*20)
        print("-----RESUMO DO PEDIDO-----")
        print("-"*20)
        
        if len(pedidoNome) == 0:
            print("Você não adicionou itens ao pedido.")
        else:
            for i in range(len(pedidoNome)):
                print(f"- {pedidoNome[i]}: R$ {pedidoValor[i]:.2f}")
                
            total = sum(pedidoValor) #comando do python para somar os valores da lista sem ter que percorrer um for
            print(f"O total a se pagar ficou: R$ {total:.2f}")
            print("Pedido finalizado")
                
            pedidoNome.clear()
            pedidoValor.clear() #reiniciando as listas para o proximo pedido
    else:
            print("Opção")