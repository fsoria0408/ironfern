import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

class MainWindow(FloatLayout):
    cocktailVol = ObjectProperty(None)
    spiritCon = ObjectProperty(None)
    cocktailCon = ObjectProperty(None)

    def btn(self):
        if self.cocktailVol.text == "" or self.cocktailCon.text == "" or self.spiritCon.text == "":
            self.volSpirit = "Error 1"
            self.volMixer = "Error 1"
        elif float(self.cocktailCon.text) >= float(self.spiritCon.text):
            self.volSpirit = "Error 2"
            self.volMixer = "Error 2"
        else:
            self.volSpirit = float(self.cocktailVol.text) * (float(self.cocktailCon.text)/float(self.spiritCon.text)) * (1 - float(self.cocktailCon.text) * 1e-2 * 0.211)/(1 - float(self.spiritCon.text) * 1e-2 * 0.211 )
            self.volMixer = float(self.cocktailVol.text) * (1 - float(self.cocktailCon.text)/float(self.spiritCon.text)) * (1 - float(self.cocktailCon.text)* 1e-2 * 0.211)
        show_popup(self)
        self.cocktailVol.text = ""
        self.spiritCon.text = ""
        self.cocktailCon.text = ""
    

class PopUpWindow(FloatLayout):
    pass

class Cocktails(App):
    def build(self):
        return MainWindow()

def show_popup(self):
    if self.volSpirit == "Error 1" or self.volMixer == "Error 1":
        show = "Please Fill All Spaces"
    elif self.volSpirit == "Error 2" or self.volMixer == "Error 2":
        show = "Cocktail Strength Must Be Smaller Than Spirit Strength"
    else:
        show = "Spirit Volume: "+str(int(round(self.volSpirit,0)))+" ml" + "   Mixer Volume: "+str(int(round(self.volMixer,0)))+" ml"
    
    poppedWindow = Popup(title="Results", content=Label(text=show), size_hint=(None,None),size=(400,400))
    
    poppedWindow.open()


if __name__ == "__main__":
    Cocktails().run()