#################################################################################
#   p227_TR_possible_solution.py
#   Example Solution:
#     Will run in code editor but ping, tracert, and nslookup
#     commands will not execute
################################################################################
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

#edits to this come from steps 9 and 10
def do_command(command):
    global command_textbox, url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

#save comes from step 11
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# set up button to run the do_command function
#Code to make the command button pass it's name to a function using lambda
#this portion will come from steps 8-10
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command("ping -c 10"))
ping_btn.pack()

trace_btn = tk.Button(frame, text="Trace route to website", command=lambda:do_command("traceroute"))
trace_btn.pack()

nslookup_btn = tk.Button(frame, text="Check the IP address of a website", command=lambda:do_command("nslookup"))
nslookup_btn.pack()

nslookup_btn = tk.Button(frame, text="Save", command=lambda:mSave())
nslookup_btn.pack()


#ping_btn.pack()

#create the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label, this comes from step 12
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)



frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

#this comes from step 6
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()


root.mainloop()