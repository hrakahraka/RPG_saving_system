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
with open("player.json","r") as f:
    data=json.load(f)
H_name=input("what is the name of your hero")
hero=player(H_name,data["level"],data["inventory"], data["health"])
hero.add_item("shield")
hero.level_up()
hero.health_bonus()
with open("player.json","w") as f:
    json.dump(hero.__dict__,f,indent=4)