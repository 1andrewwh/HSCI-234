import js
p5 = js.window

#key 1,2,3 changes states #EC

program_timer = p5.millis()
program_state = 'state1'

def setup():
    p5.createCanvas(300, 300)  
    print('finished setup..')

def draw():
    global program_timer, program_state
    p5.background(255) 
    program_state #starts with state1
    seconds = int(p5.millis()/1000) #convert to seconds
    p5.push()
    p5.translate(150,150)
    if(p5.millis() > program_timer + 2000): #timer for two second change
        program_state = 'state2'
        program_timer = p5.millis() #updates the two seconds

    if(program_state == 'state2'): #state2 style properties 
        p5.stroke(244,278,220)
        p5.fill(60)
        p5.ellipse(0,0,420,420)
        p5.fill(220,160,55)
        p5.ellipse(0,0,250,250)
        p5.fill(75)
        p5.ellipse(0,0,125,125,50)
        p5.fill(36,29,58)
        p5.ellipse(0,0,100,100,44)
        p5.fill(200,15,93)
        p5.noStroke()
        p5.quad(-35, -15, 35, -15, 10, 30, -10,30)
        p5.ellipse(0,28,20,20)
        p5.ellipse(0,-24,36,36)
        p5.fill(255)
        p5.stroke(10,28,26)
        p5.strokeWeight(2)
        p5.ellipse(0,-24,20,20)
        p5.ellipse(0,15,20,20)
        p5.noStroke()
        p5.fill(255)
        p5.text('02',-7,0)


    if(program_state == 'state3'): #state3 style properties 
        p5.fill(220,160,55)
        p5.ellipse(0,0,100,100)
        p5.rect(0,0, 150,150)
        p5.rect(-150,-150, 150,150)
        p5.fill(255)
        p5.strokeWeight(3)
        p5.stroke(10,28,26)
        p5.ellipse(0,0,30,30)
        p5.ellipse(-50,-50,30,30)
        p5.ellipse(50,50,30,30)
        p5.noStroke()
        p5.fill(0)
        p5.text('03',-7,4)

    p5.pop()
    p5.noStroke()
    p5.fill(255) 
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.text('program_state = ' + program_state, 10, 28)
    p5.text('Seconds: ' + str(seconds), 10, 43) #general labels 
    p5.fill(0)
    
    if(program_state == 'state1'): #state1 style properties 
        p5.fill(0)
        p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
        p5.text('program_state = ' + program_state, 10, 28)
        p5.text('Seconds: ' + str(seconds), 10, 43)
        p5.triangle(81,187,150,71,223,187)
        p5.rect(0,255,300,300)
        p5.push()
        p5.translate(150,150)
        p5.fill(255)
        p5.ellipse(0,15,60,60)
        p5.fill(15,15,200,200)
        p5.rect(-15,45,30,60,8)
        p5.fill(255)
        p5.text('01',-6,65)
        p5.pop()

def keyPressed(event): #EC - State changes by pressing keys 1,2,3
    global program_state, program_timer
    if(p5.key == '1'):
        program_state = 'state1'
    elif(p5.key == '2'):
        program_state = 'state2'
    elif(p5.key == '3'):
        program_state = 'state3'
    program_timer = p5.millis() #resets the state changing for two seconds

def mousePressed(event): #Q3 Changes state to state3 when mousePressed
    global program_state
    print("mousepressed")
    program_state = 'state3'



def keyReleased(event):
    pass
    
def mouseReleased(event):
    pass


























