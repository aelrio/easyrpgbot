import dice

def solveDice(dicetext):
    try:
        res = dice.roll(dicetext)
        return res
    except dice.DiceBaseException as e:
        print(e.pretty_print())


def isDiceText(dicetext):
    return False


class RpgCache:

    def __init__(self):
        self.profiles=[]
        self.healthList=dict()
        

    def __str__(self):
        return "Objeto rpgCache"

    def __repr__(self):
        return "Objeto rpgCache"