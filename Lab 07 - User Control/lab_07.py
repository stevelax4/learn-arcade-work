import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# --- Classes ---

class Kite:

    def __init__(self, x, y):
        """ Constructor. """
        self.x = x
        self.y = y
        self.speed = 5  # Speed at which the kite moves
        self.keys_pressed = set()  # Set of keys that are currently pressed

    def draw(self):
        """ Draw the kite. """
        arcade.draw_triangle_filled(self.x - 15, self.y + 10, self.x + 15, self.y + 10, self.x, self.y + 20, arcade.color.RED)
        arcade.draw_triangle_filled(self.x - 15, self.y + 10, self.x + 15, self.y + 10, self.x, self.y - 20, arcade.color.FOREST_GREEN)
        arcade.draw_triangle_filled(self.x - 15, self.y + 10, self.x + 15, self.y + 10, self.x, self.y - 5, arcade.color.ORANGE)

    def update(self):
        """ Update kite position based on keyboard input. """
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


# --- Main Game Class ---

class MyGame(arcade.Window):
    """ Our Custom Window Class """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Create kite
        self.kite = Kite(400, 300)  # Start in the middle of the screen

    def on_draw(self):
        """ Called whenever we need to draw the window. """
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

    def on_update(self, delta_time):
        """ Called to update our objects. """
        self.kite.update()

    def on_key_press(self, key, modifiers):
        """ Called when a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.DOWN or key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.kite.keys_pressed.add(key)

    def on_key_release(self, key, modifiers):
        """ Called when a key is released. """
        if key in self.kite.keys_pressed:
            self.kite.keys_pressed.remove(key)


# --- Main Function to Run the Game ---
def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
