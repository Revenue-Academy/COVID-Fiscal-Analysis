# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:03:18 2020

@author: wb305167
"""


import matplotlib as plt
#matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure
import pandas as pd
from stata_python import *
from plot_charts import *

from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

"""
category = {'home': ['utilities','rent','cable'],
'car': ['gas','oil','repairs'],
'rv':['parks','maintenance','payment']}
"""
axis_label_list = ["GDP Constant USD","GDP Growth Rate","Revenue Deficit",
              "Government Expenditure","Total Revenue excl SC","Tax Revenue",
              "Income Taxes","Value Added Tax","Excise Taxes","Trade Taxes",
              "Non-Tax Revenue","Log GDP Constant USD", "Log GDP Per-Capita"]

#global axis_var
axis_var_list = ["GDP_Constant_USD","GDP_growth_rate","revenue_deficit",
          "neg_govt_expenditure","Total_Revenue_excl_SC","Tax_Revenue",
          "Income_Taxes","Value_Added_Tax","Excise_Taxes","Trade_Taxes",
          "Total_Non_Tax_Revenue","ln_GDP_Constant_USD","ln_GDP_PC"]
#global category_label
category_label_list = ["Value Crisis","Value Pre-crisis","Crisis Shock",
                  "Crisis Year","Turn Around Year","50% Recovery Year",
                  "75% Recovery Year","Recovery Year","50% Recovery Time",
                  "75% Recovery Time", "Full Recovery Time","None"]
category_label1 = ["None"]
#global category_var
category_var_list = ["_value_crisis","_value_pre_crisis","_crisis_shock",
                "_crisis_year","_turn_around_year","_recovery_year_1_2",
                "_recovery_year_3_4","_recovery_year","_recovery_time_1_2",
                "_recovery_time_3_4","_recovery_time",""]

#global Regions
Regions_list = ["EAP","ECA","LAC","MENA","NAM","SA","SSA","WER", "WORLD"]
#global Region_desc
Region_desc_list = ["East Asia & Pacific","Eastern Europe & Central Asia",
         "Latin America & the Caribbean","Middle East & North Africa",
         "North America","South Asia","Sub-Saharan Africa","Western Europe", "World"]  
    
def gen_label_dict(axis_label_list, axis_var_list,
                   category_label_list, category_var_list,
                   Region_desc_list, Regions_list):
    axis_var={}
    category_var={}
    region_var={}
    category_menu_mapping={}
    for i in range(len(axis_label_list)):
        axis_var[axis_label_list[i]] = axis_var_list[i]
    for i in range(len(category_label_list)):
        category_var[category_label_list[i]] = category_var_list[i]
    for i in range(len(Region_desc_list)):
        region_var[Region_desc_list[i]] = Regions_list[i]
    for i in range(len(axis_label_list)):
        if i<=10:
            category_menu_mapping[axis_label_list[i]] = category_label_list[:-1]
        else:
            category_menu_mapping[axis_label_list[i]] = category_label_list[-1]
    #print(axis_dict)
    return(axis_var,category_var,region_var,category_menu_mapping)

def gen_chart():
    global choice_x1
    global choice_x2
    global choice_y1
    global choice_y2
    global choice_grp
    choices=[choice_x1, choice_x2, choice_y1, choice_y2, choice_grp]
    print(choices)
    print(axis_var[choice_x1]+category_var[choice_x2])
    print(axis_var[choice_y1]+category_var[choice_y2])
    print(region_var[choice_grp])

    x_axis = axis_var[choice_x1]+category_var[choice_x2]
    y_axis = axis_var[choice_y1]+category_var[choice_y2]
    x_axis_label = choice_x1 + " " + choice_x2
    y_axis_label = choice_y1 + " " + choice_y2
    
    df_shock_merged = pd.read_csv("Fiscal Shocks.csv")
    
    group_selection_value = region_var[choice_grp]  
    if (group_selection_value == "WORLD"):
        selection_group = None
        selection_group_value = None
    else:
        selection_group = 'Region_Code'
        selection_group_value = group_selection_value
    
    #y_ticks=[2006,2007,2008,2009,2010,2011,2012,2013,2014]
    #if (y_axis_category_selection >=3) and (y_axis_category_selection <=7):
    
    if (choice_y2.find("Year")!=-1):
        y_decimal = 0
    else:
        y_decimal = None
    
    ax = plot_scatter_chart_df(df_shock_merged, x_axis, y_axis,
                               y_decimal = y_decimal,
                               selection_group = selection_group,
                               selection_group_value = selection_group_value,
                               label_category = 'Country_Code',
                               x_axis_label=x_axis_label,
                               y_axis_label=y_axis_label,
                               color="b", marker=".")
    plt.show()
    #filename='pic.png'
    #plt.savefig('C:/Users/wb305167/Documents/python/Tax-Revenue-Analysis/' + filename, dpi=300)
   #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    #img = ImageTk.PhotoImage(Image.open(filename))    
    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    #picture = Label(image = img)
    #picture.pack()    
    #picture.grid(row=1, column=5, sticky = W, pady = (0,0), padx = (0,0))
    #canvas_for_image = Canvas(bg='green', height=400, width=400, borderwidth=0, highlightthickness=0)
    #canvas_for_image.grid(row=0, column=5, sticky='nesw', padx=0, pady=0)

    # create image from image location resize it to 200X200 and put in on canvas
    #image = Image.open(filename)
    #canvas_for_image.image = ImageTk.PhotoImage(image.resize((400, 400), Image.ANTIALIAS))
    #canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')


def callback_x1(*args):
    #choice_x1 = value_x1.get()
    global choice_x1
    choice_x1 = str(cb1.get())
    cb2['values'] = category_menu_mapping[cb1.get()]
    print('choice_x1: ', choice_x1)
def callback_x2(*args):
    #choice_x1 = value_x1.get()
    global choice_x2
    choice_x2 = str(cb2.get())
    print('choice_x2: ', choice_x2)
def callback_y1(*args):
    #choice_x1 = value_x1.get()
    global choice_y1
    choice_y1 = str(cb3.get())
    cb4['values'] = category_menu_mapping[cb3.get()]
    #print('choice_y1: ', choice_y1) 
def callback_y2(*args):
    #choice_x1 = value_x1.get()
    global choice_y2
    choice_y2 = str(cb4.get())
    #print('choice_y2: ', choice_y2)    
def callback_grp(*args):
    #choice_x1 = value_x1.get()
    global choice_grp
    choice_grp = str(GroupCombo.get())
    #print('choice_grp: ', choice_grp)

"""   
global choice_x1
global choice_x2
global choice_y1
global choice_y2
global choice_grp

