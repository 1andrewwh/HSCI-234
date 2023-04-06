import js
p5 = js.window

#PREVIEW: Click to Show characters: in-game set (state2)
state = 'Start'
bg = p5.loadImage('targettack-bg-img.jpg')
lightgreen = p5.color('#EDF2D0')
darkgreen = p5.color('#777D54')
sniper_img = p5.loadImage('Sniper.png')
sniper_runes = p5.loadImage('sniper-runes.png')
tank_runes = p5.loadImage('tank-runes.png')
mercenary_runes = p5.loadImage('mercenary-runes.png')
start_button = p5.loadImage('Targettack-start.jpg')
tank_img = p5.loadImage('Tankman.png')
mercenary_img = p5.loadImage('Mercenary.png')
img_sniper_bullet = p5.loadImage('sniperbullet.png')
img_tank_bullet = p5.loadImage('tank_bullet.png')
img_mercenary_bullet = p5.loadImage('mercenary_bullet.png')

character = ["Sniper", "Tank", "Mercenary"]
character_attributes = ["Fast Bullet", "Large Bullet", "Fast Speed"]

class Button:
    global lightgreen
    global darkgreen
    global state
    text = character[0]
    def __init__(self, x, y, w, h, text, text_x, text_y):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.text_x = text_x
        self.text_y = text_y

    def draw(self):
        p5.strokeWeight(1)
        p5.stroke(lightgreen)
        p5.fill(darkgreen)
        p5.rect(self.x,self.y,self.w,self.h,3)
        p5.fill(lightgreen)
        p5.textSize(9)
        p5.text(self.text, self.text_x, self.text_y)
        if(p5.mouseX > self.x) and (p5.mouseX < self.x + self.w) \
        and (p5.mouseY > self.y) and (p5.mouseY < self.y + self.h):
                p5.fill(lightgreen)
                p5.rect(self.x,self.y,self.w,self.h,3)
                p5.fill(darkgreen)
                p5.text(self.text, self.text_x, self.text_y)
                if(self.x == 100) and (self.y == 164):
                    startsniper.draw()
                elif(self.x == 100) and (self.y == 194):
                    starttank.draw()
                elif(self.x == 100) and (self.y == 223):
                    startmercenary.draw()

class Start:
    global sniper_runes, darkgreen
    def __init__(self, x, y, w, h, text, text_x, text_y, subtext, subtext_x, subtext_y):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.text_x = text_x
        self.text_y = text_y
        self.subtext = subtext
        self.subtext_x = subtext_x
        self.subtext_y = subtext_y

    def draw(self):
        p5.fill(255)
        p5.rect(self.x, self.y, self.w, self.h,5)
        # sniper.draw()
        p5.fill(40)
        p5.textSize(8)
        p5.textStyle(p5.NORMAL)
        p5.text(self.text, self.text_x, self.text_y)
        if(self.text == character[0]):
            sniper.draw()
            p5.image(sniper_runes, 189, 73, 17, 17)
        elif(self.text == character[1]):
            tank.draw()
            p5.image(tank_runes, 189, 73, 17, 17)
        elif(self.text == character[2]):
            mercenary.draw()
            p5.image(mercenary_runes, 189, 73, 17, 17)
        p5.fill(140)
        p5.textSize(6)
        p5.text(self.subtext, self.subtext_x, self.subtext_y)
        StartButton()
    

class Target:
    # x = 0
    # y = 0
    # circle_xspeed = 2
    # circle_yspeed = 1
    # circle_radius = 25
    def __init__(self, x=150,y=150, speedx = 2, speedy = 1, r = 25, color = 60, lives = 1):
        self.x = x 
        self.y = y 
        self.speedx = speedx
        self.speedy = speedy
        self.r = r
        self.color = color
        self.lives = lives
    def draw(self):
        p5.ellipse(self.x, self.y, 30, 30)
        p5.fill(self.color)
        p5.noStroke()
    def move(self):
        if(self.x < self.r) or (self.x > p5.width - self.r):
            self.speedx = -self.speedx
        if(self.y < self.r) or (self.y > p5.height - self.r):
            self.speedy = -self.speedy
        self.x = self.x + self.speedx
        self.y = self.y + self.speedy
        p5.ellipse(self.x, self.y, self.r*2, self.r*2)


