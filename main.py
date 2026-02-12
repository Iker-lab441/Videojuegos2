import math
import arcade

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
    arcade.draw_xywh_rectangle_filled(x - 25 * escala, y - 75 * escala, 50 * escala, 150 * escala, (50, 50, 200))
    # Piernas
    arcade.draw_xywh_rectangle_filled(x - 25 * escala, y - 125 * escala, 10 * escala, 200 * escala, (50, 50, 200))
    arcade.draw_xywh_rectangle_filled(x + 15 * escala, y - 125 * escala, 10 * escala, 200 * escala, (50, 50, 200))
    # Brazos
    if brazos_abiertos: arcade.draw_xywh_rectangle_filled(x - 75 * escala, y + 15 * escala, 50 * escala, 10 * escala, (200, 150, 150))
    else: arcade.draw_xywh_rectangle_filled(x - 35 * escala, y - 25 * escala, 10 * escala, 50 * escala, (200, 150, 150))
    arcade.draw_xywh_rectangle_filled(x - 35 * escala, y + 15 * escala, 10 * escala, 10 * escala, (50, 50, 200))
    if brazos_abiertos: arcade.draw_xywh_rectangle_filled(x + 25 * escala, y + 15 * escala, 50 * escala, 10 * escala, (200, 150, 150))
    else: arcade.draw_xywh_rectangle_filled(x + 25 * escala, y - 25 * escala, 10 * escala, 50 * escala, (200, 150, 150))
    arcade.draw_xywh_rectangle_filled(x + 25 * escala, y + 15 * escala, 10 * escala, 10 * escala, (50, 50, 200))
    # Cabeza
    arcade.draw_circle_filled(x, y + 75 * escala, 50 * escala, (200, 150, 150))
    # Ojos
    arcade.draw_circle_filled(x - 20 * escala, y + 85 * escala, 15 * escala, (255, 255, 255))
    arcade.draw_circle_filled(x - 20 * escala, y + 85 * escala, 8 * escala, (0, 0, 0))
    arcade.draw_circle_filled(x + 20 * escala, y + 85 * escala, 15 * escala, (255, 255, 255))
    arcade.draw_circle_filled(x + 20 * escala, y + 85 * escala, 8 * escala, (0, 0, 0))
    # Boca
    arcade.draw_arc_outline(x, y + 75 * escala, 80 * escala, 60 * escala, (200, 100, 100), 200, 340, 10 * escala)

juego = Juego()
arcade.run()