global x1
global x2
global y1
global y2
global grp
"""
global axis_var
global category_var
global region_var
global category_menu_mapping

win =Tk()
win.geometry('1000x600')
#win.title('Understanding the Financial Crisis - Growth and Fiscal Response')

(axis_var,category_var,region_var,category_menu_mapping) = gen_label_dict(axis_label_list, axis_var_list,
                                                           category_label_list, category_var_list,
                                                           Region_desc_list, Regions_list)
        
x1 = StringVar()
x1.trace("w", callback_x1)
x2 = StringVar()
x2.trace("w", callback_x2)
y1 = StringVar()
y1.trace("w", callback_y1)
y2 = StringVar()
y2.trace("w", callback_y2)
grp = StringVar()
grp.trace("w", callback_grp)

#value = StringVar()
#value.trace('w', calback)
#choice1=StringVar()
#choice2=StringVar()
#Label(text = 'Combo Box #1:').grid(row = 2,column = 1,padx = 10)
#Label(text = 'Combo Box #2:').grid(row = 4,column = 1,padx = 10)

l0=Label(text="Fiscal Analysis of the 2008-09 Financial Crisis",
         font = "Calibri 12 bold")
#l0.grid(row=0, column=1, columnspan=3)
l0.grid(row=0, column=1, columnspan=3)

l1=Label(text="Choose The x-axis, y-axis and Category")
l1.grid(row=1, column=0, sticky = W, pady = (10,25), padx = (10,0), columnspan=5)
l2=Label(text="x-axis: ")
l2.grid(row=2, column=0, sticky = W, pady = (0,25), padx = (10,0))
l41=Label(text="category: ")
l41.grid(row=2, column=2, sticky = W, pady = (0,25), padx = (10,0))
l3=Label(text="y-axis: ")
l3.grid(row=3, column=0, sticky = W, pady = (0,25), padx = (10,0))
l42=Label(text="category: ")
l42.grid(row=3, column=2, sticky = W, pady = (0,25), padx = (10,0))
l5=Label(text="Group: ")
l5.grid(row=4, column=0, sticky = W, pady = (0,25), padx = (10,0))              
button = ttk.Button(text = "Create Chart", command=gen_chart)
#button.pack()
button.grid(row=6, column=1, sticky = W, pady = (0,25), padx = (0,0))    
#button.place(x=0, y=0)           
#Label(text = 'Combo Box #3:').place(x=10, y=200)
cb2 = ttk.Combobox(width = 15, textvariable=x2)
cb2.grid(row = 2,column = 3, sticky = W, pady = (0,25), padx = (0,0))
#AccountCombox.grid(row = 5,column = 1,pady = 25,padx = 10)
cb4 = ttk.Combobox(width = 15, textvariable=y2)
cb4.grid(row=3, column=3, sticky = W, pady = (0,25), padx = (0,0))

cb1 = ttk.Combobox(width = 15,  values = list(category_menu_mapping.keys()), textvariable=x1)
cb1.grid(row=2, column=1, sticky = W, pady = (0,25), padx=(0, 0))
cb3 = ttk.Combobox(width = 15,  values = list(category_menu_mapping.keys()), textvariable=y1)
cb3.grid(row=3, column=1,  sticky = W, pady = (0,25), padx=(0, 0))
#choice1.trace("w", on_field_change)    
GroupCombo = ttk.Combobox(width = 15,  values = Region_desc_list, textvariable=grp)
GroupCombo.grid(row=4, column=1,  sticky = W, pady=(0,25), padx=(0, 0))

#CategoryCombox.bind('<<ComboboxSelected>>', getUpdateData_x1)
    

#print(app.choices)
win.mainloop()