import numpy as np
import copy
def WSM(decisionMatrix, weights):
    for x in range(len(decisionMatrix)):
        for y in range(len(decisionMatrix[x])):
            decisionMatrix[x][y]=weights[y]*decisionMatrix[x][y]
    wsm=decisionMatrix.sum(axis=1)
    return(wsm)

def WPM(decisionMatrix, weights):
    for x in range(len(decisionMatrix)):
        for y in range(len(decisionMatrix[x])):
            decisionMatrix[x][y]=pow(decisionMatrix[x][y],weights[y])
    wpm = decisionMatrix.prod(axis=1)
    return (wpm)

def WASPAS(wsm, wpm):
    lamda = 0.5
    for x in range(len(wsm)):
        wsm[x]=(lamda*wsm[x])+((1-lamda)*wpm[x])
    waspas=np.round(wsm,4)
    #index=np.argmax(waspas,axis=0)
    #print(factor_type[index])
    #print(max(waspas))
    # print(waspas)
    waspas_sort = waspas.argsort()[::-1]
    rank_waspas = np.empty_like(waspas_sort)
    rank_waspas[waspas_sort] = np.arange(len(waspas))
    # print("Rank:")
    # print(rank_waspas)
    return (waspas,rank_waspas)
def normalize (decisionMatrix,factorType):
        for x in range(len(decisionMatrix)):
            for y in range(len(decisionMatrix[x])):
                if (factorType[y] == False):
                    #Benefit
                    decisionMatrix[x][y] = decisionMatrix[x][y] / np.max(decisionMatrix[:, y])
                    #print(factorType[y])
                else:
                    # Cost
                    decisionMatrix[x][y] = np.min(decisionMatrix[:, y]) / decisionMatrix[x][y]
                    #print(factorType[y])

def initializeWASPAS(decision_matrix,factor_type,weights):
    normalized_decsion=copy.deepcopy(decision_matrix)
    normalized_decsion=np.array(normalized_decsion)
    normalize(normalized_decsion, factor_type)
    wsm=WSM(copy.deepcopy(normalized_decsion) , weights)
    wpm=WPM(copy.deepcopy(normalized_decsion) , weights)
    waspas_ranks,rank_waspas=WASPAS(wsm, wpm)
    return waspas_ranks