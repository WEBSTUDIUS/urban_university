import arcade


class Game(arcade.Window):
    def on_draw(self):
        self.clear((255, 255, 255))


if __name__ == 'main':
    window = Game()
    arcade.run()
