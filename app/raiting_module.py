import json


def load_jsonfile():
        with open('users.json', 'r') as jsonfile:
            data = json.load(jsonfile)
        return data


def new_user_raiting(user_id):
    if user_id in json_data:
        return Raiting(user_id, json_data[user_id])
    else:
        return Raiting(user_id, raiting=0)
    
global json_data
json_data = load_jsonfile()

class Raiting:
    

    def __init__(self, user_id, raiting=0):
        self.user_id = user_id
        self.raiting = raiting
    
    def __str__(self):
        return str(self.raiting)

    
            
    def increase_raiting(self, value):
        self.raiting += value

    def decrease_raiting(self, value):
        self.raiting -= value

    def to_json(self):
        with open('users.json', 'w') as jsonfile:
            json_data[self.user_id] = self.raiting
            data = json.dumps(json_data)
            jsonfile.write(data)


