from random import choice
class RandomWalk():
	def __init__(self, num_points = 5000):
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		while len(self.x_values) < self.num_points:
			x_direction = choice([1, -1])
			x_distance = choice([0, 1, 2, 3, 4])
			x_setp = x_direction * x_distance
			y_direction = choice([1, -1])
			y_distance = choice([0, 1, 2, 3, 4])
			y_setp = y_direction * y_distance
			if x_setp == 0 and y_setp == 0:
				continue
			next_x = self.x_values[-1] + x_setp
			next_y = self.y_values[-1] + y_setp
			self.x_values.append(next_x)
			self.y_values.append(next_y)
