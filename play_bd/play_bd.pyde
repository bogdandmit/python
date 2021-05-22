c=0
t=0
state=0
hp=100
class bilshifr:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def bildraw(self):
        push()
        translate(self.x+10, self.y)
        if keyPressed:
            if key=='w':
                self.y-=2
            if key=='s':
                self.y+=2

        fill("#FAFF00")
        triangle(50, 50, 0, 150, 100, 150)
        fill(255)
        ellipse(50,105,40,20)
        push()
        strokeWeight(2.5)
        line(50,106,50,101)
        pop()
        line(40,50,60,50)
        fill(0)
        rect(45,10,10,40)
        #правая (с моей стороны) рука
        push()
        fill("#0A50FA")
        noStroke()
        triangle(115,57.5,98,100,123,105)
        circle(110,105,25)
        fill("#0590FF")
        triangle(114,67.5,103,100,118,105)
        circle(110,105,17.5)
        pop()
        strokeWeight(2.5)
        line(76,100,100,120)
        line(100,120,110,110)
        #левая рука
        line(25,100,-10,140)
        line(50+10,150,50+10,170)
        line(50+10,170,40+10,180)
        line(50-10,150,50-10,170)
        line(50-10,170,40-10,180)
        pop()
    def atak(self):
        push()
        rect(60,342.5,195,37.5,10)
        fill("#00FF0E")
        rect(15,335,45,45,10)
        rect(60,342.5,c,37.5,10)
        line(125,342.5,125,380)
        line(190,342.5,190,380)
        scale(0.5)
        translate(self.x-15, self.y+610)
        fill("#0A50FA")
        noStroke()
        triangle(57.5,110,105,94,107.5,117.5)
        circle(110,105,25)
        fill("#0590FF")
        triangle(67.5,110,110,96,110,114)
        circle(110,105,17.5)
        pop()
   

class Bullet:
    def __init__(self,x2,y2):
        self.x2=x2
        self.y2=y2
        self.speed = 5
    def move(self):
        self.x2 += self.speed
    def draw_(self):
        push()
        translate(self.x2+10, self.y2)
        fill("#0A50FA")
        noStroke()
        triangle(57.5,110,105,94,107.5,117.5)
        circle(110,105,25)
        fill("#0590FF")
        triangle(67.5,110,110,96,110,114)
        circle(110,105,17.5)
        pop()
class ironmen:
    def __init__(self,x1,y1):
        self.x1=x1
        self.y1=y1
    def imendraw(self):
        push()
        translate(self.x1+550,self.y1)
        image(img,0,0,190,190)
        if keyPressed:
            if keyCode==UP:
                self.y1-=2
            if keyCode==DOWN:
                self.y1+=2
        pop()
class Light:
    def __init__(self,x3,y3):
        self.x=x3
        self.speed=5
        self.y=y3
        self.q=0
    def move(self):
        self.x -= self.speed
        if self.x > 475:
            self.q += self.speed
    def Ldraw(self):
        push()
        noStroke()
        #rectMode(CENTER)
        fill("#00E3FF")
        rect(self.x,self.y,self.q,8,50)
        
        pop()
men=ironmen(0,0)
bill = bilshifr(0,0)
spec=bilshifr(0,0)
LiGhT=Light(0,0)
bullet = []
light = []
def setup():
    global img
    size(700,400)
    img = loadImage("1.png")
def draw():
    global state,hp
    print(hp)
    if state==0:
        fill(0,100,255)
        rect(300,175,100,50)
        fill(255,0,0)
        triangle(325,185,325,215,375,200)
        if mousePressed:
            if mouseX>=300 and mouseX<=400 and mouseY>=175 and mouseY<=225:
                state=1
                fill(255)
    elif state==1:
        global c
        if c<195:
            c+=0.2
        background(255)
        bill.bildraw()
        men.imendraw()
        spec.atak()
        if t == 0:
            push()
            fill(0)
            textSize(20)
            text(u"SHIFT для стрельбы",15,395)  
            pop()
        for bul in bullet:
            bul.move()
            bul.draw_()
            if bul.x2 > 575:
                del bullet[0]
        for li in light:
            li.move()
            li.Ldraw()
            if li.x <= 0:
                del light[0]
                if li.y >= bill.y and li.y < bill.y + 100:
                    hp -= 25   
        
def keyReleased():
    global c,t
    if keyCode == SHIFT and len(bullet) <= 2 and c>=65:
        bullet.append(Bullet(bill.x , bill.y))
        c-=65
        t+=1
    if key == ENTER and len(light) <= 2:
        light.append(Light(men.x1+590,men.y1+100))
        
