from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle, Line
from kivy.properties import StringProperty


class AreaDeResultado(TextInput):
    
    # cor de fundo
    BACKGROUND_COLOR = (0.9, 1, 0.9, 1)
    
    # borda
    BORDER_COLOR = (0, 0, 0, 1)
    
    def __init__(self, **kwargs):
        super(AreaDeResultado, self).__init__(**kwargs)
        
        self.multiline = True
        self.readonly = True 
        self.text = "Resultado do teste IMC"
        
        #
        self.background_color = [1, 1, 1, 0]
        
        # Desenha as bordas
        self.bind(pos=self.desenhar_elementos, size=self.desenhar_elementos)
        self.desenhar_elementos()

    def desenhar_elementos(self, *args):
       
        with self.canvas.before: 
            self.canvas.before.clear()
            
            # background
            Color(*self.BACKGROUND_COLOR) 
            Rectangle(pos=self.pos, size=self.size) 
            
            # bord
            Color(*self.BORDER_COLOR)  
            Line(
                rectangle=(self.x, self.y, self.width, self.height), 
                width=1.5 # espessura da borda
            )
            
    def adicionar_log(self, mensagem):
        self.text += f"\n[INFO] {mensagem}"

