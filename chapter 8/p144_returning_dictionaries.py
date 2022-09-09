"""Return a dictionary of information about a person."""
def build_person(first_name, last_name):
	
	person = {'first': first_name, 'last': last_name}
	return person
musician = build_person('jimi', 'hendrix')
print(musician)



"""Return a dictionary of information about a person."""
def build_person(first_name, last_name, age=''):

	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

musician = build_person('jimi', 'hendrix2')
print(musician)