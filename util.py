import dice

def solveDice(dicetext):
    try:
        res = dice.roll(dicetext)
        return res
    except dice.DiceBaseException as e:
        print(e.pretty_print())


def isDiceText(dicetext):
    return False