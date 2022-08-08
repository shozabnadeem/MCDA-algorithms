import numpy as np

def ahp(data):
    a=[]
    key=list(data[0].keys())
    # print(key)
    for x in data:
        a.append(list(x.values()))
    numOfFac=len(a)

    arr=np.array(a)
    transpos=np.transpose(arr)
    sum=np.full((numOfFac),0.0)
    rand_ind=[0,0,0,.52,.89,1.11,1.25,1.35,1.40,1.45,1.49,1.51,1.54,1.56,1.57,1.58]

    # print(sum)
    for x in range(numOfFac):

        sum[x]=np.sum(transpos[x])


    # print(sum)

    for x in range(numOfFac):
        transpos[x]=transpos[x]/sum[x]


    normalize=(np.transpose(transpos))

    # print(normalize)

    priorty_Vector=np.full((numOfFac),0.0)

    for x in range(numOfFac):
        priorty_Vector[x]=np.sum(normalize[x])

    priorty_Vector=priorty_Vector/numOfFac
    # print(priorty_Vector)
    # print(numpy.sum(priorty_Vector))

    lamda=np.sum(sum*priorty_Vector)

    con_ind=(lamda-numOfFac)/(numOfFac-1)
    # print(con_ind)

    Con_rat=con_ind/rand_ind[numOfFac]
    # print(Con_rat)
    priorty_Vector=np.around(priorty_Vector,decimals=4)
    returndata=dict()
    
    for x in range(numOfFac):
        returndata[key[x]]=priorty_Vector[x]
    returndata["CR"]=Con_rat    
    return returndata
