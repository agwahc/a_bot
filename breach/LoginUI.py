import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
import dir
kivy.require("1.10.1")


username = ['alpha']
password = ['beta']


class Login(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = 20
        self.spacing = 10
        Window.size = (400, 300)
        with self.canvas.before:
            self.rect = Rectangle(size=Window.size, pos=self.pos, source=dir.source('/breach/Images/silver.jpg'))
        self.add_widget(Label(text="Username: "))
        self.username = TextInput(multiline=False, write_tab=False)
        self.username.focus = True
        self.add_widget(self.username)
        self.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline=False, write_tab=False, password=True)
        self.add_widget(self.password)
        self.login = Button(text="Login", bold=True, background_color=(0, 1, 0, .9))
        self.login.bind(on_press=self.validate)
        self.add_widget(self.login)

    def validate(self, instance):
        usr = self.username.text
        pwd = self.password.text
        if usr in username and pwd in password:
            self.PopUp("Success", "Logged In!", 'OK', background_color=(0, 1, 0, .9))
        else:
            self.PopUp("Failed", "Incorrect Username or Password!", 'Try Again', background_color=(1, 0, 0, .9))

    def PopUp(self, title, msg, msg2, background_color=None):
        box = BoxLayout(orientation='vertical', padding=(10))
        box.add_widget(Label(text=msg))
        btn1 = Button(text=msg2, background_color=background_color)
        box.add_widget(btn1)
        popup = Popup(title=title, title_size=(30), title_align='center', content=box, size_hint=(None, None),
                      size=(430, 200), auto_dismiss=True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()


class LoginUI(App):
    def build(self):
        self.title = 'Login_UI'
        return Login()


if __name__ == "__main__":
    LoginUI().run()
