from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

class StackLayoutExample(StackLayout):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      b = Button(text='Z', size_hint =(.2,.2))
      self.add_widget(b)

#class GridLayoutExample(GridLayout):
#   pass

class AnchorLayoutExample(AnchorLayout):
   pass


class BoxLayoutExample(BoxLayout):
  pass
  '''  def __init__(self, **kwargs):
        super().__init__(**kwargs)


        b1 = Button(text="A")
        b2 = Button(text="B")


        self.add_widget(b1)
        self.add_widget(b2) '''

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()