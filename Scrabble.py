letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Dictionary of letters and their respective point value
letter_to_points = {key:value for key, value in zip(letters,points)}

# Adding blank tile to the dictionary
letter_to_points[" "] = 0

# Function takes in a word and returns how many points that word is worth
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter,0)
  return point_total

brownie_points = score_word("BROWNIE")

player_to_words = {"player1": ["BLUE","TENNIS","EXIT"], "wordNerd": ["EARTH","EYES","MACHINE"], "Lexi Con": ["ERASER","BELLY","HUSKY"], "Prof Reader": ["ZAP","COMA","PERIOD"]}

player_to_points = {}

# Function that adds a player as a key and their respective points as the value into the dictionary "player_to_points"
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

# Function that takes in a player and a word, and adds that word to the list of words they’ve played
def play_word(player, word):
  player_to_words[player].append(word)