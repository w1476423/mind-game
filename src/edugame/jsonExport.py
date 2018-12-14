import json

game_name = "Symbol Game"

game_notes = [
    {'Note 1' : 'A matching game with symbols.'},
    {'Note 2' : 'Score is proportional with the number of correct answers'}
]

game_currency = [
    {"None" : "N/A"}
]

game_trophies = [
    {"None" : "N/A"}
]

game_ach = [

{"Completed Level One on Normal Difficulty" :
"40%" }

]

game_items = [
{"None" : "N/A"}
]


datadict = { game_name : [
{'game_name' : game_name},
{'game_notes' : game_notes},
{'game_currency' : game_currency},
{'game_trophies' : game_trophies},
{'game_ach' : game_ach},
{'game_items' : game_items}
]

}

def make_Pandas(datadict):
    dataframe = pd.DataFrame(datadict)
    return dataframe

def save_json_pd():
    print ('Saving game json file')
    pd_dataframe = make_Pandas(datadict)
    json_name = "jsonFiles/" + game_name + ".json"

    with open(json_name, 'w') as f:
        f.write(pd_dataframe.to_json(orient='records', lines=True))

