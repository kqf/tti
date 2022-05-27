
data.csv: en.csv pl.csv de.csv
	cat $^ > $@

en.csv: size = 100
en.csv: source = https://raw.githubusercontent.com/aruljohn/popular-baby-names/master/2000/girl_boy_names_2000.csv
en.csv:
	@# Download thed data, and skip the first row
	curl $(source) | tail -n +2 > _raw_us.csv

	@# Select male and female columns
	cat _raw_us.csv | head -n $(size) | cut -d ',' -f2 > _female_us.csv
	cat _raw_us.csv | head -n $(size) | cut -d ',' -f3 > _male_us.csv

	@# Merge the results
	cat _male_us.csv _female_us.csv > $@
	rm _*us.csv

pl.csv: size = 100
pl.csv: source = https://raw.githubusercontent.com/denmats/imiona_polskie/master/imiona_polskie.txt
pl.csv:
	@# Download thed data, remove empty lines, random shuffle
	curl $(source) | awk NF | sort --random-sort  | head -n $(size) > $@

de.csv: source = https://raw.githubusercontent.com/oliverpitsch/craft-data-german/master/craft-data-german-first_names
de.csv:
	curl $(source)-male.txt > _male_de.csv
	curl $(source)-female.txt > _female_de.csv
	cat _male_de.csv _female_de.csv | sort --random-sort > $@
