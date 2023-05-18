import math

class Coord:
    def __init__(self,x,y):
         self.x=x
         self.y=y

    def __eq__(self,other):
        if self.x==other.x and self.y==other.y :
            return True
        else :
            return False

    def __repr__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

    def __add__(self,other):
        return Coord(self.x+other.x,self.y+other.y)

    def __sub__(self,other):
        return Coord(self.x-other.x,self.y-other.y)
        
    def __mul__(self,other):
        return Coord(self.x*other,self.y*other)
    
    def distance(self,other):
        d=math.sqrt(math.pow(other.x-self.x,2)+math.pow(other.y-self.y,2))
        return d

    def direction(self,other):
        c=self-other
        cos=c.x/self.distance(other)
        if cos>1/math.sqrt(2):
            return Coord(-1,0)
        if cos<-1/math.sqrt(2):
            return Coord(1,0)
        if c.y>0 :
            return Coord(0,-1)
        else :
            return Coord(0,1)
