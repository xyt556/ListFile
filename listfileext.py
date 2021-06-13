#!/usr/bin/env python

#
# Imports
#

import os
import sys

#
# Setup
#

skip_hidden_items = True

file_extensions = []

# Get current directory
# @see https://docs.python.org/2/tutorial/stdlib.html#operating-system-interface
path = os.getcwd()

#
# User input
#

# Get command line arguments
# @see https://docs.python.org/2/tutorial/stdlib.html#command-line-arguments
user_input = sys.argv

# Check user input
if ( len(user_input) >= 2 ) :
	if ( user_input[1].index("/") == 0 ):
		path = user_input[1]
	else:
		print("Error: Not a correct path, it has to start with a slash '/'")
		exit()

#
# Search for files
#

def get_items(path):
	items = os.listdir(path)

	for item in items:
		item_path = path + "/" + item

		if not ( skip_hidden_items and item.startswith( "." ) ):
			# Check if item is file or directory and search recursivly
			if ( os.path.isfile(item_path) ):
				# Get file extension
				extension = item[item.rfind("."):]

				# Check if filee extension is already listet or add
				if ( extension not in file_extensions ):
					file_extensions.append(extension)
			else:
				get_items(item_path)

# Start searching
get_items(path)

#
# Print file types
#

file_extensions.sort()

for extension in file_extensions:
	print(extension)