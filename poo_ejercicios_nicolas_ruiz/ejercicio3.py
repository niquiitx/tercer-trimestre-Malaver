class RectanguloNicolasRuiz3:
    def __init__(self, base_nicolas_ruiz_3, altura_nicolas_ruiz_3):
        self.base_nicolas_ruiz_3 = base_nicolas_ruiz_3
        self.altura_nicolas_ruiz_3 = altura_nicolas_ruiz_3
    def area_nicolas_ruiz_3(self):
        print(self.base_nicolas_ruiz_3 * self.altura_nicolas_ruiz_3)
    def perimetro_nicolas_ruiz_3(self):
        print(2*(self.base_nicolas_ruiz_3 + self.altura_nicolas_ruiz_3))

rect_nicolas_ruiz_3 = RectanguloNicolasRuiz3(4, 5)
rect_nicolas_ruiz_3.area_nicolas_ruiz_3()
rect_nicolas_ruiz_3.perimetro_nicolas_ruiz_3()