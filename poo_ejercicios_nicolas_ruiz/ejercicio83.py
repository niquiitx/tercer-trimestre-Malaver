class RectanguloNicolasRuiz83:
    def __init__(self, base_nicolas_ruiz_83, altura_nicolas_ruiz_83):
        self.base_nicolas_ruiz_83 = base_nicolas_ruiz_83
        self.altura_nicolas_ruiz_83 = altura_nicolas_ruiz_83
    def area_nicolas_ruiz_83(self):
        print(self.base_nicolas_ruiz_83 * self.altura_nicolas_ruiz_83)
    def perimetro_nicolas_ruiz_83(self):
        print(2*(self.base_nicolas_ruiz_83 + self.altura_nicolas_ruiz_83))

rect_nicolas_ruiz_83 = RectanguloNicolasRuiz83(4, 5)
rect_nicolas_ruiz_83.area_nicolas_ruiz_83()
rect_nicolas_ruiz_83.perimetro_nicolas_ruiz_83()