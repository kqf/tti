
data.csv: en.csv pl.csv de.csv es.csv fr.csv
	cat $^ | tr '[:upper:]' '[:lower:]' > $@

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
	rm _*de.csv

es.csv: size = 100
es.csv: source = https://raw.githubusercontent.com/jvalhondo/spanish-names-surnames/master
es.csv:
	@# Download thed data, and skip the first row
	curl $(source)/male_names.csv | tail -n +2 > _male_es.csv
	curl $(source)/female_names.csv | tail -n +2 > _female_es.csv

	@# Select male and female columns
	cat _male_es.csv | head -n $(size) | cut -d ',' -f1 > _male_es.csv
	cat _female_es.csv | head -n $(size) | cut -d ',' -f1 > _female_es.csv

	@# Merge and cleanup
	cat _male_es.csv _female_es.csv > $@
	rm _*es.csv

fr.csv: size = 100
fr.csv: source = curl https://raw.githubusercontent.com/dkoslicki/pytst2/master/test/prenoms.txt
fr.csv:
	curl $(source) | iconv -f ISO-8859-1 -t UTF8  > _utf8_fr.csv
	cat _utf8_fr.csv | cut -d ';' -f1 | sort --random-sort | head -n 100 > $@
