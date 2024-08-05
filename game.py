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


class Button:
    def __init__(self, center_x, center_y, width, height, text, action_function):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.action_function = action_function

    def draw(self):
        # Draw button
        arcade.draw_lbwh_rectangle_filled(self.center_x - 100, self.center_y - 25, self.width, self.height,
                                          arcade.color.ASH_GREY)
        # Draw text
        arcade.draw_text(self.text, self.center_x, self.center_y, arcade.color.BLACK, 18, anchor_x="center",
                         anchor_y="center")

    def is_clicked(self, x, y):
        return (self.center_x - self.width / 2 < x < self.center_x + self.width / 2 and
                self.center_y - self.height / 2 < y < self.center_y + self.height / 2)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.status = None
        arcade.set_background_color(arcade.color.LIGHT_GRAY)
        self.bar = Bar()
        self.ball = Ball()
        self.score = 0
        # Create button instance
        self.button = Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5, 200, 50, "START AGAIN", self.on_button_click)
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
        arcade.draw_text(f'Score: {self.score}', 20, SCREEN_HEIGHT - 30, arcade.color.DARK_GREEN, 16)
        if self.status:
            arcade.draw_text(self.status, SCREEN_WIDTH / 3.5, SCREEN_HEIGHT / 2, arcade.color.RED, 40)
            self.button.draw()

    def on_update(self, delta):
        self.ball.on_update()
        self.bar.on_update()

        if arcade.check_for_collision(self.ball, self.bar):
            self.ball.change_y = -self.ball.change_y
            self.ball.bottom = self.bar.top
            self.score += 1
        if self.ball.bottom < 0:
            self.ball.stop()
            self.status = 'GAME OVER'

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.bar.change_x = MAIN_SPEED * 2

        if symbol == arcade.key.LEFT:
            self.bar.change_x = - MAIN_SPEED * 2

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT:
            self.bar.change_x = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if self.button.is_clicked(x, y):
            self.button.action_function()

    def on_button_click(self):
        self.__init__()


def main():
    game = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
