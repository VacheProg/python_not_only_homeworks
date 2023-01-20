# TODO 
# @staticmethod
# @classmethod
# @property



# class Triangle:
# 	_polices = 'asdasfafa'
# 	def __init__(self, edge1, edge2, angle):
# 		pass
# 	@classmethod
# 	def get_from3_edges(cls, p1, p2, p3):
# 		# calculate angle
# 		return cls(p1, p2, angle)
# 	@classmethod
# 	def from_height_edge(cls, height, edge)
# 		#calculate edge1, edge2, angle
# 		return cls()
# 	def area(self):
# 		return area
# t1 = Triangle.get_from3_edges(p1, p2, p3)
# t1 = Triangle.from(p1, p2, p3)


# print(Triangle.get_policy(12, 14))


class test:
	def __init__(self):
		self._dt = '6'
		self.dt =12
	@property
	def dt(self):
		print('called getter')
		return self._dt+ 'asdasdasd'
	@dt.setter
	def dt(self, dt2):
		if dt2 == 'a':
			raise
		print('called setter')
		self._dt = dt2

t = test()
t.dt
t.dt = '123'
print(dir(t))
print(t.dt)