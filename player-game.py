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
    def health_bonus(self,bonus):
        self.health += bonus
with open("player.json","r") as f:
    data=json.load(f)
hero=player(data["name"],data["level"],data["inventory"], data["health"])
hero.add_item("shield")
hero.level_up()
hero.health_bonus(100/hero.level)
with open("player.json","w") as f:
    json.dump(hero.__dict__,f,indent=4)