# target_list = []
# for i in range(5):    
x = p5.random(50,250)
y = p5.random(50,250)
#     easytarget = Target(x,y)
#     target_list.append(easytarget)

# for i in range(len(target_list)):
#     target_list[i].draw()
#     target_list[i].move()


class Sniper:  

    x = 0  
    y = 0  
    angle = 0

    def __init__(self, x = 0, y = 0, speed = 0):
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.rotate(self.angle + 20.38)
        p5.image(sniper_img, -15, -25, 23, 39)
        p5.pop()

    def move(self):
        if(p5.keyIsPressed == True):
            if(p5.key == 'a'):
                if(self.x > 30):
                    self.x -= 2.25
            if(p5.key == 'd'):
                if(self.x < p5.width - 60):
                    self.x +=2.25
            if(p5.key == 'w'):
                if(self.y > 60):
                    self.y -= 2.25
            if(p5.key == 's'):
                if(self.y < p5.height - 80):
                    self.y += 2.25
class SniperBullet:
    angle = 0

    def __init__(self, x = 150, y = 250, w = 4, h = 10):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(img_sniper_bullet, 0,0, self.w, self.h)
        p5.pop()

    def update(self):
        self.y -=4

        # dx = p5.mouseX - self.x
        # dy = p5.mouseY - self.y
        # distance = sqrt(dx*dx + dy*dy)

        # if(distance > 5):
        #     self.x += dx/distance * 5
        #     self.y += dy/distance * 5

class TankMan:  

    x = 0  
    y = 0  
    angle = 0

    def __init__(self, x = 0, y = 0, speed = 1):
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.rotate(self.angle + 20.38)
        p5.image(tank_img, -13, -22, 27, 29)
        p5.pop()


    def move(self):
        if(p5.keyIsPressed == True):
            if(p5.key == 'a'):
                if(self.x > 30):
                    self.x -= 1.5
            if(p5.key == 'd'):
                if(self.x < p5.width - 60):
                    self.x += 1.5
            if(p5.key == 'w'):
                if(self.y > 60):
                    self.y -= 1.5
            if(p5.key == 's'):
                if(self.y < p5.height - 80):
                    self.y += 1.5


class TankBullet:
    def __init__(self, x = 150, y = 250, w = 10, h = 18):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(img_tank_bullet, 0,0, self.w, self.h)
        p5.pop()

    def update(self):
        self.y -=3


class Mercenary:  

    x = 0  
    y = 0
    angle = 0

    def __init__(self, x = 0, y = 0, speed = 1):
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.rotate(self.angle + 20.38)
        p5.image(mercenary_img, -10, -22, 19, 30)
        p5.pop()

    def move(self):
        if(p5.keyIsPressed == True):
            if(p5.key == 'a'):
                if(self.x > 30):
                    self.x -= 3
            if(p5.key == 'd'):
                if(self.x < p5.width - 60):
                    self.x += 3
            if(p5.key == 'w'):
                if(self.y > 60):
                    self.y -= 3
            if(p5.key == 's'):
                if(self.y < p5.height - 80):
                    self.y += 3


class MercenaryBullet:
    def __init__(self, x = 150, y = 250 , w = 6, h = 6):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(img_mercenary_bullet, 0,0, self.w, self.h)
        p5.pop()

    def update(self):
        self.y -=5


