import js
p5 = js.window

#PREVIEW: Click to Show characters: in-game set (state2)
state = 'Start'
bg = p5.loadImage('targettack-bg-img.jpg')
lightgreen = p5.color('#EDF2D0')
darkgreen = p5.color('#777D54')
sniper_img = p5.loadImage('Sniper.png')
sniper_runes = p5.loadImage('sniper-runes.png')
start_button = p5.loadImage('Targettack-start.jpg')
tank_img = p5.loadImage('Tankman.png')
mercenary_img = p5.loadImage('Mercenary.png')
img_sniper_bullet = p5.loadImage('sniperbullet.png')
img_tank_bullet = p5.loadImage('tank_bullet.png')
img_mercenary_bullet = p5.loadImage('mercenary_bullet.png')

circle_x = 150
circle_y = 150
circle_xspeed = 2
circle_yspeed = 1
circle_radius = 25

class SniperBullet:
    def __init__(self, x = 150, y = 250):
        self.x = x
        self.y = y

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(img_sniper_bullet, 0,0, 4,10)
        p5.pop()

    def update(self):
        self.y -=4

class TankBullet:
    def __init__(self, x = 150, y = 250):
        self.x = x
        self.y = y

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(img_tank_bullet, 0,0, 8,15)
        p5.pop()

    def update(self):
        self.y -=2

class MercenaryBullet:
    def __init__(self, x = 150, y = 250):
        self.x = x
        self.y = y

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(img_mercenary_bullet, 0,0, 6,6)
        p5.pop()

    def update(self):
        self.y -=5

class Sniper:  

    x = 0  
    y = 0  

    def __init__(self, x = 0, y = 0, speed = 0):
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self):
        p5.image(sniper_img, self.x, self.y, 23, 39)

    def move(self):
        if(p5.keyIsPressed == True):
            if(p5.key == 'a'):
                if(self.x > 30):
                    self.x -=2
            if(p5.key == 'd'):
                if(self.x < p5.width - 60):
                    self.x +=2
            if(p5.key == 'w'):
                if(self.y > 60):
                    self.y -= 2 
            if(p5.key == 's'):
                if(self.y < p5.height - 80):
                    self.y += 2

class TankMan:  

    x = 0  
    y = 0  

    def __init__(self, x = 0, y = 0, speed = 1):
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self):
        p5.image(tank_img, self.x, self.y, 27, 29)

    def move(self):
        if(p5.keyIsPressed == True):
            if(p5.key == 'a'):
                if(self.x > 30):
                    self.x -=2
            if(p5.key == 'd'):
                if(self.x < p5.width - 60):
                    self.x +=2
            if(p5.key == 'w'):
                if(self.y > 60):
                    self.y -= 2 
            if(p5.key == 's'):
                if(self.y < p5.height - 80):
                    self.y += 2

class Mercenary:  

    x = 0  
    y = 0

    def __init__(self, x = 0, y = 0, speed = 1):
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self):
        p5.image(mercenary_img, self.x, self.y, 19, 30)

    def move(self):
        if(p5.keyIsPressed == True):
            if(p5.key == 'a'):
                if(self.x > 30):
                    self.x -=2
            if(p5.key == 'd'):
                if(self.x < p5.width - 60):
                    self.x +=2
            if(p5.key == 'w'):
                if(self.y > 60):
                    self.y -= 2 
            if(p5.key == 's'):
                if(self.y < p5.height - 80):
                    self.y += 2


mercenary = Mercenary(x = 150, y = 133, speed = 1)
tank = TankMan(x = 150, y = 133, speed = 1)
sniper = Sniper(x = 204, y = 133, speed = 2)
sniper_bullet = SniperBullet(150, 0)
tank_bullet = TankBullet(150,0)
mercenary_bullet = MercenaryBullet(150,0)

def setup():
    p5.createCanvas(300, 300)  
    global sniper, state
    sniper.x = 138
    sniper.y = 95
    tank.x = 138
    tank.y = 95
    mercenary.x = 138
    mercenary.y = 95

