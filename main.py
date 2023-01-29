"""#bloquer le programme pendant un certain temps
import time
time.sleep(1)

#afficher un point sans aller à la ligne
print(".", end="", flush=True)

#boucler chaque seconde et afficher un point à chaque seconde
for i in range(5):
    time.sleep(1)
    print(".", end="", flush=True)

d = 100
#division entière sans virgule :
min = d//60
sec = d-min*60

#compléter un chiffre qu'on affiche par un 0 juste devant :
print(f"{min:02d}")

"""

""""""

time_choice = 0


def timer(time_egg):
    import time
    while time_egg > 0:
        print(f"Temps restant : {time_egg//60}min {time_egg-time_egg//60*60}sec")
        time_egg -= 10
        for i in range(10):
            time.sleep(1)
            print(".", end="", flush=True)
    print("Votre oeuf est prêt !")


continu = True
while continu:
    print("Pour un oeuf à la coque, tapez A.")
    print("Pour un oeuf mollet, tapez B.")
    print("Pour un oeuf dur, tapez C.")
    print("Pour quitter le programme, tapez D.")
    u_choice = input("Quels cuisson des oeufs désirez-vous ?")
    if u_choice == "A":
        time_choice = 180
        continu = False
    elif u_choice == "B":
        time_choice = 360
        continu = False
    elif u_choice == "C":
        time_choice = 540
        continu = False
    elif u_choice == "D":
        continu = False
    else:
        print("Merci de taper d'une des propositions A, B, C ou D.")

if time_choice != 0:
    timer(time_choice)
