"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
import os
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
print(os.getcwd())

with open("foo.txt") as foo:
	print(foo.read())
foo.closed
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
print("---- bar.txt ----")
# YOUR CODE HERE\
bar = open("bar.txt", "w")
bar.write("Somewhere over the rainbow\n")
bar.write("I can't remember the rest of the song\n")
bar.write("But, moooo!\n")
bar.close()

with open("bar.txt") as b:
	print(b.read())