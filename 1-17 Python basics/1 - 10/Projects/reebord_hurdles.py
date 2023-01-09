def turn_right():
    for i in range(3):
        turn_left()
        
def jump_forward():
    turn_left()
    
    #going up
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right()
    
    #goind down
    while not wall_in_front():
        move()
        
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump_forward()
    else:
        move()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
