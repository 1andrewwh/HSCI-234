import js
p5 = js.window

# global variables are created outside of any functions:
angle = 0.0  # variable to keep track of angle
weapon_angle = 0.0
y_circle = 150
speed = 0.75
radius = 50


def setup():
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)  # set rectangle drawing mode to CENTER


def draw():
    p5.background(32,123,186)
    p5.fill(133,62,39)
    p5.rect(142,267,350,72)
    p5.fill(100)
    floating_ball()
    weapons()
    robot()
    ball()
    if(p5.mouseIsPressed):
        ball()
        laser()
    p5.fill(255)
    key_controls()
    grass()
    text_labels()
    spikes(2)
    spikes(1.55)
    spikes(1.25)
    spikes(1)


def key_controls():
    p5.text("Left Click = LAZER",10,35)
    p5.text("r = WARNING",10,50)
    p5.text("s = Speed Up", 10, 65)
    p5.text("a = Auto-Pilot", 10, 80)
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 20)
    

def grass():
    p5.fill(39,133,82)
    for i in range(20):
        p5.triangle(0 + i *25,231,30 + i*25,231, 18 + i *25, 260)


def weapons():
    weapon(33)
    weapon(-33)


def weapon(x_position):
    global weapon_angle
    p5.push()
    p5.translate(p5.width/2 + x_position, p5.height/2.55)
    p5.rotate(weapon_angle)  
    p5.fill(175)
    p5.noStroke()
    p5.ellipse(0,0, 50, 50)
    p5.rect(0,0, 55, 55)
    weapon_angle = weapon_angle + 0.005
    if(p5.keyIsPressed):
        if(p5.key == 'a'):
            weapon_angle = 0
    p5.pop()


def robot():
    # body
    p5.push()
    p5.translate(p5.width/2, p5.height/2.65)
    p5.fill(217)
    p5.noStroke()
    p5.rect(0,0,110,110,5)

    # eyes
    p5.fill(255)
    p5.ellipse(-27,-18, 28, 28)
    p5.fill(76,162,245)
    p5.ellipse(-27,-18, 22, 22)
    p5.fill(255)
    p5.ellipse(27,-18, 28, 28)
    p5.fill(76,162,245)
    p5.ellipse(27,-18, 22, 22)
    if(p5.keyIsPressed):
        if(p5.key == 'r'):
            p5.fill(255,76,76)
            p5.ellipse(27,-18, 22, 22)
            p5.ellipse(-27,-18, 22, 22)

    # mouth
    p5.fill(245)
    p5.rect(0,25,50,20,10)
    
    # antena
    p5.fill(140)
    p5.rect(0,-70,15,30)
    p5.fill(217)
    p5.ellipse(0,-90,25,25)
    p5.pop()


def ball():
    p5.noStroke()
    p5.fill(200)
    global y_circle, speed
    p5.ellipse(0,y_circle,radius*2,radius*2)
    y_circle = y_circle + speed
    if(y_circle > p5.height - radius - 72) or (y_circle < radius):
        speed = -speed
    if(p5.mouseIsPressed):
        p5.fill(32,123,186)
        p5.ellipse(0,y_circle,radius*2.1,radius*2.1)


def text_labels():
    p5.push()
    p5.translate(12,223)
    p5.fill(255)
    p5.textSize(10)
    p5.text("Key: " + str(p5.key), 0, 20)
    p5.text("Mouse Button: " + str(p5.mouseButton), 0, 35)
    p5.text("Key Pressed: " + str(p5.keyIsPressed), 0, 50)
    p5.text("Mouse Pressed: " + str(p5.mouseIsPressed), 0, 65)
    p5.pop()


def laser():
    p5.fill(255,78,78)
    p5.quad(0,52,138,28,140,31,0,114)
    p5.fill(200)


def floating_ball():
    global angle  # use global keyword to re-use the existing variable
    # NOTE: without the global keyword a new local variable is created
    p5.push()
    p5.translate(p5.width/2, p5.height/1.55)
    p5.rotate(angle)  
    p5.fill(75)
    p5.noStroke()
    p5.ellipse(0,0, 75, 75)
    p5.rect(0,0, 65, 65)
    angle = angle + 0.005
    if(p5.keyIsPressed):
        if(p5.key == 's'):
            angle = angle + 0.1
    p5.pop()


def spikes(y):
    global angle  # use global keyword to re-use the existing variable
    # NOTE: without the global keyword a new local variable is created
    p5.push()
    p5.translate(p5.width+20, p5.height/y)
    p5.rotate(angle)  
    p5.noFill()
    p5.stroke(50)
    p5.strokeWeight(10)
    p5.rect(0,0, 75, 75)
    angle = angle + 0.02  
    p5.pop()


