import aspose.words as aw
import tkinter as tk

root = tk.Tk()
root.title("File Converter")
root.geometry("800x400")


def convert(event):
    doc = aw.Document(target_file.get())
    doc.save(new_file.get())
    successful_label_text.config(text="Successfully converted")


frame = tk.Frame(root, bg="white")
frame.pack(expand=True, fill=tk.BOTH)

target_file = tk.Entry(frame, foreground="black", width=75)
target_file.pack(anchor="w", expand=True, padx=(10,0), pady=(20, 0))
new_file = tk.Entry(frame, foreground="black", width=75)
new_file.pack(anchor="w", expand=True, padx=(10,0), pady=(20, 0))
successful_label_text = tk.Label(frame, text="", font=("Helvetica", 18), foreground='black', background="white", )
successful_label_text.pack(anchor="w", expand=True, padx=(10,0), pady=(20, 0))

convertButton = tk.Button(frame, text="Convert")
convertButton.bind("<Button-1>", convert)
convertButton.pack(side=tk.LEFT, expand=True, padx=10, pady=10)

root.mainloop()



