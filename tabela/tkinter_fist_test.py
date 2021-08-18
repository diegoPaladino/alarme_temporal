# tkinter_fist_test
# source: https://www.python-course.eu/tkinter_text_widget.php

import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "Just a text Widget\nin two lines\n")
tk.mainloop()


# #############################################################

# import tkinter as tk

# root = tk.Tk()
# T = tk.Text(root, height=10, width=30)
# T.pack()
# quote = """HAMLET: To be, or not to be--that is the question:
# Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune
# Or to take arms against a sea of troubles
# And by opposing end them. To die, to sleep--
# No more--and by a sleep to say we end
# The heartache, and the thousand natural shocks
# That flesh is heir to. 'Tis a consummation
# Devoutly to be wished."""
# T.insert(tk.END, quote)
# tk.mainloop()