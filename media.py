import webbrowser 
class Movie ():
	"""Class to store movies, with related information to display on html page"""
	def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer):
		"""Takes the movie title,storyline, image and youtube trailer for the
		and stores in an object to use for open_movies_page"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailer

	def show_trailer(self):
		"""Function to show trailer of given Movie can be used to test the 
		trailer URL for each movie instance"""
		webbrowser.open(self.trailer_youtube_url)