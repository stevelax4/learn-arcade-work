import arcade
import random
import os

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flappy Zombie"

GRAVITY = 1
JUMP_SPEED = 12
PIPE_SPEED = 3
PIPE_GAP = 200
PIPE_SPACING = 300
PIPE_WIDTH = 80

HIGH_SCORE_FILE = "high_score.txt"

class Pipe:
    def __init__(self, width, height, x, y, is_top):
        self.width = width
        self.height = height
        self.center_x = x
        self.center_y = y
        self.is_top = is_top
        self.passed = False

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, arcade.color.GREEN)
        arcade.draw_rectangle_outline(self.center_x, self.center_y, self.width, self.height, arcade.color.DARK_GREEN, 4)
        shine_x = self.center_x - self.width // 4
        arcade.draw_rectangle_filled(shine_x, self.center_y, 5, self.height, arcade.color.WHITE_SMOKE)


def check_collision(sprite, pipe):
    left = pipe.center_x - pipe.width / 2
    right = pipe.center_x + pipe.width / 2
    bottom = pipe.center_y - pipe.height / 2
    top = pipe.center_y + pipe.height / 2

    return (
        sprite.center_x + sprite.width / 2 > left and
        sprite.center_x - sprite.width / 2 < right and
        sprite.center_y + sprite.height / 2 > bottom and
        sprite.center_y - sprite.height / 2 < top
    )


def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as f:
            try:
                return int(f.read())
            except ValueError:
                return 0
    return 0


def create_cloud(x):
    return {"x": x, "y": random.randint(400, SCREEN_HEIGHT - 50), "scale": random.uniform(0.8, 1.5)}


class FlappyZombie(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.player = None
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.new_high_score = False
        self.show_instructions = True
        self.high_score = load_high_score()

        self.clouds = []

        self.coin_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/hit1.wav")

        self.music = arcade.load_sound(":resources:music/funkyrobot.mp3")
        self.music_player = None

    def save_high_score(self):
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(self.high_score))

    def setup(self):
        self.player = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_jump.png", 0.5)
        self.player.center_x = 100
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.change_y = 0

        self.pipes.clear()
        self.score = 0
        self.game_over = False
        self.new_high_score = False
        self.show_instructions = True

        self.clouds = [create_cloud(random.randint(0, SCREEN_WIDTH)) for _ in range(5)]
        for i in range(3):
            self.create_pipe_pair(SCREEN_WIDTH + i * PIPE_SPACING)

        if self.music_player:
            self.music_player.stop()
        self.music_player = arcade.play_sound(self.music, looping=True)

    def create_pipe_pair(self, x):
        gap_y = random.randint(150, SCREEN_HEIGHT - 150)
        top_height = SCREEN_HEIGHT - gap_y - PIPE_GAP // 2
        bottom_height = gap_y - PIPE_GAP // 2

        pipe_top = Pipe(PIPE_WIDTH, top_height, x, SCREEN_HEIGHT - top_height // 2, is_top=True)
        pipe_bottom = Pipe(PIPE_WIDTH, bottom_height, x, bottom_height // 2, is_top=False)

        self.pipes.append(pipe_top)
        self.pipes.append(pipe_bottom)

    def draw_background(self):
        arcade.draw_ellipse_filled(200, 0, 600, 300, arcade.color.DARK_SPRING_GREEN)
        arcade.draw_ellipse_filled(600, 0, 700, 250, arcade.color.DARK_SPRING_GREEN)
        arcade.draw_triangle_filled(150, 0, 300, 300, 450, 0, arcade.color.GRAY)
        arcade.draw_triangle_filled(500, 0, 650, 350, 800, 0, arcade.color.LIGHT_GRAY)

        for cloud in self.clouds:
            x = cloud["x"]
            y = cloud["y"]
            scale = cloud["scale"]
            arcade.draw_circle_filled(x, y, 30 * scale, arcade.color.LIGHT_GRAY)
            arcade.draw_ellipse_filled(x + 25 * scale, y + 10 * scale, 60 * scale, 40 * scale, arcade.color.LIGHT_GRAY)
            arcade.draw_circle_filled(x + 50 * scale, y, 25 * scale, arcade.color.LIGHT_GRAY)

    def on_draw(self):
        arcade.start_render()
        self.draw_background()

        if self.show_instructions:
            arcade.draw_text("Welcome to Flappy Zombie!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                             arcade.color.BLACK, 24, anchor_x="center")
            arcade.draw_text("Press SPACE to Jump, Avoid the Pipes!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                             arcade.color.BLACK, 24, anchor_x="center")
            arcade.draw_text("Press SPACE to Start", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50,
                             arcade.color.DARK_BLUE, 20, anchor_x="center")
            return

        self.player.draw()

        for pipe in self.pipes:
            pipe.draw()

        arcade.draw_text(f"Score: {self.score}", 20, SCREEN_HEIGHT - 40, arcade.color.BLACK, 20)
        arcade.draw_text(f"High Score: {self.high_score}", 20, SCREEN_HEIGHT - 70, arcade.color.DARK_RED, 16)

        if self.game_over:
            arcade.draw_text("Game Over", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                             arcade.color.RED, 50, anchor_x="center", anchor_y="center")
            arcade.draw_text("Press R to Restart", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60,
                             arcade.color.BLACK, 20, anchor_x="center")
            if self.new_high_score:
                arcade.draw_text(f"New High Score: {self.score}!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 120,
                                 arcade.color.GOLD, 24, anchor_x="center")

    def on_update(self, delta_time):
        if self.game_over or self.show_instructions:
            return

        self.player.change_y -= GRAVITY
        self.player.center_y += self.player.change_y

        for pipe in self.pipes:
            pipe.center_x -= PIPE_SPEED

        for pipe in self.pipes:
            if check_collision(self.player, pipe):
                self.game_over = True
                arcade.play_sound(self.hit_sound)
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.new_high_score = True
                    self.save_high_score()
                return

        for i in range(0, len(self.pipes), 2):
            top_pipe = self.pipes[i]
            if not top_pipe.passed and top_pipe.center_x + PIPE_WIDTH < self.player.center_x:
                top_pipe.passed = True
                self.score += 1
                arcade.play_sound(self.coin_sound)

        self.pipes = [pipe for pipe in self.pipes if pipe.center_x > -100]
        if len(self.pipes) < 6:
            last_pipe_x = max(pipe.center_x for pipe in self.pipes)
            self.create_pipe_pair(last_pipe_x + PIPE_SPACING)

        if self.player.center_y < 0 or self.player.center_y > SCREEN_HEIGHT:
            self.game_over = True
            arcade.play_sound(self.hit_sound)
            if self.score > self.high_score:
                self.high_score = self.score
                self.new_high_score = True
                self.save_high_score()

        for cloud in self.clouds:
            cloud["x"] -= PIPE_SPEED * 0.3
            if cloud["x"] < -100:
                cloud.update(create_cloud(SCREEN_WIDTH + 100))

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            if self.show_instructions:
                self.show_instructions = False
                return
            if not self.game_over:
                self.player.change_y = JUMP_SPEED

        if key == arcade.key.R and self.game_over:
            self.setup()


def main():
    game = FlappyZombie()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