button1 = Button(x = 100, y = 164, w = 101, h = 23, text=character[0], text_x = 138, text_y = 178)
button2 = Button(x = 100, y = 194, w = 101, h = 23, text = character[1], text_x = 141, text_y = 209)
button3 = Button(x = 100, y = 223, w = 101, h = 23, text = character[2], text_x = 130, text_y = 237)
startsniper = Start(x = 85, y = 64, w = 130, h = 82, text=character[0], text_x = 95, text_y = 78, subtext = character_attributes[0], subtext_x = 95, subtext_y = 87)
starttank = Start(x = 85, y = 64, w = 130, h = 82, text=character[1], text_x = 95, text_y = 78, subtext = character_attributes[1], subtext_x = 95, subtext_y = 87)
startmercenary = Start(x = 85, y = 64, w = 130, h = 82, text=character[2], text_x = 95, text_y = 78, subtext = character_attributes[2], subtext_x = 95, subtext_y = 87)
easytarget = Target(x=30,y=30, speedx = 2, speedy = 1, r = 25, color = 180, lives = 1)
mediumtarget = Target(x=30,y=100, speedx = 2.3, speedy = 1.2, r = 20, color = 100, lives = 2)
hardtarget = Target(x=190,y=90, speedx = 3, speedy = 2, r = 15, color = 20, lives = 3)
mercenary = Mercenary(x = 150, y = 150, speed = 1)
tank = TankMan(x = 150, y = 150, speed = 1)
sniper = Sniper(x = 150, y = 150, speed = 2)
sniper_bullet = SniperBullet(150, 0)
tank_bullet = TankBullet(150,0)
mercenary_bullet = MercenaryBullet(150,0)

def setup():
    p5.createCanvas(300, 300)  
    global sniper, state
    mercenary.x = 150
    mercenary.y = 150


def draw():
    global state
    global scl
    if(state == 'Start'):
        easytarget.draw()
        easytarget.move()
        p5.fill(255)
        p5.background(bg) 
        p5.fill(0, 160)
        p5.rect(0, 0, p5.width, p5.height)
        p5.noStroke()
        p5.fill(255)
        p5.textSize(8)
        p5.text('By: Andrew Huang', 216, 19)
        p5.textSize(18)
        p5.textStyle(p5.BOLD)
        p5.text('Targettack', 105, 50)
        startsniper.draw()
        button1.draw()
        button2.draw()
        button3.draw()
        sniper.x = 152
        sniper.y = 118
        sniper.angle = 11.05
        tank.x = 150
        tank.y = 128
        tank.angle = 11.05
        mercenary.x = 149
        mercenary.y = 126
        mercenary.angle = 11.05

    if(state == 'PlaySniper'):
        target_list = []
        target_list.append(easytarget)
        p5.background(bg)
        easytarget.draw()
        easytarget.move()
        dx = p5.mouseX - sniper.x
        dy = p5.mouseY - sniper.y
        sniper.angle = p5.atan2(dy, dx) 
        sniper.draw()
        sniper.move()
        p5.fill(240, 230, 210)
        p5.textSize(24)
        p5.textStyle(p5.BOLD)
        p5.text('Level 1', 112, 280)
        p5.fill(255)
        Aim()
        sniper_bullet.update()
        sniper_bullet.draw()
        d = p5.dist(easytarget.x, easytarget.y, sniper_bullet.x + sniper_bullet.w, sniper_bullet.y + sniper_bullet.h)
        if(d < 26):  
            state = 'sniperlevel2'
        char_d = p5.dist(easytarget.x, easytarget.y, sniper.x +23, sniper.y + 39)
        if(char_d < 23):
            state = "Defeat"

    if(state == 'sniperlevel2'):
        target_list = []
        print(target_list)
        target_list.append(mediumtarget)
        p5.noStroke()
        p5.background(bg)
        p5.fill(0, 160)
        dx = p5.mouseX - sniper.x
        dy = p5.mouseY - sniper.y
        sniper.angle = p5.atan2(dy, dx) 
        sniper.draw()
        sniper.move()
        target_list[0].draw()
        target_list[0].move()
        Aim()
        sniper_bullet.update()
        sniper_bullet.draw()
        p5.fill(240, 230, 210)
        p5.textSize(24)
        p5.textStyle(p5.BOLD)
        p5.noStroke()
        p5.text('Level 2', 112, 280)
        p5.fill(255)
        d = p5.dist(mediumtarget.x, mediumtarget.y, sniper_bullet.x + sniper_bullet.w, sniper_bullet.y + sniper_bullet.h)
        if(d < 26):
            state = 'sniperlevel3'
        char_d = p5.dist(mediumtarget.x, mediumtarget.y, sniper.x, sniper.y)
        if(char_d < 26):
            state = "Defeat"

    if(state == 'sniperlevel3'):
        target_list = []
        print(target_list)
        target_list.append(hardtarget)
        p5.noStroke()
        p5.background(bg)
        p5.fill(0, 160)
        dx = p5.mouseX - sniper.x
        dy = p5.mouseY - sniper.y
        sniper.angle = p5.atan2(dy, dx) 
        sniper.draw()
        sniper.move()
        target_list[0].draw()
        target_list[0].move()
        sniper_bullet.draw()
        sniper_bullet.update()
        p5.fill(240, 230, 210)
        p5.textSize(24)
        p5.textStyle(p5.BOLD)
        p5.noStroke()
        p5.text('Level 3', 112, 280)
        p5.fill(255)
        Aim()
        d = p5.dist(hardtarget.x, hardtarget.y, sniper_bullet.x + sniper_bullet.w, sniper_bullet.y + sniper_bullet.h)
        if(d < 26):
            state = 'Victory'
        char_d = p5.dist(hardtarget.x, hardtarget.y, sniper.x, sniper.y)
        if(char_d < 26):
            state = 'Defeat'
