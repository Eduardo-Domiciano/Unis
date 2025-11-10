import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from area_resp import AreaDeResultado
from kivy.uix.button import Button
from kivy.core.window import Window

kivy.require('1.9.0')

'''
    Testando algumas configurações de resolução dinamica
'''
import platform
current_OS = platform.system()

def linux_resolution():
    import subprocess 
    try:
        windowResolution = subprocess.check_output("xrandr | grep '*'", shell=True).decode()
        monitorLinux = windowResolution.split()[0]
        largura, altura = monitorLinux.split("x")
        linux_largura = int(largura)
        linux_altura = int(altura)
        Window.size = (linux_largura * 0.3, linux_altura * 0.5)
        Window.left = linux_largura / 4
        Window.top = linux_altura / 6
        print(f"Sistema: {current_OS}, Resolução: {linux_largura} x {linux_altura}")
    except Exception as e:
        print(f"Erro ao obter resolução Linux: {e}. Usando padrão.")
        standard_resolution()

def windows_resolution():
    import tkinter as tk 
    try:
        tk_window = tk.Tk()
        windows_largura = tk_window.winfo_screenwidth()
        windows_altura = tk_window.winfo_screenheight()
        tk_window.destroy()
        Window.size = (windows_largura * 0.3, windows_altura * 0.5)
        Window.left = windows_largura // 4
        Window.top = windows_altura // 6
        print(f"Sistema: {current_OS}, Resolução: {windows_largura} x {windows_altura}")
    except Exception as e:
        print(f"Erro ao obter resolução Windows: {e}. Usando padrão.")
        standard_resolution()
    

def standard_resolution():
    Window.size = (800, 600)
    try:
        Window.left = (Window.system_size[0] - Window.size[0]) // 2
        Window.top  = (Window.system_size[1] - Window.size[1]) // 2
    except:
        pass 
    print(f"Sistema: {current_OS} não encontrado. Usando 800x600.")

match current_OS:
    case "Linux":
        linux_resolution()
    case "Windows":
        windows_resolution()
    case _:
        standard_resolution()



