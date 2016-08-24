import media
import fresh_tomatoes

rogue_one = media.Movie("Rogue One: A Star Wars Story", 
	"A group of unlikely heroes band together on a mission to steal the plans to the Death Star",
	 "https://upload.wikimedia.org/wikipedia/en/d/dd/Rogue_One_cast_revealed.jpg",
	  "https://www.youtube.com/watch?v=frdj1zb9sMY")

finding_dory = media.Movie("Finding Dory",
 "Dory goes looking for her family and adventure ensue", 
 "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg", 
 "https://www.youtube.com/watch?v=cxskm6dDfIY")

suicide_squad = media.Movie("Suicide Squad",
	"Based on the DC Comic, the government gives a team of supervillains a chance at redemption.",
	"http://static.srcdn.com/wp-content/uploads/suicide-squad-movie-2016-poster.jpeg",
	"https://www.cultofwhatever.com/wp-content/uploads/2016/08/suicide-squad-poster.jpg")

jason_bourne = media.Movie("Jason Bourne",
	"The CIA's most dangerous former operative is drawn out of hiding to uncover more explosive truths about his past.",
	"http://ia.media-imdb.com/images/M/MV5BMTU1ODg2OTU1MV5BMl5BanBnXkFtZTgwMzA5OTg2ODE@._V1_SY1000_SX632_AL_.jpg",
	"https://www.youtube.com/watch?v=F4gJsKZvqE4")

happy_gilmore = media.Movie("Happy Gilmore", 
	"A rejected hockey player puts his skills to the golf course to save his grandmother's house.",
	"https://upload.wikimedia.org/wikipedia/en/b/be/Happygilmoreposter.jpg",
	"https://www.youtube.com/watch?v=-6sT7MSJ4GE")

star_trek_beyond = media.Movie("Star Trek Beyond", 
	"The USS Enterprise crew explores the furthest reaches of uncharted space", 
	"https://upload.wikimedia.org/wikipedia/en/b/ba/Star_Trek_Beyond_poster.jpg",
	"https://www.youtube.com/watch?v=bzD8H6o1awQ")

movies= [rogue_one, finding_dory, suicide_squad, jason_bourne, happy_gilmore, star_trek_beyond]
fresh_tomatoes.open_movies_page(movies)