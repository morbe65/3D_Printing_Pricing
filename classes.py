import pickle
from tkinter import Button



class filament:
    def __init__(self, name, price, mass):
        self.name = name
        self.price = price
        self.mass = mass


class page:
    def __init__(self) -> None:
        self.widgets=[]
    
    def addWidget(self,widgetName):
        self.widgets.clear()
        for i in widgetName:
            self.widgets.append(i)
    
    def packWidgets(self):
        for i in self.widgets:
            if(type(i)==Button):
                i.pack(pady=5)
            else:
                i.pack()

    def forgetWidgets(self):
        for i in self.widgets:
            i.forget()



#Used to save filament data
def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj,f,protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported): ",ex)

#Used to load filament data
def load_object(filename):
    try:
        with open(filename,"rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported): ", ex)