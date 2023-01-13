class Rect:
	def __init__(self):
		pass
	def setw(self, tiv):
		self.w = tiv
	def seth(self, tiv):
		self.h = tiv
	def area(self):
		return self.h*self.w

class Square(Rect):
	def __init__(self):
		pass
	def setw(self, tiv):
		self.edge = tiv
	def seth(self, tiv):
		self.edge = tiv
	def area(self):
		return self.edge*self.edge


def f(r):
	r.seth(12)
	r.setw(10)
	print(r.area())

f(Rect())

f(Square())



class T:
  
  def __init__(self, phi: list):
    self.phi = phi
    
class S(T):
  
  def __init__(self, phi: str):
    self.phi = phi

if __name__ == "__main__":
  x = T(phi=["a", "b"])
  y = S(phi="c, d")
