#!/bin/python
'''
Multi winner approval voting implementation 
'''

voters = ['A', 'B', 'C', 'D']
options = ['1', '2', '3', '4', '5']

votes = {
	'A': ['1', '2', '5'],
	'B': ['1'],
	'C': ['5'],
	'D': ['4', '5', '1'] }
		
		
chosen_options =  {
	'1': ['A', 'B', 'D'],
	'2': ['A'],
	'3': [],
	'4': ['D'],
	'5': ['D']
}
