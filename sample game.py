import CEngine

game=CEngine.display(100,20,' ')

run=True

x=10
y=5
vel=[0,0]
grav=1

max_vel=3
drag=1.25

w=4
h=3

grounded=False

while run:
    if game.pressing('q'):
        run=False

    if grounded:        
        if game.pressing('w'):
            vel[1]=-max_vel
            y-=2
            grounded=False
            
    if game.pressing('d') and vel[0]<max_vel:
        vel[0]+=1
    elif game.pressing('a') and vel[0]>-max_vel:
        vel[0]-=1
    else:
        if abs(vel[0])<0.1:
            vel[0]=0
        else:
            vel[0]/=drag
        
    if y+h+vel[1]<15:
        y+=vel[1]
        if vel[1]<max_vel:
            vel[1]+=grav
        
            
    else:
        y=15-h
        vel[1]=0
        grounded=True

        
    x+=vel[0]

    
        
    
    game.draw_rect((x,y),(w,h),100)
    game.draw_rect((0,0),(1,20),"|")
    game.draw_rect((99,0),(1,20),"|")
    game.draw_rect((0,15),(100,5),"-")
    game.draw_text((0,0),str(int(vel[0]))+"+"+str(int(vel[1]))+","+str(int(x))+'+'+str(int(y)))

    game.update(0.05)