# medium target is faster and smaller

    if(state == 'PlayTank'):
        p5.background(bg)
        easytarget.draw()
        easytarget.move()
        dx = p5.mouseX - tank.x
        dy = p5.mouseY - tank.y
        tank.angle = p5.atan2(dy, dx) 
        tank.draw()
        tank.move()
        Aim()
        tank_bullet.update()
        tank_bullet.draw()
        p5.fill(240, 230, 210)
        p5.textSize(24)
        p5.textStyle(p5.BOLD)
        p5.noStroke()
        p5.text('Level 1', 112, 280)
        p5.fill(255)
        d = p5.dist(easytarget.x, easytarget.y, tank_bullet.x + tank_bullet.w, tank_bullet.y + tank_bullet.h)
        if(d < 28):  
            state = 'tanklevel2'
        char_d = p5.dist(easytarget.x, easytarget.y, tank.x, tank.y)
        if(char_d < 26):
            state = "Defeat"

    if(state == 'tanklevel2'):
        target_list = []
        print(target_list)
        target_list.append(mediumtarget)
        p5.noStroke()
        p5.background(bg)
        p5.fill(0, 160)
        dx = p5.mouseX - tank.x
        dy = p5.mouseY - tank.y
        tank.angle = p5.atan2(dy, dx) 
        tank.draw()
        tank.move()
        target_list[0].draw()
        target_list[0].move()
        Aim()
        tank_bullet.update()
        tank_bullet.draw()
        p5.fill(240, 230, 210)
        p5.textSize(24)
        p5.textStyle(p5.BOLD)
        p5.noStroke()
        p5.text('Level 2', 112, 280)
        p5.fill(255)
        d = p5.dist(mediumtarget.x, mediumtarget.y, tank_bullet.x + tank_bullet.w, tank_bullet.y + tank_bullet.h)
        if(d < 26):
            state = 'tanklevel3'
        char_d = p5.dist(mediumtarget.x, mediumtarget.y, tank.x, tank.y)
        if(char_d < 26):
            state = "Defeat"

    if(state == 'tanklevel3'):
        target_list = []
        print(target_list)
        target_list.append(hardtarget)
        p5.noStroke()
        p5.background(bg)
        p5.fill(0, 160)
        dx = p5.mouseX - tank.x
        dy = p5.mouseY - tank.y
        tank.angle = p5.atan2(dy, dx) 
        tank.draw()
        tank.move()
        target_list[0].draw()
        target_list[0].move()
        tank_bullet.draw()
        tank_bullet.update()
        p5.fill(240, 230, 210)
        p5.textSize(24)
        p5.textStyle(p5.BOLD)
        p5.noStroke()
        p5.text('Level 3', 112, 280)
        p5.fill(255)
        Aim()
        d = p5.dist(hardtarget.x, hardtarget.y, tank_bullet.x + tank_bullet.w, tank_bullet.y + tank_bullet.h)
        if(d < 26):
            state = 'Victory'
        char_d = p5.dist(hardtarget.x, hardtarget.y, tank.x, tank.y)
        if(char_d < 26):
            state = 'Defeat'
