class School():
	
	def __init__(self, name, roster = {}):
		self.name = name
		self.roster = roster

	def add_student(self, name, grade):
		if grade not in list(self.roster.keys()):
			self.roster[grade] = name
		else:
			self.roster[grade] = [self.roster[grade], name]

	def grade(self, grade):
		return self.roster[grade]

	def sort_roster(self):
		for key, val in school.roster.items():
			return (key, ":", school.roster[key])
			







