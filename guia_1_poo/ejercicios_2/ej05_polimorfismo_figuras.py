class Figura:
  def area(self):
    raise NotImplementedError

class Circulo(Figura):
  def __init__(self, r):
    self.r = r
  def area(self):
    return 3.14159265 * self.r * self.r
class Rectangulo(Figura):
  def __init__(self, w, h):
    self.w = w
    self.h = h
  def area(self):
    return self.w * self.h
    
figuras = [Circulo(2), Rectangulo(3, 4), Circulo(1)]
for f in figuras:
  print(f"Area: {f.area()}")
