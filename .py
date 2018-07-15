from tkinter import*
import random
import time;

root = Tk()
root.geometry("1366x760+0+0")
root.title("Restaurant Management Systems")

textInput=StringVar()
operator=""
#frame
Tops = Frame(root, width= 1366, relief= SUNKEN)
Tops.pack(side=TOP)

f1= Frame(root, width = 700, height= 750,  relief= SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width =300, height= 700,  relief= SUNKEN)
f2.pack(side= RIGHT)
#time
localtime = time.asctime(time.localtime(time.time()))
#title
lblInfo= Label(Tops, font=('verdana', 30, 'bold'),text= "Welcome to Restaurant management software", fg="dark red", bd=10, anchor = 'w')
lblInfo.grid(row=0, column=0)
lblInfo= Label(Tops, font=('verdana', 30, 'bold'),text= localtime, fg="orange", bd=10, anchor = 'w')
lblInfo.grid(row=1 , column=0)

#===============calculator=======================================

def btnClick(numbers):
    global operator
    operator= operator+str(numbers)
    textInput.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    textInput.set("")

def btnEqualInput():
    global operator
    sumup= str(eval(operator))
    
    textInput.set(sumup)
    operator=""
    
"""""""""
def btnPercentage():
    per= str((operator)/100)
    global operator
    operator=""
    textInput.set(per)
"""""""""
#=================================== Restaurant billing======================#

def Ref():
    x= random.randint(208, 1111119)
    randomRef= str(x)
    rand.set(randomRef)

    FriesCost= float(Fries.get())
    BurgerCost = float(Burger.get())
    ChickenCost = float(Chicken.get())
    SandwichCost=float(Sandwich.get())
    VegetablesCost=float(Vegetables.get())
    ComboMeal_1Cost=float(ComboMeal_1.get())
    ComboMeal_2Cost= float(ComboMeal_2.get())
    JuiceCost=float(Juice.get())
    CoffeeCost=float(Coffee.get())
    
    
    CostFries= FriesCost * 30
    CostBurger= BurgerCost * 80
    CostChicken= ChickenCost *  70
    CostSandwich= SandwichCost * 60
    CostVegetables = VegetablesCost * 40
    CostComboMeal_1= ComboMeal_1Cost * 180
    CostComboMeal_2= ComboMeal_2Cost * 280
    CostJuice= JuiceCost * 50
    CostCoffee= CoffeeCost * 40

    CostofMeal = str('%.2f' %(CostFries+CostBurger+CostChicken+CostSandwich+CostVegetables+CostComboMeal_1+CostComboMeal_2+CostJuice+CostCoffee)), "Taka"
    
    PayTax = ((CostFries+CostBurger+CostChicken+CostSandwich+CostVegetables+CostComboMeal_1+CostComboMeal_2+CostJuice+CostCoffee)* (15/100))
    abc= (CostFries+CostBurger+CostChicken+CostSandwich+CostVegetables+CostComboMeal_1+CostComboMeal_2+CostJuice+CostCoffee)
    Ser_Charge= ((CostFries+CostBurger+CostChicken+CostSandwich+CostVegetables+CostComboMeal_1+CostComboMeal_2+CostJuice+CostCoffee)/99)
    new_ser =(abc+ PayTax+ Ser_Charge)
    Service= str('%.2f' %(Ser_Charge)), "Taka" 
    
    PaidTax= str('%.2f'%(PayTax)), "Taka"
    allCost= str('%.2f' %(new_ser)), "Taka"
    TotalCost.set(allCost)
    Services.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    
    

    

    

def Exit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Chicken.set("")
    Sandwich.set("")
    Vegetables.set("")
    ComboMeal_1.set("")
    ComboMeal_2.set("")
    Juice.set("")
    Coffee.set("")
    Cost.set("")
    Services.set("")
    Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
        
    
    
    
txtDisplay = Entry(f2, font=('arial', 20,'bold'), textvariable= textInput, bd=30, insertwidth= 4, bg="blue", justify= 'right')
txtDisplay.grid(columnspan= 4)

btn7=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="7", bg="powder blue", command= lambda:btnClick(7)).grid(row=3,column=0)
btn8=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="8", bg="powder blue", command= lambda:btnClick(8)).grid(row=3,column=1)
btn9=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="9", bg="powder blue", command= lambda:btnClick(9)).grid(row=3,column=2)  
addition=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="+", bg="powder blue", command= lambda:btnClick('+')).grid(row=3,column=3)