# medium target is faster and smaller

    if(state == 'PlayMercenary'):
        p5.background(bg)
        dx = p5.mouseX - mercenary.x
        dy = p5.mouseY - mercenary.y
        mercenary.angle = p5.atan2(dy, dx) 
        mercenary.draw()
        mercenary.move()
        easytarget.draw()
        easytarget.move()
        Aim()
        mercenary_bullet.update()
        mercenary_bullet.draw()
        p5.fill(240, 230, 210)
        p5.textSize(24)
        p5.textStyle(p5.BOLD)
        p5.noStroke()
        p5.text('Level 1', 112, 280)
        p5.fill(255)
        d = p5.dist(easytarget.x, easytarget.y, mercenary_bullet.x + mercenary_bullet.w, mercenary_bullet.y + mercenary_bullet.h)
        if(d < 26):  
            state = 'mercenarylevel2'
        char_d = p5.dist(easytarget.x, easytarget.y, mercenary.x, mercenary.y)
        if(char_d < 26):
            state = "Defeat"
    
    if(state == 'mercenarylevel2'):
        target_list = []
        print(target_list)
        target_list.append(mediumtarget)
        p5.noStroke()
        p5.background(bg)
        p5.fill(0, 160)
        dx = p5.mouseX - mercenary.x
        dy = p5.mouseY - mercenary.y
        mercenary.angle = p5.atan2(dy, dx) 
        mercenary.draw()
        mercenary.move()
        target_list[0].draw()
        target_list[0].move()
        Aim()
        mercenary_bullet.update()
        mercenary_bullet.draw()
        p5.fill(240, 230, 210)
        p5.textSize(24)
        p5.textStyle(p5.BOLD)
        p5.noStroke()
        p5.text('Level 2', 112, 280)
        p5.fill(255)
        d = p5.dist(mediumtarget.x, mediumtarget.y, mercenary_bullet.x + mercenary_bullet.w, mercenary_bullet.y + mercenary_bullet.h)
        if(d < 26):
            state = 'mercenarylevel3'
        char_d = p5.dist(mediumtarget.x, mediumtarget.y, mercenary.x, mercenary.y)
        if(char_d < 26):
            state = "Defeat"

    if(state == 'mercenarylevel3'):
        target_list = []
        print(target_list)
        target_list.append(hardtarget)
        p5.noStroke()
        p5.background(bg)
        p5.fill(0, 160)
        dx = p5.mouseX - mercenary.x
        dy = p5.mouseY - mercenary.y
        mercenary.angle = p5.atan2(dy, dx) 
        mercenary.draw()
        mercenary.move()
        target_list[0].draw()
        target_list[0].move()
        mercenary_bullet.draw()
        mercenary_bullet.update()
        Aim()
        p5.fill(240, 230, 210)
        p5.textSize(24)
        p5.textStyle(p5.BOLD)
        p5.noStroke()
        p5.text('Level 3', 112, 280)
        p5.fill(255)
        d = p5.dist(hardtarget.x, hardtarget.y, mercenary_bullet.x + mercenary_bullet.w, mercenary_bullet.y + mercenary_bullet.h)
        if(d < 26):
            state = 'Victory'
        char_d = p5.dist(hardtarget.x, hardtarget.y, mercenary.x, mercenary.y)
        if(char_d < 26):
            state = 'Defeat'

    if(state =='Victory'):
        p5.background(bg)
        p5.fill(0, 160)
        p5.rect(0, 0, p5.width, p5.height)
        p5.fill(10,200,185)
        p5.noStroke()
        p5.textSize(40)
        p5.textStyle(p5.BOLD)
        p5.text("Victory!", 84, 150)
        p5.textStyle(p5.NORMAL)
        p5.textSize(12)
        p5.fill(220)
        p5.text("Press 'r' to Play Again", 102, 175)
        if(p5.keyIsPressed):
            if(p5.key == 'r'):
                state = "Start"

    if(state =='Defeat'):
        p5.background(bg)
        p5.fill(0, 160)
        p5.rect(0, 0, p5.width, p5.height)
        p5.fill(250,0,0)
        p5.noStroke()
        p5.textSize(40)
        p5.textStyle(p5.BOLD)
        p5.text("Defeat", 92, 150)
        p5.textStyle(p5.NORMAL)
        p5.textSize(12)
        p5.fill(220)
        p5.text("Press 'r' to Try Again", 102, 175)
        if(p5.keyIsPressed):
            if(p5.key == 'r'):
                state = "Start"

