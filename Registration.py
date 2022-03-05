import kivy
from kivy. app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textimport.import TextImport
from kivy.uix.button.import Button

class Childapp(GridLayout):
    def _ _init_ _(self,**kwargs):
        super(Childapp, self). _ _ init_ _()
        self.cols = 3
        self.add_widget(Label(text = 'Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)
        
            self.add_widget(Label(text = 'E-mail'))
        self.s_e-mail  = TextInput()
        self.add_widget(self.s_e-mail)
        
            self.add_widget(Label(text = 'Age'))
        self.s_age = TextInput()
        self.add_widget(self.s_age)
        
        self.press = Button(text_=_'Save')
        self.press.bind(on_press = self.save)
        self.add_widget(self.press)
        
       def click_me(self, instance):
       print( "Name is "+self_name.text)
       print( "E-mail is "+self_e-mail.text)
       print( "Age is "+self_age.text)
       print('' '')

 class parentApp(App)
       def build(self)
       return childapp()
if _ _name_ _ ==''_ _main_ _'':
    parentApp().run()