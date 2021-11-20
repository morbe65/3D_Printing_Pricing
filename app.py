import tkinter as tk
from tkinter.constants import OUTSIDE, ROUND
from typing import Sequence

import classes



#Variable Declarations
filamentPrice=0
filamentMass=0
mass=0
printTime=0
designTime=0
expectedWage=0
inputs = [filamentPrice,filamentMass,mass,printTime,designTime,expectedWage]

price=0
cost=0
material_cost=0
outputs=[price,cost,material_cost]

#Creating the Tkinter window and naming it
window= tk.Tk()
window.title("3D Printing Pricing")


#Filament Text
f_purchase=tk.Label(window,text="Filament Purchase Price in $", font=("Helvetica 15 underline"))
#Filament Text Entry
f_purchase_price=tk.Entry(width=20)

#Filament Mass Text
f_mass_text=tk.Label(window,text="Filament Purchase Mass in g", font=("Helvetica 15 underline"))
#Filament Text Entry
f_mass=tk.Entry(width=23)


#Mass text
p_text_mass= tk.Label(window, text="Mass of Print in g", font=("Helvetica 15 underline"))
#Mass Text Entry
p_mass= tk.Entry(window, width= 16)

#Print Time Text
pTime_text=tk.Label(window, text="Print Time in mins", font=("Helvetica 15 underline"))
pTime_text.pack()
#Print Time Text Entry
pTime= tk.Entry(window,width=22)
pTime.pack()

#Design Time Text
dTime_text=tk.Label(window, text="Deisgn +Assembly Time in min", font=("Helvetica 15 underline"))
dTime_text.pack()
#Design Time Text Entry
dTime= tk.Entry(window,width=24)
dTime.pack()

#Expected Wage Text
eWage_text=tk.Label(window, text="Expected Wage in $/hr", font=("Helvetica 15 underline"))
eWage_text.pack()
#Design Time Text Entry
eWage= tk.Entry(window,width=21)
eWage.pack()

#Price Text
price_text=tk.Label(text="Price of print: $"+str(outputs[0]), font=("Helvetica 15"))
#Cost Text
cost_text=tk.Label(text="Cost of print: $"+str(outputs[1]), font=("Helvetica 15"))
#Material Cost
material_cost_text=tk.Label(text="Print's Material Cost: $"+str(outputs[2]),font=("Helvetica 15"))


#Function to get all the data from the text entries
def data_retrieval(inputs):
    inputs[0]=float(f_purchase_price.get())
    inputs[1]=float(f_mass.get())
    inputs[2]=float(p_mass.get())
    inputs[3]=float(pTime.get())
    inputs[4]=float(dTime.get())
    inputs[5]=float(eWage.get())
    
#Function to calculate Cost and Price of Print   
def price_of_print(outputs):
    outputs[0]= ((inputs[0]/inputs[1])*1.5*inputs[2]) +(inputs[5]*1.25*(inputs[4])/60)+(inputs[5]*1.25/60/6*inputs[3])
    outputs[1]=((inputs[0]/inputs[1])*inputs[2]) +(inputs[5]*inputs[4]/60)+(inputs[5]/60/6*inputs[3])
    outputs[2]=(inputs[0]/inputs[1])*inputs[2]


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
enter_button.pack()

price_text.pack()
cost_text.pack()
material_cost_text.pack()

insert_filament_page_list=[f_purchase,f_purchase_price,f_mass_text,f_mass]
insert_filament_page= classes.page()
insert_filament_page.addWidget(insert_filament_page_list)




pricing_page_list= [p_text_mass,p_mass,pTime_text,pTime,dTime_text,dTime,eWage_text,eWage,price_text,cost_text,material_cost_text]
pricing_page= classes.page()
pricing_page.addWidget(pricing_page_list)

last_page=pricing_page


def forget_last_page():
    last_page.forgetWidgets()


def main_callback():
    return "Menu"
def subpage_callback():
    return "Submenu"
def stored_filaments():
    print("stored")
    return "Stored"
def insert_filament():
    forget_last_page()
    insert_filament_page.packWidgets()
    global last_page
    last_page=insert_filament_page

print(last_page)
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



