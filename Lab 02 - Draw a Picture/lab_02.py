import arcade
arcade.open_window(400,400, "Grossman Tree")
arcade.set_background_color(arcade.color.SKY_BLUE)
arcade.start_render()

arcade.draw_circle_filled(350, 350, 40, arcade.color.YELLOW)

arcade.draw_rectangle_filled(200, 50, 400, 100, arcade.color.GREEN)

arcade.draw_rectangle_filled(100, 120, 20, 60, arcade.color.DARK_BROWN)

arcade.draw_circle_filled(100, 160, 30, arcade.color.FOREST_GREEN)
arcade.draw_circle_filled(85, 145, 25, arcade.color.FOREST_GREEN)
arcade.draw_circle_filled(115, 145, 25, arcade.color.FOREST_GREEN)

arcade.finish_render()

arcade.run()



