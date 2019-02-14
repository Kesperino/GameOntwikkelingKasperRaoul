import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

def draw_background():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT * (1 / 8), arcade.color.SKY_BLUE)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 8, 0, arcade.color.DARK_SPRING_GREEN)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Platform Game")
    arcade.start_render()
    draw_background()
    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()  