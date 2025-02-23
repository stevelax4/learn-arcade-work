import arcade


def draw_road():
    arcade.draw_lrtb_rectangle_filled(0, 400, 150, 100, arcade.color.DARK_GRAY)
    for i in range(0, 400, 40):
        arcade.draw_lrtb_rectangle_filled(i + 10, i + 30, 127, 123, arcade.color.WHITE)


def draw_bus():
    arcade.draw_rectangle_filled(200, 200, 150, 80, arcade.color.YELLOW)

    # Windows
    for i in range(3):
        arcade.draw_rectangle_filled(160 + i * 40, 230, 30, 40, arcade.color.LIGHT_BLUE)

    # Stop Sign
    arcade.draw_rectangle_filled(275, 200, 20, 20, arcade.color.RED)
    arcade.draw_text("STOP", 267, 193, arcade.color.WHITE, 8, bold=True)

    # Wheels
    for x in [140, 260]:
        arcade.draw_circle_filled(x, 170, 15, arcade.color.BLACK)
        arcade.draw_circle_filled(x, 170, 7, arcade.color.GRAY)


def draw_tree():
    # Trunk
    arcade.draw_rectangle_filled(70, 180, 20, 60, arcade.color.BROWN)

    # Leaves
    arcade.draw_circle_filled(70, 220, 40, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(50, 200, 30, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(90, 200, 30, arcade.color.DARK_GREEN)


def draw_sun():
    arcade.draw_circle_filled(350, 350, 40, arcade.color.YELLOW)


def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, 400, 100, 0, arcade.color.GREEN)


def on_draw():
    arcade.start_render()
    draw_grass()
    draw_road()
    draw_bus()
    draw_tree()
    draw_sun()


def main():
    arcade.open_window(400, 400, "Road, Bus, Tree")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.schedule(lambda dt: on_draw(), 1 / 60)
    arcade.run()


main()