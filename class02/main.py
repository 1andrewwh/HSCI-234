import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    white = 255
    black = 0
    light_grey = 170
    medium_grey = 150
    greyish_white = 210
    dark_grey = 120
    lighter_grey = 240
    p5.background(103,12,21)
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 20)
    p5.noStroke()
    
    # moon
    p5.fill(251, 173, 16)
    p5.ellipse(150, 150, 240 , 240)
    
    # body
    p5.fill(light_grey)
    p5.fill(greyish_white)
    for i in range(3):
        p5.triangle(105 + i * 34,129,140 + i *34,133, 112 + i * 34,142)
    p5.fill(medium_grey+10)
    for i in range(3):
        p5.quad(121+i*34,181,132+i*34,179,146+i*34,205,117+i*34,192)
    p5.fill(greyish_white)
    p5.quad(214,205,224,180,241,200,236,213)
    p5.fill(medium_grey-10)
    p5.quad(180,205,185,191,208,208,197,216)
    p5.fill(greyish_white)
    for i in range(1,5):
        p5.quad(44 + i * 34, 142, 73 + i * 34, 133, 98+ i * 34, 179, 88 + i * 34, 181)
    p5.fill(light_grey+20)
    for i in range(1,5):
        p5.triangle(44 + i * 34, 142, 88 + i * 34, 180, 78+ i * 34, 205)
    p5.fill(greyish_white-10)
    
    # legs
    p5.fill(light_grey+10)
    p5.quad(87, 180, 98, 178, 113, 207, 88, 196)
    p5.fill(dark_grey)
    p5.quad(73,163,87,180,80,194, 65,192)
    p5.fill(dark_grey+10)
    p5.quad(65,192,80,194,71,208,58,206)
    p5.fill(205)
    p5.quad(88,196,112,206,98,227,82,223)
    
    # head
    p5.fill(light_grey)
    p5.quad(45,142,74,136,91,138,60,147)
    p5.triangle(60,147,78,142,78,163)
    p5.quad(60,147,78,142,98,178,87,180)
    p5.fill(lighter_grey-25)
    p5.triangle(53, 120, 76, 125, 87, 112)
    p5.triangle(87, 112, 53, 120, 76, 105)
    p5.fill(lighter_grey-10)
    p5.triangle(87, 112, 88, 93, 76, 105)
    p5.triangle(87, 112, 95, 126, 69, 135)
    p5.quad(58, 103, 76, 105, 53, 120, 41, 118)
    p5.fill(greyish_white-5)
    p5.quad(41, 118, 53, 120, 53, 131, 38, 133)
    p5.fill(lighter_grey-10)
    p5.quad(53, 120, 76, 125, 75, 136, 53, 131)
    p5.quad(53, 120, 76, 125, 75, 136, 53, 131)
    p5.quad(69, 93, 88, 93, 76, 105, 58, 103)
    p5.quad(88, 94, 103, 97, 113, 111, 87, 112)
    p5.fill(light_grey+10)
    p5.triangle(44, 142, 52, 131, 73, 136)
    p5.quad(87, 112, 113, 111, 116, 125, 95, 126)
    p5.quad(76, 126, 116, 125, 113, 141, 74, 136)
    p5.triangle(38,133,52,131,45,142)
    
    # eye
    p5.fill(black)
    p5.ellipse(85, 114, 8, 8)
    p5.fill(white)
    
    # ears 
    p5.fill(lighter_grey)
    p5.quad(78, 50, 98, 51, 88, 93, 69, 93)
    p5.fill(lighter_grey-20)
    p5.quad(77, 51, 102, 12, 111, 8, 98, 51)
    p5.fill(medium_grey)
    p5.quad(88, 94, 98, 50, 123, 60, 102, 97)
    p5.fill(dark_grey)
    p5.quad(98, 50, 148, 14, 160, 18, 123, 60)


