'''
Nom: Burnier Daniel
Date: 03.03.2020
Description programme:  Menu déroulant pour la sélection de musique
                        pour un piano automatique
'''
 
DEBUG = True

from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.lang import Builder
from os import listdir

class DropDownTest(FloatLayout):
    def __init__(self, **kwargs):
        super(DropDownTest, self).__init__(**kwargs)
        self.size_hint = (1,1)
        
    def createdd(self):
        self.dropdown = DropDown()
        musDir = listdir(r'/home/pi/Desktop/Music21/midi')
        for file in musDir:
            if file.endswith('.mid'):
                btn = Button(text=str(file[:-4]),size_hint_y=None,height=44)
                btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
                self.dropdown.add_widget(btn)
        mainbutton = Button(text='Liste Chansons', size_hint=(0.33, 0.1), 
                            on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: DropDownTest.returnitnow(mainbutton,x))
        self.add_widget(mainbutton)

    def returnitnow(inst,txt):
        
        setattr(inst, 'text', txt)
        if DEBUG:
            print(txt+'.mid')
        return txt+'.mid'

class DropDownApp(App):

    def build(self):
        self.ddtest = DropDownTest()
        self.ddtest.createdd()
        return self.ddtest

if __name__ == '__main__':
    DropDownApp().run()