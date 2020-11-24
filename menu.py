
import arcade
import random
import os
from game import *

SCREEN_WIDTH = 1260
SCREEN_HEIGHT = 650
SCREEN_TITLE = "FLIP SOCCER"


class TextButton:
    """ Text-based button """

    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text,
                 font_size=18,
                 font_face="Arial",
                 face_color=arcade.color.TAUPE_GRAY,
                 highlight_color=arcade.color.BABY_BLUE_EYES,
                 shadow_color=arcade.color.BABY_BLUE,
                 button_height=10):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
        
        """ Desenha o botão"""
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False


def check_mouse_press_for_buttons(x, y, button_list):
    """ verifica se precisamos registrar algum clique de botão."""
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(_x, _y, button_list):
    """verifica se precisamos processar
        quaisquer eventos de lançamento. """
    for button in button_list:
        if button.pressed:
            button.on_release()


class BotaoParaIniciar(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 300, 80, "Jogar", 50, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class BotaoParaSair(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 200, 80, "Sair", 50, "Times")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        quit()


class MenuGame(arcade.View):
    """
    Menu do jogo
    """

    def __init__(self):
        
        super().__init__()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
       


        self.parar = False
        
        self.lista_de_botoes = None
        self.som_menu = arcade.load_sound("music/menu_som.mp3")
        arcade.play_sound(self.som_menu)
        

    def setup(self):
        """
        Configurações, criar botões
        """
    
        self.lista_de_botoes = []

        botao_jogar = BotaoParaIniciar(SCREEN_WIDTH/2, SCREEN_HEIGHT/2+10, self.iniciar_jogo)  
        
        self.lista_de_botoes.append(botao_jogar)

        botao_sair = BotaoParaSair(SCREEN_WIDTH/2, SCREEN_HEIGHT/2-130, self.parar_jogo)
        self.lista_de_botoes.append(botao_sair)

    def on_draw(self):
        """
        Desenha a tela
        """

        arcade.start_render()
        

     
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,arcade.load_texture("img/plano.jpg"))

        # Dessenha os botões
        for button in self.lista_de_botoes:
            button.draw()

    

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Chamado quando o usuário pressiona um botão do mouse.
        """
        check_mouse_press_for_buttons(x, y, self.lista_de_botoes)
        

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Chamado quando o usuário libera um botão do mouse.
        """
        check_mouse_release_for_buttons(x, y, self.lista_de_botoes)

    def parar_jogo(self):
        
        self.parar = True

    def iniciar_jogo(self):
        arcade.stop_sound(self.som_menu)
        jogo = GameView()
        self.window.show_view(jogo)
        jogo.setup()
        


def main():
    """ Main method """
    
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu = MenuGame()
    window.show_view(menu)
    menu.setup()
    arcade.run()


if __name__ == "__main__":
    main()