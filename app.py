import pickle
import tkinter as tk
from os import name, path
from pickle import EMPTY_LIST
from tkinter.constants import COMMAND, END, GROOVE, LEFT, OUTSIDE, ROUND
from typing import Sequence
from ttkbootstrap import Style

import classes
from invoiceGenerator import invoiceGenerator

##Variable Declarations
#Input Variables
mass=0
printTime=0
designTime=0
expectedWage=0
inputs = [mass,printTime,designTime,expectedWage]

#Output Varaibles
price=0
cost=0
material_cost=0
outputs=[price,cost,material_cost]

#Creating Bootstrap stuff
style=Style(theme="darkly")

#Creating the Tkinter window and naming it
window= style.master
window.iconbitmap('LookOut.ico')
window.title("3D Printing Invoices")




### Insert Filament Page
#Filament Name Text
f_name_text =tk.Label(window,text="Name of Filament")
#Filament Name Entry
f_name=tk.Entry(width = 20,justify=tk.LEFT)
#Filament Text
f_purchase=tk.Label(window,text="Filament Purchase Price in $")
#Filament Text Entry
f_purchase_price=tk.Entry(width=20,font="Arial 12")
#Filament Mass Text
f_mass_text=tk.Label(window,text="Filament Purchase Mass in g")
#Filament Text Entry
f_mass=tk.Entry(width=20)

#Saving inputed filament to data.pickle and list
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
stored_filament_listbox=tk.Listbox(window,width=75,height=10)
stored_filament_entry=tk.Entry(width=39)
stored_filament_entry.insert(0,"Which filament # would you like to delete?")
saved_filaments_names=[]

#Going through and updating saved filaments list
def populate_stored_filaments(saved_filaments):
    if (len(saved_filaments) !=0):
        global saved_filaments_names
        saved_filaments_names.clear()
        stored_filament_listbox.delete(0,END)
        for i,x in enumerate(saved_filaments):
            stored_filament_listbox.insert(i,"Filament {} -- Name: {} -- Price: {} -- Mass: {}".format(i+1,x.name,x.price,x.mass))
            saved_filaments_names.append(x.name)
    else:
        stored_filament_listbox.insert("No Filaments Saved")

#Original Update
populate_stored_filaments(saved_filaments)

#Getting rid of filaments
def clear_filaments():
    global saved_filaments
    if len(saved_filaments)>1:
        saved_filaments=list(classes.load_object("data.pickle"))
        del saved_filaments[int(stored_filament_entry.get())-1]
        classes.save_object(saved_filaments)
        populate_stored_filaments(saved_filaments)
    else:
        print("Need At Least One Type of Filament")
    stored_filament_entry.delete(0,END)

#Clear filaments button
stored_filament_clear=tk.Button(window, text="Clear Filaments",command=clear_filaments)


###For Main Page
#Filament Choice Text
filament_choice_text=tk.Label(text="Type of Filament")
#Filament Choice
value_inside_filament_choice=tk.StringVar(window)
value_inside_filament_choice.set("Select an Option")
filament_choice=tk.OptionMenu(window,value_inside_filament_choice,*saved_filaments_names)
filament_choice.configure(borderwidth=0)


# I have no clue how this function works
def filament_choice_reconstructor():
    global filament_choice
    global value_inside_filament_choice
    global saved_filaments_names
    global saved_filaments
    filament_choice['menu'].delete(0,END)
    populate_stored_filaments(saved_filaments)
    for choices in saved_filaments_names:
        filament_choice['menu'].add_command(label=choices, command= tk._setit(value_inside_filament_choice,choices))


#Mass text
p_text_mass= tk.Label(window, text="Mass of Print in g")
#Mass Text Entry
p_mass= tk.Entry(window, width= 16)

#Print Time Text
pTime_text=tk.Label(window, text="Print Time in mins")
#Print Time Text Entry
pTime= tk.Entry(window,width=22)

#Design Time Text
dTime_text=tk.Label(window, text="Deisgn + Assembly Time in min")
#Design Time Text Entry
dTime= tk.Entry(window,width=24)

