#!/usr/bin/env python

import curses
from enum  import Enum
from itertools import count, accumulate
from bisect import bisect_left
from dotenv import load_dotenv
import sys
import os


# load_dotenv()

def main():



'''
	DOTENV TRIALS::::::::::

	if len(sys.argv) == 2:
		all = sys.argv
		print(all)
		print('tier based approach')
		tier = sys.argv[1]
		print(f'using config from tier: {tier}')
		if tier == 'DEV':
			user = os.getenv('devuser')
			pwd = os.getenv('devpass')
		elif tier == "PROD":
			user = os.getenv('user')
			pwd = os.getenv('pass')
		else:
			raise SystemExit('unknownn tier')


		print(f"Working intier: {tier}, user: {user}, password: {pwd} ")
	else:
		print("dryrun ....exiting")
		print("EXIT COMPLETE. BYE")
	
'''



'''
	index(5,5)

	def index(a, x):
	i = bisect_left(a, x, lo=0, hi=len(a))
	return i
'''






'''
enum trials


	class color(Enum):
		RED = 1
		GREEN = 2
		BLUE = 3
	print(repr(color.RED))
	print(type(color.RED))

	for i in color:

		print(type(i.name))
'''




'''
CURSES MODULE:
	
	screen = curses.initscr()

	my_window = curses.newwin(15, 20, 0, 0)

	my_window.addstr(4,4, "h")
	my_window.addstr(4,4, "e")
	my_window.refresh()
	curses.napms(2000)

	screen.clear()
	screen.refresh()
	curses.endwin()

	# screen.addstr(0, 0, "this string is printed at position (0,0)")
	# screen.addstr(3, 1, "this string is printed at position (3,1)")
	# screen.addstr(4, 4, "X")
	# screen.addstr(5, 5, "Y")



	# screen.refresh()
	# curses.napms(5000)
	# screen.clear()

	# screen.addstr(5, 5, "Y")
	# screen.addstr(5, 5, "Y")

	# screen.refresh()




	# curses.napms(5000)
	# curses.endwin()

	# print("Initialising to initialise screen.....")
	# screen = curses.initscr()
	# print("Screen initialised")
	# screen.refresh()


	# curses.napms(2000)
	# curses.endwin()


	# print("window ended")

'''



if __name__  == '__main__':
	main()