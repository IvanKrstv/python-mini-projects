level = 0 # The user's level
count_of_games = 0 # Keeping track of the number of games for the levels

def user_level():
    global level
    if count_of_games >= 30:
        level = 10
    elif count_of_games >= 26:
        level = 9
    elif count_of_games >= 22:
        level = 8
    elif count_of_games >= 18:
        level = 7
    elif count_of_games >= 14:
        level = 6
    elif count_of_games >= 10:
        level = 5
    elif count_of_games >= 7:
        level = 4
    elif count_of_games >= 4:
        level = 3
    elif count_of_games >= 2:
        level = 2
    else:
        level = 1
    return level

def limit_range():
    return level * 100

def increment_games_played():
    global count_of_games
    count_of_games += 1