def draw():
    global state
    global x, y
    if(state == 'Start'):
        p5.fill(255)
        p5.background(bg) 
        p5.fill(0, 160)
        p5.rect(0, 0, p5.width, p5.height)
        p5.fill(255)
        p5.textSize(8)
        p5.text('By: Andrew Huang', 216, 19)
        p5.textSize(13)
        p5.textStyle(p5.BOLD)
        p5.text('Targettack', 122, 44)
        StartSniper()
        Button1()
        Button2()
        Button3()

    if(state == 'PlaySniper'):
        p5.background(bg)
        sniper.draw()
        sniper.move()
        Target()
        Aim()
        sniper_bullet.update()
        sniper_bullet.draw()
        d = p5.dist(circle_x, circle_y, sniper_bullet.x, sniper_bullet.y)
        if(d < 26):  
            state = 'Victory'
        char_d = p5.dist(circle_x, circle_y, sniper.x, sniper.y)
        if(char_d < 26):
            state = "Defeat"
    if(state =='Victory'):
        p5.background(255)
        p5.fill(0)
        p5.stroke(0)
        p5.textSize(24)
        p5.text("Victory!", 150, 150)
    if(state =='Defeat'):
        p5.background(0)
        p5.fill(255)
        p5.stroke(255)
        p5.textSize(24)
        p5.text("Defeat", 150, 150)

    if(state == 'PlayTank'):
        p5.background(bg)
        tank.draw()
        tank.move()
        Target()
        Aim()
        tank_bullet.update()
        tank_bullet.draw()
        d = p5.dist(circle_x, circle_y, tank_bullet.x, tank_bullet.y)
        if(d < 26):  
            state = 'Victory'
        char_d = p5.dist(circle_x, circle_y, tank.x, tank.y)
        if(char_d < 26):
            state = "Defeat"
    if(state =='Victory'):
        p5.background(255)
        p5.fill(0)
        p5.stroke(0)
        p5.textSize(24)
        p5.text("Victory!", 150, 150)
    if(state =='Defeat'):
        p5.background(0)
        p5.fill(255)
        p5.stroke(255)
        p5.textSize(24)
        p5.text("Defeat", 150, 150)

    if(state == 'PlayMercenary'):
        p5.background(bg)
        mercenary.draw()
        mercenary.move()
        Target()
        Aim()
        mercenary_bullet.update()
        mercenary_bullet.draw()
        d = p5.dist(circle_x, circle_y, mercenary_bullet.x, mercenary_bullet.y)
        if(d < 26):  
            state = 'Victory'
        char_d = p5.dist(circle_x, circle_y, mercenary.x, mercenary.y)
        if(char_d < 26):
            state = "Defeat"
    if(state =='Victory'):
        p5.background(255)
        p5.fill(0)
        p5.stroke(0)
        p5.textSize(24)
        p5.text("Victory!", 150, 150)
    if(state =='Defeat'):
        p5.background(0)
        p5.fill(255)
        p5.stroke(255)
        p5.textSize(24)
        p5.text("Defeat", 150, 150)



def StartButton():
    global state
    button_x = 187
    button_y = 119
    button_w = 18
    button_h = 18
    p5.image(start_button, button_x, button_y, button_w, button_h)
    if(p5.mouseX > button_x) and (p5.mouseX < button_x + button_w) \
    and (p5.mouseY > button_y) and (p5.mouseY < button_y + button_h):
        pass


def StartSniper():
    global sniper_runes, darkgreen
    p5.fill(255)
    p5.rect(85, 64, 130,82,5)
    sniper.draw()
    p5.image(sniper_runes, 189, 73, 17, 17)
    p5.fill(darkgreen)
    p5.textSize(8)
    p5.textStyle(p5.NORMAL)
    p5.text("Sniper", 95, 78)
    p5.textSize(6)
    p5.text("Long Range", 95, 87)
    StartButton()

