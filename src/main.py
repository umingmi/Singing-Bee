import json
import time
import colorama
import displays
from colorama import Fore, Back, Style
from os import system
from pygame import mixer
from rich.console import Console
from rich.markdown import Markdown
colorama.init(autoreset=True)

year_choice = []  # stores the year choice of player
song_choice = []  # stores the song choice of player
choice = {}  # stores the keys player can press and use it to call the key from the song list json file
player_name = None  # stores the player's name
player_choice = None  # stores the every action of the player.
player_points = 0  # stores the points of the user once the round started
hints = 3
console = Console()
copyright = "# COPYRIGHT DISCLAMER NOTICE !"
logo = """                                   
                    _____ _         _            _           
                   |   __|_|___ ___|_|___ ___   | |_ ___ ___ 
                   |__   | |   | . | |   | . |  | . | -_| -_|
                   |_____|_|_|_|_  |_|_|_|_  |  |___|___|___|
                               |___|     |___|               
"""
game_menu_header = f"# WELCOME TO SINGING BEE {player_name} !"
about_header = "# ABOUT THE GAME"
help_header = "# INSTRUCTIONS"


# reading from the song list json file
def open_song_list_file():
    with open('songList.json') as f:
        song_list = json.load(f)

# plays the sound from the dictionary
def play_sound(path):
    mixer.music.load(path)
    mixer.music.play()



# input validator for some options
def options(keys):
    option = keys
    return option


def print_position(line,column,text):
    print("\n" * line," " * column, text)


# def display_advice():
#     clear_screen()
#     md = Markdown(warning)
#     console.print(md)
#     print_position(10,10,f"{Fore.YELLOW}We advise to lower your volume to prevent any ear injuries.")
#     displays.press_any_key()


def display_copyright_disclamer():
    clear_screen()
    md = Markdown(copyright)
    console.print(md)
    print_position(5, 3, f"""{Fore.YELLOW}We do not claim the ownership of all of the music/soundsyou will hear.
        All material is the copyright property of its respective owner(s).\n
                     Under Section 107 of the Copyright Act 1976,
         allowance is made for “fair use” for purposes such as criticism, 
          comment, news reporting, teaching, scholarship, and research.\n
                  Fair use is a use permitted by copyright statute 
                        that might otherwise be infringing.\n
                       Non-profit, educational or personal use 
                      tips the balance in favour of fair use.\n
                       WE DO NOT OWN THE RIGHTS OF ANY SONG. 
                     No Copyright infringement intended here.{Fore.WHITE}
    """)
    displays.press_any_key()


def get_player_name():
    global player_name
    clear_screen()
    print_position(10, 20, logo)
    print_position(2,24,f"{Fore.YELLOW}Welcome brood! your name is? : ")
    player_choice = get_user_choice_in_position(1,27)
    print()
    return player_name


def display_loading_screen():
    count = 0
    while count < 4:
        clear_screen()
        print_position(10, 20, logo)
        print("\n", " " * 30, f"{Fore.YELLOW}Loading", "." * count)
        time.sleep(1)
        count += 1


def display_welcome_screen():
    display_loading_screen()
    get_player_name()
    display_advice()
    display_copyright_disclamer()
    clear_screen()


def get_user_choice_in_position(line, column):
    print("\n"*line, " " * column, end="")
    player_choice = input(f"{Fore.YELLOW}{Style.BRIGHT}>> {Fore.WHITE}")
    return player_choice


def display_about():
    md = Markdown(about_header)
    console.print(md)
    print_position(3,30,f"""
                      {Fore.YELLOW}Singing Bee is a console game that 
                tests your knowledge of the most iconic songs.
                   Fill in the missing lyrics and sing along
          to your most treasured tunes from the 1960s up to the 2020s!\n\n
        
              Singing Beewas based on a Philippine TV show called 
                "The Singing Bee". We combined this TV show with 
               "Who Wants to be a Millionaire". Both concepts of
                    the said shows results to this game.\n\n
                    
                          Bees communicate by dancing!{Fore.WHITE}  
    """)
    displays.press_any_key()
    clear_screen()


