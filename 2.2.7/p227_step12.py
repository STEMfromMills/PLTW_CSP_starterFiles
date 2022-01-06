# Modifies the ping button parameters.
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", 
    command=lambda:do_command("ping"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    image=img, bg="black", activebackground="gray")
ping_btn.pack() 