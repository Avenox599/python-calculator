# Vérification de l'indentité
print("Salut Emmanuel")
import math
print("\n---------- OMNIBYTE ----------")
print("Bonjour.")
while True:
    user_name = input("Entrez votre nom : ")
    user_password = input("Entrez votre nom de passe : ")
    if user_name in ["Emmanuel", "André", "Louis", "Sacré"] and user_password == "10BTx":
        print(f"\nBienvenue {user_name} :), Je suis prêt à effecter des caclculs !!")
        break
    else:
        print("Les indentifiants entrés sont incorrecte. Veuillez réessayer.")
        continue

# Choix de l'opération

def menu():
    print("------Menu------\n" "1. Calcule du discriminant \n" "2. Résolution d'une équation du segond degré")


while True:
    menu()
    user_operation = input("Entrez le calcul à effectuer : ")
    if user_operation in ["1", "2", "Calcule du discriminant", "Résolution d'une équation du segond degré"]:
        verification_operation = input(f"Est-ce le bon {user_operation} ? Y/N ")
        if verification_operation in ["Yes", "Y", "Oui", "oui", "y"]:
            print("Super !")
            break
        elif verification_operation in ["No", "N", "Non", "non", "n"]:
            continue
        else:
            continue
    else:
        print("\nRegarder bien, le nemu et faite votre choix")
        continue

# Pour le discriminant

if user_operation in ["1", "Calcule du discriminant"]:
    print("\nVous avez choisi le discrinimant !")
    print("Sachez que l'équation est de la forme ax²+bx+c")
    while True:
        valeur_a = input("Entrez donc, la valeur de a : ")
        try:
            valeur_a = float(valeur_a)
            break
        except ValueError:
            print("Vous avez entrez la mauvaise valeur (elle doit être un nombre réel)")
            continue
    while True:
        valeur_b = input("Entrez donc, la valeur de b : ")
        try:
            valeur_b = float(valeur_b)
            break
        except ValueError:
            print("Vous avez entrez la mauvaise valeur (elle doit être un nombre réel)")
            continue  
    while True:
        valeur_c = input("Entrez donc, la valeur de c : ")
        try:
            valeur_c = float(valeur_c)
            break
        except ValueError:
            print("Vous avez entrez la mauvaise valeur (elle doit être un nombre réel)")
            continue      
    discriminant = valeur_b**2-4*(valeur_a*valeur_c)
    print(f"La valeur du discriminant est : {discriminant:.2f}")

# Pour la résolution de l'équation du segond degrè

elif user_operation in ["2", "Résolution d'une équation du segond degré"]:  
    print("Vous avez choisi la résolution d'une équation du segond degré !")
    while True:
        valeur_a = input("Entrez donc, la valeur de a : ")
        try:
            valeur_a = float(valeur_a)
            break
        except ValueError:
            print("Vous avez entrez la mauvaise valeur (elle doit être un nombre réel)")
            continue
    while True:
        valeur_b = input("Entrez donc, la valeur de b : ")
        try:
            valeur_b = float(valeur_b)
            break
        except ValueError:
            print("Vous avez entrez la mauvaise valeur (elle doit être un nombre réel)")
            continue  
    while True:
        valeur_c = input("Entrez donc, la valeur de c : ")
        try:
            valeur_c = float(valeur_c)
            break
        except ValueError:
            print("Vous avez entrez la mauvaise valeur (elle doit être un nombre réel)")
            continue      
    valeur_discriminant = valeur_b**2-4(valeur_a*valeur_c)
    print(f"Valeur du discriminant est {valeur_discriminant:.2f}")
    if valeur_discriminant < 0 :
        print("L'équation n'admet pas de solution.")
    elif valeur_discriminant == 0:
        print("Comme discriminant est égal à 0 alors, l'équation admet deux racines doubles, notées X")
        valeur_X = -valeur_b / (2*valeur_a)
        print("La solution est X0 = {}".format(valeur_X))
    elif valeur_discriminant > 0 :
        print("Comme discriminant est supérieur à 0 alors, l'équation admet deux racines doubles distinctes, notées X' et X''")
        racine = math.sqrt(valeur_discriminant)
        valeur_X1 = -valeur_b -racine / (2*valeur_a)
        valeur_X2 = -valeur_b +racine / (2*valeur_a)
        print("La solution est X' = {} et X'' = {}".format(valeur_X1, valeur_X2))
