from pickle import EMPTY_LIST
import pickle
import tkinter as tk
from tkinter.constants import END, OUTSIDE, ROUND
from typing import Sequence

import classes



#Variable Declarations
filamentPrice=0
filamentMass=0
mass=0
printTime=0
designTime=0
expectedWage=0
inputs = [mass,printTime,designTime,expectedWage]

price=0
cost=0
material_cost=0
outputs=[price,cost,material_cost]

#Creating the Tkinter window and naming it
window= tk.Tk()
window.title("3D Printing Pricing")



### Insert Filament Page
#Filament Name Text
f_name_text =tk.Label(window,text="Name of Filament", font=("Helvetica 15"))
#Filament Name Entry
f_name=tk.Entry(width = 20)
#Filament Text
f_purchase=tk.Label(window,text="Filament Purchase Price in $", font=("Helvetica 15"))
#Filament Text Entry
f_purchase_price=tk.Entry(width=20)
#Filament Mass Text
f_mass_text=tk.Label(window,text="Filament Purchase Mass in g", font=("Helvetica 15"))
#Filament Text Entry
f_mass=tk.Entry(width=20)


def save_filament():
    inputted_filament= classes.filament(f_name.get(),float(f_purchase_price.get()),float(f_mass.get()))
    f_name.delete(0,END)
    f_purchase_price.delete(0,END)
    f_mass.delete(0,END)

    global saved_filaments
    saved_filaments.append(inputted_filament)
    classes.save_object(saved_filaments)

#Filament save Button
f_save_button=tk.Button(window, text="Save",command=save_filament)


###Stored Filament Page
saved_filaments=classes.load_object("data.pickle")
stored_filament_listbox=tk.Listbox(window,width=50)
stored_filament_entry=tk.Entry(width=38)
stored_filament_entry.insert(0,"Which filament # would you like to delete?")
saved_filaments_names=[]

def populate_stored_filaments(saved_filaments):
    if (len(saved_filaments) !=0):
        global saved_filaments_names
        saved_filaments_names.clear()
        stored_filament_listbox.delete(0,END)
        for i,x in enumerate(saved_filaments):
            stored_filament_listbox.insert(i,"Filament {}-- Name: {} Price: {} Mass: {}".format(i+1,x.name,x.price,x.mass))
            saved_filaments_names.append(x.name)
    else:
        stored_filament_listbox.insert("No Filaments Saved")

populate_stored_filaments(saved_filaments)

def clear_filaments():
    global saved_filaments
    if len(saved_filaments)>1:
        saved_filaments=list(classes.load_object("data.pickle"))
        del saved_filaments[int(stored_filament_entry.get())-1]
        classes.save_object(saved_filaments)
        populate_stored_filaments(saved_filaments)
    else:
        print("Need At Least One Type of Filament")


stored_filament_clear=tk.Button(window, text="Clear Filaments",command=clear_filaments)


###For Main Page
#Filament Choice Text
filament_choice_text=tk.Label(text="Type of Filament", font=("Helvetica 15"))
#Filament Choice
value_inside_filament_choice=tk.StringVar(window)
value_inside_filament_choice.set("Select an Option")
filament_choice=tk.OptionMenu(window,value_inside_filament_choice,*saved_filaments_names)

def filament_choice_reconstructor():
    global filament_choice
    global value_inside_filament_choice
    global saved_filaments_names
    global saved_filaments
    filament_choice.option_add
    populate_stored_filaments(saved_filaments)
    filament_choice.destroy()
    filament_choice = tk.OptionMenu(window,value_inside_filament_choice,*saved_filaments_names)


#Mass text
p_text_mass= tk.Label(window, text="Mass of Print in g", font=("Helvetica 15"))
#Mass Text Entry
p_mass= tk.Entry(window, width= 16)

#Print Time Text
pTime_text=tk.Label(window, text="Print Time in mins", font=("Helvetica 15"))
#Print Time Text Entry
pTime= tk.Entry(window,width=22)

#Design Time Text
dTime_text=tk.Label(window, text="Deisgn + Assembly Time in min", font=("Helvetica 15"))
#Design Time Text Entry
dTime= tk.Entry(window,width=24)

