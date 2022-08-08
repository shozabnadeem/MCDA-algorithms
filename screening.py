
import numpy as np

def perform(data):
    a=[]
    for x in data:
        a.append(list(x.values()))
    ratings=np.array(a)
    rating_mean=np.sum(ratings,axis=0)
    rating_mean=rating_mean/len(data)
    # print(rating_mean)
    rating_mean=np.around(rating_mean,decimals=4)
    threshold=np.sum(rating_mean)
    threshold=threshold/len(rating_mean)
    threshold=np.around(threshold,decimals=4)
    att_names=list(data[0].keys())
    shortlisted_attributes=[]
    return_data=dict()
    for x in range(len(rating_mean)):
        if rating_mean[x]>=threshold:
            shortlisted_attributes.append(att_names[x])
            return_data[att_names[x]]=rating_mean[x]
    # print(return_data)
    return(return_data)