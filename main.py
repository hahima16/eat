import arcade


# Creates player
class Player(arcade.Sprite):
    #
    def __init__(self):
        #
        super().__init__("sprites/PlayerTemp.png", 1)
        self.center_x = 200
        self.center_y = 300


class Main(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        # Sprites
        self.player = Player()

        # Movement

        self.up_held = False
        self.down_held = False
        self.right_held = False
        self.left_held = False

        arcade.set_background_color(arcade.color.WINE)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        arcade.start_render()
        #  self.player_list.draw()

        self.player.draw()

    def on_update(self, delta_time: float):
        self.move_handler()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_held = True
            print("up true")
        elif key == arcade.key.DOWN:
            self.down_held = True
            print("down true")
        elif key == arcade.key.RIGHT:
            self.right_held = True
            print("right true")
        elif key == arcade.key.LEFT:
            self.left_held = True
            print("left true")

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_held = False
            print("up false")
        elif key == arcade.key.DOWN:
            self.down_held = False
            print("down false")
        elif key == arcade.key.RIGHT:
            self.right_held = False
            print("right false")
        elif key == arcade.key.LEFT:
            self.left_held = False
            print("left false")

    def move_handler(self):
        if self.up_held:
            self.player.center_y += 5
        if self.down_held:
            self.player.center_y -= 5
        if self.right_held:
            self.player.center_x += 5
        if self.left_held:
            self.player.center_x -= 5
        self.player.draw()
    

def main():
    window = Main(640,  480, "Game")
    window.setup()
    arcade.run()


main()
