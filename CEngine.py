import os,time

KYBRD=True
try:
    import keyboard
except:
    print("ERROR: Keyboard Module not found !!!")
    try:
        print("Installing Keyboard...")
        import pip
        pip.main(['install','keyboard'])
        import keyboard
        print("Keyboard installed Sucessfully")
    except:
        KYBRD=False
        print("ERROR: Failed to install Keyboard !!!")
    time.sleep(3)

    
def clear():
    os.system('cls')

class display:
    def __init__(self,width,height,backdrop='.'):
        self.buffer=[backdrop]*width*height
        self.lastframe=[backdrop]*width*height
        self.backdrop=backdrop
        self.width=width
        self.lut=" `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
        #self.lut=" -*&#"

    
    def color(self,bright=0):
        index = int(len(self.lut)*bright/100.0)
        
        if index>len(self.lut)-1:
            index=len(self.lut)-1
        elif index<0:
            index=0
        
        return self.lut[index]

    def draw_point(self,pos,intensity=0):
        try:
            pos=int(pos[0]),int(pos[1])
            if pos[0]>=0 and pos[1]>=0:
                if pos[0]<=self.width and pos[1]<=len(self.buffer)/self.width:
                    if type(intensity)==int:
                        self.buffer[pos[0]+(pos[1]*self.width)] = self.color(intensity)
                    else:
                        self.buffer[pos[0]+(pos[1]*self.width)] = str(intensity[0])
        except:
            pass

    def draw_rect(self,pos,size,intensity=100):
        for x in range(size[0]):
            for y in range(size[1]):
                self.draw_point( (pos[0]+x , pos[1]+y) , intensity )

        
    def draw_text(self,pos,char=' '):
        pos=int(pos[0]),int(pos[1])
        if len(str(char))>1:
            for i,c in enumerate(str(char)):
                index= i + pos[0] + (pos[1]*self.width)
                if pos[0]+i < self.width:
                    self.buffer[index]=c
        else:
            self.buffer[pos[0]+(pos[1]*self.width)]=str(char)[0]


    def pressing(self,key):
        if KYBRD:
            return keyboard.is_pressed(str(key))    
        else:
            return False

    def update(self,pause=0.05):
        image=""
        diff=False
        for i,char in enumerate(self.buffer):
            if not(self.lastframe[i]==self.buffer[i]):
                self.lastframe[i]=self.buffer[i]
                diff=True
                
                
            self.buffer[i]=self.backdrop
            if i>0 and i%self.width==0:
                image+='\n'
            image+=char
            
        if diff:
            clear()
            print(image)
        
        time.sleep(pause)
        


