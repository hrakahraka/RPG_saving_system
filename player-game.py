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
    def throw_item(self,index):
        self.inventory.pop(index)
        print(self.inventory[index]+" have been thrown succsessfully")
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
    def reward(self,ev_list,event,database):
        self.xp_bonus(ev_list[event][6])
        print("you gained +"+str(ev_list[event][6])+" xp points")
        g=randint(1,3)
        category=""
        p=""
        if g==1:
            category="weapons"
            p=str(randint(1,len(database[category])))
        elif g==2:
            category="shields"
            p=str(randint(101,len(database[category])+100))
        else:
            category="potions"
            p=str(randint(201,len(database[category])+200))
        self.add_item(database[category][p]["name"])
        print("you gained "+str(database[category][p]["name"])) #reminder!!: we add an inventory limit later and show the power of each weapon

    def heal(self,value):
        self.health += value
        if self.health > self.max_health:
            self.health= self.max_health
    def check_item_in_inventory(self,database):
        global weapon , shield , potion
        weapon=False
        shield=False
        potion=False
        for item in self.inventory:
            for key , value in database.items():
                for i in value:
                    if i["name"]==item:
                        if key=="weapons":
                            weapon=True
                        elif key=="shields":
                            shield=True
                        elif key=="potions":
                            potion=True
                    
            
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
def saving():
    with open("player.json" , "w") as f:
        json.dump(hero.__dict__ , f , indent=4)
    print("progress saved successfully you may exit safely")
def death():
    initial={
        "level":1,
        "inventory":["iron sword","leather shield"],
        "xp":0,
        "health":100
    }
    print("you died")
    with open("player.json" , "w") as f:
        json.dump(initial,f,indent=4)
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
count=0
while hero.level != 60:
    count+=1
    if count>=2:
        save=input("do you wan't to save your progress: ")
        while not((save.upper()=="YES")or(save.upper()=="NO")):
            print("invalid input")
            save=input("YES or NO: ")
        if save.upper()=="YES":
            saving()
            count=0
    event=str(randint(1,len(ev_list)))
    print(ev_list[event][0])
    command=input("what do you want to do(write //help// if you need assistance): ")
    check_cmd(command,cmd_list)
    action=""
    while action=="":
        if command.upper()=="INVENTORY":
            hero.show_inventory()
            sleep(3)
            print(ev_list[event][0])
            command=input("what do you want to do next: ")
            check_cmd(command,cmd_list)
            continue
        elif command.upper()=="HEAL":
            hero.check_item_in_inventory(database)
            if potion==True:
                health_addition=0
                potion_found=False
                while not potion_found:
                    choice=int(input("choose your potion: "))
                    for key , value in database["potions"].items():
                        if value["name"]==hero.inventory[choice]:
                            health_addition=int(value["value"])
                            potion_found=True
                    if potion_found==False:
                        print("not a valid potion")
                        
                hero.heal(health_addition)
                print(health_addition,"HP points added")
                print("you have",hero.health,"HP points")
                sleep(3)
                print(ev_list[event][0])
                command=input("what do you want to do next: ")
                check_cmd(command,cmd_list)
                continue
            else:
                print("you don't have any potions")
                sleep(3)
                print(ev_list[event][0])
                command=input("what do you want to do next: ")
                check_cmd(command,cmd_list)
                continue
        elif command.upper()=="THROW":
            hero.show_inventory()
            item_chosen=False
            index=""
            while not item_chosen:
                index=input("choose the item you want to throw: ")
                if (index.isdigit())and(int(index)<=len(hero.inventory)):
                    index=int(index)
                    item_chosen=True
            decide=input("are you sure: ")
            while not((decide.upper()=="YES")or(decide.upper()=="NO")):
                print("invalid input")
                decide=input("YES or NO: ")
            if decide.upper()=="NO":
                print("action cancelled")
                sleep(3)
                print(ev_list[event][0])
                command=input("what do you want to do next: ")
                check_cmd(command,cmd_list)
                continue
            elif decide.upper()=="YES":
                hero.throw_item(index)
                sleep(3)
                print(ev_list[event][0])
                command=input("what do you want to do next: ")
                check_cmd(command,cmd_list)
                continue
        elif command.upper()=="ATTACK":
            hero.check_item_in_inventory(database)
            if sword==True and shield==True:
                W1=0
                S2=0
                weapon_found=False
                while not weapon_found:
                    choice1=int(input("choose your weapon: "))
                    for key , value in database["weapons"].items():
                        if value["name"]==hero.inventory[choice1]:
                            W1=int(value["damage"])
                            weapon_found=True
                    if weapon_found==False:
                        print("not a valid weapon")
                        hero.show_inventory()
                shield_found=False
                while not shield_found:
                    choice2=int(input("choose your shield: "))
                    for key , value in database["shields"].items():
                        if value["name"]==hero.inventory[choice2]:
                            S2=int(value["resistance"])
                            shield_found=True
                    if shield_found==False:
                        print("not a valid shield")
                power=(W1+S2)/2
                threshold=int(ev_list[event][4])
                percentage_of_win=int((power / threshold) * 100)
                decide=input("you have "+str(percentage_of_win)+"%"+" chance to win do you want to proceed: ")
                while not((decide.upper()=="YES")or(decide.upper()=="NO")):
                    print("invalid input")
                    decide=input("YES or NO: ")
                if decide.upper()=="NO":
                    if hero.health>int(ev_list[event][5]):
                        print(ev_list[event][2]+"(-"+str(ev_list[event][5])+" health)")
                        hero.health -=int( ev_list[event][5])
                        print("you have "+str(hero.health)+" HP left")
                        action="next"
                    else:
                        print("you tried to flee but you couldn,t")
                        death()
                        action="end"
                else:
                    if power >= threshold or (power < threshold and randint(1, 100) <= percentage_of_win) :
                        print(ev_list[event][3])
                        hero.reward(ev_list,event,database)
                        if hero.xp>=hero.level*200:
                            hero.level_up()
                            print("LEVEL UP !! (max HP increased you have: )"+str(hero.max_health)+" Max HP")
                            print(hero.level*200,"xp needed to reach level ",hero.level+1)   
                        action="next"
                    else:
                        print(ev_list[event][1])
                        death()
                        action="end"
            else:
                print("you don't have the necessary equipments for fighting")
                sleep(3)
                print(ev_list[event][0])
                command=input("what do you want to do next: ")
                check_cmd(command,cmd_list)
                continue
        elif command.upper()=="FLEE":
            if hero.health>int(ev_list[event][5]):
                print(ev_list[event][2]+"(-"+str(ev_list[event][5])+" health)")
                hero.health -=int( ev_list[event][5])
                print("you have "+str(hero.health)+" HP left")
                action="next"
            else:
                print("you tried to flee but you couldn,t")
                death()
                action="end"
    if action=="next":
        continue
    elif action=="end":
        break
if hero.level>=60:
    print("congrats you won!!")
else:
    print("this is not supposed to happen, but you won?")