btn4=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="4", bg="powder blue", command= lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="5", bg="powder blue", command= lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="6", bg="powder blue", command= lambda:btnClick(6)).grid(row=2,column=2)  
subtraction=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="-", bg="powder blue", command= lambda:btnClick('-')).grid(row=2,column=3)

btn1=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="1", bg="powder blue", command= lambda:btnClick(1)).grid(row=1,column=0)
btn2=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="2", bg="powder blue", command= lambda:btnClick(2)).grid(row=1,column=1)
btn3=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="3", bg="powder blue", command= lambda:btnClick(3)).grid(row=1,column=2)  
multiply=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="*", bg="powder blue", command= lambda:btnClick('*')).grid(row=1,column=3)

btn0=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="0", bg="powder blue", command= lambda:btnClick(0)).grid(row=4,column=0)
dot=Button(f2, padx=18, pady=18, bd= 9, fg= "black", font= ('arial', 20,'bold'), text=".", bg="powder blue", command= lambda:btnClick('.')).grid(row=4,column=1)
equal=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="=", bg="powder blue", command= btnEqualInput).grid(row=4,column=2)  
division=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 20,'bold'), text="/", bg="powder blue", command= lambda:btnClick('/')).grid(row=4,column=3)


clear=Button(f2, padx=16, pady=16, bd= 8, fg= "black", font= ('arial', 18,'bold'), text="C", bg="powder blue", command=lambda:btnClearDisplay()).grid(row=5,column=0)
percent= Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 19, 'bold'), text="%", bg="powder blue", command = lambda:btnClick('%')).grid (row=5, column=1)
reset= Button(f2, padx=16, pady=16, bd=8, fg= "black", font= ('arial',15, 'bold' ), text="RE", bg= "powder blue", command=lambda:btnClearDisplay()).grid(row=5, column=2)
plusMinus= Button(f2, padx= 16, pady= 16, bd= 8, fg="black", font=('arial', 16, 'bold'), text= "+/-", bg= "powder blue").grid(row=5, column= 3)
#==========Calculator ends====================

#=============================Restaurant products=======

rand= StringVar()
Fries= StringVar()
Burger=StringVar()
Chicken= StringVar()
Sandwich=StringVar()
Vegetables=StringVar()
ComboMeal_1=StringVar()
ComboMeal_2=StringVar()
Juice=StringVar()
Coffee=StringVar()
Cost= StringVar()
Services= StringVar()
Tax= StringVar()
SubTotal= StringVar()
TotalCost= StringVar()

lblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0,  column=0)
txtReference=Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10,  insertwidth=4, bg= "powder blue", justify= 'right')
txtReference.grid(row=0, column=1)

lblFries = Label(f1, font=('arial', 16, 'bold'), text="Fries", bd=16, anchor='w')
lblFries.grid(row=1,  column=0)
txtFries=Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10,  insertwidth=4, bg= "powder blue", justify= 'right')
txtFries.grid(row=1, column=1)

lblBurger = Label(f1, font=('arial', 16, 'bold'), text="Burger", bd=16, anchor='w')
lblBurger.grid(row=2,  column=0)
txtBurger=Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10,  insertwidth=4, bg= "powder blue", justify= 'right')
txtBurger.grid(row=2, column=1)

lblChicken = Label(f1, font=('arial', 16, 'bold'), text="Chicken", bd=16, anchor='w')
lblChicken.grid(row=3,  column=0)
txtChicken=Entry(f1, font=('arial', 16, 'bold'), textvariable=Chicken, bd=10,  insertwidth=4, bg= "powder blue", justify= 'right')
txtChicken.grid(row=3, column=1)

lblSandwich = Label(f1, font=('arial', 16, 'bold'), text="Sandwich", bd=16, anchor='w')
lblSandwich.grid(row=4,  column=0)
txtSandwich=Entry(f1, font=('arial', 16, 'bold'), textvariable=Sandwich, bd=10,  insertwidth=4, bg= "powder blue", justify= 'right')
txtSandwich.grid(row=4, column=1)

