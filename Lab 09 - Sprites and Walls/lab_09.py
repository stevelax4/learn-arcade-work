""" Sprite Sample Program """

import arcade
import random


# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5

COIN_COUNT = 50

class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Sprite lists
        self.physics_engine = None
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None

        self.coin_sound = arcade.load_sound(":resources:sounds/coin5.wav")

        self.score = 0

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

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
        wall.center_y = 244
        self.wall_list.append(wall)

        # Manually create and position a box at 364, 200
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 328
        wall.center_y = 180
        self.wall_list.append(wall)

        # Manually create and position a box at 364, 200
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 136
        wall.center_y = 244
        self.wall_list.append(wall)


        # --- Place boxes inside a loop
        for x in range(200, 799, 64):
            for i in range(1):
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
                wall.center_x = x
                wall.center_y = i * 64 + 364
                self.wall_list.append(wall)

        for x in range(200, 630, 64):
            for i in range(1):
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
                wall.center_x = x
                wall.center_y = i * 64 + 308
                self.wall_list.append(wall)

        for x in range(1, 720, 64):
            for i in range(1):
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
                wall.center_x = x
                wall.center_y = i * 64 + 125
                self.wall_list.append(wall)

        for x in range(1, 799, 64):
            for i in range(1):
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
                wall.center_x = x
                wall.center_y = i * 64 + -8
                self.wall_list.append(wall)

        for x in range(1, 720, 64):
            for i in range(1):
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
                wall.center_x = x
                wall.center_y = i * 64 + 627
                self.wall_list.append(wall)




        # --- Place walls with a list
        coordinate_list = [[400, 500],
                           [464, 500],
                           [400, 564],
                           [464, 564],
                           [458, 180],
                           [394, 180],
                           [586, 244],
                           [705, 180],
                           [705, 244],
                           [-3, 244],
                           [-3, 180],
                           [-3, 308],
                           [-3, 372],
                           [-3, 436],
                           [-3, 500],
                           [-3, 564],
                           [60, 365],
                           [125, 500],
                           [189, 500],
                           [189, 436],
                           [253, 500],
                           [253, 436],
                           [585, 500],
                           [585, 436],
                           [699, 500],
                           [699, 564],
                           [820, 64],
                           [820, 120],
                           [820, 185],
                           [820, 249],
                           [820, 313],
                           [820, 377],
                           [820, 441],
                           [820, 505],
                           [820, 569],
                           [820, 633],
                           [820, 697],
                           [820, 761],
                           [820, 825]]



        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        while len(self.coin_list) < COIN_COUNT:
            coin = arcade.Sprite(":resources:images/items/coinGold_ul.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
            if len(hit_list) == 0:
                self.coin_list.append(coin)


    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.wall_list.draw()
        self.coin_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def update(self, delta_time, hit_list=None):
        self.physics_engine.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list,)

        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)

            self.coin_list.on_update(delta_time)

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