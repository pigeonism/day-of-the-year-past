# day of year ww
# test date: feb 11 1978
# used for anchor days
sunday = 0
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6
# same as above but to print the day used for step [7]
days = {
0:"sunday",
1:"monday",
2:"tuesday",
3:"wednesday",
4:"thursday",
5:"friday",
6:"saturday"
}

# known doomsday years, a guide for step [7]
doomsdays = {
"february":28, # 29 for leap year
"march":7,
"april":4, 
"may":9, 
"june":6, 
"july":11, 
"august":8, 
"september":5, 
"october":10, 
"november":7, 
"december":12,
"january":3 # 4 for leap year
}
# known anchor days, used in step [4]
# 1800 - 1899: Friday
# 1900 - 1999: Wednesday
# 2000 - 2099: Tuesday
# 2100 - 2199: Sunday

# see day of year text for adding more
anchor_pairs = {1800:friday, 1900:wednesday, 2000:tuesday, 2100:sunday}
anchor_day = 9 # placeholder

#year = 1978
#entered_month = "february"
#entered_day = 11

year = 2019
entered_month = "may"
entered_day = 11

# would be from tkinter entry  later. just getting the digits needed
# from the date's year, the last two
year_end_pair_string = str(year)[2:]
year_end_digits = int(year_end_pair_string)
print("end of year digits:\t\t\t", year_end_digits)

# use // integer division which ignores floating point numbers 
# to get how many times 12 fits in to that year suffix
print("end of year digits (/12):\t\t", year_end_digits // 12)
twelves_number_of = year_end_digits // 12 # [1]

print ("number of twelves:\t\t\t",twelves_number_of )
print ("product of number of twelves times 12:",twelves_number_of * 12)

diff = year_end_digits - (twelves_number_of * 12) # [2]
print("difference (year - product):\t\t", diff)


fours_number_of = diff // 4 # [3]
print("difference divided by 4:\t\t", fours_number_of)


# [4] anchor_day
for anchor_year in anchor_pairs:
	#print(anchor_year)
	# account for year (1800) and less than 1 (1899) hence 99
	if (year >= anchor_year and year < anchor_year+99):
		anchor_day = anchor_pairs[anchor_year]

print("anchor day:\t\t\t\t", anchor_day)



# [5] add them all
total = twelves_number_of + diff + fours_number_of + anchor_day
print("steps total:\t\t\t\t", total)

# [6] get the remainder of the total if stuffed with 7's
# the result should indicate a number that matches a day at the top of
# this prog, to be used later in step 7
step_six_day = total % 7
print("total subtracting multiples of 7:\t", step_six_day)

print("############\n")
# [7] search known doomsdays by month, add a condition for feb and jan
# which are different in leap years
def match_day(doom_day):
	#get the doomsday, subtract 7 or add 7, check if near to entered_day
	# strip multiples of 7 so we can count from the remainder to
	# entered day
	# 7 goes into the avg 30 or so day month 4 times
	# so two passes is ok for now. but lower numbers need to be handled first
	if entered_day <= 7:
		diff = abs(doom_day - entered_day)
		return diff

	# if diff is still big after this(another 7 can fit), another step is done
	# a diff of 7 is ok, it just means we add 7 days and we're done
	diff = (abs((doom_day - 7) - entered_day)) 
	
	if diff > 7:
		diff = abs(diff - 7)
		
	print ("final difference:\t\t",diff)

	return diff

final_day = 99999 # placeholder
for month in doomsdays:
	if(month == entered_month):
		# leap year test would be here
		doomsday = (doomsdays[month])
		# task is to get closer to the day supplied

		# this should eventually return true
		count = match_day(doomsday)
		
		# figure out if to count back or forward the totals should be within 7 (<7)
		if doomsday > entered_day:
			final_day = step_six_day - count # 

		if entered_day > doomsday:
			
			final_day = step_six_day + count
		
		print("###########\n")
		# the final day should be <7    (2 - 3 ) % 7    or (2 - 3 ) % 7 [account for all 0-6]
		print (final_day % 7) 
		print(days[ final_day % 7 ])
