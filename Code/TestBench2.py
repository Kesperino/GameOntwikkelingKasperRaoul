import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"
SPRITE_SCALING = 0.5



class Player():

    def __init__(self):
        self.x = 50
        self.y = 100
        self.delta_x = 0
        self.delta_y = 0

    def setup(self):
        self.x = 0
        self.y = 0
        self.delta_x = 0
        self.delta_y = 0
        
    def on_draw(self):
        self.player_sprite = Player(path, SPRITE_SCALING)


    def update(self, delta_time):
        self.x += self.delta_x
        self.y += self.delta_y

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.delta_x = -5
        elif key == arcade.key.RIGHT:
            self.delta_x = 5
        elif key == arcade.key.UP:
            self.delta_y = 5
        elif key == arcade.key.DOWN:
            self.delta_y = -5

    def on_key_release(self, key, key_modifiers):
        self.delta_y = 0
        self.delta_x = 0



class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)
        self.score = 0
        self.player = None


    def setup(self):
        self.score = 0
        self.player = Player()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT * (1 / 8), arcade.color.SKY_BLUE)
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 8, 0, arcade.color.DARK_SPRING_GREEN)

        self.player_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = Player("visuele onderdelen/grape fruit man.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        arcade.draw_text("Welcome", 10, 550, arcade.color.BLACK, 40)
        arcade.draw_text(f"Score: {self.score}", 200, 200, arcade.color.BLACK, 40)

    def update(self, delta_time):
        self.score += 1
        self.player.update(delta_time)


    def on_key_press(self, key, key_modifiers):
        self.player.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.player.on_key_release(key, key_modifiers)



def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()