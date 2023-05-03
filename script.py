while True:
    # Ouvrir le fichier en mode lecture
    with open('fichier.txt', 'r') as f:
        # Lire toutes les lignes du fichier et les stocker dans une liste
        numeros = f.readlines()

    # Demander un nombre à l'utilisateur
    numero = input("Entrez un nombre de 8 chiffres (ou tapez 'leave' pour quitter): ")

    # Vérifier si l'utilisateur veut quitter
    if numero.lower() == 'leave' or numero.lower() == 'quitter':
        print("Merci d'avoir utilisé le programme.")
        break

    # Vérifier si le nombre est déjà dans la liste
    if numero+'\n' in numeros:
        print("Le nombre existe déjà dans le fichier.")
    else:
        # Ajouter le nombre à la fin du fichier
        with open('fichier.txt', 'a') as f:
            f.write(numero+'\n')
        print("Le nombre a été ajouté au fichier.")