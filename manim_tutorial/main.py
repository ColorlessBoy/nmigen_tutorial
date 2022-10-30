import manim


class Positioning(manim.Scene):
    def construct(self):
        ax = manim.Axes(x_range=(-3, 4), y_range=(-3, 4))
        curve = ax.plot(lambda x: (x + 2) * x * (x - 2) / 2, color=manim.RED)
        area = ax.get_area(curve, x_range=(-2, 0))
        self.play(manim.Create(ax), manim.Create(curve))
        self.wait(2)
        self.play(manim.Create(area))
