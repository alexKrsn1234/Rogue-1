class Game:
    def __init__(self):
        self._mat=[]
        for i in range(6):
            self._mat.append([0]*7)
        self._player=1
        self._winner=0

    def __str__(self):
        s=""
        for i in range(6):
            for j in range(7):
                s+=str(self._mat[i][j])+" "
            s+="\n"
        return s

    def play(self,col):
        if self._winner!=0:
            raise Exception("Game is over")
        if col<0 or col>6:
            raise Exception("Invalid column")
        if self._mat[0][col]!=0:
            raise Exception("Column is full")
        for i in range(5,-1,-1):
            if self._mat[i][col]==0:
                self._mat[i][col]=self._player
                break
        self._winner=self.checkWinner()
        if self._winner==0:
            self._player=3-self._player

    def checkWinner(self):
        for i in range(6):
            for j in range(4):
                if self._mat[i][j]!=0 and self._mat[i][j]==self._mat[i][j+1] and self._mat[i][j]==self._mat[i][j+2] and self._mat[i][j]==self._mat[i][j+3]:
                    return self._mat[i][j]
        for i in range(3):
            for j in range(7):
                if self._mat[i][j]!=0 and self._mat[i][j]==self._mat[i+1][j] and self._mat[i][j]==self._mat[i+2][j] and self._mat[i][j]==self._mat[i+3][j]:
                    return self._mat[i][j]
        for i in range(3):
            for j in range(4):
                if self._mat[i][j]!=0 and self._mat[i][j]==self._mat[i+1][j+1] and self._mat[i][j]==self._mat[i+2][j+2] and self._mat[i][j]==self._mat[i+3][j+3]:
                    return self._mat[i][j]
        for i in range(3):
            for j in range(3,7):
                if self._mat[i][j]!=0 and self._mat[i][j]==self._mat[i+1][j-1] and self._mat[i][j]==self._mat[i+2][j-2] and self._mat[i][j]==self._mat[i+3][j-3]:
                    return self._mat[i][j]
        return 0

    def winner(self):
        return self._winner

    def player(self):
        return self._player

    def copy(self):
        g=Game()
        g._mat=[]
        for i in range(6):
            g._mat.append([0]*7)
        for i in range(6):
            for j in range(7):
                g._mat[i][j]=self._mat[i][j]
        g._player=self._player
        g._winner=self._winner
        return g

    def playAll(self):
        if self._winner!=0:
            raise Exception("Game is over")
        for i in range(7):
            if self._mat[0][i]==0:
                g=self.copy()
                g.play(i)
                if g.winner()!=0:
                    return i
        return -1

    def playAll2(self):
        if self._winner!=0:
            raise Exception("Game is over")
        for i in range(7):
            if self._mat[0][i]==0:
                g=self.copy()
                g.play(i)
                if g.winner()!=0:
                    return i
        for i in range(7):
            if self._mat[0][i]==0:
                g=self.copy()

                g.play(i)
                for j in range(7):
                    if g._mat[0][j]==0:
                        g2=g.copy()
                        g2.play(j)
                        if g2.winner()!=0:
                            return i
            return -1

    def playAll3(self):
        if self._winner!=0:
            raise Exception("Game is over")
        for i in range(7):
            if self._mat[0][i]==0:
                g=self.copy()
                g.play(i)
                if g.winner()!=0:
                    return i
        for i in range(7):
            if self._mat[0][i]==0:
                g=self.copy()
                g.play(i)
                for j in range(7):
                    if g._mat[0][j]==0:
                        g2=g.copy()
                        g2.play(j)
                        if g2.winner()!=0:
                            return i
        for i in range(7):
            if self._mat[0][i]==0:
                g=self.copy()
                g.play(i)
                for j in range(7):
                    if g._mat[0][j]==0:
                        g2=g.copy()
                        g2.play(j)
                        for k in range(7):
                            if g2._mat[0][k]==0:
                                g3=g2.copy()
                                g3.play(k)
                                if g3.winner()!=0:
                                    return i
        return -1
    
    def playAll4(self):
        if self._winner!=0:
            raise Exception("Game is over")
        for i in range(7):
            if self._mat[0][i]==0:
                g=self.copy()
                g.play(i)
                if g.winner()!=0:
                    return i
        for i in range(7):
            if self._mat[0][i]==0:
                g=self.copy()
                g.play(i)
                for j in range(7):
                    if g._mat[0][j]==0:
                        g2=g.copy()
                        g2.play(j)
                        if g2.winner()!=0:
                            return i
        for i in range(7):
            if self._mat[0][i]==0:
                g=self.copy()
                g.play(i)
                for j in range(7):
                    if g._mat[0][j]==0:
                        g2=g.copy()
                        g2.play(j)
                        for k in range(7):
                            if g2._mat[0][k]==0:
                                g3=g2.copy()
                                g3.play(k)
                                if g3.winner()!=0:
                                    return i
        for i in range(7):
            if self._mat[0][i]==0:
                g=self.copy()
                g.play(i)
                for j in range(7):
                    if g._mat[0][j]==0:
                        g2=g.copy()
                        g2.play(j)
                        for k in range(7):
                            if g2._mat[0][k]==0:
                                g3=g2.copy()
                                g3.play(k)
                                for l in range(7):
                                    if g3._mat[0][l]==0:
                                        g4=g3.copy()
                                        g4.play(l)
                                        if g4.winner()!=0:
                                            return i
        return -1


Game().playAll2()