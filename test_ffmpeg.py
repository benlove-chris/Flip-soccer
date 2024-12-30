import arcade

try:
    sound = arcade.load_sound(":resources:sounds/coin1.wav")
    print("Som carregado com sucesso!")
except Exception as e:
    print("Erro ao carregar som:", e)