def StartTank():
    global sniper_runes, darkgreen
    p5.fill(255)
    p5.rect(85, 64, 130,82,5)
    tank.draw()
    p5.image(sniper_runes, 189, 73, 17, 17)
    p5.fill(darkgreen)
    p5.textSize(8)
    p5.textStyle(p5.NORMAL)
    p5.text("Tank", 95, 78)
    p5.textSize(6)
    p5.text("Large Shots", 95, 87)
    StartButton()

def StartMercenary():
    global sniper_runes, darkgreen
    p5.fill(255)
    p5.rect(85, 64, 130,82,5)
    mercenary.draw()
    p5.image(sniper_runes, 189, 73, 17, 17)
    p5.fill(darkgreen)
    p5.textSize(8)
    p5.textStyle(p5.NORMAL)
    p5.text("Mercenary", 95, 78)
    p5.textSize(6)
    p5.text("Strong Pulse", 95, 87)
    StartButton()


def Button1():
    button1_x = 100
    button1_y = 164
    button1_w = 101
    button1_h = 23
    global lightgreen
    global darkgreen
    global state
    p5.strokeWeight(1)
    p5.stroke(lightgreen)
    p5.fill(darkgreen)
    p5.rect(button1_x,button1_y,button1_w,button1_h,3)
    p5.fill(lightgreen)
    p5.textSize(9)
    p5.text('Sniper', 138, 178)
    if(p5.mouseX > button1_x) and (p5.mouseX < button1_x + button1_w) \
    and (p5.mouseY > button1_y) and (p5.mouseY < button1_y + button1_h):
            p5.fill(lightgreen)
            p5.rect(button1_x,button1_y,button1_w,button1_h,3)
            p5.fill(darkgreen)
            p5.text('Sniper', 138, 178)
            StartSniper()


    

def Button2():
    global lightgreen
    global darkgreen
    button2_x = 100
    button2_y = 194
    button2_w = 101
    button2_h = 23
    p5.strokeWeight(1)
    p5.stroke(lightgreen)
    p5.fill(darkgreen)
    p5.rect(button2_x,button2_y,button2_w,button2_h,3)
    p5.fill(lightgreen)
    p5.textSize(9)
    p5.text('Tank', 141, 209)
    if(p5.mouseX > button2_x) and (p5.mouseX < button2_x + button2_w) \
    and (p5.mouseY > button2_y) and (p5.mouseY < button2_y + button2_h) \
    and (p5.mousePressed):
        p5.fill(lightgreen)
        p5.rect(button2_x,button2_y,button2_w,button2_h,3)
        p5.fill(darkgreen)
        p5.text('Tank', 141, 209)
        StartTank()

def Button3():
    global lightgreen
    global darkgreen
    global state
    button3_x = 100
    button3_y = 223
    button3_w = 101
    button3_h = 23
    p5.strokeWeight(1)
    p5.stroke(lightgreen)
    p5.fill(darkgreen)
    p5.rect(button3_x,button3_y,button3_w,button3_h,3)
    p5.fill(lightgreen)
    p5.textSize(9)
    p5.text('Mercenary', 130, 237)
    if(p5.mouseX > button3_x) and (p5.mouseX < button3_x + button3_w) \
    and (p5.mouseY > button3_y) and (p5.mouseY < button3_y + button3_h) \
    and (p5.mousePressed):
        p5.fill(lightgreen)
        p5.rect(button3_x,button3_y,button3_w,button3_h,3)
        p5.fill(darkgreen)
        p5.text('Mercenary', 130, 237)
        StartMercenary()
    
def Target():   
    global circle_x, circle_xspeed
    global circle_y, circle_yspeed
    p5.fill(200)
    p5.noStroke()
    if(circle_x < circle_radius) or (circle_x > p5.width - circle_radius):
        circle_xspeed = -circle_xspeed
    if(circle_y < circle_radius) or (circle_y > p5.height - circle_radius):
        circle_yspeed = -circle_yspeed
    
    circle_x = circle_x + circle_xspeed
    circle_y = circle_y + circle_yspeed
    p5.ellipse(circle_x, circle_y, circle_radius*2, circle_radius*2)

