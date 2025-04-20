from tkinter import Tk, Canvas as TkCanvas

class Canvas:
    def __init__(self, width, height):
        self.root = Tk()
        self.canvas = TkCanvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.last_click = None
        self.mouse_x = 0
        self.mouse_y = 0
        self.canvas.bind("<Button-1>", self._click)
        self.canvas.bind("<Motion>", self._motion)
        self.root.update()

    def _click(self, event):
        self.last_click = (event.x, event.y)

    def _motion(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def moveto(self, shape_id, x, y):
        coords = self.canvas.coords(shape_id)
        width = coords[2] - coords[0]
        height = coords[3] - coords[1]
        self.canvas.coords(shape_id, x, y, x + width, y + height)
        self.root.update()

    def set_color(self, shape_id, color):
        self.canvas.itemconfig(shape_id, fill=color)
        self.root.update()

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def get_mouse_x(self):
        return self.mouse_x

    def get_mouse_y(self):
        return self.mouse_y

    def wait_for_click(self):
        while self.last_click is None:
            self.root.update()

    def get_last_click(self):
        return self.last_click
