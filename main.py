import math
import arcade
from arcade.types import Color

color_carne = Color(200, 150, 150)
color_esclera = Color(255, 255, 255)
color_pupila = Color(0, 0, 0)
color_ropa = Color(50, 50, 200)

class Juego(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Dibujos")
        self.x = 300
        self.y = 300
        self.escala = 1
        self.brazos_abiertos = False
        self.speed = 10
        self.t = 0

    def on_update(self, delta_time: float):
        self.t += delta_time * (1.25 + math.sin(self.t)) * self.speed

    def on_draw(self):
        self.clear()
        dibujar_chaval(self.x + math.sin(self.t) * 100, self.y, self.escala, self.brazos_abiertos)
        self.escala = 1.5 + math.sin(self.t / 2.0)
        self.brazos_abiertos = self.escala > 1


def dibujar_chaval(x: float, y: float, escala: float, brazos_abiertos: bool) -> None:
    # Cuerpo
    arcade.draw_lbwh_rectangle_filled(x - 25 * escala, y - 75 * escala, 50 * escala, 150 * escala, color_ropa)

    # Piernas
    # Pierna izquierda
    arcade.draw_lbwh_rectangle_filled(x - 25 * escala, y - 125 * escala, 10 * escala, 200 * escala, color_ropa)
    # Pierna derecha
    arcade.draw_lbwh_rectangle_filled(x + 15 * escala, y - 125 * escala, 10 * escala, 200 * escala, color_ropa)

    # Brazos
    if brazos_abiertos:
        # Brazo izquierdo
        arcade.draw_lbwh_rectangle_filled(x - 75 * escala, y + 15 * escala, 50 * escala, 10 * escala, color_carne)
        # Brazo derecho
        arcade.draw_lbwh_rectangle_filled(x + 25 * escala, y + 15 * escala, 50 * escala, 10 * escala, color_carne)
    else:
        # Brazo izquierdo
        arcade.draw_lbwh_rectangle_filled(x - 35 * escala, y - 25 * escala, 10 * escala, 50 * escala, color_carne)
        # Brazo derecho
        arcade.draw_lbwh_rectangle_filled(x + 25 * escala, y - 25 * escala, 10 * escala, 50 * escala, color_carne)

    # Mangas
    # Manga izquierda
    arcade.draw_lbwh_rectangle_filled(x - 35 * escala, y + 15 * escala, 10 * escala, 10 * escala, color_ropa)
    # Manga derecha
    arcade.draw_lbwh_rectangle_filled(x + 25 * escala, y + 15 * escala, 10 * escala, 10 * escala, color_ropa)

    # Cabeza
    arcade.draw_circle_filled(x, y + 75 * escala, 50 * escala, color_carne)
    # Ojos
    # Esclera izquierda
    arcade.draw_circle_filled(x - 20 * escala, y + 85 * escala, 15 * escala, color_esclera)
    # Pupila izquierda
    arcade.draw_circle_filled(x - 20 * escala, y + 85 * escala, 8 * escala, color_pupila)
    # Esclera derecha
    arcade.draw_circle_filled(x + 20 * escala, y + 85 * escala, 15 * escala, color_esclera)
    # Pupila derecha
    arcade.draw_circle_filled(x + 20 * escala, y + 85 * escala, 8 * escala, color_pupila)

    # Boca
    arcade.draw_arc_outline(x, y + 75 * escala, 80 * escala, 60 * escala, (200, 100, 100), 200, 340, 10 * escala)

if __name__ == "__main__":
    juego = Juego()
    arcade.run()