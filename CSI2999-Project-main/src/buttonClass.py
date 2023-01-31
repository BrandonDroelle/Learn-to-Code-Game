
class buttonClass:
    def __init__(self, img, x, y, font = 0, text = '', tx = 0, ty = 0):
        self.img = img
        self.x = x
        self.y = y
        self.w = img.get_width()
        self.h = img.get_height()
        self.font = font
        self.text = font.render(text, True, (255, 255, 255))
        self.tx = tx
        self.ty = ty

    #draw button onto screen
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        win.blit(self.text, (self.x + self.tx, self.y + self.ty))
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getW(self):
        return self.w

    def getH(self):
        return self.h
