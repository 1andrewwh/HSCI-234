import js
p5 = js.window

# Makes hair move in random positions every time the code runs
rand = p5.random(80,90)
rand_hair = p5.random(60,80)
rand_hair2 = p5.random(40,60)
rand_hair1 = p5.random(90,110)
rand_hair3 = p5.random(140,160)
rand_hair4 = p5.random(180,200)

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 


def draw():
    p5.background(230)
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 20)
    p5.noStroke()
    p5.push()
    draw_ears()
    draw_neck()
    draw_face()
    p5.pop()
    draw_eyes()
    draw_lips()
    draw_nose()
    side_hair()
    p5.quad(77,113,101,90,rand,rand_hair2,rand_hair2,rand)
    p5.quad(101,90,138,80,rand,rand_hair2,rand_hair2,rand)
    p5.quad(138,80,179,84,rand_hair3,rand_hair2,rand,rand_hair2)
    p5.quad(179,84,204,98,rand_hair4,rand_hair2,rand_hair1,rand_hair2)
    p5.quad(204,98,227,118,243,86,rand_hair4,rand_hair2)
    draw_shirt()
    hand_cursor(p5.mouseX, p5.mouseY)

def draw_face():
    p5.translate(150,150)
    for i in range(30):
        p5.fill(234 - (i + 10),197 - (i+30),165 - (i + 40))
        p5.rotate(p5.radians(360/30))
        draw_skin()


def draw_lips():
    p5.push()
    p5.translate(108, 186)
    p5.fill(206,92,90)
    p5.arc(40,0, 60,20, p5.radians(-10), p5.radians(190))
    p5.pop()


def hand_cursor(x,y):
    p5.noStroke()
    p5.fill(20)
    p5.quad(x-2,y,x-2,y-40,x+2,y-40,x+2,y)
    p5.fill(255)
    p5.stroke(20)
    p5.strokeWeight(2)
    p5.fill(137,198,255,50)
    p5.ellipse(x,y-80,80,80)


def draw_eyes():
    for i in range(1,4,2):
        p5.fill(245)
        p5.stroke(5)
        p5.ellipse(213 - i*32, 124, 50, 20)
        p5.fill(0)
        p5.ellipse(213 - i*32, 124, 20, 20)
        p5.fill(157,77,13)
        p5.ellipse(213 - i *32, 124, 7, 7)


def draw_shirt():
    p5.fill(41,51,69)
    p5.quad(18,300,32,255,150,300,30,300)
    p5.line(32,254,103,229)
    p5.fill(162, 175, 196)
    p5.quad(32,254,103,229,150,300,30,300)
    p5.fill(41,51,69)
    p5.quad(123,300,280,300,262,254,200,234)


def side_hair():
    p5.fill(67,59,55)
    p5.quad(62,86,80,104,80,157,64,146)
    p5.quad(222,157,237,146,243,86,225,104)


def draw_ears():
    p5.fill(215,163,134)
    p5.ellipse(64,136,20,80)
    p5.ellipse(236,136,20,80)


def draw_neck():
    p5.fill(196,150,113)
    p5.quad(108,220,194,220,216,296,78,296)


def draw_skin():
    p5.arc(20,10, 80, 140, p5.radians(40), p5.radians(190))

def draw_nose():
    p5.fill(234,197,165)
    p5.quad(144,142,156,142,165,167,134,167)
    



















