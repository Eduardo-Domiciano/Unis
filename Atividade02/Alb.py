from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from dias_anos import converter_dias_para_idade
from MenorDe3 import encontrar_menor_de_tres
from kivy.uix.scrollview import ScrollView
from primo import eh_primo
from inverte_palavras import inverter_letras_por_palavra
from kivy.uix.textinput import TextInput 
from kivy.core.window import Window
from triangulo import processar_triangulo

# Tamano da janela
import subprocess 
windowResolution = subprocess.check_output("xrandr | grep '*'", shell=True).decode()
monitorLinux = windowResolution.split()[0]
largura, altura = monitorLinux.split("x")
linux_largura = int(largura)
linux_altura = int(altura)
Window.size = (linux_largura * 0.3, linux_altura * 0.5)
# Posição 
Window.left = linux_largura / 4
Window.top = linux_altura / 6
print(f"Resolução: {linux_largura} x {linux_altura}")

class ConteudoTelaBase(BoxLayout):
    """
    Essa é a janela princpal
    """
    def __init__(self, tela_nome: str, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        
        # Rótulo de Identificação
        self.add_widget(Label(
            text=f"Esse Script é: {tela_nome.replace('_', ' ').title()}",
            font_size=28,
            size_hint_y=0.10
        ))
        
        self.content_placeholder = BoxLayout(orientation='vertical', spacing=10)
        self.add_widget(self.content_placeholder) # Adiciona o placeholder ao layout

        # Botao pra voltar no menu principal
        btn_voltar = Button(
            text="Voltar pro menu <==",
            size_hint_y=0.10
        )
        btn_voltar.bind(on_release=self.voltar_ao_menu)
        self.add_widget(btn_voltar)

    def voltar_ao_menu(self, instance):
        """callback para o botão Voltar."""
        App.get_running_app().root.current = 'menu_principal'


# 1. Definição das Telas Placeholder
# Estas telas são simples, apenas contêm o layout base.

class Tela1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # O layout principal desta tela
        layout = ConteudoTelaBase(tela_nome="Conversor de Idade")
        
        # Layout para os widgets de entrada/saída (fica acima do botão Voltar)
        self.conversion_area = BoxLayout(orientation='vertical', spacing=10, size_hint_y=0.8)
        
        # Campo de Entrada
        self.input_dias = TextInput(
            hint_text="Digite a idade em dias", 
            input_type='number', 
            multiline=False,
            size_hint_y=None,
            height=40
        )
        self.conversion_area.add_widget(self.input_dias)
        
        # Botão de Conversão
        btn_converter = Button(text="Calcular Idade", size_hint_y=None, height=50)
        btn_converter.bind(on_release=self.realizar_conversao)
        self.conversion_area.add_widget(btn_converter)
        
        # Sessao resultado
        self.resultado_label = Label(
            text="Resposta aqui", 
            font_size=16,
            halign='center'
        )
        self.conversion_area.add_widget(self.resultado_label)
        
        layout.add_widget(self.conversion_area, index=1) # index=1 faz ficar em cima
        
        self.add_widget(layout)




    def realizar_conversao(self, instance):
        dias_str = self.input_dias.text
        
        
        try:
            dias = int(dias_str)
            # Esse é o modulo que importado
            anos, meses, dias_finais = converter_dias_para_idade(dias)

            mensagemFinal = (
                f"Geração Minecraft!" if anos < 20 else""
                f"Geração da corrida Naruto!" if anos > 20 and anos <30 else""
                f"Assistil TV Colosso com certeza!" if anos > 30 and anos < 40 else""
                f"Ja se veste de Papai Noel no Natal" if anos > 40 else""
            )
            # Atualiza a informação pra resposta
            self.resultado_label.text = (
                f"Idade de {dias} dias:\n"
                f"{anos} anos, {meses} meses e {dias_finais} dias.\n"
                f"{mensagemFinal}"
                
            )
            self.resultado_label.color = (0, 0.5, 0, 1)    
        except ValueError as e:
            # Caso o valor inserido nao seja numero ou valor negatvo
            self.resultado_label.text = f"Erro: {e}"
            self.resultado_label.color = (1, 0, 0, 1) 
        except Exception:
           # Campo vazio
            self.resultado_label.text = "Erro: Digite um número válido."
            self.resultado_label.color = (1, 0, 0, 1) # Errro sai em vermelho


#####################################################################

class Tela2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = ConteudoTelaBase(tela_nome="Verifica Triângulo")
        # layout dos campos de entrada
        input_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
        
        # campos de Entrada
        self.input_a = TextInput(hint_text="Lado A", input_type='number', multiline=False)
        self.input_b = TextInput(hint_text="Lado B", input_type='number', multiline=False)
        self.input_c = TextInput(hint_text="Lado C", input_type='number', multiline=False)
        input_layout.add_widget(self.input_a)
        input_layout.add_widget(self.input_b)
        input_layout.add_widget(self.input_c)
        # Botao
        btn_verificar = Button(text="Verificar e Calcular Área", size_hint_y=None, height=50)
        btn_verificar.bind(on_release=self.realizar_verificacao)
        


        # Resultado
        self.resultado_label = Label(
            text="Digite 3 lados para verificar.", 
            font_size=16,
            halign='center',
            text_size=(Window.size[0] - 10, None)
        )
        
        # adiciona os widgets na tela
        layout.content_placeholder.add_widget(input_layout)
        layout.content_placeholder.add_widget(btn_verificar)
        layout.content_placeholder.add_widget(self.resultado_label)
        
        self.add_widget(layout)


    def realizar_verificacao(self, instance):
        # Função chama o modulo
        try:
            # converte pra inteiro
            a = int(self.input_a.text)
            b = int(self.input_b.text)
            c = int(self.input_c.text)
            resultado = processar_triangulo(a, b, c)
            
            # Condicional do resultado
            if isinstance(resultado, float):
                self.resultado_label.text = (
                    f"Esses valores formam um triangulo!\n"
                    # unidades quadradas eu peguei de IA, nao sei como definir o resultado final do calculo
                    f"area Calculada: {resultado:.2f} unidades quadradas."
                )
                self.resultado_label.color = (0, 0.5, 0, 1)
                
            elif isinstance(resultado, tuple):
                self.resultado_label.text = (
                    f"Falhou! Os valores {resultado[0]}, {resultado[1]}, {resultado[2]} \n"
                    f"Não formam triângulo algum."
                )
                self.resultado_label.color = (1, 0.5, 0, 1) # Laranja/Atenção
            
            elif isinstance(resultado, str):
                # pega os erros dos valores
                self.resultado_label.text = f"ERRO: {resultado}"
                self.resultado_label.color = (1, 0, 0, 1)

        except ValueError:
            # Se os valores inseridos nao derem certos
            self.resultado_label.text = "ERRO: Tem que ser numeros inteiros."
            self.resultado_label.color = (1, 0, 0, 1) # Erro sempre em vermelho
        except Exception as e:
            self.resultado_label.text = f"ERRO INESPERADO: {type(e).__name__}"
            self.resultado_label.color = (1, 0, 0, 1)

#################################################################################

class Tela3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = ConteudoTelaBase(tela_nome="Menor de 3")
        
        # Layout dos inputs
        input_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
        self.input_n1 = TextInput(hint_text="Número 1", input_type='text', multiline=False)
        self.input_n2 = TextInput(hint_text="Número 2", input_type='text', multiline=False)
        self.input_n3 = TextInput(hint_text="Número 3", input_type='text', multiline=False)
        input_layout.add_widget(self.input_n1)
        input_layout.add_widget(self.input_n2)
        input_layout.add_widget(self.input_n3)
        
        # Botao
        btn_verificar = Button(text="Encontrar Menor", size_hint_y=None, height=50)
        btn_verificar.bind(on_release=self.encontrar_menor)
        
        # Resultado
        self.resultado_label = Label(
            text="Digite 3 números para encontrar o menor.", 
            font_size=18,
            halign='center',
            text_size=(Window.size[0] - 20, None)
        )
        
        # Adiciona os widgets ao placeholder da ConteudoTelaBase
        layout.content_placeholder.add_widget(input_layout)
        layout.content_placeholder.add_widget(btn_verificar)
        layout.content_placeholder.add_widget(self.resultado_label)
        
        self.add_widget(layout)


    def encontrar_menor(self, instance):
        """
        Método que obtém os inputs e chama a função para encontrar o menor.
        """
        try:
            # Tenta converter os inputs para float, para lidar com inteiros ou decimais
            n1 = float(self.input_n1.text)
            n2 = float(self.input_n2.text)
            n3 = float(self.input_n3.text)
            
            # --- CHAMA O MÓDULO IMPORTADO AQUI ---
            menor_numero = encontrar_menor_de_tres(n1, n2, n3)
            
            # Atualiza a interface
            self.resultado_label.text = (
                f"Numeros digitados: {n1}, {n2}, {n3}\n"
                f"O menor: {menor_numero}"
            )
            self.resultado_label.color = (0, 0.5, 0, 1) # Verde para sucesso

        except ValueError:
            # Erro se a entrada não for um número (vazio, texto, etc.)
            self.resultado_label.text = "ERRO: Todos os campos devem ser preenchidos com números válidos."
            self.resultado_label.color = (1, 0, 0, 1) # Vermelho
        except Exception as e:
            self.resultado_label.text = f"ERRO INESPERADO: {type(e).__name__}"
            self.resultado_label.color = (1, 0, 0, 1)

##########################################################################

class Tela4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = ConteudoTelaBase(tela_nome="Verificar Número Primo") 
        # inpuit de entrada
        self.input_num = TextInput(
            hint_text="Digite um número inteiro positivo", 
            input_type='number', # tipo do input
            multiline=False,
            size_hint_y=None, 
            height=40
        )
        # Botã
        btn_verificar = Button(
            text="Verificar se é Primo", 
            size_hint_y=None, 
            height=50
        )
        btn_verificar.bind(on_release=self.verificar_primo_callback)
        

        # Rótulo de Resultado
        self.resultado_label = Label(
            text="Resultado.", 
            font_size=18,
            halign='center',
            text_size=(Window.size[0] - 20, None)
        )
        layout.content_placeholder.add_widget(self.input_num)
        layout.content_placeholder.add_widget(btn_verificar)
        layout.content_placeholder.add_widget(self.resultado_label)
        
        self.add_widget(layout)



    def verificar_primo_callback(self, instance):
        try:
            # converte valor pra inteiro
            num_str = self.input_num.text.strip()
            if not num_str:
                raise ValueError("Insira o numero!")


            n = int(num_str)


            # ve se é positivo
            if n <= 0:
                raise ValueError("O numero tem que ser inteiro e positivo")
            resultado_bool = eh_primo(n)
            if resultado_bool:
                resultado_texto = f"Numero {n} é PRIMO!\n(Resultado: VERDADEIRO \o/)"
                cor = (0, 0.5, 0, 1) # Positivo é sempre verde
            else:
                resultado_texto = f"Numero {n} NÃO é primo.\n(Resultado: FALSO xD)"
                cor = (0.7, 0, 0, 1) # Erro sempre em verm  
            self.resultado_label.text = resultado_texto
            self.resultado_label.color = cor

        except ValueError as e:
            # Se der erro
            self.resultado_label.text = f"ERRO: Só aceita numeros inteiros positivos. {str(e).strip('.')}"
            self.resultado_label.color = (1, 0, 0, 1) 
        except Exception as e:
            self.resultado_label.text = f"ERRO INESPERADO: {type(e).__name__}"
            self.resultado_label.color = (1, 0, 0, 1)

###########################################################################


class Tela5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = ConteudoTelaBase(tela_nome="Invertedor de palavras")
        
        # input grande
        self.input_frase = TextInput(
            hint_text="insira a frase que será invertida.", 
            multiline=True,
            size_hint_y=None, 
            height=100
        )
        
        # Botao
        btn_inverter = Button(
            text="Inverter", 
            size_hint_y=None, 
            height=50
        )
        btn_inverter.bind(on_release=self.inverter_frase)
        
        
        self.resultado_label = Label(
            text="A frase invertida aqui", 
            font_size=16,
            halign='center', 
            valign='top',
            text_size=(Window.size[0] - 20, None)
        )
        layout.content_placeholder.add_widget(self.input_frase)
        layout.content_placeholder.add_widget(btn_inverter)
        layout.content_placeholder.add_widget(self.resultado_label)
        
        self.add_widget(layout)


    def inverter_frase(self, instance):

        frase_original = self.input_frase.text.strip()
        try:
            if not frase_original:
                raise ValueError("Ta vazio! Cade a frase???.")
                
            frase_invertida = inverter_letras_por_palavra(frase_original)
            
            # Resposta
            self.resultado_label.text = (
                f"Frase inserida:\n{frase_original}\n"
                f"\nResultado Invertido:\n{frase_invertida}"
            )
            self.resultado_label.color = (0, 0.5, 0, 1)

        except ValueError as e:
            self.resultado_label.text = f"ERRO: {e}"
            self.resultado_label.color = (1, 0, 0, 1)
        except Exception as e:
            self.resultado_label.text = f"ERRO INESPERADO: {type(e).__name__}"
            self.resultado_label.color = (1, 0, 0, 1)

###########################################################################

#Tela Principal Menu
class MenuPrincipal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        layout.add_widget(Label(
            text='''
            Atividade 02
            Escolha um dos Scripts
            ''',
            font_size=32,
            size_hint_y=0.3
        ))
        
        botoes_layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Lista de Scripts
        destinos = [('1. Dias/Anos', 'tela_1'), 
                    ('2. Triangulo', 'tela_2'), 
                    ('3. Menor de 3', 'tela_3'), 
                    ('4. Nº Primo', 'tela_4'), 
                    ('5. Inverter Frase', 'tela_5')]
        
        # Cria os botao
        for texto_botao, nome_tela in destinos:
            btn = Button(text=texto_botao)
            
            # Vaipra tela certa
            btn.bind(on_release=lambda instance, tela=nome_tela: self.mudar_tela(tela))
            
            botoes_layout.add_widget(btn)
        
        layout.add_widget(botoes_layout)
        self.add_widget(layout)

    def mudar_tela(self, nome_tela):
        # muda de tela
        App.get_running_app().root.current = nome_tela


# Aplicativo aqui
class GerenciadorJanelasPuroApp(App):
    
    def build(self):
        # cria Telas
        sm = ScreenManager()

        # adiciona as Telas  defini o nome
        sm.add_widget(MenuPrincipal(name='menu_principal'))
        sm.add_widget(Tela1(name='tela_1'))
        sm.add_widget(Tela2(name='tela_2'))
        sm.add_widget(Tela3(name='tela_3'))
        sm.add_widget(Tela4(name='tela_4'))
        sm.add_widget(Tela5(name='tela_5'))
        
        return sm

if __name__ == '__main__':
    GerenciadorJanelasPuroApp().run()