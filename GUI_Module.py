import tkinter as tk

class GUI:
    def __init__(self, callback):
        self.callback = callback

        self.root = tk.Tk()
        self.root.geometry("800x540")
        self.root.minsize(800,540)
        self.root.title("Greek String Converter")

        label = tk.Label(self.root, text="Type in some text and program will replace it with greek characters", font=('Consolas',13))
        label.pack(pady=20)

        self.textbox = tk.Text(self.root, width=75, height=20, font=('Open Sans', 16))
        self.textbox.pack()

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        button = tk.Button(button_frame, text="Convert", font=('Consolas',15), command=self.execute_callback)
        button.pack(side="left", padx=10, pady=20,)

        button2 = tk.Button(button_frame, text="Copy to clipboard", font=('Consolas',15), command=self.copy_clipboard)
        button2.pack(side="right", padx=10, pady=20)

        self.root.mainloop()

    def execute_callback(self):
        text = self.textbox.get("1.0", "end-1c")
        converted_text = self.callback(text)
        self.update_textbox(converted_text)

    def copy_clipboard(self):
        text_copy = self.textbox.get("1.0", "end-1c")
        self.root.clipboard_clear()
        self.root.clipboard_append(text_copy)


    def update_textbox(self, text):
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", text)
