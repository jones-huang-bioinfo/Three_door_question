import random
switch=0
switch_win=0
stay=0
stay_win=0
play_time=int(input('please type in the number of the game you want to play\n'))
for play_num in range(play_time):
    change=random.choice([True,False])
    car_door=random.randint(0,2)
    my_door=random.randint(0,2)
    if change:
    #count the number
        switch +=1
        if my_door!=car_door:
        #wrong from the beginning
            switch_win+=1
    else:
        stay+=1
        if my_door==car_door:
            #correct from beginning
            stay_win+=1
print('If choose to switch, there is '+'%.1f'%float(switch_win/switch*100)+'%'+' chance to win.')
print('If choose to stay, there is '+'%.1f'%float(stay_win/stay*100)+'%'+' chance to win.')
