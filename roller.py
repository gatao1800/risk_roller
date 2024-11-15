import tkinter as tk
from tkinter import ttk
import random

ATTACKER = 0
DEFENDER = 1

def on_button_click():
    try:
        armys =[0,0]
        armys[ATTACKER] = int(attacking_units.get())
        armys[DEFENDER] = int(defending_units.get())
        rounds = amount_rounds.get()
        if((str is  type(rounds))):
            if(rounds == "max"):
                rounds = 100000000000000000000000
            else:
                rounds = int(rounds)
        threshold = int(player_threshold.get())
        resulting_units = CalcRounds(armys,rounds, threshold)
        # print(resulting_units)

        attacking_units.delete(0, tk.END)
        attacking_units.insert(0, str(resulting_units[ATTACKER]))

        defending_units.delete(0, tk.END)
        defending_units.insert(0, str(resulting_units[DEFENDER])) 
    except ValueError:
        print("error")

def main():
    global attacking_units, defending_units, amount_rounds, player_threshold

    # Create the main window
    window = tk.Tk()
    window.title("Risiko Würfler")

    # Create input fields for attacking and defending units
    tk.Label(window, text="Angreifend").pack()
    attacking_units = tk.Entry(window)
    attacking_units.pack()

    tk.Label(window, text="Verteidigend").pack()
    defending_units = tk.Entry(window)
    defending_units.pack()

    # Create input for the number of rounds
    tk.Label(window, text="Spielrunden (oder 'max')").pack()
    amount_rounds = tk.Entry(window)
    amount_rounds.pack()

    # Create input for the player threshold
    tk.Label(window, text="Würfelschwelle").pack()
    player_threshold = tk.Entry(window)
    player_threshold.pack()

    # Create a button that triggers the calculation
    button = tk.Button(window, text="Berechnen", command=on_button_click)
    button.pack()

    # Start the Tkinter event loop
    window.mainloop()

def CalcRounds(total_armys, num_rounds, dice_threshold):
    for round in range(num_rounds):
        if(total_armys[ATTACKER] == 0 or total_armys[DEFENDER] == 0):
            return total_armys
        lost_figures = CalcFiguresLost([GetMaxAttackingUnits(total_armys[ATTACKER], 3),GetMaxAttackingUnits(total_armys[DEFENDER], 2)], dice_threshold)
        # print(GetMaxAttackingUnits(total_armys[DEFENDER], 2))
        total_armys = [total_armys[i] - lost_figures[i] for i in range(len(total_armys))]
        # print(lost_figures, " + ", total_armys)
    return total_armys

def GetMaxAttackingUnits(army, max_units):
    if army >= max_units:
        return max_units
    else:
        return army

def CalcFiguresLost(armys, dice_threshold):
    attack_dice=[]
    defence_dice=[]
    losing_figures=[0,0]
    for attacks in range(armys[ATTACKER]):
        attack_dice.append(random.randint(1,6))
    attack_dice.sort(reverse=True)
    if(armys[DEFENDER] > 1 and ((len(attack_dice) <= 1) or attack_dice[1] > dice_threshold)):
        armys[DEFENDER] -= 1
    for defences in range(armys[DEFENDER]):
        defence_dice.append(random.randint(1,6))
    defence_dice.sort(reverse=True)
    for figures_lost in range(len(ChooseShorterArray(attack_dice, defence_dice))):
        if(attack_dice[figures_lost] > defence_dice[figures_lost]):
            losing_figures[DEFENDER] += 1
        else:
            losing_figures[ATTACKER] += 1
    return losing_figures

    
def ChooseShorterArray(*arrays):
    # Find the array with the largest size
    larger_array = min(arrays, key=len)
    return larger_array


if __name__ == "__main__":
    main()