import pyautogui
import time
import json
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    window_frame = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ Ce bot est fait par la team SILOW                                                                                    ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    """
    title = """
                                                                ███████╗██╗██╗      ██████╗ ██╗    ██╗
        ===============================                         ██╔════╝██║██║     ██╔═══██╗██║    ██║
           BOT DE RÉCOLTE AUTOMATISÉ                            ███████╗██║██║     ██║   ██║██║ █╗ ██║
        ===============================                          ╚═══██║██║██║     ██║   ██║██║███╗██║
                                                                ███████║██║███████╗╚██████╔╝╚███╔███╔╝
                                                                 ╚═════╝╚═╝╚══════╝ ╚═════╝  ╚══╝╚══╝
    """
    options = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  Choisissez votre métier :                                                                                           ║
║  1 - Mineur                                                                                                          ║
║  2 - Bûcheron                                                                                                        ║
║  3 - Pêcheur                                                                                                         ║
║  4 - Paysan                                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        """
    print(window_frame)
    print(title)
    print(options)
    time.sleep(1)  # Pause pour l'effet

def display_soustitle(metier):
    if metier == '1':
        submenu_title = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                Menu Mineur                                                           ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        """
        options = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  Choisissez votre zone :                                                                                             ║
║  1 - MineYjupe + Mine_Auderie + Mine_Istairameur                                                                     ║
║  2 - MineYjupe                                                                                                       ║
║  3 - Mine_Auderie                                                                                                    ║
║  4 - Mine_Istairameur                                                                                                ║
║  5 - Mine_Hérale                                                                      0 - Retour au menu principal   ║
║  6 - Tunnel_de_Kartonpath                                                                                            ║
║  7 - Mine_Lac_de_Cania                                                                                               ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        """
    elif metier == '2':
        submenu_title = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                Menu Bûcheron                                                         ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        """
        options = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  Choisissez votre zone :                                                                                             ║
║  1 - Foret_de_leo                                                                                                    ║
║  2 - Foret_de_armand                                                                                                 ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        """
    elif metier == '3':
        submenu_title = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                Menu Pêcheur                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        """
        options = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  Choisissez votre zone :                                                                                             ║
║  1 - Zone1                                                                                                           ║
║  2 - Zone2                                                                                                           ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        """
    elif metier == '4':
        submenu_title = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                Menu Paysan                                                           ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        """
        options = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  Choisissez votre zone :                                                                                             ║
║  1 - Zone1                                                                                                           ║
║  2 - Zone2                                                                                                           ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        """
    print(submenu_title)
    print(options)
    time.sleep(1)  # Pause pour l'effet

def load_maps_data(metier):
    while True:
        zone = input("Choisissez votre zone : ")
        if zone == '0':
            return None, None  # Indique que l'utilisateur veut retourner au menu principal

        if metier == '1':
            if zone == '1':
                with open('mineur\\mineur.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['mineur_amakna_maps']
            elif zone == '2':
                with open('mineur\\grotte_unique.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['MineYjupe']
            elif zone == '3':
                with open('mineur\\grotte_unique.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['Mine_Auderie']
            elif zone == '4':
                with open('mineur\\grotte_unique.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['Mine_Istairameur']
            elif zone == '5':
                with open('mineur\\grotte_unique.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['Mine_Herale']
            elif zone == '6':
                with open('mineur\\grotte_unique.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['Tunnel_de_Kartonpath']
            elif zone == '7':
                with open('mineur\\grotte_unique.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['Mine_Lac_de_Cania']
            else:
                print("Choix invalide. Veuillez réessayer.")
                time.sleep(2)
                continue
            resource_type = 'minerals'

        elif metier == '2':
            if zone == '1':
                with open('bucheron\\bucheron.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['Foret_de_leo']
            elif zone == '2':
                with open('bucheron\\bucheron.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['Foret_de_armand']
            else:
                print("Choix invalide. Veuillez réessayer.")
                time.sleep(2)
                continue
            resource_type = 'bois'

        elif metier == '3':
            if zone == '1':
                with open('pecheur\\pecheur.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['Zone1']
            elif zone == '2':
                with open('pecheur\\pecheur.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['Zone2']
            else:
                print("Choix invalide. Veuillez réessayer.")
                time.sleep(2)
                continue
            resource_type = 'poisson'

        elif metier == '4':
            if zone == '1':
                with open('paysan\\paysan.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['Zone1']
            elif zone == '2':
                with open('paysan\\paysan.json', 'r') as file:
                    maps_data = json.load(file)
                maps = maps_data['Zone2']
            else:
                print("Choix invalide. Veuillez réessayer.")
                time.sleep(2)
                continue
            resource_type = 'ble'

        if maps and resource_type:
            return maps, resource_type


def collect_resources(locations):
    for x, y in locations:
        pyautogui.moveTo(x, y, duration=0.3)
        pyautogui.mouseDown(x, y)
        time.sleep(0.1) # Temp de 0.1 seconde de click declick
        pyautogui.mouseUp(x, y)
        time.sleep(0.5)  # Pause pour simuler le temps de minage

def change_map(position):
    pyautogui.moveTo(position[0], position[1], duration=10)
    time.sleep(2)  # Pause avant de cliquer
    pyautogui.mouseDown()
    time.sleep(0.1) # Temp de 0.1 seconde de click declick
    pyautogui.mouseUp()


def main():

    while True:
        clear_console()
        display_title()

        metier = input("Votre choix: ")

        if metier in ['1', '2', '3', '4']:
            clear_console()
            display_title()
            display_soustitle(metier)
            maps, resource_type = load_maps_data(metier)

            if maps is None and resource_type is None:
                # Retourner au menu principal
                continue
            if maps and resource_type:
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
                time.sleep(2)
        else:
            print("Choix invalide. Veuillez réessayer.")
            time.sleep(2)

    current_index = 0
    num_maps = len(maps)

    while True:
        current_map = maps[current_index]
        
        print(f"Récolte dans {current_map['name']}")
        collect_resources(current_map[resource_type])
        
        # Passer à la carte suivante
        current_index = (current_index + 1) % num_maps
        next_map = maps[current_index]
        
        print(f"Changement de carte depuis {current_map['name']} vers {next_map['name']}")
        change_map(current_map['change_position'])
        
        time.sleep(3)  # Attendre avant de commencer le processus dans la nouvelle carte

if __name__ == "__main__":
    main()
