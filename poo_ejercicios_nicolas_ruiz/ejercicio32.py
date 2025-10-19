class Punto2NicolasRuiz32:
    def __init__(self, x_nicolas_ruiz_32, y_nicolas_ruiz_32):
        self.x_nicolas_ruiz_32 = x_nicolas_ruiz_32
        self.y_nicolas_ruiz_32 = y_nicolas_ruiz_32
    def distancia_origen_nicolas_ruiz_32(self):
        print((self.x_nicolas_ruiz_32**2 + self.y_nicolas_ruiz_32**2)**0.5)
p_nicolas_ruiz_32 = Punto2NicolasRuiz32(1, 4)
p_nicolas_ruiz_32.distancia_origen_nicolas_ruiz_32()