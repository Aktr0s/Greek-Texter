import tkinter as tk

class GUI:
    def __init__(self, callback):
        self.callback = callback

        self.root = tk.Tk()
        self.root.geometry("1000x650")
        self.root.title("Greek String Converter")

        label = tk.Label(self.root, text="Type in some text and program will replace it with greek characters", font=('Consolas',13))
        label.pack(pady=20)

        self.textbox = tk.Text(self.root, width=75, height=20, font=('Open Sans', 16))
        self.textbox.pack()

        button = tk.Button(self.root, text="Convert", font=('Consolas',15), command=self.execute_callback)
        button.pack(pady=20)

        self.root.mainloop()

    def execute_callback(self):
        text = self.textbox.get("1.0", "end-1c")
        converted_text = self.callback(text)
        self.update_textbox(converted_text)

    def update_textbox(self, text):
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", text)
