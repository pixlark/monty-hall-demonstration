#!/usr/bin/python3

from random import choice, randrange

def random_door():
	return randrange(3)

def follows_rules(car, initial_choice, montys_choice, remaining_doors):
	if montys_choice == initial_choice:
		return False
	if montys_choice == car:
		return False
	if len(remaining_doors) != 1:
		return False
	return True
	
iterations = 100000
times_won = 0

for _ in range(iterations):
	car = random_door()
	initial_choice = random_door()
	choices = set(range(3)) - set([initial_choice, car])
	montys_choice = choice(list(choices))
	remaining_doors = set(range(3)) - set([initial_choice, montys_choice])
	if not follows_rules(car, initial_choice, montys_choice, remaining_doors):
		print("State invalidated somehow. Exiting.")
		break
	if remaining_doors.pop() == car:
		times_won += 1

print("After {0} iterations, picking the remaining door netted you the car {1}% of the time.".format(iterations, (times_won / iterations) * 100))
