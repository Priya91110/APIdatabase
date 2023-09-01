input = {
    "country": [
        {
            "country_id": "GH",
            "probability": 0.224
        },
        {
            "country_id": "PH",
            "probability": 0.084
        },
        {
            "country_id": "NG",
            "probability": 0.073
        },
        {
            "country_id": "US",
            "probability": 0.061
        },
        {
            "country_id": "NE",
            "probability": 0.034
        }
    ],
    "name": "nathaniel"
}
# output = {
#     'country_id': ['GH', 'FH', "akdj"],
#     'probablity': [0.2, 2, 0.1, 1.1]          
#           }
output = {}
# print(input['country'])
print(input['country'][0])

# for i,j in input.items():
#     print(i,j)

for i in input:
    print(input['country'][i])
    
