import arcade
from player import *
from random import randint

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
        if self.name == "LIF":
            self.damage_tick = 5
            self.probability = 1
        

    def get_name(self):
        return self.name

    def use_effect(self, target): 
        if randint(0, 10)/10 < self.probability:
            target.status = self.name
            return f"Additional damage dealt due to {self.name}", self.damage_tick
        else:
            return "", 0

weapon_sprite_path = f'./weapons_sprite/{Player.get_current_weapon()}.png'

weapon_data = {
    'Punch': {'damage': 0, 'durability': 0, 'effect': None, 'sprite': None, 'status': 'early'},
    'Clé à molette': {'damage': 5, 'durability': 12, 'effect': None, 'sprite': None, 'status': 'early'},
    'Couteau de combat': {'damage': 5, 'durability': 12, 'effect': Effect("SAI"), 'sprite': None, 'status': 'early'},
    'Tuyau': {'damage': 5, 'durability': 12, 'effect': None, 'sprite': None, 'status': 'early'},
    'Pistolet à cloue': {'damage': 5, 'durability': 12, 'effect': Effect("PSN"), 'sprite': None, 'status': 'early'},

    'Masse': {'damage': 5, 'durability': 10, 'effect': Effect("PEU"), 'sprite': None, 'status': 'mid'},
    'Exo Gant': {'damage': 5, 'durability': 10, 'effect': None, 'sprite': None, 'status': 'mid'},
    'Blaster': {'damage': 5, 'durability': 10, 'effect': Effect('BRU'), 'sprite': None, 'status': 'mid'},

    'Fusil à pompe': {'damage': 5, 'durability': 8, 'effect': None, 'sprite': None, 'status': 'late'},
    'Lance-Flamme': {'damage': 5, 'durability': 8, 'effect': Effect('BRU'), 'sprite': None, 'status': 'late'},
}

"""
    avec une condition pour switch d'arme ca donne ça (lors de l'input de touche E par exemple)
    if key_press_e: (jsp si c'est vraiment comme ça)
        if self.weapon_index < len(list(weapon_data.keys())) - 1:
					self.weapon_index += 1
				else:
					self.weapon_index = 0
					
				self.weapon = list(weapon_data.keys())[self.weapon_index]
"""
