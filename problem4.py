food = input("Что вы хотеди покушать и попить?")

def menu(food):
    with open("menu.txt", 'w') as f:
        f.write(food)
menu(food)
