# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
	"""docstring for LatLon"""
	def __init__(self, obj):
		self.lat = obj["lat"]
		self.lon = obj["lon"]


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
	"""docstring for Waypoint"""
	def __init__(self, obj):
		self.name = obj["name"]
		super().__init__(obj)

	def __str__(self):
		return f"{self.name}, {self.lat}, {self.lon}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
	"""docstring for Geocache"""
	def __init__(self, obj):
		self.difficulty = obj["difficulty"]
		self.size = obj["size"]
		super().__init__(obj)

	def __str__(self):
		return f"{self.name}, diff {self.difficulty}, size {self.size}, {self.lat} {self.lon}"


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
test = { 'name': "Catacombs", "lat": 41.70505, "lon": -121.51521 }
waypoint = Waypoint({ 'name': "Catacombs", "lat": 41.70505, "lon": -121.51521 })

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache({ 'name': "Newberry", "difficulty": 1.5, "size": 2, "lat": 44.052137, "lon": -121.41556 })

# Print it--also make this print more nicely
print(geocache)
