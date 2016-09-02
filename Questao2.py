'''
ALGORITMO "Contador de opinião da satisfação de um filme!"
DECLARE contador_otimo, contador_bom, contador_regular, opiniao INTEIRO

contador_otimo <- 0
contador_bom <- 0
contador_regular <- 0

PARA X de 0 até 10 faça

    ESCREVA "Digite aqui sua opinião com relação ao filme: 1 para regular, 2 para bom ou 3 para ótimo: "
    LEIA opiniao

    SE opiniao = 1
        ENTÃO contador_regular <- contador_regular + 1
        ESCREVA - "Regular"
    SE opiniao = 2
        ENTÃO contador_bom <- contador_bom + 1
        ESCREVA - "Bom"
    SE opiniao = 3
        ENTÃO contador_otimo <- contador_otimo + 1
        ESCREVA - "Ótimo"
    SENÃO
        ESCREVA - "Opção inválida."
ESCREVA "a) contador_otimo <- "pessoas que responderam otimo."
ESCREVA "b) contador_bom <- "pessoas que responderam bom."
ESCREVA "c) contador_regular <- "pessoas que responderam regular."
'''
