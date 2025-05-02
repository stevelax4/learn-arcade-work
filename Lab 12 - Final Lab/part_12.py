import arcade
import random

#High score = 36

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flappy Zombie"

GRAVITY = 1
JUMP_SPEED = 12
PIPE_SPEED = 3
PIPE_GAP = 200
PIPE_SPACING = 300

class Pipe(arcade.SpriteSolidColor):
    def __init__(self, width, height, x, y, is_top):
        super().__init__(width, height, arcade.color.GREEN)
        self.center_x = x
        self.center_y = y
        self.is_top = is_top
        self.passed = False

class FlappyZombie(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.player = None
        self.pipes = []
        self.score = 0
        self.coin_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.game_over = False

    def setup(self):
        self.player = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_jump.png", 0.5)
        self.player.center_x = 100
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.change_y = 0

        self.pipes.clear()
        self.score = 0
        self.game_over = False

        # Create initial pipes
        for i in range(3):
            self.create_pipe_pair(SCREEN_WIDTH + i * PIPE_SPACING)

    def create_pipe_pair(self, x):
        gap_y = random.randint(150, SCREEN_HEIGHT - 150)
        pipe_top = Pipe(80, SCREEN_HEIGHT - gap_y - PIPE_GAP // 2, x, SCREEN_HEIGHT - (SCREEN_HEIGHT - gap_y - PIPE_GAP // 2) // 2, is_top=True)
        pipe_bottom = Pipe(80, gap_y - PIPE_GAP // 2, x, (gap_y - PIPE_GAP // 2) // 2, is_top=False)
        self.pipes.append(pipe_top)
        self.pipes.append(pipe_bottom)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        for pipe in self.pipes:
            pipe.draw()

        arcade.draw_text(f"Score: {self.score}", 20, SCREEN_HEIGHT - 40, arcade.color.BLACK, 20)

        if self.game_over:
            arcade.draw_text("Game Over", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                             arcade.color.RED, 50, anchor_x="center", anchor_y="center")

    def on_update(self, delta_time):
        if self.game_over:
            return

        self.player.change_y -= GRAVITY
        self.player.center_y += self.player.change_y

        # Update pipes
        for pipe in self.pipes:
            pipe.center_x -= PIPE_SPEED

        # Check for collisions
        for pipe in self.pipes:
            if self.player.collides_with_sprite(pipe):
                self.game_over = True
                return

        # Check for passing pipes
        for i in range(0, len(self.pipes), 2):
            top_pipe = self.pipes[i]
            if not top_pipe.passed and top_pipe.center_x + top_pipe.width < self.player.center_x:
                top_pipe.passed = True
                self.score += 1
                arcade.play_sound(self.coin_sound)

        # Remove off-screen pipes and add new ones
        self.pipes = [pipe for pipe in self.pipes if pipe.center_x > -100]
        if len(self.pipes) < 6:
            last_pipe_x = max(pipe.center_x for pipe in self.pipes)
            self.create_pipe_pair(last_pipe_x + PIPE_SPACING)

        # Game over if player falls off the screen
        if self.player.center_y < 0 or self.player.center_y > SCREEN_HEIGHT:
            self.game_over = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and not self.game_over:
            self.player.change_y = JUMP_SPEED

        if key == arcade.key.R and self.game_over:
            self.setup()

def main():
    game = FlappyZombie()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()


