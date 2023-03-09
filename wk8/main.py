import js
p5 = js.window

years= 0 

class Player:  

    x = 0  
    y = 0  

    def __init__(self, x = 0, y = 0):
        self.x = x 
        self.y = y 


    def move_point(self, distance_x, distance_y):
        self.x -= distance_x
        self.y += distance_y


    def Opponent(self):
        p5.stroke(230,50,50)
        p5.push()
        p5.translate(self.x, self.y)
        p5.fill(self.y,120,self.x)
        p5.quad(-8, 0, -2, -20,2,-25,6,2)
        p5.fill(165,42,42)
        p5.triangle(-7, 5, 0, -20,5 ,-5)
        p5.ellipse(0, 0, 20, 20)
        p5.fill(220)
        p5.ellipse(-2, 2, 8, 8)
        p5.fill(165,42,42)
        p5.text('(' + str(self.x) + ',' + str(self.y) + ')', 15, 5)
        p5.text('Meteor', 15, -10)
        p5.pop()


    def You(self):
        p5.stroke(255)
        p5.fill(self.x,206,250)
        p5.push()
        p5.translate(self.x, self.y)
        p5.ellipse(0, 0, 60, 60)
        p5.text('(' + str(self.x) + ',' + str(self.y) + ')', 35, 15)
        p5.text('Planet Uranus', 35, -2)
        p5.pop()





player1 = Player(int(p5.random(255)),75)
print(player1.x)

player2 = Player(150, 250)
print(player2.x)



def setup():
    p5.createCanvas(300, 300)  

def draw():
    global years
    global x, y
    p5.fill(255)


    p5.background(0) 
    p5.textSize(18)
    p5.text('Years: ' + str(years), 215, 80)
    p5.textSize(12)

    player1.Opponent()
    player1.x
    player1.y += 4
    if(player1.y > p5.width):
        years += 1
        player1.y = 0
        player1.x = int(p5.random(255))  
    player2.You()

    for i in range(10):
        x = 50
        p5.fill(27,37,134)
        p5.noStroke()
        p5.ellipse(0 + i * x,15,x,x)
        p5.rect(0 + i * 25,5,60,20)

    if(player2.x + 20 > p5.width):
        player2.x = p5.width/2
    if(player2.x + 20 < 0):
        player2.x = p5.width/2


        

def keyPressed(event):
    if(p5.keyCode == p5.RIGHT_ARROW):
        print('move point 10 pixels to the right..')
        player2.move_point(-25, 0)
    if(p5.keyCode == p5.LEFT_ARROW):
        print('move point 10 pixels to the right..')
        player2.move_point(25, 0)  


















        

        
        





















 







    
























