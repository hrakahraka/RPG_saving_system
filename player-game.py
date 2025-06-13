import json
from random import randint
class player:
    def __init__(self,name,level,xp,inventory,health):
        self.name=name
        self.level=level
        self.xp=xp
        self.inventory=inventory
        self.health=health
    def add_item(self,item):
        self.inventory.append(item)
    def xp_bonus(self):
        self.
    def level_up(self):
        self.level += 1
    def health_bonus(self):
        self.health += int(100/self.level)
    def show_inventory(self):
        print(self.inventory)
with open("database.json","r")as b:
    data=json.load(b)
with open("player.json","r") as f:
    data=json.load(f)
with open("command_list.json", "r") as c:
    cmd_list=json.load(c)
with open("events.json","r") as d:
    ev_list=json.load(d)
H_name=input("what is the name of your hero: ")
hero=player(H_name,data["level"],data["xp"],data["inventory"], data["health"])
while hero.level != 60:
    event=str(randint)
    print(ev_list[event][1])
    command=input("what do you want to do(write //help// if you need assistance): ")
    test=False
    for key in cmd_list.items():
        if command==key:
            test=True
    while command.upper()=="HELP" or test==False:
        for key , value in cmd_list.items():
         print(f"{key}:{value}")
        command=input("what do you want to do(write //help// if you need assistance): ")
    if command=="inventory":
        hero.show_inventory()
    
          