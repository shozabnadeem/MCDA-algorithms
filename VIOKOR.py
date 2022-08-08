import numpy as np
def VIKOR(decionmatrix , weights , factor_type):
    Xi_plus=np.arange(len(factor_type))#best
    Xi_minus=np.arange(len(factor_type))#worst
    decionmatrixTranspose=np.transpose(decionmatrix)
    # print(decionmatrixTranspose)
    for x in range(len(decionmatrixTranspose)):
        if(factor_type[x]):
            Xi_plus[x]=min(decionmatrixTranspose[x])
            Xi_minus[x]=max(decionmatrixTranspose[x])
        else:
            Xi_plus[x]=max(decionmatrixTranspose[x])
            Xi_minus[x]=min(decionmatrixTranspose[x])
#     print("Xi_plus:\n",Xi_plus)
#     print("Xi_minus:\n",Xi_minus)
    for x in range(len(decionmatrix)):
        for y in range(len(decionmatrix[x])):
            decionmatrix[x][y]=weights[y]*((Xi_plus[y]-decionmatrix[x][y])/(Xi_plus[y]-Xi_minus[y]))
#     print(decionmatrix)
    Si=np.sum(decionmatrix,axis=1)
    Si=np.round(Si,4)
#     print("SI\n",Si)
    Ri=np.amax(decionmatrix,axis=1)
    Ri=np.round(Ri,4)
#     print("RI\n",Ri)
    sStar=round(min(Si),4)
    rStar=round(min(Ri),4)
    sMinus=round(max(Si),4)
    rMinus=round(max(Ri),4)
#     print(sStar,sMinus)
#     print(rStar,rMinus)
    Q=np.arange(len(Si),dtype=np.float)
    for x in range(len(Q)):
        Q[x]=(.5*((Si[x]-sStar)/(sMinus-sStar)))+(.5*((Ri[x]-rStar)/(rMinus-rStar)))
    return Q