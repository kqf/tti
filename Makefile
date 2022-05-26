uslink=https://raw.githubusercontent.com/aruljohn/popular-baby-names/master/2000/girl_boy_names_2000.csv

all:
	curl $(uslink) > us-raw.csv
