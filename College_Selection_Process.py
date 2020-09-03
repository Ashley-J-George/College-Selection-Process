'''           
@Author: Ryan Schachte
@Publication-Date: 1/12/17 5:23 PM
@Description: 
The stable matching algorithm seeks to solve the problem of finding a stable match between two sets of equal size
given a list of preferences for each element. 
We can define "matching" and "stable" by the following definitions.
Matching: Mapping from the elements of one set to the elements of another set
Stable: No element A of the first set that prefers an element B of the second set over its current partner such that element B prefers element A over its current partner. 

Output:
['Ryan', 'Josh', 'Blake', 'Connor']
DEALING WITH Ryan
Ryan is no longer a free man and is now tentatively engaged to Lizzy
DEALING WITH Blake
Blake is no longer a free man and is now tentatively engaged to Sarah
DEALING WITH Josh
Sarah is taken already..
She's satisfied with Blake..
Lizzy is taken already..
She's satisfied with Ryan..
Josh is no longer a free man and is now tentatively engaged to Daniella
DEALING WITH Connor
Lizzy is taken already..
She's satisfied with Ryan..
Sarah is taken already..
She's satisfied with Blake..
Connor is no longer a free man and is now tentatively engaged to Zoey

Matching Pairs: [['Ryan', 'Lizzy'], ['Blake', 'Sarah'], ['Josh', 'Daniella'], ['Connor', 'Zoey']], ['Sarah', 'Lizzy', 'Daniella', 'Zoey']
'''

import collections

#The colleges that the students prefer
preferred_rankings_students = {
	'Ryan': 	['IIT Bombay', 'BITS Pilani', 'COEP', 'PCCOE'],
	'Josh': 	['BITS Pilani', 'IIT Bombay', 'PCCOE', 'COEP'],
	'Blake': 	['BITS Pilani', 'PCCOE', 'COEP', 'IIT Bombay'],
	'Connor': 	['IIT Bombay', 'BITS Pilani', 'COEP', 'PCCOE']
}

#The students that the colleges prefer
preferred_rankings_colleges = {
	'IIT Bombay': 	['Ryan', 'Blake', 'Josh', 'Connor'],
	'BITS Pilani': 	['Ryan', 'Blake', 'Connor', 'Josh'],
	'COEP':  	['Connor', 'Josh', 'Ryan', 'Blake'],
	'PCCOE':	['Ryan', 'Josh', 'Connor', 'Blake'] 
}

#Keep track of the people that "may" end up together
tentative_engagements = []

#Men who still need to propose and get accepted successfully
free_students = []

def init_free_students():
	'''Initialize the arrays of women and men to represent 
		that they're all initially free and not engaged'''
	for student in preferred_rankings_students.keys():
		free_students.append(student)

def begin_matching(student):
	'''Find the first free college available to a student at
		any given time'''

	print("DEALING WITH %s"%(student))
	for college in preferred_rankings_students[student]:

		#Boolean for whether college is taken or not
		taken_match = [couple for couple in tentative_engagements if college in couple]

		if (len(taken_match) == 0):
			#tentatively engage the student and college
			tentative_engagements.append([student, college])
			free_students.remove(student)
			print('%s is no longer a free student and is now tentatively engaged to %s'%(student, college))
			break

		elif (len(taken_match) > 0):
			print('%s is taken already..'%(college))

			#Check ranking of the current dude and the ranking of the 'to-be' dude
			current_guy = preferred_rankings_colleges[college].index(taken_match[0][0])
			potential_guy = preferred_rankings_colleges[college].index(student)

			if (current_guy < potential_guy):
				print('She\'s satisfied with %s..'%(taken_match[0][0]))
			else: 
				print('%s is better than %s'%(student, taken_match[0][0]))
				print('Making %s free again.. and tentatively engaging %s and %s'%(taken_match[0][0], student, college))
				
				#The new guy is engaged
				free_students.remove(student)

				#The old guy is now single
				free_students.append(taken_match[0][0])

				#Update the fiance of the college (tentatively)
				taken_match[0][0] = student
				break

def stable_matching():
	'''Matching algorithm until stable match terminates'''
	while (len(free_students) > 0):
		for student in free_students:
			begin_matching(student)


def main():
	init_free_students()
	print(free_students)
	stable_matching()
	print(tentative_engagements)

main()





