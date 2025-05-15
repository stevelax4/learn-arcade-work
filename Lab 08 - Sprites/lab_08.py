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
        self.center_x -= 1
        if self.right < 0:
            self.left = SCREEN_WIDTH


class Coin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.change_x = 0
        self.change_y = 0

    def on_update(self, delta_time: float = 1 / 60) -> None:
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.coin_list = None
        self.rock_list = None
        self.game_over = False

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

        self.coin_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.rock_sound = arcade.load_sound(":resources:sounds/rockHit2.wav")

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        self.score = 0
        self.game_over = False

        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/zombie/zombie_jump.png", SPRITE_SCALING_PLAYER
        )
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for _ in range(COIN_COUNT):
            coin = Coin(":resources:images/items/coinGold_ul.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randint(-3, 3)
            coin.change_y = random.randint(-3, 3)
            self.coin_list.append(coin)

        for _ in range(ROCK_COUNT):
            rock = Rock(":resources:images/space_shooter/meteorGrey_med2.png", SPRITE_SCALING_ROCK)
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)
            self.rock_list.append(rock)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.rock_list.draw()
        self.player_list.draw()

        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 20, arcade.color.WHITE, 14)

        if self.game_over:
            arcade.draw_text(
                "GAME OVER!",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                arcade.color.RED,
                50,
                anchor_x="center",
                anchor_y="center"
            )

    def on_mouse_motion(self, x, y, dx, dy):
        if not self.game_over:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def on_update(self, delta_time):
        if self.game_over:
            return  # Stop updating when game over

        self.coin_list.on_update(delta_time)
        self.rock_list.update()

        # Handle coin collisions
        coins_hit = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)

        # Handle rock collisions
        rocks_hit = arcade.check_for_collision_with_list(self.player_sprite, self.rock_list)
        for rock in rocks_hit:
            rock.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(self.rock_sound)

        # End game when all coins are collected
        if len(self.coin_list) == 0:
            self.game_over = True
            print("Game Over! Final Score:", self.score)


def main():
    game = MyGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
