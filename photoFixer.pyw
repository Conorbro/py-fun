import sys, os
from Tkinter import *
import tkMessageBox

root = Tk()
textBox = Entry(root, width=40)
textBox.pack()

class Photo_Recovery:

	def __init__(self):
		button = Button(root, text='Recover Photos', width=40, command = self.fixPhotos).pack()
		root.title("Corrupt Photo Recovery")

	def fixPhotos(self):

		directory = textBox.get();
		count = 0

		for filename in os.listdir(directory):
			path = os.path.join(directory, filename)
			target = os.path.join(directory, 'Photo' + str(count) + '.jpg')
			os.rename(path, target)
			count += 1

		tkMessageBox.showinfo('Success!', str(count) + ' photos potentially reovered!')


program = Photo_Recovery()
root.mainloop()
