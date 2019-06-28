"""
Description: Extracting player's information on multiple category 
Dependenies:
        -requests
        -bs4
        -pandas
output: Multiple csv file containing players information as per category

"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


output_file = "player_ranking.csv"
response = requests.get("http://www.dolphinsim.com/ratings/pga/")
soup = BeautifulSoup(response.content, "lxml")
texts = soup.code
number_of_events, wins, top_10s, cuts_made, rounds_made = [],[],[],[],[]
shots_per_round, money_earned, ranks, shots_hit, scores_name, players_name = [],[],[],[],[],[]
lists = []
data = []
all_value = []
new_lines = texts.text.split("\n")

for new_line in new_lines: 
    separating_first_item = new_line.split("  ") # splitting values to collect players' name
    values = new_line.split() # spliting items to get the players' information 
    lists.append(separating_first_item) 
    all_value.append(values)

for num_of_list in lists[1:228]:

    if "NAME" in num_of_list[0]:
        continue
    player_name = num_of_list[0]
    players_name.append(player_name)

for value in all_value[1:228]:
    if value[0]=="NAME":
        continue
    items = value[-10::]
    """
    items represents the data without player name.
    """
    number_of_event = items[0]
    number_of_events.append(number_of_event)
    win = items[1]
    wins.append(win)
    top_10 = items[2]
    top_10s.append(top_10)
    cut_made = items[3]
    cuts_made.append(cut_made)
    round_made = items[4]
    rounds_made.append(round_made)
    shot_per_round = items[5]
    shots_per_round.append(shot_per_round)
    money = items[6]
    money_earned.append(money)
    rank = items[7]
    ranks.append(rank)
    shot_hit = items[8]
    shots_hit.append(shot_hit)
    score_name = items[9]
    scores_name.append(score_name)

for i11,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10 in zip(players_name, number_of_events, wins, top_10s, cuts_made, rounds_made,shots_per_round, 
                                                money_earned, ranks, shots_hit, scores_name, ):
    data.append({
        
        "number of events":i1,
        "wins":i2,
        "top_10s":i3, 
        "cuts_made":i4, 
        "rounds_made":i5,
        "shots_per_round":i6, 
        "money_earned":i7, 
        "ranks":i8, 
        "shots_hit":i9, 
        "scores_name":i10,
        "player name":i11,     

        })
if data:
        df = pd.DataFrame(columns=["player name", "number of events", "wins", "top_10s", "cuts_made", "rounds_made", 
                                    "shots_per_round", "money_earned", "ranks", "shots_hit", "scores_name"])
        df= df.append(data, ignore_index=True)
        df.to_csv(output_file, index=False)


output_file = "all_player_rankings.csv"
for num_of_list in lists[232:723]:
    if "NAME" in num_of_list[0]:
        continue
for value in all_value[232:723]:
    if value[0]=="NAME":
        continue
    items = value[-10::]
    """
    items represents the data without player name.
    """
    number_of_event = items[0]
    number_of_events.append(number_of_event)
    win = items[1]
    wins.append(win)
    top_10 = items[2]
    top_10s.append(top_10)
    cut_made = items[3]
    cuts_made.append(cut_made)
    round_made = items[4]
    rounds_made.append(round_made)
    shot_per_round = items[5]
    shots_per_round.append(shot_per_round)
    money = items[6]
    money_earned.append(money)
    rank = items[7]
    ranks.append(rank)
    shot_hit = items[8]
    shots_hit.append(shot_hit)
    score_name = items[9]
    scores_name.append(score_name)

for i11,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10 in zip(players_name, number_of_events, wins, top_10s, cuts_made, rounds_made,shots_per_round, 
                                                money_earned, ranks, shots_hit, scores_name, ):
    data.append({
        
        "number of events":i1,
        "wins":i2,
        "top_10s":i3, 
        "cuts_made":i4, 
        "rounds_made":i5,
        "shots_per_round":i6, 
        "money_earned":i7, 
        "ranks":i8, 
        "shots_hit":i9, 
        "scores_name":i10,
        "player name":i11,     

        })
if data:
        df = pd.DataFrame(columns=["player name", "number of events", "wins", "top_10s", "cuts_made", "rounds_made", 
                                    "shots_per_round", "money_earned", "ranks", "shots_hit", "scores_name"])
        df= df.append(data, ignore_index=True)
        df.to_csv(output_file, index=False)
