import json


def load_jsonfile():
        with open('users.json', 'r') as jsonfile:
            data = json.load(jsonfile)
        return data


def new_user_raiting(user_id, user_name):
    if user_id in json_data:
        return Raiting(user_id, user_name, raiting=json_data[user_id][0])
    else:
        return Raiting(user_id, user_name, raiting=0)
    

def show_leaderboard():
    sorted_leads = sorted(json_data.values(), key=lambda value: value[0])[::-1]
    s = ''
    for i in range(len(sorted_leads)):
        s += f'{i + 1}. {sorted_leads[i][1]}  {sorted_leads[i][0]}\n'
    return s
    
global json_data
json_data = load_jsonfile()

class Raiting:
    

    def __init__(self, user_id, user_name, raiting=0):
        self.user_id = user_id
        self.user_name = user_name
        self.raiting = raiting
    
    def __str__(self):
        return str(self.raiting)
            
    def increase_raiting(self, value):
        self.raiting += value

    def decrease_raiting(self, value):
        self.raiting -= value

    def to_json(self):
        with open('users.json', 'w') as jsonfile:
            json_data[self.user_id] = (self.raiting, self.user_name)
            data = json.dumps(json_data)
            jsonfile.write(data)


