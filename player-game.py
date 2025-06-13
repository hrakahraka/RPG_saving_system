import json
class player:
    def __init__(self,name,level,inventory,health):
        self.name=name
        self.level=level
        self.inventory=inventory
        self.health=health
    def add_item(self,item):
        self.inventory.append(item)
    def level_up(self):
        self.level += 1
    def health_bonus(self):
        self.health += int(100/self.level)
    def show_inventory(self):
        print(self.inventory)
with open("player.json","r") as f:
    data=json.load(f)
with open("command_list.json", "r") as c:
    cmd_list=json.load(c)
H_name=input("what is the name of your hero")
hero=player(H_name,data["level"],data["inventory"], data["health"])
command=input("what do you want to do(write //help// if you need assistance)")
if command.upper()=="HELP":
    for key , value in cmd_list.items():
        print(f"{key}:{value}")