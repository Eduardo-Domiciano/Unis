import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

kivy.require('1.9.0')
'''
    Configurações de resolução da Janela
'''
# Detecta o sistema operacional em que o scipt esta sendo rodado
import platform
current_OS = platform.system()
from kivy.core.window import Window
# Descobre a resolução do monitor no Linux OS para definir o tamanho da janela e a posição
def linux_resolution():
    # Tamanho da janela Linux
    import subprocess 
    windowResolution = subprocess.check_output("xrandr | grep '*'", shell=True).decode()
    monitorLinux = windowResolution.split()[0]
    largura, altura = monitorLinux.split("x")
    linux_largura = int(largura)
    linux_altura = int(altura)
    Window.size = (linux_largura * 0.3, linux_altura * 0.5)
    # Posição da Janela
    Window.left = linux_largura / 4
    Window.top = linux_altura / 6
    print(f"Sistema: {current_OS}, Resolução: {linux_largura} x {linux_altura}")

# Descobre a resolução do monitor no Windows OS, para definir o tamanho da janela e a posição
def windows_resolution():
    #Tamanho da tela Windows
    import tkinter as tk 
    tk_window = tk.Tk()
    windows_largura = tk_window.winfo_screenwidth()
    windows_altura = tk_window.winfo_screenheight()
    tk_window.destroy()
    Window.size = (windows_largura * 0.3, windows_altura * 0.5)
    # Posição da Janela
    Window.left = windows_largura // 4
    Window.top = windows_altura // 6
    print(f"Sistema: {current_OS}, Resolução: {windows_largura} x {windows_altura}")
    

def standard_resolution():
    Window.size = (800, 600)
    Window.left = (Window.system_size[0] - Window.size[0]) // 2
    Window.top  = (Window.system_size[1] - Window.size[1]) // 2
    print(f"Sistema: {current_OS} nao encontrado")

match current_OS:
    case "Linux":
        linux_resolution()
    case "Windows":
        windows_resolution()
    case "":
        standard_resolution()

class mainWindow(BoxLayout):
    """
    Janela principal é um boxlayout
    """
    def __init__(self, **kwargs):
        super(mainWindow, self).__init__(**kwargs)
        self.orientation = "vertical" 

        """
            Conteudo da primeira Sessao
        """
        primeiraSessao = BoxLayout(
            size_hint=(1, 0.1), # 100% Largura, 20% Altura
            orientation='vertical' 
        )
        self.add_widget(primeiraSessao)

        #=================================================Sessao 01 Formulário 01
        formularioUm_primeiraSessao = BoxLayout(
            size_hint=(0.8, 0.1), # 100% Largura, 20% Altura
            orientation='horizontal',
            padding=13 
        )
        primeiraSessao.add_widget(formularioUm_primeiraSessao)
        #1 Label ===== Formulário01
        LabelForm01 = Label(text="Nome do paciente: ",size_hint=(0.2, 1), halign='center',valign='middle')
        formularioUm_primeiraSessao.add_widget(LabelForm01)
        #1 input ======= Formulario01
        inputForm01 = TextInput(
            text='Digite aqui...', 
            multiline=False,
            size_hint_x=0.8,
            size_hint_y=1
        )
        formularioUm_primeiraSessao.add_widget(inputForm01)

        #====================================================Sessao 01 Formulário 02
        formularioDois_primeiraSessao = BoxLayout(
            size_hint=(0.8, 0.1),
            orientation='horizontal' ,
            padding=13
        )
        primeiraSessao.add_widget(formularioDois_primeiraSessao)
        #1 Label ===== Formulário02
        LabelForm02 = Label(text="Endereço completo: ",size_hint=(0.2, 1), halign='center',valign='middle')
        formularioDois_primeiraSessao.add_widget(LabelForm02)
        #1 input ======= Formulario02
        inputForm02 = TextInput(
            text='Digite aqui...', 
            multiline=False,
            size_hint_x=0.8,
            size_hint_y=1
        )
        formularioDois_primeiraSessao.add_widget(inputForm02)




        """
            Conteudo da Segunda Sessao
        """
        segundaSessao = BoxLayout(
            size_hint=(1, 0.2), # 100% Largura, 20% Altura
            orientation='horizontal' 
        )
        segundaSessao.add_widget(Label(text="Área Superior (20%)"))
        self.add_widget(segundaSessao)


        """
            Conteudo da Terceira Sessao
        """
        terceiraSessao = BoxLayout(
            size_hint=(1, 0.2), # 100% Largura, 20% Altura
            orientation='horizontal' 
        )
        terceiraSessao.add_widget(Label(text="Área Superior (20%)"))
        self.add_widget(terceiraSessao)

        # 1. Adiciona um Label
        label_info2 = Label(
            text="Digite seu nome:", 
            size_hint=(1, 0.2)  # Ocupa 20% da altura do layout
        )
        terceiraSessao.add_widget(label_info2)
        
        # 2. Adiciona um TextInput (campo de entrada)
        input_nome = TextInput(
            text='Seu nome aqui', 
            multiline=False,     # Apenas uma linha
            size_hint=(1, 0.3)   # Ocupa 30% da altura do layout
        )
        terceiraSessao.add_widget(input_nome)
        
        # Você pode adicionar mais elementos, por exemplo, um Label
        # que exibe o texto atual do TextInput
        label_exibicao = Label(
            text="Texto digitado aparecerá aqui.",
            size_hint=(1, 0.5) # Ocupa os 50% restantes
        )
        terceiraSessao.add_widget(label_exibicao)
        
        # Opcional: Liga um evento para atualizar o Label de exibição
        #terceiraSessao.input_nome.bind(text=ao_mudar_texto)

    def ao_mudar_texto(self, instance, value):
        """
        Função chamada toda vez que o texto do TextInput muda.
        """
        terceiraSessao.label_exibicao.text = f"Você digitou: {value}"
        
        


class MinhaApp(App):
    """
    Classe principal da aplicação Kivy.
    """
    def build(self):
        # Retorna a nossa classe de interface como o widget raiz.
        return mainWindow()

if __name__ == '__main__':
    MinhaApp().run()