import arcade
import os
from gameover import *

SCREEN_WIDTH = 1260
SCREEN_HEIGHT = 650
SCREEN_TITLE = "FLIP SOCCER"

#BOLA
TAMANHO_BOLA = 0.035
GRAVIDADE_BOLA = 0.3
BOUNCE = 0.9

#JOGADOR 
VELOCIDADE_JOGADOR = 9
SALTO_JOGADOR = 14
GRAVIDADE_JOGADOR = 0.6


class GameView(arcade.View):
    def __init__(self):
        
        super().__init__()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.bola_list = None
        self.player_list = None
        self.gramado_list = None
        
        self.linha_gol1_list = None
        self.linha_gol2_list = None

        self.physics_engine2 = None
        self.physics_engine1 = None


        self.background = None
        

        self.gramado = None
        self.player1_sprite = None
        self.player2_sprite = None

        self.tentando = None

        self.score1 = None
        self.score2 =  None
        
        self.score_text = None


        self.apito_gol = arcade.load_sound("music/apito.mp3")
        self.som_chute = arcade.load_sound("music/chute.ogg")
        self.som_fundo = arcade.load_sound("music/fundo.mp3")
        arcade.play_sound(self.som_fundo)
        
        
        
        
        




        
    def setup(self):
        self.score1 = 0 
        self.score2 = 0


        self.bola_list = arcade.SpriteList()

        self.linha_gol1_list = arcade.SpriteList()
        self.linha_gol2_list = arcade.SpriteList()

        self.player_list = arcade.SpriteList()

        
        self.gramado_list = arcade.SpriteList()

        


        self.background = arcade.load_texture("img/fundo.png")
        self.grama = arcade.load_texture("img/grama.png")

        

        
        self.linha_gol1 = arcade.Sprite("img/linha_gol.png", 0.7)
        self.linha_gol2 = arcade.Sprite("img/linha_gol.png", 0.8)

        """Para segurar o jogador sobre a grama
        """
        #gramado = arcade.Sprite("img/grama.png", 500)
        for i in range(32, SCREEN_WIDTH-32, 64):
            gramado = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.5)
            gramado.bottom = 0  
            gramado.left = i
            self.gramado_list.append(gramado) 
        


        """Para segurar o jogador nos dois lados
        """
        for y in range(96, SCREEN_HEIGHT, 30):
            # Left
            gramado = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.2)
            gramado.center_x = 175
            gramado.center_y = y
            self.gramado_list.append(gramado)

            # Right
            gramado = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.2)
            gramado.center_x = SCREEN_WIDTH - 175
            gramado.center_y = y 
            self.gramado_list.append(gramado)





        self.player1_sprite = arcade.Sprite("img/jogador1.png", 0.35)
        self.player2_sprite = arcade.Sprite("img/jogador2.png", 0.35)

        

        bola = arcade.Sprite("img/bola1.png", TAMANHO_BOLA)
        


        self.player1_sprite.center_x = 240
        self.player1_sprite.center_y = 120

        


        self.player2_sprite.center_x = 1000
        self.player2_sprite.center_y = 120

    
        

        """posição linha2"""
        self.linha_gol1.center_x = 165
        self.linha_gol1.center_y = 160

        """posição linha2"""
        self.linha_gol2.center_x = 1130
        self.linha_gol2.center_y = 160


         


    
        """posição inicial ca bola"""
        bola.center_x = SCREEN_WIDTH/2+15
        bola.center_y =  450
        

        self.player_list.append(self.player1_sprite)
        self.player_list.append(self.player2_sprite)
        
        self.bola_list.append(bola)
       
        

        self.linha_gol1_list.append(self.linha_gol1)
        self.linha_gol2_list.append(self.linha_gol2)
        

        self.physics_engine1 = arcade.PhysicsEnginePlatformer(self.player1_sprite,self.gramado_list,gravity_constant=GRAVIDADE_JOGADOR)
        self.physics_engine2 = arcade.PhysicsEnginePlatformer(self.player2_sprite,self.gramado_list,gravity_constant=GRAVIDADE_JOGADOR)
        
        

        
    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,self.background)
        
        
        self.player_list.draw()
        self.bola_list.draw()
        
        arcade.draw_text(f"{self.score1}",500, 420, arcade.color.GRAY_BLUE, 80, font_name='comic.ttf')  
        arcade.draw_text(f"{self.score2}",680, 420, arcade.color.GRAY_BLUE, 80, font_name='comic.ttf')
        
        
    



    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        #controle 1
        if key == arcade.key.W:
            if self.physics_engine1.can_jump():
                self.player1_sprite.change_y = SALTO_JOGADOR
        
        elif key == arcade.key.A:
            self.player1_sprite.change_x = -VELOCIDADE_JOGADOR

        elif key == arcade.key.D:
            self.player1_sprite.change_x = VELOCIDADE_JOGADOR
        
        #controle 2
        elif key == arcade.key.UP:
            if self.physics_engine2.can_jump():
                self.player2_sprite.change_y = SALTO_JOGADOR
        elif key == arcade.key.LEFT:
            self.player2_sprite.change_x = -VELOCIDADE_JOGADOR

        elif key == arcade.key.RIGHT:
            self.player2_sprite.change_x = VELOCIDADE_JOGADOR
        



    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        #controle 1
        if key == arcade.key.A or key == arcade.key.D:
            self.player1_sprite.change_x = 0

        #controle 2
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player2_sprite.change_x = 0

        

    
    def on_update(self,delta_time):
        
        self.physics_engine1.update()
        self.physics_engine2.update()

        

        for bola in self.bola_list:
            

            bola.center_x += bola.change_x
            bola.center_y += bola.change_y
            bola.change_y -= GRAVIDADE_BOLA




            """Colisão com o personagem - chute"""
            colission = arcade.check_for_collision_with_list(bola, (self.player_list))
            for coll in colission:
                arcade.play_sound(self.som_chute)
                if coll == self.player1_sprite:
                    
                    bola.change_x = 10
                    bola.change_y = -8
                else:
                    bola.change_x = -10
                    bola.change_y = -8
                    #bola.change_y *= -1
            
                
                    
            """Limite da bola """
            if bola.center_x-180 < TAMANHO_BOLA and bola.change_x < 0:
                bola.change_x *= -BOUNCE
            elif bola.center_x > (SCREEN_WIDTH-150) - TAMANHO_BOLA and bola.change_x > 0:
                bola.change_x *= -BOUNCE

            if bola.center_y-90 < TAMANHO_BOLA and bola. change_y < 0:     
                if bola.change_y * -1 > GRAVIDADE_BOLA * 10:
                    bola.change_y *= -BOUNCE
                else:
                    bola.change_y *= -BOUNCE / 70

        
        
        #verifica se há gols
     
        check_goal_scored1 = arcade.check_for_collision_with_list(self.linha_gol2,self.bola_list) 
        
        for gol in check_goal_scored1:
            #verifica gol do jogador 1
            arcade.play_sound(self.apito_gol)

            bola.center_x = SCREEN_WIDTH/2+15
            bola.center_y = 300
            bola.change_x = 0
            

            self.player1_sprite.center_x = SCREEN_WIDTH/2-200
            self.player2_sprite.center_x = SCREEN_WIDTH/2+200
            self.score1 += 1
        

        check_goal_scored2 = arcade.check_for_collision_with_list(self.linha_gol1, self.bola_list)
        for gol in check_goal_scored2:
            #verifica gol do jogador 2
            arcade.play_sound(self.apito_gol)
            
            bola.center_x = SCREEN_WIDTH/2+15
            bola.center_y = 300
            bola.change_x = 0
            
            self.player1_sprite.center_x = SCREEN_WIDTH/2-200
            self.player2_sprite.center_x = SCREEN_WIDTH/2+200
            self.score2 += 1
        
        #Game over - vencedor
        
        if self.score1 == 5:
            arcade.stop_sound(self.som_fundo)
            game_over_view = Vitoria1()
            
            self.window.set_mouse_visible(True)
            self.window.show_view(game_over_view)
            
        elif self.score2 == 5:
            arcade.stop_sound(self.som_fundo)
            game_over_view = Vitoria2()
            
            self.window.set_mouse_visible(True)
            self.window.show_view(game_over_view)
            
        
        


def main():
    

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu = GameView()
    window.show_view(menu)
    menu.setup()
    arcade.run()

if __name__ == "__main__":
    main()
