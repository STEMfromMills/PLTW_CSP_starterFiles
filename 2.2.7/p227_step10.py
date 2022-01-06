# Modify the do_command(command) function: 
#   to use the text box for input to the functions
global command_textbox, url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    # use url_val 
    p = subprocess.Popen(command + ' ::1', stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2