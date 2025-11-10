import tkinter as tk
r = tk.Tk()	
r.title('Naše aplikace')
r.geometry("300x600")


a = tk.Label(r, text='GeeksForGeeks.org!')
a.pack()

button = tk.Button(r, text='Stop', width=25, command=r.destroy, background="pink", activebackground="blue")
button.pack()
r.mainloop()