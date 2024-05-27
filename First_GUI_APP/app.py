from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.core.window import Window

ROWS = COLS = 3


# class GridApp(App):
#     def build(self, ):
#         root = GridLayout(rows=ROWS, cols=COLS)
#         for i in range(ROWS):
#             for j in range(COLS):
#                 root.add_widget(Button(text=f"({i}, {j})"))
#
#         return root


# class MainApp(App):
#     def build(self):
#         return GridApp()

class CanvasApp(App):
    def build(self):
        root = Widget()
        width = Window.size[0] * 0.95
        height = Window.size[1] * 0.95
        pos_x_1 = 10
        pos_y_1 = 10
        pos_x_2 = Window.size[0] - 10
        pos_y_2 = Window.size[1] - 10

        with root.canvas:
            Rectangle(size=[width, height], pos=[pos_x_1, pos_y_1])

        return root


CanvasApp().run()
