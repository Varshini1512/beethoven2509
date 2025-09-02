players=[
    {'id':101,'name':'RohitSharma'},
    {'id':102,'name':'ViratKohli'}
]

player={}

player['id']=103
player['name']="Hardik pandya"
print(player)

players.append(player)
print(players)

for player in players:
    if player['id']==103:
        print(player)

player_dict={101:players[0],102:player[1],103:players[2]}

print(player_dict[102])