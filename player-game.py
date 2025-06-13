import json
from random import randint
from time import sleep
class player:
    def __init__(self,name,level,xp,inventory,health):
        self.name=name
        self.level=level
        self.xp=xp
        self.inventory=inventory
        self.health=health
        self.max_health=health
    def add_item(self,item):
        self.inventory.append(item)
    def xp_bonus(self,bonus):
        self.xp += bonus
    def level_up(self):
        self.level += 1
        self.max_health += 100*self.level
        self.health=self.max_health
    def health_bonus(self):
        self.max_health += int(100/self.level)
    def show_inventory(self):
        print(self.inventory)
        for i, item in enumerate(self.inventory):
            print(f"{i}: {item}")

    def heal(self,value):
        self.health += value
        if self.health > self.max_health:
            self.health= self.max_health
def check_cmd(command,cmd_list):
    test=False
    for key in cmd_list:
            if command.upper()==key.upper():
                test=True
    while command.upper()=="HELP" or test==False:
        for ke , value in cmd_list.items():
         print(f"{ke}:{value}")
        command=input("what do you want to do(write //help// if you need assistance): ")
        for key in cmd_list:
            if command.upper()==key.upper():
                test=True
def reward(ev_list,event,database):
    hero.xp_bonus(ev_list[event][7])
    print("you gained +"+str(ev_list[event][6])+" xp points")
    g=randint(1,3)
    category=""
    p=""
    if g==1:
        category="weapons"
        p=str(randint(1,2))
    elif g==2:
        category="shields"
        p=str(randint(101,102))
    else:
        category="potions"
        p=str(randint(201,202))
    hero.add_item(database[category][p][0])
    print("you gained "+str(database[category][p][0]))
with open("database.json","r")as b:
    database=json.load(b)
with open("player.json","r") as f:
    data=json.load(f)
with open("command_list.json", "r") as c:
    cmd_list=json.load(c)
with open("events.json","r") as d:
    ev_list=json.load(d)
H_name=input("what is the name of your hero: ")
hero=player(H_name,data["level"],data["xp"],data["inventory"], data["health"])
while hero.level != 60:
    event=str(randint(1,len(ev_list)))
    print(ev_list[event][0])
    command=input("what do you want to do(write //help// if you need assistance): ")
    check_cmd(command,cmd_list)
    if command.upper()=="inventory":
        hero.show_inventory()
        sleep(5)
        print(ev_list[event][0])
        command=input("what do you want to do next")
        check_cmd(command,cmd_list)
    if command.upper()=="ATTACK":
        W1=""
        S2=""
        tt=False
        while tt==False:
            choice1=int(input("choose your weapon"))
            for item in database["weapons"].items():
                if [item][0]==hero.inventory[choice1]:
                    W1=item
                    tt=True
            if tt==False:
                print("not a valid weapon")
        t=False
        while t==False:
            choice2=int(input("choose your shield"))
            for item in database["shields"].items():
                if [item][0]==hero.inventory[choice2]:
                    S2=item
                    tt=True
            if tt==False:
                print("not a valid shield")
        power=(int(database["weapons"][W1][1])+int(database["shields"][S2][1]))/2
        if power >= int(ev_list[event][4]):
            print(ev_list[event][3])
            reward(ev_list,event,database)
            if hero.xp>=hero.level*200:
                hero.level_up()
                print("LEVEL UP !! (max HP increased you have: )"+str(hero.max_health)+" Max HP")
                
            continue
        else:
            print(ev_list[event][1])
            sleep(5)
            break
        
    elif command.upper()=="FLEE":
        print(ev_list[event][2]+"(-"+str(ev_list[event][5])+" health")
        hero.health -= ev_list[event][5]
        print("you have "+str(hero.health)+" HP left")
        if hero.health<=0:
            print("you died")
            break
        else:
            continue