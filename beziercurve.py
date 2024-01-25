import tkinter as tk

class Beziercurve:
    def __init__(self, root):
        self.root = root
        self.root.title("Bezier Curve Drawer")

        self.canvas = tk.Canvas(root, width=1280, height=960, bg="white")
        self.canvas.pack()

        self.points = []
        self.curve = None

        self.canvas.bind("<Button-1>", self.right_click)
        self.root.bind("<space>", self.space_click)

    def right_click(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red")
        
        if len(self.points) > 1:
            if self.curve:
                self.canvas.delete(self.curve)
            self.draw_bezier_curve()

    def space_click(self, event):
        self.canvas.delete("all")
        self.points = []

    def draw_bezier_curve(self):
        points = self.points
        bezier_curve = []

        for t in range(0, 101, 1):
            t = t / 100.0
            x = int(sum((self.bezier_form(t, i) * point[0] for i, point in enumerate(points))))
            y = int(sum((self.bezier_form(t, i) * point[1] for i, point in enumerate(points))))
            bezier_curve.append((x, y))

        self.curve = self.canvas.create_line(bezier_curve, fill="black")

    def binomial_coeff(self, n, k):
        if 0 <= k <= n:
            result = 1
            for i in range(1, min(k, n - k) + 1):
                result = result * (n - i + 1) // i
            return result
        else:
            return 0

    def bezier_form(self, t, i):
        #bernstein basis polynomial
        return self.binomial_coeff(len(self.points) - 1, i) * (1 - t)**(len(self.points) - 1 - i) * t**i
run = tk.Tk()
program = Beziercurve(run)
run.mainloop()