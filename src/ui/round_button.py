import tkinter as tk


class RoundButton(tk.Canvas):
    def __init__(self, parent, diameter, color, command=None, **kwargs):
        super().__init__(parent, width=diameter, height=diameter, highlightthickness=0, **kwargs)
        self.command = command
        self.color = color
        self.diameter = diameter
        self.bind("<Button-1>", self._on_button_click)
        self._draw_button()

    def _draw_button(self):
        self.delete("all")
        self.create_oval(0, 0, self.diameter, self.diameter, fill=self.color, outline=self.color)
        
    def _on_button_click(self, event):
        if self.command is not None:
            self.command()
