import arcade


class Ramez(arcade.Sprite):
    def __init__(self):
        super().__init__("sprites/Ramez.png", 1)
        self.center_x = 200
        self.center_y = 300


class Main(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        # Sprites
        self.player = Ramez()

        arcade.set_background_color(arcade.color.WINE)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        arcade.start_render()
        #  self.player_list.draw()

        self.player.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.center_y += 5


def main():
    window = Main(640,  480, "Game")
    window.setup()
    arcade.run()

main()
