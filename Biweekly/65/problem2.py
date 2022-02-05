class Robot(object):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.dir = "East"
        self.pos = [0, 0]

    def move(self, num):
        if self.dir == "East":
            self.pos[0] += num
        if self.dir == "North":
            self.pos[1] += num
        if self.dir == "West":
            self.pos[0] -= num
        if self.dir == "South":
            self.pos[1] -= num
        while self.pos[0] > self.width - 1 or self.pos[1] > self.height - 1 or self.pos[0] < 0 or self.pos[1] < 0:
            if self.pos[0] > self.width - 1:
                self.pos[1] += self.pos[0] - (self.width - 1)
                self.pos[0] = self.width - 1
                
                self.dir = "North"
            if self.pos[1] > self.height - 1:
                self.pos[0] -= self.pos[1] - (self.height - 1)
                self.pos[1] = self.height - 1
                self.dir = "West"
            if self.pos[0] < 0 :
                self.pos[1] -= 0 - (self.pos[0])
                self.pos[0] = 0
                self.dir = "South"
            if self.pos[1] < 0:
                self.pos[0] += 0 - (self.pos[1])
                self.pos[1] = 0
                self.dir = "East"
        

        

    def getPos(self):
        return self.pos
        

    def getDir(self):
        return self.dir