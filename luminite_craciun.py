# A "Lights Out" style puzzle.
#
# The board is an n x n grid of tiles, each in one of two colors. Clicking a
# tile flips its color and the colors of its (up to four) direct neighbours.
# The goal is to make every tile the "winning" color, yellow(khaki1)

import random
import turtle

t=turtle.Turtle() # the turtle that draws squares and writes the message
s=turtle.Screen() # the window; needed to register the click handler


# Settings, unpacked in one line:
#   a      = side length of one tile (pixels)
#   bx, by = bottom-left corner of the board on screen
#   c      = leftover value (150); not used anywhere in the program
#   n      = the board is n x n tiles
a,bx,by,c,n=70,-170,-200,150,6

# L is the board: L[i][j] is the state (0 or 1) of the tile in column i, row j.
# It starts as all zeros and is filled randomly by drawing().
L=[[0]*n for i in range(n)]
Lcol=['DarkSlateBlue','khaki1']

#title and instructions
t.penup()
t.goto(-200,300)
t.write("The lights went out!", font=("Broadway", 25, "bold"))
t.penup()
t.goto(-700,-50)
t.write("Help bring back the lights!", font=("Arial", 16, "normal"))
t.penup()
t.goto(-700,-70)
t.write("Click the tiles, and flip the colors,", font=("Arial", 16, "normal"))
t.penup()
t.goto(-700,-90)
t.write("until there's no more darkness left!", font=("Arial", 16, "normal"))


def draw_square(turtle, color, a, x, y):
  """Draws one filled square of side `a` with its bottom-left corner at (x, y).
  (The parameter `turtle` shadows the module name inside this function; it
  is the Turtle object passed in, e.g. `t`.)"""
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (4):
    turtle.forward(a)
    turtle.left(90)
  turtle.end_fill()
  turtle.penup()
  turtle.setheading(0)

def drawing(L,bx,by):
    """Fills the board with random states and draws it. Called once at the start.
    Tile (i, j) is drawn at x = a*i + bx, y = a*j + by."""
    turtle.tracer(0) #turns animation off so the board appears at once
    for i in range(len(L[0])):
        for j in range(len(L[0])):
            L[i][j]=int(random.random()*len(Lcol))
            draw_square(t,Lcol[L[i][j]],a,a*i+bx,a*j+by)
    turtle.tracer(1) #brings animation back on again
    print(L)

def redraw(L,bx,by):
    """Redraws the board from the current contents of L (without changing it).
    Called after every click."""
    turtle.tracer(0)
    for i in range(len(L[0])):
        for j in range(len(L[0])):
            draw_square(t, Lcol[L[i][j]], a, a * i + bx, a * j + by)
    turtle.tracer(1)

def neighbours(q):
    """Returna the tiles directly above, left, below and right of tile q = [r, c],
    keeping only those that lie inside the board."""
    r,c=q
    V=[]
    if r>0:
        V.append([r-1,c])
    if c>0:
        V.append([r,c-1])
    if r<n-1:
        V.append([r+1,c])
    if c<n-1:
        V.append([r,c+1])
    return V

def change(L,q):
    """Applies one move at tile q: flip q and each of its neighbours.
    1 - x turns 0 into 1 and 1 into 0."""
    i,j=q
    L[i][j]=1-L[i][j]
    for v in neighbours(q):
        i,j=v
        L[i][j] = 1 - L[i][j]

def fun3(x,y):
    """Click handler (registered with s.onclick): converts the click position
    to a tile, play that move, redraw, and check for a win."""
    i,j=int((x-bx)/a),int((y-by)/a)
    if 0<=i<n and 0<=j<n: #only reacts to clicks on the board
        change(L,[i,j])
        redraw(L,bx,by)
        if verify(L):
            t.penup()
            t.goto(0, 200)
            t.pendown()
            t.color("DeepPink4")
            t.write("Congratulations!You won!", font=("Arial", 15, "bold"), align="center")

def verify(L):
    """Returns True if every tile is in state 1 (the winning color)."""
    for row in L:
        if any(cell!=1 for cell in row):
            return False
    return True
# ---------------------------------------------------------------------------
# Program start
drawing(L,bx,by) #creates a random board and draws it
s.onclick(fun3)  #every click on the window calls fun3
turtle.done()    #keeps the window open and waits for clicks