#Expected Wage Text
eWage_text=tk.Label(window, text="Expected Wage in $/hr")
#Design Time Text Entry
eWage= tk.Entry(window,width=21)

#Price Text
price_text=tk.Label(text="Price of print: $"+str(outputs[0]))
#Cost Text
cost_text=tk.Label(text="Cost of print: $"+str(outputs[1]))
#Material Cost
material_cost_text=tk.Label(text="Material cost of print: $"+str(outputs[2]))


#Function to get all the data from the text entries
def data_retrieval(inputs):
    inputs[0]=float(p_mass.get()) # Print Mass
    inputs[1]=float(pTime.get()) # Print Time
    inputs[2]=float(dTime.get()) # Deisgn + Assembly Time
    inputs[3]=float(eWage.get()) # Expected Wage

#Function to calculate Cost and Price of Print  
# outputs[0]= Price
# outputs[1]= Cost
# outputs[2]= Material Cost
def price_of_print(outputs):
    print("calculations Not done")
    print(value_inside_filament_choice.get())

    for i,x in enumerate(saved_filaments):
        if saved_filaments[i].name == value_inside_filament_choice.get():
            option=i


    outputs[0]= ((saved_filaments[option].price/saved_filaments[option].mass)*1.5*inputs[0]) +(inputs[3]*1.25*(inputs[2])/60)+(inputs[3]*1.25/60/6*inputs[1])
    outputs[1]=((saved_filaments[option].price/saved_filaments[option].mass)*inputs[0]) +(inputs[3]*inputs[2]/60)+(inputs[3]/60/6*inputs[1])
    outputs[2]=(saved_filaments[option].price/saved_filaments[option].mass)*inputs[0]


#Function to call both data_retrieval and price_of_print
def button_click():
    print("Clicked")    
    data_retrieval(inputs)
    price_of_print(outputs)

    price_text.configure(text="Price of print: ${:.2f}".format(outputs[0]))
    cost_text.configure(text="Cost of print: ${:.2f}".format(outputs[0]))
    material_cost_text.configure(text="Material cost of print: ${:.2f}".format(outputs[0]))
    global pricing_page
    pricing_page.addWidget(pricing_page_list2)
    pricing_page.packWidgets()


#Enter Button 
enter_button= tk.Button(window,text="Calculate", command=button_click)

#Name of Project
name_of_project_text=tk.Label(text="Name of Project")
name_of_project_entry=tk.Entry()

#Name of Client
name_of_client_text=tk.Label(text="Name of Client")
name_of_client_entry=tk.Entry()

#Generate Invoice Button
def generate_customer_invoice():
    invoiceGenerator(name_of_client_entry.get(),name_of_project_entry.get(), outputs[0]).generate()

generateInvoice= tk.Button(text="Generate Invoice",command=generate_customer_invoice)




#Insert Filament Widegt Page List
insert_filament_page_list=[f_name_text,f_name,f_purchase,f_purchase_price,f_mass_text,f_mass,f_save_button]
#Insert Filament Page Instance
insert_filament_page= classes.page()
insert_filament_page.addWidget(insert_filament_page_list)

#Pricing Widegt Page List
pricing_page_list= [filament_choice_text,filament_choice,p_text_mass,p_mass,pTime_text,pTime,dTime_text,dTime,eWage_text,eWage,enter_button,price_text,cost_text,material_cost_text]
pricing_page_list2= [filament_choice_text,filament_choice,p_text_mass,p_mass,pTime_text,pTime,dTime_text,dTime,eWage_text,eWage,enter_button,price_text,cost_text,material_cost_text,name_of_project_text,name_of_project_entry,name_of_client_text,name_of_client_entry,generateInvoice]
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
    pricing_page.addWidget(pricing_page_list)
    pricing_page.packWidgets()
    filament_choice_reconstructor()
    forget_last_page()
    pricing_page.packWidgets()
    global last_page
    last_page=pricing_page

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


main=tk.Menu()
main.add_command(label="Pricer/Invoicer",command=main_callback)


main.add_command(label="Stored Filaments", command=stored_filaments)
main.add_command(label="Insert Filament", command=insert_filament)
window.configure(menu=main)



window.resizable(width= True,height=True)
window.mainloop()



