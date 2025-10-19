class RectanguloNicolasRuiz63:
    def __init__(self, base_nicolas_ruiz_63, altura_nicolas_ruiz_63):
        self.base_nicolas_ruiz_63 = base_nicolas_ruiz_63
        self.altura_nicolas_ruiz_63 = altura_nicolas_ruiz_63
    def area_nicolas_ruiz_63(self):
        print(self.base_nicolas_ruiz_63 * self.altura_nicolas_ruiz_63)
    def perimetro_nicolas_ruiz_63(self):
        print(2*(self.base_nicolas_ruiz_63 + self.altura_nicolas_ruiz_63))

rect_nicolas_ruiz_63 = RectanguloNicolasRuiz63(4, 5)
rect_nicolas_ruiz_63.area_nicolas_ruiz_63()
rect_nicolas_ruiz_63.perimetro_nicolas_ruiz_63()