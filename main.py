from kivy.app import App
from kivy.uix.label import Label
class MainApp(App):
    def build(self):
        return Label(text='UDP APK Success!')
if __name__ == '__main__':
    MainApp().run()
