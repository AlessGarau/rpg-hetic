from weapons import weapon_data, Effect

class Player:
    def __init__(self, name,level):
        self.name = name
        self.level = level
        self.hp = level * 5
        self.ad = level * 3
        self.defense = level * 2 
        self.statut = None
        self.inventory = {
            "weapons" : [],
            "items" : []
        }
        self.current_weapon = weapon_data['punch']
        self.xp_to_next_lvl = 5
        self.current_xp = 0

    def level_up(self):
        self.level += 1
    
    def get_xp(self):
        self.current_xp += 4
        if self.current_xp >= self.xp_to_next_lvl:
            self.level_up()
            self.xp_to_next_lvl += 5 * (self.level + 1)

    def get_current_weapon(self):
        return self.current_weapon

    def use_weapon(self, target):
        weapon_damage = weapon_data[self.current_weapon]['damage'] + self.ad - target.defense
        if weapon_data[self.current_weapon]['effect']:
            announce, effect_damage = weapon_data[self.current_weapon]['effect'].use_effect
        return weapon_damage + effect_damage 

    def add_item(self):
        self.inventory["items"].append()
    
    def remove_item(self, target):
        self.inventory["items"].remove(target)
    
    def show_inventory(self):
        print(f"Inventaire de {self.name}:")
        for key, value in self.inventory:
            if not value:
                print(f"VIDE")
            else:
                for slot in value:
                    print(slot + "-" + key)

test = Player('name',1)

"""J'ai upgrade la fonction d'attaque avec mon système d'arme, 
j'ai setup l'inventaire d'arme et de consommable 
(et du coup j'ai modifié l'inventaire pour que tout fonctionne)"""