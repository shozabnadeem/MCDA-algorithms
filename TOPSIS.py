import numpy as np

def swappers(ideal_best,ideal_worst,factor_type):
    for x in range(len(ideal_best)):
        if(factor_type[x]):
            ideal_best[x],ideal_worst[x]=ideal_worst[x],ideal_best[x]

def topsis(decision_matrix,factor_type,weights):
    deno=(np.sum(decision_matrix**2, axis=0))
    deno=deno**0.5
    
    normailize_decision_matrix=decision_matrix/deno[None,:]
    
    weighted_normalized_mat=normailize_decision_matrix*weights[None,:]
    weighted_normalized_mat=np.around(weighted_normalized_mat,decimals=4)
    print("WN matrix \n",weighted_normalized_mat)

    ideal_best_val=np.amax(weighted_normalized_mat,axis=0)


    ideal_worst_val=np.amin(weighted_normalized_mat,axis=0)
    swappers(ideal_best_val,ideal_worst_val,factor_type)
    print("ideal best values\n",ideal_best_val)
    print("ideal worst values\n",ideal_worst_val)
    #eucleadian distance
    ideal_best_vector=(weighted_normalized_mat - ideal_best_val)**2
    ideal_best_vector=np.sum(ideal_best_vector,axis=1)
    ideal_best_vector**=0.5
    # ideal_best_vector
    print(weighted_normalized_mat-ideal_worst_val)
    ideal_worst_vector=(weighted_normalized_mat - ideal_worst_val)**2
    ideal_worst_vector=np.sum(ideal_worst_vector,axis=1)
    ideal_worst_vector**=0.5
    # ideal_worst_vector

    
    print("ideal beast \n",ideal_best_vector)
    print("ideal worst \n",ideal_worst_vector)
    performance_score=(ideal_worst_vector+ideal_best_vector)
    performance_score=ideal_worst_vector/performance_score
    print("performance \n",performance_score)
    return performance_score