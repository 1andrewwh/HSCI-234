
import js
p5 = js.window

random_size = int(p5.random(25,125)) #Q1
random_size1 = int(p5.random(40,60)) #Q6
random_size2 = int(p5.random(60,80)) #Q6
random_size3 = int(p5.random(80,120)) #Q6
alpha = 0 #Q8

# Left Click to Display Square 4

def setup():
    p5.createCanvas(300, 300) 
    print('finished setup')

def draw():
    global random_size1, random_size2, random_size3 #Q6
    global alpha #Q8
    alpha += 1 #Q8
    if(alpha == 255):
        alpha = 0

    p5.noStroke()
    p5.background(255)       
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.strokeWeight(2)  # stroke weight
    p5.text(random_size, 10, 30) #guide
    p5.stroke(107, 0, 245)
    random_square_at(x = 30, y = 30, size = random_size) #Q5 execute
    p5.stroke(25, 127, 84)
    random_square_at(x = random_size1, y = random_size2, size = random_size3) #Q6 execute
    p5.stroke(177, 140, 0, alpha) #Q8 transparency
    random_square_at(x = random_size3, y = random_size3, size = random_size1) #Q6 execute
    if(p5.mouseIsPressed == True): #Q7 conditional
        if(p5.mouseButton == p5.LEFT):
            p5.stroke(125, 29, 117)
            random_square_at(x = random_size2, y = random_size3, size = random_size1) #Q6 execute
    # inside_square() #10 Attempted



def random_square(size): #Q3 function
    p5.line(30, 30, size, 30) #Q2 code
    p5.line(size, 30, size, size)
    p5.line(30, 30, 30, size) 
    p5.line(30, size, size, size) 

def random_square_at(x, y, size): #Q5 function
    p5.push() #Q4 code
    p5.translate(x,y)
    random_square(size)
    p5.pop()

# def inside_square(): #Q10 Attempted
#     global random_size
#     if(p5.mouseX > 30) and (p5.mouseX < 30 + random_size) \ #Q9
#     and (p5.mouseY > random_size) and (p5.mouseY < 30+ random_size):
#         p5.stroke(29, 187, 34)
#         random_square_at(x = 30, y = 30, size = random_size)
#     else:
#         p5.stroke(25, 127, 84)
#         random_square_at(x = 30, y = 30, size = random_size)
        
#     if(p5.mouseX > 30) and (p5.mouseX < 30 + random_size) \ #10
#     and (p5.mouseY > random_size) and (p5.mouseY < 30 + random_size):
#         return True
#     else:
#         return False