#Expected Wage Text
eWage_text=tk.Label(window, text="Expected Wage in $/hr", font=("Helvetica 15"))
#Design Time Text Entry
eWage= tk.Entry(window,width=21)

#Price Text
price_text=tk.Label(text="Price of print: $"+str(outputs[0]), font=("Helvetica 15"))
#Cost Text
cost_text=tk.Label(text="Cost of print: $"+str(outputs[1]), font=("Helvetica 15"))
#Material Cost
material_cost_text=tk.Label(text="Print's Material Cost: $"+str(outputs[2]),font=("Helvetica 15"))


#Function to get all the data from the text entries
def data_retrieval(inputs):
    inputs[0]=float(p_mass.get())
    inputs[1]=float(pTime.get())
    inputs[2]=float(dTime.get())
    inputs[3]=float(eWage.get())

#Function to calculate Cost and Price of Print   
def price_of_print(outputs):
    print("calculations Not done")
    # outputs[0]= ((inputs[0]/inputs[1])*1.5*inputs[2]) +(inputs[5]*1.25*(inputs[4])/60)+(inputs[5]*1.25/60/6*inputs[3])
    # outputs[1]=((inputs[0]/inputs[1])*inputs[2]) +(inputs[5]*inputs[4]/60)+(inputs[5]/60/6*inputs[3])
    # outputs[2]=(inputs[0]/inputs[1])*inputs[2]


#Function to call both data_retrieval and price_of_print
def button_click():
    print("Clicked")    
    # data_retrieval(inputs)
    # price_of_print(outputs)

    # price_text.configure(text="Price of print: $"+str(round(outputs[0],2)))
    # cost_text.configure(text="Cost of print: $"+str(round(outputs[1],2)))
    # material_cost_text.configure(text="Print's Material Cost: $"+str(round(outputs[2],2)))

#Enter Button 
enter_button= tk.Button(window,text="Calculate", command=button_click)




#Insert Filament Widegt Page List
insert_filament_page_list=[f_name_text,f_name,f_purchase,f_purchase_price,f_mass_text,f_mass,f_save_button]
#Insert Filament Page Instance
insert_filament_page= classes.page()
insert_filament_page.addWidget(insert_filament_page_list)

#Pricing Widegt Page List
pricing_page_list= [filament_choice_text,filament_choice,p_text_mass,p_mass,pTime_text,pTime,dTime_text,dTime,eWage_text,eWage,enter_button,price_text,cost_text,material_cost_text]
#Pricing Page Instance
pricing_page= classes.page()
pricing_page.addWidget(pricing_page_list)
pricing_page.packWidgets()

#Stored Filaments Page List
stored_filaments_page_list=[stored_filament_listbox,stored_filament_entry,stored_filament_clear]
stored_filaments_page=classes.page()
stored_filaments_page.addWidget(stored_filaments_page_list)



#Making the last page pricing page to start
last_page=pricing_page


#Go through and remove last page's widgets
def forget_last_page():
    last_page.forgetWidgets()


def main_callback():
    filament_choice_reconstructor()
    forget_last_page()
    pricing_page.packWidgets()
    global last_page
    last_page=pricing_page

def subpage_callback():
    return "Submenu"

def stored_filaments():
    global saved_filaments
    populate_stored_filaments(saved_filaments)
    forget_last_page()
    stored_filaments_page.packWidgets()
    global last_page
    last_page=stored_filaments_page

def insert_filament():
    forget_last_page()
    insert_filament_page.packWidgets()
    global last_page
    last_page=insert_filament_page

subpages=tk.Menu()
subpages.add_command(label="Filament 1", command= subpage_callback)

main=tk.Menu()
main.add_command(label="Main",command=main_callback)
#main.add_cascade(label="Filaments", menu= subpages)
main.add_command(label="Stored Filaments", command=stored_filaments)
main.add_command(label="Insert Filament", command=insert_filament)
window.configure(menu=main)



window.resizable(width= True,height=True)
window.mainloop()



