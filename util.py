import dice

def solveDice(dicetext):
    try:
        res = sum(dice.roll(dicetext))
        return str(res)
    except dice.DiceBaseException as e:
        print(e.pretty_print())


def isDiceText(dicetext):
    return str(dicetext).find("d") > -1


class RpgCache:

    def __init__(self):
        self.profiles=[]
        self.healthList=dict()
        

    def __str__(self):
        return "Objeto rpgCache"

    def __repr__(self):
        return "Objeto rpgCache"