def criar_heap(tamanho):
    heap = [False] * tamanho
    lista_livre = [{'inicio': 0, 'tamanho': tamanho}]
    alocacoes = {}
    return heap, lista_livre, alocacoes

def definir_estrategia():
    return input("Digite a estratégia de heap (best, worst, first & next): ").strip().lower()

def encontrar_bloco_livre(lista_livre, tamanho, estrategia):
    global ultima_pos

    if estrategia == 'best':
        melhor_indice = None
        melhor_tamanho = float('inf')
        for i, bloco in enumerate(lista_livre):
            if bloco['tamanho'] >= tamanho and bloco['tamanho'] < melhor_tamanho:
                melhor_tamanho = bloco['tamanho']
                melhor_indice = i
        return melhor_indice
    elif estrategia == 'worst':
        pior_indice = None
        pior_tamanho = -1
        for i, bloco in enumerate(lista_livre):
            if bloco['tamanho'] >= tamanho and bloco['tamanho'] > pior_tamanho:
                pior_tamanho = bloco['tamanho']
                pior_indice = i
        return pior_indice

def alocar(heap, lista_livre, alocacoes, id, tamanho, estrategia):
    indice = encontrar_bloco_livre(lista_livre, tamanho, estrategia)
    if indice is not None:
        bloco = lista_livre[indice]
        alocacoes[id] = {'inicio': bloco['inicio'], 'tamanho': tamanho}
        for i in range(bloco['inicio'], bloco['inicio'] + tamanho):
            heap[i] = True
        if bloco['tamanho'] == tamanho:
            lista_livre.pop(indice)
        else:
            bloco['inicio'] += tamanho
            bloco['tamanho'] -= tamanho
    else:
        print(f"Não foi possível alocar {tamanho} blocos para {id}.")

def desalocar(heap, lista_livre, alocacoes, id):
    if id in alocacoes:
        bloco = alocacoes.pop(id)
        for i in range(bloco['inicio'], bloco['inicio'] + bloco['tamanho']):
            heap[i] = False
        lista_livre.append({'inicio': bloco['inicio'], 'tamanho': bloco['tamanho']})
        fundir_lista_livre(lista_livre)

def fundir_lista_livre(lista_livre):
    lista_livre.sort(key=lambda x: x['inicio'])
    lista_fundida = []
    atual = lista_livre[0]
    for i in range(1, len(lista_livre)):
        if atual['inicio'] + atual['tamanho'] == lista_livre[i]['inicio']:
            atual['tamanho'] += lista_livre[i]['tamanho']
        else:
            lista_fundida.append(atual)
            atual = lista_livre[i]
    lista_fundida.append(atual)
    lista_livre[:] = lista_fundida

def exibir_heap(heap):
    print("Heap:", ''.join(['█' if b else '.' for b in heap]))

def menu():
    global ultima_pos
    ultima_pos = 0
    tamanho_heap = 40
    heap, lista_livre, alocacoes = criar_heap(tamanho_heap)
    estrategia = 'best'

    while True:
        print("\n--- Menu ---")
        print("1. Definir estratégia de alocação")
        print("2. Alocar")
        print("3. Desalocar")
        print("4. Exibir")
        print("5. Sair")

        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Entrada inválida.")
            continue

        if opcao == 1:
            estrategia = definir_estrategia()
            if estrategia == 'best':
                print("Estratégia de Alocação digitada: Best")
            elif estrategia == 'worst':
                print("Estratégia de Alocação digitada: Worst")
            elif estrategia == 'first':
                print("Estratégia de Alocação digitada: First")
            elif estrategia == 'next':
                print("Estratégia de Alocação digitada: Next")
        elif opcao == 2:
            id = input("ID da alocação: ")
            tamanho = int(input("Tamanho do bloco: "))
            alocar(heap, lista_livre, alocacoes, id, tamanho, estrategia)
        elif opcao == 3:
            id = input("ID para desalocar: ")
            desalocar(heap, lista_livre, alocacoes, id)
        elif opcao == 4:
            exibir_heap(heap)
        elif opcao == 5:
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
