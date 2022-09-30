def troca_fig(figurinhas_maria, figurinhas_joao):

    controle = 0
    qtd = 0

    if len(figurinhas_maria) < len(figurinhas_joao):  
        for i in range(len(figurinhas_maria)):
            for j in range(len(figurinhas_joao)):
                if figurinhas_maria[i] == figurinhas_joao[j]:
                    controle += 1
        qtd = len(figurinhas_maria) - controle


    elif len(figurinhas_joao) < len(figurinhas_maria):
        for i in range(len(figurinhas_joao)):
            for j in range(len(figurinhas_maria)):
                if figurinhas_joao[i] == figurinhas_maria[j]:
                    controle += 1
        qtd = len(figurinhas_joao) - controle

                                                              
    else:
        for i in range(len(figurinhas_maria)):
            for j in range(len(figurinhas_joao)):
                if figurinhas_maria[i] == figurinhas_joao[j]:
                    controle += 1
        qtd = len(figurinhas_maria) - controle

    return qtd