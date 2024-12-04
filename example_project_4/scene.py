from manim import *

class SinAnimate(Scene):
    def construct(self):
        ax=Axes(x_range=[-5,5,0.5], y_range=[-3,3,0.5], 
                x_axis_config={"numbers_to_include": np.arange(-5,5,1)}, 
                y_axis_config={"numbers_to_include": [1]})
        #ax_labels=ax.get_axis_labels(x_label="Time (t)", y_label=Tex(r"y=sin(x)"))
        ax_labels=ax.get_axis_labels()

        sin_graph = ax.plot(
            lambda x: np.sin(x),       # The sine function
            color=DARK_BLUE,                # Curve color
            x_range=[-5,5,0.5]          # Range of x for plotting
        )
        cos_graph = ax.plot(
            lambda x: np.cos(x),
            color=RED,
            x_range=[-5,5,0.5]
        )
        #sin_graph=ax.get_graph(lambda x: np.sin(2*x))
        sin_label=ax.get_graph_label(sin_graph, label="\\sin(x)", 
                                     x_val=-4.5, direction=UP*4)
        cos_label=ax.get_graph_label(cos_graph, label="\\cos(x)", 
                                     x_val=4.5, direction=DOWN*4)
        ax_group=VGroup(ax, ax_labels)
        #labels=VGroup(sin_label, cos_label)
        
        self.play(Create(ax_group), run_time=6)
        self.wait()
        self.play(Write(sin_label))
        self.play(Create(sin_graph), run_time=2)
        self.wait()
        self.play(Create(cos_graph), run_time=2)
        self.play(Write(cos_label))
        self.wait()