# Daniel Burnier
# kivy.Spinner test
# TPI
# 09.03.20

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.lang import Builder
from os import listdir

DEBUG = False

Builder.load_string('''

<mycls>:
    FloatLayout:
        id: layout
        Spinner:
            id: 'spin'
            size_hint: None, None
            size: 200, 44
            pos: (layout.center_x - self.width/2, 0)
            text: 'Music'
            values: root.musList
            on_text: root.showselection(self.text)
''')

class mycls(FloatLayout):

    musDir = r'C:\Users\danburnier\Desktop\PythonPrograms'
    musList = listdir(musDir)

    def showselection(self,textt):
        print(textt)

class mineapp(App):
    def build(self):
        return mycls()

if __name__ == '__main__':
    mineapp().run()