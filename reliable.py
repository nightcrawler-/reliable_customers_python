#get you csv file
import csv
from datetime import datetime
from operator import itemgetter

def get_best_customer(transactions_csv_file_path, n):

	with open(transactions_csv_file_path) as f:
	    data=[tuple(line) for line in csv.reader(f)]

	#chuck first line as is titles
	data.pop(0)

	#sort the tie breaker: account name, might not be necessacry at this stage
	data.sort(key=itemgetter(1), reverse=True) 

	#sort by date with the formats provided
	data.sort(key=lambda L: datetime.strptime(L[2], '%Y-%m-%d %H:%M:%S'))

	#loop though list, use dictonary to increment streak for each customer (will not include broken streaks, yet)
	#dictonary of tuples to keep track of streak, sort by whatever

	customers = {}
	for customer in data:
	 #get current customer from dict
	 #could be empty
	 #create object in tuple for streaks* based on date comparisons, get day in year for compare: caveat: will not work for datasets with several years :) but meh, 2017 baby!
	 #current customer should be dict with acc as key, and streak list as value
	 current_customer = customers.get(customer[0]) #if is null/None], deal
	 customer = list(customer)

	 if current_customer is None:
	  #increment streak
	  streaks = [1,]
	  customer.append(streaks)
	  #assing to csutomer on dict
	  customers[customer[0]] = customer
	 else:
	 	#set customer streak to cached value
	 	customer.append(current_customer[3])

	 	t1 = datetime.strptime(customer[2], '%Y-%m-%d %H:%M:%S').timetuple()
	 	day_in_yea1 = t1[7]

	 	t2 = datetime.strptime(current_customer[2], '%Y-%m-%d %H:%M:%S').timetuple()
	 	day_in_yea2 = t2[7]

	 	if (day_in_yea1 - day_in_yea2) is 1:
	 		#streak is still on, add to current streak object
	 		customer[3][len(customer[3])-1] = customer[3][len(customer[3])-1] + 1
	 	else:
	 		#streak was broken, create new streak object and move
	 		customer[3] += [1,]
	 	customers[customer[0]] = customer

	#now sort then slice, phew
	#first sort streaks for each to get longest, add new element for that
	#use largest streak to sort dataset
	#tie break sort
	#slice
	#might need to go from dict to list as now only account with relevant data appear
	for account in customers.values():
		account[3].sort(reverse=True)
		account.append(account[3][0])

	sorted_by_longest_streak = customers.values()

	#tie breaker sort
	sorted_by_longest_streak.sort(key=itemgetter(1))
	sorted_by_longest_streak.sort(key=itemgetter(4), reverse=True)
	#slice:
	sublist =  sorted_by_longest_streak[0:n]
	#sanitize output
	result = []

	for item in sublist:
		result.append(item[0])

	print result
	#print customers

get_best_customer('transaction_data_2.csv', 2)

