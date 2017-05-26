#!/usr/bin/python
import random

class RollDice:

	def __init__(self,num_face):
		if(isinstance(num_face,int) and num_face > 0):
			self.num_face = num_face
		else:
			self.num_face = 6

	def rollDice(self):
		return random.randint(1,self.num_face)
