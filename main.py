import arcade


# Creates player
class Player(arcade.Sprite):
    # Creates a player
    def __init__(self):
        super().__init__("sprites/PlayerTemp.png", 1)  # Image path
        self.center_x = 200  # x-location
        self.center_y = 300  # y-location


class Main(arcade.Window):
    # Setup for game
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        # Sprites
        self.player = Player()  # Calls player

        # Movement Booleans

        self.up_held = False
        self.down_held = False
        self.right_held = False
        self.left_held = False

        # Camera
        self.camera = None
        self.camera = arcade.Camera(self.width, self.height)
        self.camera.use()

        arcade.set_background_color(arcade.color.WINE)

    # Setup required for python arcade; i don't know what it does
    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        arcade.start_render()
        #  self.player_list.draw()

        self.player.draw()

    # Movement, key pressed
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_held = True
            print("up true")
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_held = True
            print("down true")
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_held = True
            print("right true")
        elif key == arcade.key.LEFT or arcade.key.A:
            self.left_held = True
            print("left true")

    # Movement, key released
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_held = False
            print("up false")
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_held = False
            print("down false")
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_held = False
            print("right false")
        elif key == arcade.key.LEFT or arcade.key.A:
            self.left_held = False
            print("left false")

    # Movement handler, moves player by 5 when respective keypress boolean is True
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

    def camera_handler(self):
        screen_center_x = self.player.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player.center_y - (self.camera.viewport_height / 2)

        if screen_center_x < 0:
            screen_center_x = 0
        elif screen_center_x > self.player.center_x:
            screen_center_x = self.player.center_x
        if screen_center_y < 0:
            screen_center_y = 0
        elif screen_center_y > self.player.center_y:
            screen_center_y = self.player.center_y

        player_centered = screen_center_x, screen_center_y
        self.camera.move_to(player_centered)

    # Calls functions every time screen updates
    def on_update(self, delta_time: float):
        self.camera_handler()
        self.move_handler()


# Main function
def main():
    window = Main(640,  480, "Game")
    window.setup()
    arcade.run()


main()
