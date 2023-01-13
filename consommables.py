import arcade
from weapons import Effect
class Consommables:
    def __init__(self, name, heal = 0, effect_to_debuff = None, stat_boost = ""):
        super().__init__()
        self.name = name
        self.heal = heal
        self.effect_to_debuff = effect_to_debuff
        self.stat_boost = stat_boost

    def use_item(self, player):
        if self.heal:
            player.hp += self.heal
        if self.effect_to_debuff:
            if player.status == self.effect_to_debuff.name:
                player.status == None
        if self.stat_boost == "defense":
            player.defense += 5
        elif self.stat_boost == "ad":
            player.ad += 5
            
        print(f"Vous venez d'utiliser {self.name}")
    

consommables_data = {
    "early": {
        'Kit de secours': Consommables('Kit de secours (+HP)', 5),
        'Spray anti-BRU': Consommables('Spray anti-BRU (-BRU)', 0, Effect('BRU')),
        'Antidote': Consommables('Antidote (-PSN)', 0, Effect('PSN')),
        'Bandage': Consommables('Bandage (-SAI)', 0, Effect('SAI')),

    },
    "mid": {
        'Morphine' : Consommables('Morphine (-DEF)', 0, None, "defense"),
        'Orangina' : Consommables('Orangina (+AD)', 0, None, "ad"),
        'Kit de secours 2' : Consommables('Kit de secours 2 (+HP)', 10),
        'Bandage 2' : Consommables('Bandage 2 (-SAI)', 0, Effect('SAI')),
        'Antidote': Consommables('Antidote (-PSN)', 0, Effect('PSN')),
        'Spray anti-BRU': Consommables('Spray anti-BRU (-BRU)', 0, Effect('BRU')),
    },
    "late": {
        'Morphine' : Consommables('Morphine (-DEF)', 0, None, "defense"),
        'Pomme dorée': Consommables('Pomme dorée', 10, Effect('PSN'), "defense"),
        'Kit de secours 3' : Consommables('Kit de secours 3 (+HP)', 10),
        'Dose éléctrique': Consommables('Dose éléctrique (+AD)', 0, None, "ad")
    }
}