def Aim():
    p5.stroke(255,0,0)
    p5.noFill()
    p5.ellipse(p5.mouseX, p5.mouseY, 20, 20)
    p5.fill(255,0,0)
    p5.line(p5.mouseX,p5.mouseY-25,p5.mouseX, p5.mouseY+25)
    p5.line(p5.mouseX-25, p5.mouseY,p5.mouseX+25, p5.mouseY)
    p5.noFill()



def keyReleased(event):
    pass


def mousePressed(event):
    global sniper_bullet
    if(state == 'PlaySniper'):
        if(p5.mousePressed):
            sniper_bullet.x = sniper.x
            sniper_bullet.y = sniper.y
    if(state == 'PlayTank'):
        if(p5.mousePressed):
            tank_bullet.x = tank.x
            tank_bullet.y = tank.y
    if(state == 'PlayMercenary'):
        if(p5.mousePressed):
            mercenary_bullet.x = mercenary.x
            mercenary_bullet.y = mercenary.y



def mouseReleased(event):
    button1_x = 100
    button1_y = 164
    button1_w = 101
    button1_h = 23
    button2_x = 100
    button2_y = 194
    button2_w = 101
    button2_h = 23
    button3_x = 100
    button3_y = 223
    button3_w = 101
    button3_h = 23
    global state
    if(state == 'Start'):
    #    state = 'Reset'
    #else:
    #    state = 'PlaySniper'
        if(p5.mouseX > button1_x) and (p5.mouseX < button1_x + button1_w) \
        and (p5.mouseY > button1_y) and (p5.mouseY < button1_y + button1_h):
            state = 'PlaySniper'
        if(p5.mouseX > button2_x) and (p5.mouseX < button2_x + button2_w) \
        and (p5.mouseY > button2_y) and (p5.mouseY < button2_y + button2_h) \
        and (p5.mousePressed):
            state = 'PlayTank'
        if(p5.mouseX > button3_x) and (p5.mouseX < button3_x + button3_w) \
        and (p5.mouseY > button3_y) and (p5.mouseY < button3_y + button3_h) \
        and (p5.mousePressed):
            state = 'PlayMercenary'
    print('change state to ' + state)



def keyPressed(event):
    global state
    if(p5.key == '1'):
        state = 'PlaySniper'
    elif(p5.key == '2'):
        state = 'PlayTank'
    elif(p5.key == '3'):
        state = 'PlayMercenary'





# def SniperMove():
#     global sniper
#     if(p5.keyIsPressed == True):
#         if(p5.key == 'a'):
#             if(sniper.x > 30):
#                 sniper.x -=2
#         if(p5.key == 'd'):
#             if(sniper.x < p5.width - 60):
#                 sniper.x +=2
#         if(p5.key == 'w'):
#             if(sniper.y > 60):
#                 sniper.y -= 2 
#         if(p5.key == 's'):
#             if(sniper.y < p5.height - 80):
#                 sniper.y += 2 

# def TankMove():
#     global tank
#     if(p5.keyIsPressed == True):
#         if(p5.key == 'a'):
#             if(tank.x > 30):
#                 tank.x -=2
#         if(p5.key == 'd'):
#             if(tank.x < p5.width - 60):
#                 tank.x +=2
#         if(p5.key == 'w'):
#             if(tank.y > 60):
#                 tank.y -= 2 
#         if(p5.key == 's'):
#             if(tank.y < p5.height - 80):
#                 tank.y += 2 

# def MercenaryMove():
#     global mercenary
#     if(p5.keyIsPressed == True):
#         if(p5.key == 'a'):
#             if(mercenary.x > 30):
#                 mercenary.x -=2
#         if(p5.key == 'd'):
#             if(mercenary.x < p5.width - 60):
#                 mercenary.x +=2
#         if(p5.key == 'w'):
#             if(mercenary.y > 60):
#                 mercenary.y -= 2 
#         if(p5.key == 's'):
#             if(mercenary.y < p5.height - 80):
#                 mercenary.y += 2 