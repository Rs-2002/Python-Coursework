from graphics import *
# colourList=["blue","orange","red"]
#win = GraphWin("test",500,500)
#offset = Point(0,0)

def hash(win,offset,colour):
    
    xOffset = offset.getX()     #xOffset uses the getX() function from grapics to get the X coordinate of the offset so we know what to offset the start point by
    yOffset = offset.getY()     #xOffset uses the getY() function from grapics to get the Y coordinate of the offset so we know what to offset the start point by
    cornerDiag = Line(Point(xOffset+0,yOffset+0),Point(xOffset+100,yOffset+100))    #Creates the diagonal line from 0,0 to 100,100
    cornerDiag2 = Line(Point(xOffset+100,yOffset+0),Point(xOffset+0,yOffset+100))   #Creates the diagonal line from 0,100 to 100,0
    cornerDiag.draw(win)
    cornerDiag.setFill(colour)  #uses the setFill() fumction from graphics to colour the lines
    cornerDiag2.draw(win)
    cornerDiag2.setFill(colour)
    for i in range(0,(100),20):     #the iteration used to draw the lines from 0 - 100 going up by 20 each time. 
        #------------------Drawing of the Lines for the hash-------------------------------
        l = Line(Point(xOffset+0,yOffset+100-i),Point(xOffset+0+i,yOffset+100)) 
        l.draw(win)
        l.setFill(colour)
        l2 = Line(Point(xOffset+100-i,yOffset+0),Point(xOffset+100,yOffset+0+i))
        l2.draw(win)
        l2.setFill(colour)
        l3 = Line(Point(xOffset+0+i,yOffset+0),Point(xOffset+0,yOffset+0+i))
        l3.draw(win)
        l3.setFill(colour)
        l4 = Line(Point(xOffset+100-i,yOffset+100),Point(xOffset+100,yOffset+100-i))
        l4.draw(win)
        l4.setFill(colour)
        #win.getMouse()
#hash(win,offset,colourList[1])        
        
#this function is used to create the 100x100 patch dicatetd by the penultimate number of my student id.
#It needs the window it has to draw it in, the top left coordinates offset from 0,0, and the colour it is meant to fill the triangles with. 
def triangles1(win,offset,colour): 
    xOffset = offset.getX() 
    yOffset = offset.getY()
    r1 = Rectangle(Point(xOffset+0,yOffset+20),Point(xOffset+100,yOffset+40))
    r1.draw(win)
    r1.setFill(colour)
    r1.setOutline(colour)
    r2 = Rectangle(Point(xOffset+0,yOffset+60),Point(xOffset+100,yOffset+80))
    r2.draw(win)
    r2.setFill(colour)
    r2.setOutline(colour)
    for x in range(0,100,20):
        for y in range (0,100,40):
            tri1 = Polygon(Point(xOffset+x,yOffset+20+y),Point(xOffset+x+10,yOffset+0+y),Point(xOffset+x+20,yOffset+20+y))
            tri1.draw(win)
            tri1.setFill(colour)
            tri1.setOutline(colour)
    for x in range(0,100,20):
        for y in range (0,80,40):
            tri2 = Polygon(Point(xOffset+x,yOffset+y+20),Point(xOffset+x+10,yOffset+y+40),Point(xOffset+x+20,yOffset+y+20))
            tri2.draw(win) 
            tri2.setFill("white")
            tri2.setOutline(colour)    
#triangles1(win,offset,colourList[1])     

def square(win,offset,colour): # A testing function to chech wether the patchwork works before i added the patterns to it.
    xOffset = offset.getX()
    yOffset = offset.getY()
    square = Rectangle(Point(xOffset+0,yOffset+0),Point(xOffset+100,yOffset+100))
    square.draw(win)
    square.setFill(colour)
    square.setOutline(colour)

def patchwork(win,colourList,size):
    
    i=1
    for x in range(0,(size*100+100),100):
        i=i+1
        for y in range (0,(size*100-x+100),100):
            offset = Point(x,(size*100)-y)
            triangles1(win,offset,colourList[(i%2)*2])

    # (i%2*2) is used to flip the colours of the triangle pattern between the necessary colours as % gives either 1 or 0 in this situation then itis * by 2 so that the correct colours are chosen the forst or last entered by the user

    # for x in range (0,(size*100),200):
    #     for y in range (0+x,(size*100),100):
    #         offset = Point(x,y)
    #         triangles1(win,offset,colourList[0])
        
            
    # for x in range (100,(size*100),200):
    #     for y in range (0+x,(size*100),100):
    #         offset = Point(x,y)
    #         triangles1(win,offset,colourList[2])
            
    for x in range(100,(size*100),100):
        for y in range (0,(size*100-x),100):
            offset = Point((size*100)-x,y)
            hash(win,offset,colourList[1])             
    win.getMouse()



def patchworkNoPatterns(win,colourList,size):
    
    for x in range (0,(size*100),200):
        for y in range (0+x,(size*100),100):
            offset = Point(x,y)
            square(win,offset,colourList[0])
            i=i+10
    for x in range (100,(size*100),200):
        for y in range (0+x,(size*100),100):
            offset = Point(x,y)
            square(win,offset,colourList[2])
            i=i+10
    for x in range(100,(size*100),100):
        for y in range (0,(size*100-x),100):
            offset = Point((size*100)-x,y)
            square(win,offset,colourList[1])             
    win.getMouse()



def colourPicker(colourList):  
    #this part of code asks the user for the colours to be used in a while loop so that the user cant enter colours that are not allowed.
    while len(colourList) != 3:
        colourChoice = str(input("Enter either red ,green,blue,magenta,orange or cyan: "))
        if colourChoice == "red":
            colourList.append(colourChoice)
        elif colourChoice == "green":
            colourList.append(colourChoice)
        elif colourChoice =="blue":
            colourList.append(colourChoice)
        elif colourChoice == "magenta":
            colourList.append(colourChoice)
        elif colourChoice =="orange":
            colourList.append(colourChoice)
        elif colourChoice == "cyan":
            colourList.append(colourChoice)
        else:
            print("that colour is not allowed!")
    return (colourList)

# colourPicker(colourList)
def main():
    #checking wether the size inputed is allowed this is in a loop so you can re enter. 
    allowed = False
    while allowed == False:
        size = int(input("enter either 5,7 or 9:"))
        if size == 5:
            allowed = True
        elif size == 7:
            allowed = True
        elif size == 9:
            allowed = True
        else:
            allowed = False
            
    win = GraphWin("Python Coursework",size*100,size*100)

    colourList = []
    colourPicker(colourList) # this line calls the function colour picker to create the list of colours 
            
    patchwork(win,colourList,size) # this calls the function that creates the patchwork out of the two patterns
#main()    


def stairs():
    colourList = ["red","yellow","blue"]
    win = GraphWin("stairs",600,600)
    i=0
    for x in range(100,500,100):
        i=i+1
        for y in range (0,500-x,100):
            offset = Point(x,500-y)
            square(win,offset,colourList[i%2])
    win.getMouse()
#stairs()

main()