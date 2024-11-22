import os
os.system('cls')

def discount(price:float, percent:int):
    if percent >= 0 and percent <= 100:
        return round(price * (1-percent/100), 3)


 