def Aim():
    p5.stroke(255,0,0)
    p5.noFill()
    p5.ellipse(p5.mouseX, p5.mouseY, 20, 20)
    p5.fill(255,0,0)
    p5.line(p5.mouseX,p5.mouseY-25,p5.mouseX, p5.mouseY+25)
    p5.line(p5.mouseX-25, p5.mouseY,p5.mouseX+25, p5.mouseY)
    p5.noFill()

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
    if(state == 'sniperlevel2'):
        if(p5.mousePressed):
            sniper_bullet.x = sniper.x
            sniper_bullet.y = sniper.y
    if(state == 'sniperlevel3'):
        if(p5.mousePressed):
            sniper_bullet.x = sniper.x
            sniper_bullet.y = sniper.y
    if(state == 'tanklevel2'):
        if(p5.mousePressed):
            tank_bullet.x = tank.x
            tank_bullet.y = tank.y
    if(state == 'tanklevel3'):
        if(p5.mousePressed):
            tank_bullet.x = tank.x
            tank_bullet.y = tank.y
    if(state == 'mercenarylevel2'):
        if(p5.mousePressed):
            mercenary_bullet.x = mercenary.x
            mercenary_bullet.y = mercenary.y
    if(state == 'mercenarylevel3'):
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


# def Target():   
#     global circle_x, circle_xspeed
#     global circle_y, circle_yspeed
#     p5.fill(200)
#     p5.noStroke()
#     if(circle_x < circle_radius) or (circle_x > p5.width - circle_radius):
#         circle_xspeed = -circle_xspeed
#     if(circle_y < circle_radius) or (circle_y > p5.height - circle_radius):
#         circle_yspeed = -circle_yspeed
    
#     circle_x = circle_x + circle_xspeed
#     circle_y = circle_y + circle_yspeed
#     p5.ellipse(circle_x, circle_y, circle_radius*2, circle_radius*2)


# target.move()
# for i in range(len(sprite_list)):
# target_list[i].draw()
# target_list[i].move()

# targetAngle = p5.atan2(p5.mouseY - y, p5.mouseX - x)
# p5.strokeWeight(2)
# p5.stroke(p5.color(255, 0, 0))
# p5.line(x, y, x + p5.cos(targetAngle) * scl,
# y + p5.sin(targetAngle) * scl)
# p5.noStroke() 

# def StartSniper():
#     global sniper_runes, darkgreen
#     p5.fill(255)
#     p5.rect(85, 64, 130,82,5)
#     sniper.draw()
#     p5.image(sniper_runes, 189, 73, 17, 17)
#     p5.fill(40)
#     p5.textSize(8)
#     p5.textStyle(p5.NORMAL)
#     p5.text("Sniper", 95, 78)
#     p5.fill(140)
#     p5.textSize(6)
#     p5.text("Long Range", 95, 87)
#     StartButton()