class mainWindow(BoxLayout):
    
    def __init__(self, **kwargs):
        super(mainWindow, self).__init__(**kwargs)
        self.orientation = "vertical" 
        self.spacing = 20

        '''
            Sessao 1 ======================== Nome endereço======================================================
        '''
        primeiraSessao = GridLayout(
            size_hint_y=0.2,
            cols=2,
            padding=10,
            spacing=10,
            row_default_height=35,
            row_force_default=True
        )
        self.add_widget(primeiraSessao)
        
        # Form nome
        primeiraSessao.add_widget(
            Label(text="Nome do paciente: ", size_hint_x=0.3, halign='left', valign='middle')
        )
        self.inputForm01 = TextInput(
            text='', 
            multiline=False,
            size_hint_x=0.7
        )
        primeiraSessao.add_widget(self.inputForm01)


        #Form  endereço
        primeiraSessao.add_widget(
            Label(text="Endereço completo: ", size_hint_x=0.3, halign='left', valign='middle')
        )
        
        self.inputForm02 = TextInput(
            text='', 
            multiline=False,
            size_hint_x=0.7
        )
        primeiraSessao.add_widget(self.inputForm02)




        '''
            Sessao 2 ==========================  Altura Peso e resultado ===========================
        '''
        segundaSessao = BoxLayout(
            size_hint=(1, 0.65), 
            orientation='horizontal',
            padding=[10, 5, 10, 5],
            spacing=15
        )
        self.add_widget(segundaSessao)

        # Area esquerda para form de Altura e peso
        areaInput_segundaSessao = GridLayout(
            size_hint_x=0.4,
            cols=2,
            padding=5,
            spacing=10,
            row_default_height=35,
            row_force_default=True
        )
        segundaSessao.add_widget(areaInput_segundaSessao)

                
        # Altura
        areaInput_segundaSessao.add_widget(
            Label(text="Altura (cm): ", size_hint_x=0.5, halign='left', valign='middle')
        )
        
        self.inputForm03 = TextInput( 
            multiline=False,
            size_hint_x=0.5,
            input_filter='float' 
        )
        areaInput_segundaSessao.add_widget(self.inputForm03)
        
        # Peso
        areaInput_segundaSessao.add_widget(
            Label(text="Peso (Kg): ", size_hint_x=0.5, halign='left', valign='middle')
        )
        
        self.inputForm04 = TextInput(
            multiline=False,
            size_hint_x=0.5,
            input_filter='float'
        )
        areaInput_segundaSessao.add_widget(self.inputForm04)
        
        # Controlador de espaço pra ajustar os elementos
    
        areaInput_segundaSessao.add_widget(Label(size_hint_y=None, height=1)) 
        areaInput_segundaSessao.add_widget(Label())


        # Area Direita para Resultados (Resultado da AreaDeResultado) ====================================
        areaResultado_segundaSessao = BoxLayout(
            size_hint_x=0.6,
        )
        segundaSessao.add_widget(areaResultado_segundaSessao)
        self.resultado_area = AreaDeResultado(text="Area de Resultados do calculo IMC.")
        areaResultado_segundaSessao.add_widget(self.resultado_area)

        '''
            Sessao 3 ==========================  Botoes ===========================
        '''
        terceiraSessao = BoxLayout(
            size_hint=(1, 0.15),
            orientation='horizontal',
            padding=[20, 10, 20, 10], 
            spacing=10 
        )
        self.add_widget(terceiraSessao)


        # 1. Espaçador Esquerdo de controle de posição de elementos
        terceiraSessao.add_widget(Label())
        terceiraSessao.add_widget(Label()) 
        terceiraSessao.add_widget(Label()) 

        # 2. Botão Calcular
        self.button_calc = Button(
            text='Calcular',
            size_hint=(None, None), 
            size=(100, 40)
        )
        terceiraSessao.add_widget(self.button_calc)
        # ligação com o metodo de calculo
        self.button_calc.bind(on_release=self.calcular_imc)

        # 4. Botão Restart
        self.button_restart = Button(
            text='Restart',
            size_hint=(None, None), 
            size=(100, 40)
        )
        terceiraSessao.add_widget(self.button_restart)
        self.button_restart.bind(on_release=self.resetar_campos)

        # 5. Espaçador Central 2 
        terceiraSessao.add_widget(Label()) 
        terceiraSessao.add_widget(Label())

        # 6. Botão Sair
        self.Button_exit = Button(
            text='Sair',
            size_hint=(None, None), 
            size=(100, 40)
        )
        terceiraSessao.add_widget(self.Button_exit)
        self.Button_exit.bind(on_release=App.get_running_app().stop) 

    

    '''
        Metodo de calculo
    '''

    def calcular_imc(self, instance):
        
        nome = self.inputForm01.text.strip()
        endereco = self.inputForm02.text.strip()      
        
        try:
            altura_cm = float(self.inputForm03.text.replace(',', '.'))
            peso_kg = float(self.inputForm04.text.replace(',', '.'))
        except ValueError:
            self.resultado_area.text = "ERRO: Por favor, insira valores numéricos válidos (apenas números, use ponto ou vírgula) para Altura e Peso."
            return

        if not nome:
            self.resultado_area.text = "ERRO: O campo 'Nome do paciente' é obrigatório para realizar o cálculo."
            return

        # valores pos
        if altura_cm <= 0 or peso_kg <= 0:
            self.resultado_area.text = "ERRO: Altura e Peso devem ser valores positivos maiores que zero."
            return

        # Modelo de calc e classificacao
        altura_m = altura_cm / 100.0 
        imc = peso_kg / (altura_m ** 2)
        if imc < 18.5:
            classificacao = "Abaixo do peso"
            cor = "Amarelo (Risco)"
        elif 18.5 <= imc <= 24.9:
            classificacao = "Peso normal"
            cor = "Verde (Saudável)"
        elif 25.0 <= imc <= 29.9:
            classificacao = "Sobrepeso"
            cor = "Laranja (Moderado)"
        elif 30.0 <= imc <= 34.9:
            classificacao = "Obesidade Grau I"
            cor = "Vermelho (Alto)"
        elif 35.0 <= imc <= 39.9:
            classificacao = "Obesidade Grau II (Severa)"
            cor = "Vermelho Escuro (Muito Alto)"
        else: # imc >= 40.0
            classificacao = "Obesidade Grau III (Mórbida)"
            cor = "Roxo (Máximo)"
            
        # Saida
        resultado_str = (
            "--- RESULTADO DO CÁLCULO IMC ---\n"
            f"Paciente: {nome if nome else '[Nome Não Informado]'}\n"
            f"Endereço: {endereco if endereco else '[Endereço Não Informado]'}\n"
            "\n"
            f"IMC: {imc:.2f}\n"
            f"Situação: {classificacao}\n"
            f"Nível de Risco: {cor}\n"
            "--------------------------------\n"
        )
        
        self.resultado_area.text = resultado_str

    def resetar_campos(self, instance):
        self.inputForm01.text = ''
        self.inputForm02.text = ''
        self.inputForm03.text = '0' 
        self.inputForm04.text = '0'
        self.resultado_area.text = "Campos limpos. Insira Altura e Peso para um novo cálculo."


class MinhaApp(App):
    
    title = 'Calculo do IMC - Indice de Massa Corporal'
    
    def build(self):
        return mainWindow()

if __name__ == '__main__':
    App.run(MinhaApp())