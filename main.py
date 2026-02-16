from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        return Label(text="Hello! APK built on GitHub Actions.", font_size='24sp', color=(1,1,1,1))

if __name__ == "__main__":
    MyApp().run()
