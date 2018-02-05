from microbit import*

side = 0        #N = 0, E = 1, S = 2, W = 3
x = 0
y = 0
wait_time = 0

def square_scroll(wait_time, side, x, y):
    delay = 200
    current_time = running_time()
    if current_time > wait_time:
        if side == 0:
            if x == 4:
                side += 1
            else:
                x = x + 1
        if side == 1:
            if y == 4:
                side += 1
            else:
                y += 1
        if side == 2:
            if x == 0:
                side += 1
            else:
                x -= 1
        if side == 3:
            if y == 0:
                side = 0
                x = x + 1
            else:
                y -= 1
        wait_time = current_time + delay
        display.show(Image.SQUARE)
        display.set_pixel(x, y, 0) 
        wait_time = current_time + delay
    return(wait_time, side, x, y)
              
while True:
    wait_time, side, x, y = square_scroll(wait_time, side, x, y)        #Use this line to update the scroll.