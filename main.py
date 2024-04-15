
import arcade

# Creates player


class Player(arcade.Sprite):
    # Creates a player
    def __init__(self):
        super().__init__("sprites/PlayerTemp.png", 1)  # Image path
        self.center_x = 200  # x-location
        self.center_y = 300  # y-location


# Projectile class
class Projectile(arcade.Sprite):
    def __init__(self, start_x, start_y, target_x, target_y):
        super().__init__("sprites/Bullet.png", 1)
        self.center_x = start_x
        self.center_y = start_y
        self.target_x = target_x
        self.target_y = target_y

    def move_to_target(self):

        pass


class Main(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)
        self.player = Player()
        self.projectile_list = arcade.SpriteList()  # List to hold projectiles

        self.up_held = False
        self.down_held = False
        self.right_held = False
        self.left_held = False

        self.camera = arcade.Camera(self.width, self.height)
        arcade.set_background_color(arcade.color.WINE)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.camera.use()
        self.player.draw()
        self.projectile_list.draw()  # Draw all projectiles

    def on_key_press(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.W):
            self.up_held = True
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.down_held = True
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.right_held = True
        elif key in (arcade.key.LEFT, arcade.key.A):  # Fixed condition
            self.left_held = True

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.W):
            self.up_held = False
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.down_held = False
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.right_held = False
        elif key in (arcade.key.LEFT, arcade.key.A):  # Fixed condition
            self.left_held = False

    def move_handler(self):
        if self.up_held:
            self.player.center_y += 5
        if self.down_held:
            self.player.center_y -= 5
        if self.right_held:
            self.player.center_x += 5
        if self.left_held:
            self.player.center_x -= 5

    def camera_handler(self):
        p_x = self.player.center_x
        p_y = self.player.center_y

        # Calculate the 1/3rd thresholds of the screen
        x_threshold = self.width / 3
        y_threshold = self.height / 3

        # Calculate the center of the screen/camera view
        screen_center_x = self.camera.position[0] + self.width / 2
        screen_center_y = self.camera.position[1] + self.height / 2

        # Determine if the player has moved beyond the 1/3rd thresholds
        move_camera_x = p_x < screen_center_x - x_threshold or p_x > screen_center_x + x_threshold
        move_camera_y = p_y < screen_center_y - y_threshold or p_y > screen_center_y + y_threshold

        # Only move the camera if the player has moved beyond the threshold
        if move_camera_x or move_camera_y:
            target_camera_x = p_x - self.width / 2
            target_camera_y = p_y - self.height / 2
            self.camera.move_to((target_camera_x, target_camera_y), 0.025)  # Smoothness parameter can be adjusted

    def on_update(self, delta_time: float):
        self.camera_handler()
        self.move_handler()
        print(self.camera.position)
        print(self.player.position)
        for projectile in self.projectile_list:
            projectile.move_to_target()  # Uwwwwwpdate each projectile's position

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        projectile = Projectile(self.player.center_x, self.player.center_y, x, y)
def main():
    window = Main(640,  480, "Game")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