# def StartTank():
#     global sniper_runes, darkgreen
#     p5.fill(255)
#     p5.rect(85, 64, 130,82,5)
#     tank.draw()
# p5.image(sniper_runes, 189, 73, 17, 17)
#     p5.fill(darkgreen)
#     p5.textSize(8)
#     p5.textStyle(p5.NORMAL)
#     p5.text("Tank", 95, 78)
#     p5.textSize(6)
#     p5.text("Large Shots", 95, 87)
#     StartButton()

# def StartMercenary():
#     global sniper_runes, darkgreen
#     p5.fill(255)
#     p5.rect(85, 64, 130,82,5)
#     mercenary.draw()
#     p5.image(sniper_runes, 189, 73, 17, 17)
#     p5.fill(darkgreen)
#     p5.textSize(8)
#     p5.textStyle(p5.NORMAL)
#     p5.text("Mercenary", 95, 78)
#     p5.textSize(6)
#     p5.text("Strong Pulse", 95, 87)
#     StartButton()


# def Button1():
#     button1_x = 100
#     button1_y = 164
#     button1_w = 101
#     button1_h = 23
#     global lightgreen
#     global darkgreen
#     global state
#     p5.strokeWeight(1)
#     p5.stroke(lightgreen)
#     p5.fill(darkgreen)
#     p5.rect(button1_x,button1_y,button1_w,button1_h,3)
#     p5.fill(lightgreen)
#     p5.textSize(9)
#     p5.text('Sniper', 138, 178)
#     if(p5.mouseX > button1_x) and (p5.mouseX < button1_x + button1_w) \
#     and (p5.mouseY > button1_y) and (p5.mouseY < button1_y + button1_h):
#             p5.fill(lightgreen)
#             p5.rect(button1_x,button1_y,button1_w,button1_h,3)
#             p5.fill(darkgreen)
#             p5.text('Sniper', 138, 178)
#             StartSniper()
    

# def Button2():
#     global lightgreen
#     global darkgreen
#     button2_x = 100
#     button2_y = 194
#     button2_w = 101
#     button2_h = 23
#     p5.strokeWeight(1)
#     p5.stroke(lightgreen)
#     p5.fill(darkgreen)
#     p5.rect(button2_x,button2_y,button2_w,button2_h,3)
#     p5.fill(lightgreen)
#     p5.textSize(9)
#     p5.text('Tank', 141, 209)
#     if(p5.mouseX > button2_x) and (p5.mouseX < button2_x + button2_w) \
#     and (p5.mouseY > button2_y) and (p5.mouseY < button2_y + button2_h) \
#     and (p5.mousePressed):
#         p5.fill(lightgreen)
#         p5.rect(button2_x,button2_y,button2_w,button2_h,3)
#         p5.fill(darkgreen)
#         p5.text('Tank', 141, 209)
#         StartTank()

# def Button3():
#     global lightgreen
#     global darkgreen
#     global state
#     button3_x = 100
#     button3_y = 223
#     button3_w = 101
#     button3_h = 23
#     p5.strokeWeight(1)
#     p5.stroke(lightgreen)
#     p5.fill(darkgreen)
#     p5.rect(button3_x,button3_y,button3_w,button3_h,3)
#     p5.fill(lightgreen)
#     p5.textSize(9)
#     p5.text('Mercenary', 130, 237)
#     if(p5.mouseX > button3_x) and (p5.mouseX < button3_x + button3_w) \
#     and (p5.mouseY > button3_y) and (p5.mouseY < button3_y + button3_h) \
#     and (p5.mousePressed):
#         p5.fill(lightgreen)
#         p5.rect(button3_x,button3_y,button3_w,button3_h,3)
#         p5.fill(darkgreen)
#         p5.text('Mercenary', 130, 237)
#         StartMercenary()


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