import js
p5 = js.window

#PREVIEW: Click to Show characters: in-game set (state2)

state = 'state1'
bg = p5.loadImage('targettack-bg-img.jpg')
lightgreen = p5.color('#EDF2D0')
darkgreen = p5.color('#777D54')
sniper_img = p5.loadImage('Sniper.png')
sniper_runes = p5.loadImage('sniper-runes.png')
start_button = p5.loadImage('Targettack-start.jpg')
tank_img = p5.loadImage('Tankman.png')
mercenary_img = p5.loadImage('Mercenary.png')


class Sniper:  

    x = 0  
    y = 0  

    def draw(self, x, y):
        p5.image(sniper_img, x, y, 23, 39)

class TankMan:  

    x = 0  
    y = 0  

    def draw(self, x, y):
        p5.image(tank_img, x, y, 27, 29)

class Mercenary:  

    x = 0  
    y = 0

    def draw(self, x, y):
        p5.image(mercenary_img, x, y, 19, 30)


mercenary = Mercenary()
tank = TankMan()
sniper = Sniper()

def setup():
    p5.createCanvas(300, 300)  

def draw():

    global x, y
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
    Button()
    Button2()
    Button3()
    if(state == 'state2'):
        p5.background(bg)
        mercenary.draw(74,142)
        tank.draw(136,142)
        sniper.draw(204,133)

def StartSniper():
    global sniper_runes, darkgreen
    p5.fill(255)
    p5.rect(85, 64, 130,82,5)
    sniper.draw(138,95)
    # p5.image(sniper_img, 138, 95, 23, 39)
    p5.image(sniper_runes, 189, 73, 17, 17)
    p5.fill(darkgreen)
    p5.textSize(8)
    p5.textStyle(p5.NORMAL)
    p5.text("Sniper", 95, 78)
    p5.textSize(6)
    p5.text("Long Range", 95, 87)
    p5.image(start_button, 187, 119, 18, 18)



def Button():
    global lightgreen
    global darkgreen
    p5.strokeWeight(1)
    p5.stroke(lightgreen)
    p5.fill(darkgreen)
    p5.rect(100,164,101,23,3)
    p5.fill(lightgreen)
    p5.textSize(9)
    p5.text('Sniper', 138, 178)

def Button2():
    global lightgreen
    global darkgreen
    p5.strokeWeight(1)
    p5.stroke(lightgreen)
    p5.fill(darkgreen)
    p5.rect(100,194,101,23,3)
    p5.fill(lightgreen)
    p5.textSize(9)
    p5.text('Tank', 141, 209)

def Button3():
    global lightgreen
    global darkgreen
    p5.strokeWeight(1)
    p5.stroke(lightgreen)
    p5.fill(darkgreen)
    p5.rect(100,223,101,23,3)
    p5.fill(lightgreen)
    p5.textSize(9)
    p5.text('Mercenary', 130, 237)
    
    




def keyReleased(event):
    pass

def mousePressed(event):
    global state
    state = "state2"

def mouseReleased(event):
    global state
    state = "state1"

def keyPressed(event):
    pass
