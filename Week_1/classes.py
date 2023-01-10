


class Triangle():
	"""vochmi bani"""
	def __init__(self, e1, e2, angle):
		"""aystex linume docstring ))"""
		self.e1 = 12
		self.e2 = e2
		self.angle = angle
	
	def __repr__(self):
		pass
	def __str__(self):
		return f"{self.e1}"

	def __eq__(self, obj):
		return obj == 14

	def a(self):
		print(self.e1)
a = 'asdas'
print(Triangle)
my_tri = Triangle(1, 2, 60)
my_tri.e1 = 13
my_tri.a()
print('zzzzzzzz',my_tri)
if my_tri == 15:
	print('hello_world')