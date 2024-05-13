timeslots = [250, 500, 750]
player_schedule = [[100,'on'],[300, 'off'],[200,'on'],[400,'off']]
is_on_court = []

time_on_court = 0
i = 0
for slot in timeslots:
    while i < len(player_schedule) and time_on_court + player_schedule[i][0] <= slot:
        #if player_schedule[i][1] == 'on':
        time_on_court += player_schedule[i][0]
        i += 1
    is_on_court.append(player_schedule[i][1] == 'on' if i > 0 else False)

print(is_on_court)