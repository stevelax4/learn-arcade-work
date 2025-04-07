""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_ROCK = 0.7
COIN_COUNT = 50
ROCK_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Rock(arcade.Sprite):
    def update(self):
        self.center_x -= -1

        if self.left < 0:
            self.right = SCREEN_WIDTH

class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def on_update(self, delta_time: float = 1 / 60) -> None:

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.rock_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

        self.coin_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.rock_sound = arcade.load_sound(":resources:sounds/rockHit2.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_jump.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin(":resources:images/items/coinGold_ul.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(ROCK_COUNT):
            rock = Rock(":resources:images/space_shooter/meteorGrey_med2.png", SPRITE_SCALING_ROCK)

            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)

            self.rock_list.append(rock)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.rock_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.on_update(delta_time)
        self.rock_list.update()


        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list,
                                                        self.rock_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)

        for rock in hit_list:
            rock.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(self.rock_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
