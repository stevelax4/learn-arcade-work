import arcade

# Constants
ROW_COUNT = 10
COLUMN_COUNT = 10
WIDTH = 20
HEIGHT = 20
MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

# Create the grid
grid = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

def on_draw():
    arcade.start_render()

    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            color = arcade.color.WHITE
            if grid[row][column] == 1:
                color = arcade.color.GREEN
            x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
            y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
            arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

def on_mouse_press(x, y, button, modifiers):
    column = x // (WIDTH + MARGIN)
    row = y // (HEIGHT + MARGIN)

    if row < 0 or row >= ROW_COUNT or column < 0 or column >= COLUMN_COUNT:
        return

    # Function to toggle a cell safely
    def toggle_cell(r, c):
        if 0 <= r < ROW_COUNT and 0 <= c < COLUMN_COUNT:
            grid[r][c] = 1 if grid[r][c] == 0 else 0

    # Toggle clicked cell and its neighbors
    toggle_cell(row, column)
    toggle_cell(row - 1, column)  # up
    toggle_cell(row + 1, column)  # down
    toggle_cell(row, column - 1)  # left
    toggle_cell(row, column + 1)  # right

    # Count total selected
    total_selected = sum(cell for row in grid for cell in row)
    print(f"Total of {total_selected} cells are selected.")

    # Count per row
    for r in range(ROW_COUNT):
        row_count = sum(grid[r])
        print(f"Row {r} has {row_count} cells selected.")

    # Count per column
    for c in range(COLUMN_COUNT):
        col_count = sum(grid[r][c] for r in range(ROW_COUNT))
        print(f"Column {c} has {col_count} cells selected.")

    # Continuous selected blocks in rows
    for r in range(ROW_COUNT):
        continuous_count = 0
        for c in range(COLUMN_COUNT):
            if grid[r][c] == 1:
                continuous_count += 1
            else:
                if continuous_count > 2:
                    print(f"There are {continuous_count} continuous blocks selected on row {r}.")
                continuous_count = 0
        # Edge case: row ends in a continuous block
        if continuous_count > 2:
            print(f"There are {continuous_count} continuous blocks selected on row {r}.")

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Array Backed Grid Lab")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.start_render()

    arcade.schedule(lambda delta_time: on_draw(), 1/60)
    arcade.window_commands.get_window().on_mouse_press = on_mouse_press
    arcade.run()

if __name__ == "__main__":
    main()
