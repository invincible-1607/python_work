import turtle
import requests

WIDTH = 550
background_color = (251,247,245)
original_grid_element_color = (52, 31, 151)
buffer = 5

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

def insert(win, position):
    i,j = position[1], position[0]
    myfont = turtle.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in turtle.event.get():
            if event.type == turtle.QUIT:
                return
            if event.type == turtle.KEYDOWN:
                if(grid_original[i-1][j-1] != 0):
                    return
                if(event.key == 48): #checking with 0
                    grid[i-1][j-1] = event.key - 48
                    turtle.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    turtle.display.update()
                    return
                if(0 < event.key - 48 <10):  #We are checking for valid input
                    turtle.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    value = myfont.render(str(event.key-48), True, (0,0,0))
                    win.blit(value, (position[0]*50 +15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    turtle.display.update()
                    return
                return
        


def main():    
    turtle.init()
    win = turtle.display.set_mode((WIDTH, WIDTH))
    turtle.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = turtle.font.SysFont('Comic Sans MS', 35)
    
    for i in range(0,10):
        if(i%3 == 0):
            turtle.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            turtle.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        turtle.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        turtle.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    turtle.display.update()
    
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    turtle.display.update()
            
        
    while True: 
        for event in turtle.event.get():
            if event.type == turtle.MOUSEBUTTONUP and event.button == 1:
                pos = turtle.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == turtle.QUIT:
                turtle.quit()
                return
   
main()