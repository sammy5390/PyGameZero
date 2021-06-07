import pgzrun
import random

SIZE = 96
WIDTH = SIZE *3
HEIGHT = SIZE *3
pics=[]
finished= False
lastpic=Actor("puzzle_pic8")
lastpic.left=2 * SIZE
lastpic.top=2 * SIZE

def draw():
	screen.fill((255,255,255))
	
	for pic in pics:
		pic.draw()
	
	if finished:
		lastpic.draw()
		screen.draw.text("Finished!", center=(WIDTH //2, HEIGHT //2), fontsize=50, color="red")
		
	
for i in range(8):
	pic=Actor("puzzle_pic" + str(i))
	pic.index=i
	pics.append(pic)
	
random.shuffle(pics)

for i in range(8):
	pics[i].left=i%3*SIZE
	pics[i].top=i//3*SIZE
	
def on_mouse_down(pos):
	grid_x=pos[0] // SIZE
	grid_y=pos[1] // SIZE
	thispic=get_pic(grid_x, grid_y)
	if thispic ==None:
		return
	if grid_y >0 and get_pic(grid_x, grid_y -1) == None:
		thispic.y -=SIZE
		return
	if grid_y <2 and get_pic(grid_x, grid_y +1) == None:
		thispic.y +=SIZE
		return	
	if grid_x >0 and get_pic(grid_x-1, grid_y) == None:
		thispic.x -=SIZE
		return
	if grid_x <2 and get_pic(grid_x+1, grid_y) == None:
		thispic.x +=SIZE
		return
		
def get_pic(grid_x,grid_y):
	for pic in pics:
		if pic.x // SIZE ==grid_x and pic.y // SIZE == grid_y:
			return pic
	return None
	
def update():
	global finished
	if finished:
		return
	for i in range(8):
		pic=get_pic(i % 3, i // 3)
		if(pic == None or pic.index !=i):
			return

pgzrun.go()
