import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget 
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Config.set('graphics', 'resizable', True) 

class MyApp(App):

    def build(self):

        Window.clearcolor = (1, 0.827, 0.894, 1)

        layout = BoxLayout(orientation="vertical", padding=10)

        layout.add_widget(Label(text='[color=000000]I Wan Attention >~<',
                                markup=True))

##        attentionButton = Button(
##                    text="[color=000000]Attenshun :3",
##                    background_color="[]"
##                    )
##        urgentAttentionButton = Button(
##                    text="[color=000000]Urgent Attenshun :(((",
##                    background_color="[]"
##                    )
        busyButton = Button(
                    text="[color=000000]Im Busy >:3",
                    markup=True,
                    background_color=[1, 0, 0, 1]
                    )

        busyButton.bind(on_press=self.busy)
        
##        layout.add_widget(attentionButton)
##        layout.add_widget(urgentAttentionButton)
        layout.add_widget(busyButton)
        
        return layout

    def busy(self, event):
        self.busyButton.background_color=[0,1,1,1]


if __name__ == '__main__':
    MyApp().run()

x = 0

while True:
    x += 0.001
    print('a')
    self.busyButton.background_color=[x, x, x, x]