def display_help():
    md = Markdown(help_header)
    console.print(md)
    print_position(3, 0, f""" 
    {Fore.YELLOW}•{Fore.WHITE} You can choose {Fore.YELLOW}any songs{Fore.WHITE} based on the songlist\n
    {Fore.YELLOW}•{Fore.WHITE} You should guess the {Fore.YELLOW}missing word/s{Fore.WHITE} on the lyrics of the song.\n
    {Fore.YELLOW}•{Fore.WHITE} Your choices will be: {Fore.YELLOW}A{Fore.WHITE},{Fore.YELLOW}B{Fore.WHITE},{Fore.YELLOW}C{Fore.WHITE},{Fore.YELLOW}D{Fore.WHITE} and {Fore.YELLOW}H{Fore.WHITE} for a {Fore.YELLOW}hint{Fore.WHITE} that may use in the round.\n
    {Fore.YELLOW}•{Fore.WHITE} Correct answer without hint will be {Fore.YELLOW}1000 honeys{Fore.WHITE}.\n
    {Fore.YELLOW}•{Fore.WHITE} While correct answer using hint will be {Fore.YELLOW}500 honey{Fore.WHITE}.\n
    {Fore.YELLOW}•{Fore.WHITE} And if your answer is wrong with or without hint, you get {Fore.YELLOW}0 honey{Fore.WHITE}.\n
    {Fore.YELLOW}•{Fore.WHITE} Check the song list here -> {Fore.YELLOW}tinyurl.com/DaBeeBook{Fore.WHITE}\n
    {Fore.YELLOW}•{Fore.WHITE} May you gather the most honeys in the game. Enjoy!\n\n

            {Fore.YELLOW}    Bees can fly up to 12 mph. On every foraging trip, 
                a bee will visit 50-100 flowers to collect nectar!{Fore.WHITE}
    """)
    displays.press_any_key()


def display_quit_screen():
    print_position(15,29,f"""Goodbye, {Fore.YELLOW}{player_name}{Fore.WHITE}.\n
        No matter where you are, the hive will be always a home for you.\n
                              Sing-you soon!
    """)
    time.sleep(5)
    clear_screen()
    exit()

def display_game_menu_header():
    game_menu_header = f"# WELCOME TO SINGING BEE {player_name} !"
    md = Markdown(game_menu_header)
    console.print(md)

def display_invalid_option(line, column):
    print_position(line, column, "Invalid Option")
    time.sleep(1)


def game_menu():
    global player_name
    global player_choice
    while True:
        clear_screen()
        display_game_menu_header()
        print_position(3, 32,f"{Fore.YELLOW}[P] Play")
        print_position(1, 32,f"{Fore.YELLOW}[A] About")
        print_position(1, 32,f"{Fore.YELLOW}[H] Help")
        print_position(1, 32,f"{Fore.YELLOW}[Q] Quit\n")
        player_choice = get_user_choice_in_position(1,31)

        if player_choice.upper() in options(["P", "A", "H", "Q"]):
            if player_choice.upper() == "A":
                clear_screen()
                display_about()

            elif player_choice.upper() == "H":
                clear_screen()
                display_help()

            elif player_choice.upper() == "Q":
                clear_screen()
                display_quit_screen()

            elif player_choice.upper() == "P":
                clear_screen()
                break
        else:
            display_invalid_option(0,0)


# calls the key from a specific song
def song_info(value):
    return song_list[year_choice[0]][song_choice[0]][value]


# displays the enumeration list of year or song
def display_list(item):
    for num, key in enumerate(item, start=1):
        choice[str(num)] = key

    for n, items in choice.items():
        print_position(1,13,f"[{Fore.YELLOW}{n}{Fore.WHITE}] {items}")

def display_song_header():
    song_header = f"# SELECT A SONG FROM {year_choice[0]} \n## SONG CART:{len(song_choice)}"
    md = Markdown(song_header)
    console.print(md)

def display_year_header():
    year_header = f"# SELECT YEAR \n\n## SONG CART:{len(song_choice)}"
    md = Markdown(year_header)
    console.print(md)

def display_your_song_list():
    your_songs_header = f"# YOUR SONG LIST \n## Total songs:{len(song_choice)}"
    md = Markdown(your_songs_header)
    console.print(md)


