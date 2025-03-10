import arcade

#Open the window
arcade.open_window(400,400, "Grossman Tree")

#Set the background
arcade.set_background_color(arcade.color.SKY_BLUE)

#Get ready to draw
arcade.start_render()

#Draw the sun
arcade.draw_circle_filled(350, 350, 40, arcade.color.YELLOW)

#Draw the grass
arcade.draw_rectangle_filled(200, 50, 400, 100, arcade.color.GREEN)

#Draw the tree trunk
arcade.draw_rectangle_filled(100, 120, 20, 60, arcade.color.DARK_BROWN)

#Draw the leaves for the tree
arcade.draw_circle_filled(100, 160, 30, arcade.color.FOREST_GREEN)
arcade.draw_circle_filled(85, 145, 25, arcade.color.FOREST_GREEN)
arcade.draw_circle_filled(115, 145, 25, arcade.color.FOREST_GREEN)

#Draw the tree trunk 2
arcade.draw_rectangle_filled(200, 100, 20, 60, arcade.color.DARK_BROWN)

#Draw the leaves for the tree 2
arcade.draw_circle_filled(200, 140, 30, arcade.color.FOREST_GREEN)
arcade.draw_circle_filled(185, 125, 25, arcade.color.FOREST_GREEN)
arcade.draw_circle_filled(215, 125, 25, arcade.color.FOREST_GREEN)

#Draw clouds
arcade.draw_circle_filled(20, 300, 20, arcade.color.WHITE)
arcade.draw_circle_filled(30, 300, 25, arcade.color.WHITE)
arcade.draw_circle_filled(40, 320, 25, arcade.color.WHITE)
arcade.draw_circle_filled(50, 300, 25, arcade.color.WHITE)
arcade.draw_circle_filled(70, 300, 25, arcade.color.WHITE)

arcade.draw_circle_filled(200, 310, 25, arcade.color.WHITE)
arcade.draw_circle_filled(230, 310, 30, arcade.color.WHITE)
arcade.draw_circle_filled(240, 330, 30, arcade.color.WHITE)
arcade.draw_circle_filled(250, 310, 30, arcade.color.WHITE)
arcade.draw_circle_filled(270, 310, 20, arcade.color.WHITE)

#Draw pond
arcade.draw_circle_filled(350, 30, 70, arcade.color.BLUE)
arcade.draw_circle_filled(300, 30, 60, arcade.color.BLUE)
arcade.draw_circle_filled(270, 10, 60, arcade.color.BLUE)

#Draw fish
arcade.draw_circle_filled(325, 30, 5, arcade.color.ORANGE)
arcade.draw_rectangle_filled(320,30, 6, 6, arcade.color.ORANGE)

arcade.draw_circle_filled(320, 10, 5, arcade.color.ORANGE)
arcade.draw_rectangle_filled(315,10, 6, 6, arcade.color.ORANGE)

arcade.draw_circle_filled(335, 40, 5, arcade.color.ORANGE)
arcade.draw_rectangle_filled(330,40, 6, 6, arcade.color.ORANGE)

# --- Finish Drawing ---
arcade.finish_render()

#Keep the window open until it is closed
arcade.run()