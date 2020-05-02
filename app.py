from constants import PLAYERS as players
from constants import TEAMS as teams
from statistics import mean


def clean_data():
    """ convert players expreience to boolean, 
    slice and convert height value in the constant.py file
     """
    for player in players:
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False

        player['height'] = int(player['height'][:2])


def balance_team():
    """ Runs the clean function
        splits the players into teams base on experience
    """
    clean_data()
    per_team = int((len(players) / len(teams)))
    exp_divider = per_team / 2
    team_counter = 0
    counter = 0
    for player in players:
        if player['experience'] == True:
            player['team'] = teams[team_counter]
            team_counter += 1
            if team_counter == exp_divider:
                team_counter = 0
        elif player['experience'] == False:
            player['team'] = teams[counter]
            counter += 1
            if counter == exp_divider:
                counter = 0


def display_tool_header():
    ''' Display the tool title'''

    print("""
    BASKETBALL TEAM STATS TOOL

    --------MENU-------
    """)


def menu_options(menu):
    ''' Helper function to coerce the input value to a int
    and return -> int
    '''
    print(menu)
    return int(input("enter an option > "))


def player_choice(menu, options):
    ''' Helper function to vaildate user numeric input
                        or
        Simpler terms: making sure the user do not go above or under 
        the choices.
    '''
    while (True):
        try:
            user_input = menu_options(menu)
            if user_input < options[0] or user_input > options[1]:
                continue
            else:
                return user_input
        except ValueError:
            print("\n\nPLEASE ENTER THE CORRECT VALUE")
            continue


def print_team_stats(*args):
    ''' Helper function: to display the team stats'''
    team_name, players, experienced, inexperienced, height, names, guardians = args

    print("""
    Team: {} Stats
    ------------------------
    Total players: {}
    Total experienced: {}
    Total inexperienced: {}
    Average height: {}

    Players on Team:
        {}

    Guardians:
        {}
""".format(team_name, players, experienced, inexperienced, height, names, guardians))


def get_data(team_name):
    ''' Helper function: to help store the calculated stats'''
    stats = []
    team_data = [player for player in players if player['team'] == team_name]
    stats.append(team_name)
    stats.append(len(team_data))

    stats.append(len([exp['experience']
                      for exp in team_data if True == exp['experience']]))

    stats.append(len([exp['experience']
                      for exp in team_data if True != exp['experience']]))

    stats.append(round(mean([height['height'] for height in team_data]), 1))
    stats.append(", ".join([name['name'] for name in team_data]))
    stats.append(", ".join([guardians['guardians']
                            for guardians in team_data]))

    print_team_stats(*stats)


def start_tool():
    ''' Main function: calls the balance_team() and display_tool_header() 
    never ending loop until the user is done.
    '''
    balance_team()
    display_tool_header()
    while (True):
        user_option = player_choice("""
    Here are your options (pick a number):
        1) Display Team Stats
        2) Quit"
        """, [1, 2])
        if user_option == 2:
            break
        else:
            user_option = player_choice("""
    Here are your options (pick a number):
        1) Panthers
        2) Bandits
        3) Warriors
        """, [1, 3])

            get_data(teams[user_option - 1])

            input("Press ENTER to continue...")


# when app starts run the start_tool()
if __name__ == '__main__':
    start_tool()
