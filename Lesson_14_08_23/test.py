#what it's need to make a game

map = [[3, 1, 1, 0, 1, 0, 0, 2],
       [0, 1, 1, 0, 0, 0, 0, 2],
       [0, 0, 1, 0, 1, 1, 0, 2],
       [0, 1, 1, 0, 0, 0, 0, 2],
       [0, 1, 1, 0, 0, 0, 0, 2]]


#get map
map = get_map()


# initialise pygame
width = 800
height = 600
init_pygame(width, height)


fps = 50
while True:
# game loop
#       redraw map
#       check keyboard
#       if exit key is pressed leave loop
#       if arrow key is pressed leave loop
#       some delay 1/fps in seconds