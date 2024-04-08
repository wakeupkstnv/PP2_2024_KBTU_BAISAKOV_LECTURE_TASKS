def isIcon(position):
    if 350 <= position[0] <= 380 and 20 <= position[1] <= 50:
        print('rect')
        return 'rect'
    if 350 <= position[0] <= 380 and 70 <= position[1] <= 100:
        print('circle')
        return 'circle'
    if 400 <= position[0] <= 430 and 20 <= position[1] <= 50:
        print('pen')
        return 'pen'
    if 400 <= position[0] <= 430 and 70 <= position[1] <= 100:
        return 'eraser'
    
def isPalitre(position):
    if 25 <= position[1] <= 45 and 25 <= position[0] <= 45: # blue
        return (0, 0, 255)
    if 25 <= position[1] <= 45 and 75 <= position[0] <= 95: # green
        return (0, 255, 0)
    if 25 <= position[1] <= 45 and 125 <= position[0] <= 145: # red
        return (255, 0, 0)
    if 65 <= position[1] <= 85 and 25 <= position[0] <= 45: # black
        return (0, 0, 0)
    if 65 <= position[1] <= 85 and 75 <= position[0] <= 95: # white
        return (255, 255, 255)
    if 65 <= position[1] <= 85 and 125 <= position[0] <= 145: # yellow
        return (255, 255, 0)
    if 105 <= position[1] <= 125 and 25 <= position[0] <= 45: # pink
        return (255, 192, 203)
    if 105 <= position[1] <= 125 and 75 <= position[0] <= 95: # purple 
        return (128, 0, 128) # purple 
    if 105 <= position[1] <= 125 and 125 <= position[0] <= 145: # brown
        return (150, 75, 0)
          
    return  