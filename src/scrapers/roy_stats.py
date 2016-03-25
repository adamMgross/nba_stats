'''
Extracts all rankings for ROY and dumps all data into
individual json files named by year and type of stat
'''

from datetime import date
import basketball_reference

# Year since which ROY rankings were available
year = 1984

# Used to get stats till the last year
current_year = date.today().year

# Type of stat for which you want rankings
type_of_stat = "div_roy"

# Dumps all stats for the year into individual json files
while (year < current_year):
    basketball_reference.dump_stats(type_of_stat, year)
    year += 1
    print ".",

print "Done!"