import pygame,math,time
pygame.init()
from pygame.math import Vector2
screen = pygame.display.set_mode((1400, 900))
clock = pygame.time.Clock()

car2=pygame.image.load('car1.png')
angle2=0
u0,v0=95,695#700
Q=23
border=[0]*Q
images=['img05.png','img1.png','img2.png','img3.png','img4.png',\
        'img5.png','img6.png','imgeе7.png','imgeе8.png',\
        'imgeе9.png','imgeе10.png','img11.png','img12.png','img13.png',\
        'img14.png','img15.png','img16.png','img17.png','img18.png',\
        'img19.png','img20.png','img21.png','img22.png']

for i in range(Q):
    border[i]=pygame.image.load(images[i])
    
X=[700,120,180,250,350,415,460,570,570,665,970,990,1230,1290,1330,1200,985,\
   685,705,595,560,135,90]
Y=[450,610,610,580,580,570,650,590,350,255,550,260,280,300,210,120,125,\
   450,680,640,760,745,670]
u,v=0,-5

u,v=0,-5

border_rect=[0]*Q
Pos=[0]*Q
for i in range (Q):
    border_rect[i]=border[i].get_rect(center=(X[i],Y[i]))
    Pos[i]=Vector2(border_rect[i].center)
ddelta=[0]*Q
        
def turn():
    global u0,v0,CAR2_pos
    u=(3*math.sin(3.14*angle2/180))
    v=(3*math.cos(3.14*angle2/180))
    CAR2=pygame.transform.rotate(car2,angle2)
    u0,v0=u0-u,v0-v
    
def condition1(i,level,S,du,dv,a):
    global k,s,angle2,u0,v0#,ang
    if ddelta[i]<level:
        k=i    
    if k==i and s<=S:
        s=(s+1)
        angle2=angle2-5*a
        #ang=angle2
        #print('k=',k,'s=',s,'angle2=',angle2)
        turn()
    
    if k==i and s>S:

        #if s==S+1:
            #print('k=',k,'s=',s,'angle2=',angle2)
        u0=u0+du
        v0=v0+dv
s,k=0,0
while True:
    #print('u0=',u0,'v0=',v0,'s=',s)
    screen.fill((124,252,0))
    for i in range (1,Q):
        screen.blit(border[i],border_rect[i])
    screen.blit(border[0],border_rect[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    CAR2=pygame.transform.rotate(car2,angle2)
    CAR2_rect=CAR2.get_rect(center=(u0,v0))
    CAR2_pos=Vector2(CAR2_rect.center)
    screen.blit(CAR2,CAR2_rect)
    
    for i in range(1,Q):
        ddelta[i]=pygame.math.Vector2.length(Pos[i]-CAR2_pos)
        
    if angle2==0:
        v0=v0-5
#-------------------------------------------------  
    condition1(1,50,17,5,0,1)
#-----------------------------------------------------------        
    condition1(2,40,22,6,-4,-1)
#-------------------------------------------------------------
    condition1(3,55,27,5,0.5,1)
#---------------------------------------------------
    condition1(4,40,30,3,-1,-1)
#-------------------------------------------
    condition1(5,35,45,0.5,2,1)
#--------------------------------------------------------------
    condition1(6,30,64,2,-1,-1)
#----------------------------------------------
    condition1(7,20,75,0.5,-4,-1)
#------------------------------------------------------------
    condition1(8,29,83,3,-4,1)
#------------------------------------------------------------
    condition1(9,50,101,4,4,1)
#--------------------------------------------------
    condition1(10,60,127,0.1,-2.5,-1)
#------------------------------------------
    condition1(11,55,145,5,0,1)
#------------------------------------------------------------
    condition1(12,55,154,3,3,1)
#-----------------------------------------------
    condition1(13,95,177,2,-3,-1)
    
#-----------------------------------------------
    condition1(14,95,190,-3,-3,-1)
#-----------------------------------------------
    condition1(15,65,195,-3,0,-1)
#---------------------------------------------
    condition1(16,40,204,-3,3,-1)
    
#---------------------------------------------
    condition1(17,50,213,0,3,-1)
    
#---------------------------------------------
    condition1(18,77,231,-3,0,1)
    
#--------------------------------------------------
    condition1(19,60,243,-3,4.5,-1)
    
#--------------------------------------------------
    condition1(20,35,255,-5,0,1)
    
#--------------------------------------------------
    condition1(21,30,264,-4,-4.2,1)
#----------------------------------------
    if angle2!=0:
        
        condition1(22,40,271,0,-4,1)
    
    if s==268:
        s=0
        angle2=0
        k=0
        u0=95
        v0=695
    if s==0:
        print('u0=',u0,'v0=',v0)
    pygame.display.flip()
    clock.tick(100)
        
    
    

