from numpy.core.defchararray import count
from screening import perform
import numpy as np
import copy
from TOPSIS import topsis
from WASPAS import initializeWASPAS
from VIOKOR import VIKOR

def ranks(rankings):
    sort = rankings.argsort()[::-1]
    rank = np.empty_like(sort)
    rank[sort] = np.arange(len(rankings))
    return rank

def bordaCount(Trank,Wrank,Vrank):
    final_rank=np.add(np.add(Trank,Wrank),Vrank)
    return final_rank

def ranking(data):
    dm=data['decisionmatrix']
    ft=data['factortype']
    we=data['weights']
    names=data['alternates']
    factor_type=list(ft.values())
    weight=list(we.values())
    decisionmatrix=[]
    for x in dm:
        decisionmatrix.append(list(x.values()))
    decisionmatrix=np.array(decisionmatrix)
    weights=np.array(weight)
    rank_borda=find_ranks(decisionmatrix,factor_type,weights)
    sensitivity_results=perform_sensitivity(decisionmatrix,factor_type,weights)
    print(rank_borda)
    sensitive=check_robustness(rank_borda,sensitivity_results)
    print("sensi ",sensitive)
    factor_names=list(names.values())
    result=dict()
    # print(factor_names)
    for x in range(len(factor_names)):
        result[factor_names[x]]=int(rank_borda[x])
    return result

def find_ranks(decisionmatrix,factor_type,weights):
    topsisRanks=topsis(copy.deepcopy(decisionmatrix),factor_type,weights)
    viokorRanks=VIKOR(copy.deepcopy(decisionmatrix),weights,factor_type)
    waspasRanks=initializeWASPAS(copy.deepcopy(decisionmatrix),factor_type,weights)
    topsisRank=ranks(topsisRanks)
    viokorRank=ranks(viokorRanks)
    waspasRank=ranks(waspasRanks)
    print("topsis ",topsisRank+1)
    # print(waspasRank)
    # print(viokorRank)
    borda_ranks=bordaCount(topsisRank,waspasRank,viokorRank)
    # print(borda_ranks)
    borda_sort = borda_ranks.argsort()[::1]
    rank_borda = np.empty_like(borda_sort)
    rank_borda[borda_sort] = np.arange(len(borda_ranks))
    rank_borda=rank_borda+1
    # print(rank_borda)
    return rank_borda

def perform_sensitivity(decisionmatrix,factor_type,weights):
    iternations=len(weights)
    results=[]
    for i in range(1,iternations):
        swaped_weights=copy.deepcopy(weights)
        swaped_weights[0],swaped_weights[i]=swaped_weights[i],swaped_weights[0]
        # print(swaped_weights)
        results.append(list(find_ranks(decisionmatrix,factor_type,swaped_weights)))
    results=np.array(results)
    return results

def check_robustness(acutualresult,tested_results):
    count=0
    for i in range(len(tested_results)):
        if (tested_results[i]==acutualresult).all():
            count+=1
    percentage=count/len(tested_results)
    print("per ",percentage*100)
    if(percentage*100>=70):
        return True
    else:
        return False

    