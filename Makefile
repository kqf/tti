pllink=https://github.com/denmats/imiona_polskie/blob/master/imiona_polskie.csv


data.csv: en.csv
	cat $< > $@

en.csv: size = 100
en.csv: source = https://raw.githubusercontent.com/aruljohn/popular-baby-names/master/2000/girl_boy_names_2000.csv
en.csv:
	curl $(source) | _raw_us.csv
	cat _raw_us.csv | head -n $(size) | cut -d ',' -f2 > _female_us.csv
	cat _raw_us.csv | head -n $(size) | cut -d ',' -f3 > _male_us.csv
	cat _male_us.csv _female_us.csv > $@
