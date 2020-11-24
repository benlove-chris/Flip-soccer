

import arcade
import os
from menu import *


file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)




SCREEN_WIDTH = 1260
SCREEN_HEIGHT = 650
SCREEN_TITLE = "GAME OVER"



class Vitoria1(arcade.View):
    
    def __init__(self):
        super().__init__()
        self.gameOverSong = arcade.load_sound("music/gameover_som.mp3")
        arcade.play_sound(self.gameOverSong)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,arcade.load_texture("img/vitoria1.jpg"))
        

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        arcade.stop_sound(self.gameOverSong)
        menu = MenuGame()
        self.window.show_view(menu)
        menu.setup()


class Vitoria2(arcade.View):
    
    def __init__(self):
        super().__init__()
        self.gameOverSong = arcade.load_sound("music/gameover_som.mp3")
        arcade.play_sound(self.gameOverSong)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,arcade.load_texture("img/vitoria2.jpg"))
        

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        arcade.stop_sound(self.gameOverSong)
        menu = MenuGame()
        self.window.show_view(menu)
        menu.setup()

    



