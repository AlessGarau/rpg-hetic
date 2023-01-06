import arcade
from random import randint

"""
quand attaque =>
		weapon_damage = weapon_data[self.weapon]['damage']
        if weapon_data[self.weapon]['effect']:
            annonce, effect_damage = weapon_data[self.weapon]['effect'].use_effect

        total_damage = weapon_damage + effect_damage
"""

class Effect:
    def __init__(self, name):
        self.name = name


        if self.name == 'BRU':
            self.damage_tick = 5
            self.probability = .4
        if self.name == 'PSN':
            self.damage_tick = 2
            self.probability = .2
        if self.name == 'PEU':
            self.damage_tick = 5
            self.probability = .1
        if self.name == 'SAI':
            self.damage_tick = 5
            self.probability = .1
        if self.name == 'CRT':
            self.damage_tick = 8
            self.probability = .4
        
    def get_name(self):
        return self.name

    def use_effect(self, monster):
        if randint(0, 10)/10 < self.probability:
            monster.status == self.name
            return f"Additional damage dealt due to {self.name}", self.damage_tick
        else:
            
            return "", 0
#pour mettre les sprites suffit de rajouter  "graphics": /le_path/ 
weapon_data = {
    'Clé à molette': {'damage': 5, 'durability': 12, 'effect': None, 'sprite': None},
    'Couteau de combat': {'damage': 5, 'durability': 12, 'effect': Effect("SAI"), 'sprite': None},
    'Tuyau': {'damage': 5, 'durability': 12, 'effect': None, 'sprite': None},
    'Pistolet à cloue': {'damage': 5, 'durability': 12, 'effect': Effect("PSN"), 'sprite': None},
    
    'Masse': {'damage': 5, 'durability': 10, 'effect': Effect("PEU"), 'sprite': None},
    'Exo Gant': {'damage': 5, 'durability': 10, 'effect': None, 'sprite': None},
    'Blaster': {'damage': 5, 'durability': 10, 'effect': Effect('BRU'), 'sprite': None},

    'Fusil à pompe': {'damage': 5, 'durability': 8, 'effect': None, 'sprite': None},
    'Lance-Flamme': {'damage': 5, 'durability': 8, 'effect': Effect('BRU'), 'sprite': None},

}


#dans player il y aura donc ça pour les armes
class Player:
    def __init__(self) -> None:


        # en updatant weapon_key, on switch d'arme + créer un ramassage d'item i guess, pour l'instant ici toutes les armes sont availables
        self.weapon_key = 0
        self.weapon = list(weapon_data.keys())[self.weapon_key]

"""
    avec une condition pour switch d'arme ca donne ça (lors de l'input de touche E par exemple)
    if key_press_e: (jsp si c'est vraiment comme ça)
        if self.weapon_index < len(list(weapon_data.keys())) - 1:
					self.weapon_index += 1
				else:
					self.weapon_index = 0
					
				self.weapon = list(weapon_data.keys())[self.weapon_index]
"""
    
