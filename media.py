# Class to store movie data
class movie:
	def __init__(self, title, imgUrl, youtubeUrl, rating, starring):
		self.title = title
		self.poster_image_url = imgUrl
		self.trailer_youtube_url = youtubeUrl
		self.rating = rating
		self.starring = starring
