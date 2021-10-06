import random

#creating 2d matrix
map = []
length = int(input("Length: "))
height = int(input("Height: "))
#this translates to a 2d array in C#
map = [[0 for i in range(length)] for j in range(height)]

#setting the start room
current_room = [random.randint(0, length - 1), 0]

#setting the start point of the room
map[0][current_room[0]] = 1
previous_decision = map[0][current_room[0]]

#layout generation
while True:
    #roll decision on what to do
    decision = random.randint(1, 5)
    #move the current room
    if decision == 5:
        current_room[1] += 1
    if decision == 1 or decision == 2:
        if current_room[0] != 0 and previous_decision != 3 and previous_decision != 4:
            current_room[0] -= 1
        else:
            decision = 5
            current_room[1] += 1
    if decision == 3 or decision == 4:
        if current_room[0] != length - 1 and previous_decision != 1 and previous_decision != 2:
            current_room[0] += 1
        else:
            decision = 5
            current_room[1] += 1
    #check if the current room is at the bottom; place exit room if it is
    if current_room[1] == height:
        current_room[1] -= 1
        map[current_room[1]][current_room[0]] = 4
        break
    #set room as type 1
    map[current_room[1]][current_room[0]] = 1
    #check if current room is going down, then override last room with type 2 and set current room as type 3
    if decision == 5:
        map[current_room[1] - 1][current_room[0]] = 2
        map[current_room[1]][current_room[0]] = 3
        if previous_decision != 5:
            map[current_room[1] - 1][current_room[0]] = 5
    #set previous decision
    previous_decision = decision

#this is just to print the map in a human-readable form
final_map = ""
room = ""
for i in map:
    for j in map[map.index(i)]:
        if j == 0:
            room = "##"
        if j == 1:
            room = "--"
        if j == 2:
            room = "||"
        if j == 3:
            room = "__"
        if j == 4:
            room = "Ex"
        if j == 5:
            room = "\\/"
        final_map = final_map + room
    final_map = final_map + "\n"
print(final_map)

#ROOM KEYS:
#Type 0: no room (or bonus room)
#Type 1: horizontal corridor
#Type 2: vertical corridor
#Type 3: left/right and top doors
#Type 4: level finish
#Type 5: left/right and bottom doors
    