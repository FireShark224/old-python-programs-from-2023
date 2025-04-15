import random
import time

# lista graczy
words = ["PolykaczMchu", "dejw_bity_pasem", "Cesarz_Dewolaj_Serowaty_III", "furas", "niska_potrzebuje_taboretu", "chivas#4lyfe"]

# losowanko sigma sigma
random.shuffle(words)

# druzyny lol
team1 = [words.pop(), words.pop()]  # Remove 2 players for team 1
team2 = [words.pop(), words.pop()]  # Remove 2 players for team 2
team3 = [words.pop(), words.pop()]  # Remove 2 players for team 3

# efekt koncowy
print("Team 1 words:", team1)
print("Team 2 words:", team2)
print("Team 3 words:", team3)

time.sleep(10)
