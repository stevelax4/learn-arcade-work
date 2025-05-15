import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



class Kite:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5  # Speed at which the kite moves
        self.keys_pressed = set()  # Set of keys that are currently pressed

    def draw(self):
        arcade.draw_triangle_filled(self.x - 15, self.y + 10, self.x + 15, self.y + 10, self.x, self.y + 20,
                                    arcade.color.RED)
        arcade.draw_triangle_filled(self.x - 15, self.y + 10, self.x + 15, self.y + 10, self.x, self.y - 20,
                                    arcade.color.FOREST_GREEN)
        arcade.draw_triangle_filled(self.x - 15, self.y + 10, self.x + 15, self.y + 10, self.x, self.y - 5,
                                    arcade.color.ORANGE)

    def update(self):
        if arcade.key.UP in self.keys_pressed:
            self.y += self.speed
        if arcade.key.DOWN in self.keys_pressed:
            self.y -= self.speed
        if arcade.key.LEFT in self.keys_pressed:
            self.x -= self.speed
        if arcade.key.RIGHT in self.keys_pressed:
            self.x += self.speed

        # Keep the kite within the screen boundaries
        self.x = max(20, min(self.x, SCREEN_WIDTH - 20))
        self.y = max(20, min(self.y, SCREEN_HEIGHT - 20))


class Balloon:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20

    def draw(self):
        # Draw the balloon body
        arcade.draw_circle_filled(self.x, self.y, self.radius, arcade.color.PINK)
        # Draw the balloon knot
        arcade.draw_triangle_filled(self.x - 5, self.y - self.radius, self.x + 5, self.y - self.radius, self.x,
                                    self.y - self.radius - 10, arcade.color.DARK_PINK)
        # Draw the string
        arcade.draw_line(self.x, self.y - self.radius - 10, self.x, self.y - self.radius - 40, arcade.color.DARK_BROWN,
                         2)

    def update_position(self, x, y):
        # Update position to follow the mouse, constrained inside the screen
        self.x = max(self.radius, min(x, SCREEN_WIDTH - self.radius))
        self.y = max(self.radius, min(y, SCREEN_HEIGHT - self.radius))


# --- Functions to Draw Objects ---

def draw_sun(x, y):
    arcade.draw_circle_filled(x, y, 40, arcade.color.YELLOW)


def draw_grass(x, y):
    arcade.draw_rectangle_filled(x, y, 800, 100, arcade.color.GREEN)


def draw_tree_trunk(x, y):
    arcade.draw_rectangle_filled(x, y, 20, 60, arcade.color.DARK_BROWN)


def draw_tree_leaves(x, y):
    arcade.draw_circle_filled(x, y, 30, arcade.color.FOREST_GREEN)
    arcade.draw_circle_filled(x - 15, y - 15, 25, arcade.color.FOREST_GREEN)
    arcade.draw_circle_filled(x + 15, y - 15, 25, arcade.color.FOREST_GREEN)


def draw_clouds(x, y):
    arcade.draw_circle_filled(x, y, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 10, y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 20, y + 20, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 30, y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 50, y, 25, arcade.color.WHITE)


def draw_pond(x, y):
    arcade.draw_circle_filled(x, y, 70, arcade.color.BLUE)
    arcade.draw_circle_filled(x - 50, y, 60, arcade.color.BLUE)
    arcade.draw_circle_filled(x - 80, y - 20, 60, arcade.color.BLUE)


def draw_fish(x, y):
    arcade.draw_circle_filled(x + 5, y, 5, arcade.color.ORANGE)
    arcade.draw_rectangle_filled(x, y, 6, 6, arcade.color.ORANGE)



class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Create kite controlled by keyboard
        self.kite = Kite(400, 300)  # Start in the middle of the screen

        # Create balloon controlled by mouse
        self.balloon = Balloon(600, 300)

        # Load a simple sound effect to play on mouse click
        self.pop_sound = arcade.load_sound(":resources:sounds/hit3.wav")

    def on_draw(self):
        arcade.start_render()

        # Draw the background and scene elements
        draw_sun(350, 350)  # Sun
        draw_grass(400, 50)  # Grass
        draw_tree_trunk(100, 120)  # First tree trunk
        draw_tree_leaves(100, 160)  # First tree leaves
        draw_tree_trunk(200, 100)  # Second tree trunk
        draw_tree_leaves(200, 140)  # Second tree leaves
        draw_tree_trunk(450, 100)  # third tree trunk
        draw_tree_leaves(450, 140)  # third tree leaves
        draw_tree_trunk(600, 80)  # fourth tree trunk
        draw_tree_leaves(600, 120)  # fourth tree leaves
        draw_clouds(20, 300)  # Cloud 1
        draw_clouds(400, 250)  # Cloud 2
        draw_clouds(600, 400)  # Cloud 3
        draw_clouds(20, 300)  # Cloud 4
        draw_clouds(200, 310)  # Cloud 5
        draw_pond(350, 30)  # Pond
        draw_fish(325, 30)  # Fish 1
        draw_fish(320, 10)  # Fish 2
        draw_fish(335, 40)  # Fish 3

        # Draw the kite
        self.kite.draw()

        # Draw the balloon
        self.balloon.draw()

    def on_update(self, delta_time):
        self.kite.update()

    def on_key_press(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN, arcade.key.LEFT, arcade.key.RIGHT]:
            self.kite.keys_pressed.add(key)

    def on_key_release(self, key, modifiers):
        if key in self.kite.keys_pressed:
            self.kite.keys_pressed.remove(key)

    def on_mouse_motion(self, x, y, dx, dy):
        self.balloon.update_position(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        # Play pop sound when mouse clicked
        arcade.play_sound(self.pop_sound)


def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
