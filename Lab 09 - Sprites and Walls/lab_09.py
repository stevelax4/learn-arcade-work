""" Sprite Sample Program """

import arcade

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Create the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_jump.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # --- Manually place walls

        # Manually create and position a box at 300, 200
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 200
        wall.center_y = 172
        self.wall_list.append(wall)

        # Manually create and position a box at 364, 200
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 328
        wall.center_y = 172
        self.wall_list.append(wall)

        # --- Place boxes inside a loop
        for x in range(200, 778, 64):
            for i in range(2):
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
                wall.center_x = x
                wall.center_y = i * 64 + 300
                self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[400, 500],
                           [464, 500],
                           [400, 564],
                           [464, 564]]


        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)


    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.wall_list.draw()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()