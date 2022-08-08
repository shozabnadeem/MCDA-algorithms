# MCDA algorithms
It's a Flask API to perform Multi Criteria Decision Analysis on given data
## Steps
thre process of MCDA includes following steps
- Screening 
- Weight Assessment 
- Ranking
- Rank Aggregation
## Screeing
the process of screening takes scores on the the factors that might effect the decision. I took geomatrical mean on scores of those factors and returns factors sorted with respect to their mean score
to call screening use 
> /screening

and pass json of data: 2D array 
> 2D array must be square array
## Weight Assessment 
the process of weight assessment finds the weight of factors. I'm using AHP to find the weights of factors.
To call weight assessment user
> /weightassessment

and pass json array named by pairwise containg factor names against their score for example
>"pairwise": [
        {
            "column1": 1.0,
            "column2": 3.0,
            "column3": 7.0,
            "column4": 9.0
        },
        {
            "column1": 0.33,
            "column2": 1.0,
            "column3": 5.0,
            "column4": 7.0
        },
        {
            "column1": 0.14,
            "column2": 0.20,
            "column3": 1.0,
            "column4": 3.0
        },
        {
            "column1": 0.11,
            "column2": 0.14,
            "column3": 0.33,
            "column4": 1.0
        }
    ]

this will return json named with key named as weights
