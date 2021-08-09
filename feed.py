import curses
import time
from enum import Enum
import requests
from itertools import count, accumulate
from bisect import bisect_left
import statistics
import os
from dotenv import load_dotenv


load_dotenv()

node = os.environ.get('RPC_URL')

ModeNames = Enum('Modes','LATEST_FEES BOXPLOT BOXPLOT_NO_OUTLINERS FULLNESS BASE BURN MEDIAN_PRIORITY MAX_RATIO MIN_PRIORITY')
mode_keys = [ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7'), ord('8'), ord('9')]
price_string = 'nanoether per gas( Gwei per gas )'
oldest_block_depth = 200


'''
Modes.LATEST_FEES: {},
Modes.BOXPLOT: {},
Modes.BOXPLOT_NO_OUTLINERS: {},
Modes.FULLNESS: {},
Modes.BASE: {},
Modes.BURN: {},
Modes.MEDIAN_PRIORITY: {},
Modes.MAX_RATIO: {},
Modes.MIN_PRIORITY: {}

'''


mode_params = {
	
	ModeNames.LATEST_FEES: {

	},
	ModeNames.BOXPLOT: {

	},
	ModeNames.BOXPLOT_NO_OUTLINERS: {

	},
	ModeNames.FULLNESS: {

	},
	ModeNames.BASE: {

	},
	ModeNames.BURN: {

	},
	ModeNames.MEDIAN_PRIORITY: {

	},
	ModeNames.MAX_RATIO: {

	},
	ModeNames.MIN_PRIORITY: {

	}
}


block_call_ids = count();


def hex_to_int(hex_string):
	if hex_string:
		return int(hex_string, 16)
	else:
		return None




def main():






if __name__ == '__main__':
	main()