# SONG SELECTION
def song_selection():
    while True:
        # >>>>>>>>>>>>YEAR SELECT<<<<<<<<<<<
        # clears the key choices from songs
        choice.clear()
        clear_screen()
        display_year_header()
        print("\n" * 2)

        # displays the year of the song list file
        display_list(song_list)
        print_position(1, 13, f"[{Fore.YELLOW}D{Fore.WHITE}] Done")
        player_choice = get_user_choice_in_position(2, 12)

        # checks if player is done choosing
        if player_choice.upper() == 'D':
            clear_screen()
            display_your_song_list()
            print("\n" * 2)
            for num, song in enumerate(song_choice, start=1):
                print_position(1,14,f"{Fore.YELLOW}{num}{Fore.WHITE}. {song}")

            # allows player to go back to year category
            print_position(4, 32, f"[{Fore.YELLOW}B{Fore.WHITE}] Back")
            print_position(1, 25, f"{Fore.YELLOW}Press any key to start")
            player_choice = get_user_choice_in_position(0,26)

            if player_choice.upper() == 'B':
                clear_screen()
                continue

            else:
                year_choice.reverse()
                song_choice.reverse()
                clear_screen()
                break

        if player_choice in choice:
            # inserts the year choice of user from the year category
            year_choice.insert(0, choice[player_choice])

        else:
            display_invalid_option(0, 11)
            clear_screen()
            continue

        # >>>>>>>>>>SONG SELECT<<<<<<<<<<<
        # clears the key choices from year
        clear_screen()
        choice.clear()
        display_song_header()
        print("\n" * 2)
        display_list(song_list[year_choice[0]])
        print_position(1, 13, f"[{Fore.YELLOW}B{Fore.WHITE}] Back")

        player_choice = get_user_choice_in_position(2, 12)
        if player_choice.upper() == 'B':
            year_choice.pop()
            clear_screen()
            continue

        if player_choice in choice:
            if choice[player_choice] in song_choice:
                print_position(0, 11, "You already chose that song")
                time.sleep(1)
                continue

            else:
                # inserts the song choice of user from the song category
                song_choice.insert(0, choice[player_choice])
                continue
        else:
            display_invalid_option(0, 11, )
            year_choice.pop()
            continue


def is_empty(empty):
    if not empty:
        return True
    else:
        return False


# TODO
# START OF ROUND
def round_start():
    global player_points
    global hints
    global player_choice
    while True:

        print(song_choice[0])
        print(song_info("lyrics"))
        print(song_info("choices"))

        print("Total hints available: ", hints)
        while True:
            player_choice = input("What is your choice: ")
            if player_choice.upper() in options(["A", "B", "C", "D", "H"]):
                hint_used = False

                if player_choice.upper() == "H":
                    if hints > 0:
                        if not hint_used:
                            print(song_info("hint"))
                            hint_used = True
                            hints = hints - 1
                            while True:
                                player_choice = input("What is your choice: ")
                                if player_choice.upper() in song_info("hint"):
                                    break
                                else:
                                    print("Invalid Option")

                if player_choice.upper() == (song_info("answer")):
                    print("Correct!")

                    if hint_used:
                        print("You earned 500 honeys!")
                        player_points = player_points + 500
                        break
                    else:
                        print("You earned 1000 honeys!")
                        player_points = player_points + 1000
                        break
                else:
                    print("Wrong")
                    print("You earned 0 honeys")
                    break
            else:
                print("Invalid Option")

        song_choice.pop(0)
        year_choice.pop(0)

        if is_empty(year_choice):
            while True:
                player_choice = input("Do you want to play again? Y/N : ")
                if player_choice.upper() in options(["Y", "N"]):
                    if player_choice.upper() == "Y":
                        return main()
                    elif player_choice.upper() == "N":
                        return display_quit_screen()
                else:
                    print("Invalid Option")






def main():
    displays.set_screen_size(80,40)
    open_song_list_file()
    mixer.init()
    displays.clear_screen()
    displays.advice_screen()
    # song_selection()



if __name__ == "__main__":
    main()
