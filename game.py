import random

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAIN_SPEED = 5
SCREEN_TITLE = "Ping Pong Game"


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.3)

    def on_update(self):
        self.center_x += self.change_x

        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

        if self.left <= 0:
            self.left = 0


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.3)
        self.change_x = MAIN_SPEED
        self.change_y = MAIN_SPEED

    def on_update(self):
        super().update()
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = -self.change_x

        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y = -self.change_y


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.LIGHT_GRAY)
        self.bar = Bar()
        self.ball = Ball()
        self.all_sprites = arcade.SpriteList()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
        self.all_sprites.append(self.bar)
        self.all_sprites.append(self.ball)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Hello, athletes!", 300, 550, arcade.color.WHITE, 24)
        self.all_sprites.draw()

    def on_update(self, delta):
        self.ball.on_update()
        self.bar.on_update()

        if arcade.check_for_collision(self.ball, self.bar):
            self.ball.change_y = -self.ball.change_y
            self.ball.bottom = self.bar.top

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.bar.change_x = MAIN_SPEED * 2

        if symbol == arcade.key.LEFT:
            self.bar.change_x = - MAIN_SPEED * 2

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT:
            self.bar.change_x = 0


def main():
    game = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