lblVegetables = Label(f1, font=('arial', 16, 'bold'), text="Vegetables", bd=16, anchor='w')
lblVegetables.grid(row=5,  column=0)
txtVegetables=Entry(f1, font=('arial', 16, 'bold'), textvariable=Vegetables, bd=10,  insertwidth=4, bg= "powder blue", justify= 'right')
txtVegetables.grid(row=5, column=1)

lblComboMeal_1 = Label(f1, font=('arial', 16, 'bold'), text="Combo Meal 1", bd=16, anchor='w')
lblComboMeal_1.grid(row=6,  column=0)
txtComboMeal_1=Entry(f1, font=('arial', 16, 'bold'), textvariable=ComboMeal_1, bd=10,  insertwidth=4, bg= "powder blue", justify= 'right')
txtComboMeal_1.grid(row=6, column=1)

lblComboMeal_2 = Label(f1, font=('arial', 16, 'bold'), text="Combo Meal 2", bd=16, anchor='w')
lblComboMeal_2.grid(row=7,  column=0)
txtComboMeal_2=Entry(f1, font=('arial', 16, 'bold'), textvariable=ComboMeal_2, bd=10,  insertwidth=4, bg= "powder blue", justify= 'right')
txtComboMeal_2.grid(row=7, column=1)

lblJuice = Label(f1, font=('arial', 16, 'bold'), text="Juice", bd=16, anchor='w')
lblJuice.grid(row=8,  column=0)
txtJuice=Entry(f1, font=('arial', 16, 'bold'), textvariable=Juice, bd=10,  insertwidth=4, bg= "powder blue", justify= 'right')
txtJuice.grid(row=8, column=1)

lblCoffee = Label(f1, font=('arial', 16, 'bold'), text="Coffee", bd=16, anchor='w')
lblCoffee.grid(row=9,  column=0)
txtCoffee=Entry(f1, font=('arial', 16, 'bold'), textvariable=Coffee, bd=10,  insertwidth=4, bg= "powder blue", justify= 'right')
txtCoffee.grid(row=9, column=1)

#============Restaurant Billing================

lblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost", bd=16, anchor='w')
lblCost.grid(row=0,  column=2)
txtCost=Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10,  insertwidth=4, bg= "yellow", justify= 'right')
txtCost.grid(row=0, column=3)

lblServices=Label(f1, font=('arial', 16, 'bold'), text="Service Charge", bd= 16, anchor='w')
lblServices.grid(row=1, column=2)
txtServices=Entry(f1, font=('arial', 16, 'bold'), textvariable=Services,bd=10, insertwidth=4, bg="yellow", justify='right')
txtServices.grid(row=1, column=3)

lblTax=Label(f1, font=('arial', 16, 'bold'), text="Tax", bd= 16, anchor='w')
lblTax.grid(row=2, column=2)
txtTax=Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax,bd=10, insertwidth=4, bg="yellow", justify='right')
txtTax.grid(row=2, column=3)

lblSubTotal=Label(f1, font=('arial', 16, 'bold'), text="Sub Total", bd= 16, anchor='w')
lblSubTotal.grid(row=3, column=2)
txtSubTotal=Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal,bd=10, insertwidth=4, bg="yellow", justify='right')
txtSubTotal.grid(row=3, column=3)

lblTotalCost=Label(f1, font=('arial', 16, 'bold'), text="Total Bill", bd= 16, anchor='w')
lblTotalCost.grid(row=4, column=2)
txtTotalCost=Entry(f1, font=('arial', 16, 'bold'), textvariable=TotalCost, bd=10, insertwidth=4, bg="yellow", justify='right')
txtTotalCost.grid(row=4, column=3)

#=====================Buttons================

btnTotal= Button(f1, padx=7, pady=4, bd= 8, fg="black", font=('arial', 12, 'bold'), width=10, text="Total", bg= "red", command= Ref).grid(row=5, column=3)

btnReset= Button(f1, padx=7, pady=4, bd= 8, fg="black", font=('arial', 12, 'bold'), width=10, text="Reset", bg= "red", command= Reset).grid(row=6, column=3)

btnPrint= Button(f1, padx=7, pady=4, bd= 8, fg="black", font=('arial', 12, 'bold'), width=10, text="Print", bg= "red").grid(row=5, column=4)

btnExit= Button(f1, padx=7, pady=4, bd= 8, fg="black", font=('arial', 12, 'bold'), width=10, text="Exit", bg= "red", command= Exit).grid(row=6, column=4)























root.mainloop()
