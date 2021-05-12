import pgzrun

WIDTH = 500
HEIGHT = 300
NUM=5
balls=[]

for i in range(NUM):
        ball=Actor("sball")
        ball.x=50*i+100
        ball.y=100
        ball.dx=5+i
        ball.dy=5+i
        balls.append(ball)

def draw():
        screen.fill((255,255,255))
        for ball in balls:
                ball.draw()

def update():
        for ball in balls:
                ball.x += ball.dx
                ball.y += ball.dy   
                if ball.right > WIDTH or ball.left <0:
                        ball.dx = -ball.dx
                if ball.bottom > HEIGHT or ball.top <0:
                        ball.dy = -ball.dy



pgzrun.go()
