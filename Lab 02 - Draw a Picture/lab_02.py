import arcade


# Function to draw the sun at a given position
def draw_sun(x, y):
    arcade.draw_circle_filled(x, y, 40, arcade.color.YELLOW)


# Function to draw the grass at a given position
def draw_grass(x, y):
    arcade.draw_rectangle_filled(x, y, 400, 100, arcade.color.GREEN)


# Function to draw a tree trunk at a given position
def draw_tree_trunk(x, y):
    arcade.draw_rectangle_filled(x, y, 20, 60, arcade.color.DARK_BROWN)


# Function to draw the leaves of the tree at a given position
def draw_tree_leaves(x, y):
    arcade.draw_circle_filled(x, y, 30, arcade.color.FOREST_GREEN)
    arcade.draw_circle_filled(x - 15, y - 15, 25, arcade.color.FOREST_GREEN)
    arcade.draw_circle_filled(x + 15, y - 15, 25, arcade.color.FOREST_GREEN)


# Function to draw a second tree trunk at a given position
def draw_tree_trunk2(x, y):
    arcade.draw_rectangle_filled(x, y, 20, 60, arcade.color.DARK_BROWN)


# Function to draw the leaves of the second tree at a given position
def draw_tree_leaves2(x, y):
    arcade.draw_circle_filled(x, y, 30, arcade.color.FOREST_GREEN)
    arcade.draw_circle_filled(x - 15, y - 15, 25, arcade.color.FOREST_GREEN)
    arcade.draw_circle_filled(x + 15, y - 15, 25, arcade.color.FOREST_GREEN)


# Function to draw clouds at a given position
def draw_clouds(x, y):
    arcade.draw_circle_filled(x, y, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 10, y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 20, y + 20, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 30, y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 50, y, 25, arcade.color.WHITE)


# Function to draw the pond at a given position
def draw_pond(x, y):
    arcade.draw_circle_filled(x, y, 70, arcade.color.BLUE)
    arcade.draw_circle_filled(x - 50, y, 60, arcade.color.BLUE)
    arcade.draw_circle_filled(x - 80, y - 20, 60, arcade.color.BLUE)


# Function to draw fish at a given position
def draw_fish(x, y):
    arcade.draw_circle_filled(x + 5, y, 5, arcade.color.ORANGE)
    arcade.draw_rectangle_filled(x, y, 6, 6, arcade.color.ORANGE)


# --- Main Function to Call All Drawings ---
def main():
    # Open the window
    arcade.open_window(400, 400, "Grossman Tree")

    # Set the background color
    arcade.set_background_color(arcade.color.SKY_BLUE)

    # Start drawing
    arcade.start_render()

    # Draw each element in the scene
    draw_sun(350, 350)  # Draw the sun at (350, 350)
    draw_grass(200, 50)  # Draw the grass at (200, 50)

    # Draw trees
    draw_tree_trunk(100, 120)  # Draw first tree trunk at (100, 120)
    draw_tree_leaves(100, 160)  # Draw first tree leaves at (100, 160)

    draw_tree_trunk2(200, 100)  # Draw second tree trunk at (200, 100)
    draw_tree_leaves2(200, 140)  # Draw second tree leaves at (200, 140)

    # Draw clouds in different locations
    draw_clouds(20, 300)  # First cloud cluster at (20, 300)
    draw_clouds(200, 310)  # Second cloud cluster at (200, 310)

    # Draw pond at (350, 30)
    draw_pond(350, 30)

    # Draw fish in the pond at different positions
    draw_fish(325, 30)  # Fish 1
    draw_fish(320, 10)  # Fish 2
    draw_fish(335, 40)  # Fish 3

    # Finish drawing
    arcade.finish_render()

    # Keep the window open until it is closed
    arcade.run()


# Call the main function
if __name__ == "__main__":
    main()
