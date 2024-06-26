import tkinter as tk
from tkinter import END, ttk
from tkinter import messagebox

class JollyMcKing(tk.Tk):
  def __init__(self):
      super().__init__()





      self.Username = tk.Label(self, text = "USER NAME:")
      self.Username.grid(row=1, column = 1)
      self.UsernameEntry = tk.Entry(self, width= 25)
      self.UsernameEntry.grid(row=1, column = 2)

      self.Password = tk.Label(self, text = "PASSWORD ")
      self.Password.grid(row= 2,column = 1)
      self.PasswordEntry = tk.Entry(self, width= 25,show='*')
      self.PasswordEntry.grid(row= 2,column = 2)


      self.ButtonLogin = tk.Button(self, text= "OK",command=self.Login)
      self.ButtonLogin.grid(row= 2, column=3)

      self.OrderLabel = tk.Label(self, text = "CHOOSE YOUR ORDER")
      self.OrderLabel.grid(row=3, column =2)

      self.FirstMealVariable = tk.BooleanVar()
      self.FirstMeal = tk.Checkbutton(self, text= "Value Meal #1 P25.00",onvalue=True, offvalue=False, variable= self.FirstMealVariable)
      self.FirstMeal.grid(row=4, column =2)

      self.SecondMealVariable = tk.BooleanVar()
      self.SecondMeal = tk.Checkbutton(self, text= "Value Meal #2 P30.00",onvalue=True, offvalue=False, variable= self.SecondMealVariable)
      self.SecondMeal.grid(row=5, column =2)

      self.ThirdMealVariable = tk.BooleanVar()
      self.ThirdMeal = tk.Checkbutton(self, text= "Value Meal #3 P30.00",onvalue=True, offvalue=False, variable= self.ThirdMealVariable)
      self.ThirdMeal.grid(row=6, column =2)

      self.SoftDrinksVariable = tk.StringVar()
      self.SoftDrinks = ttk.Combobox(self, width= 25, textvariable=self.SoftDrinksVariable)
      self.SoftDrinks['values']=('Coke','Sprite','RootBeer')
      self.SoftDrinks.grid(row=6, column =3)

      self.ExtraRiceVariable = tk.IntVar()
      self.ExtraRice = tk.Radiobutton(self, text="Extra Rice", variable= self.ExtraRiceVariable, value =1)
      self.ExtraRice.grid(row=7, column = 2)

      self.NoExtraRice = tk.Radiobutton(self, text="No Extra Rice", variable= self.ExtraRiceVariable, value =0)
      self.NoExtraRice.grid(row=7, column = 3)

    
      self.TotalBill = tk.Label(self, text="Total Bill Is:")
      self.TotalBillEntry = tk.Entry(self,width=25)
      self.TotalBill.grid(row =8, column =2)
      self.TotalBillEntry.grid(row = 8, column =3)



      self.ComputeButton = tk.Button(self, text="Compute"
                                    ,command=self.Compute)
      self.ComputeButton.grid(row = 7, column =4)
      
      self.ClearButton = tk.Button(self, text="Clear"  
                                  ,command=self.Clear)
      self.ClearButton.grid(row= 9, column=3)
          
      self.CloseButton = tk.Button(self, text="Close"  
                                  ,command=self.close)
      self.CloseButton.grid(row= 9, column=4)


      self.FirstMeal.config(state='disabled')
      self.SecondMeal.config(state='disabled')
      self.ThirdMeal.config(state='disabled')
      self.ExtraRice.config(state='disabled')
      self.NoExtraRice.config(state='disabled')
      self.SoftDrinks.config(state='disabled')
      self.ClearButton.config(state='disabled')
      self.ComputeButton.config(state='disabled')
      self.CloseButton.config(state='disabled')
      self.TotalBillEntry.config(state='disabled')
      
  def Login(self):
        username = self.UsernameEntry.get()
        password = self.PasswordEntry.get()

        if not password:
           messagebox.showinfo("Invalid Action", "Please enter your credentials")
           return
        
        if password == "AlwynPythonGods" and not username:
           messagebox.showerror("Invalid Action", "Please enter your username")
           return
        elif password =="AlwynPythonGods":
    
           self.FirstMeal.config(state='normal')
           self.SecondMeal.config(state='normal')
           self.ThirdMeal.config(state='normal')
           self.ExtraRice.config(state='normal')
           self.NoExtraRice.config(state='normal')
           self.SoftDrinks.config(state='normal')
           self.ComputeButton.config(state='normal')
           self.ClearButton.config(state='normal')

           self.CloseButton.config(state='normal')

     


  def Compute(self):
    try:
        TotalBill = 0
        if self.FirstMealVariable.get():
           TotalBill += 25
        if self.SecondMealVariable.get():
           TotalBill += 30
        if self.ThirdMealVariable.get():
           TotalBill +=35
        if self.ExtraRiceVariable.get() == 1:
           TotalBill += 25
        self.TotalBillEntry.config(state='normal')
        self.TotalBillEntry.delete(0,END)
        self.TotalBillEntry.insert(0,TotalBill)
        self.TotalBillEntry.config(state='disabled')
  
        self.TotalBillEntry.config(state='readonly')

    except ValueError:
        messagebox.showerror("Invalid Input")

  
  def Clear(self):
      if messagebox.askyesno("Confirmation", "Are you sure you want to clear?"):
        self.UsernameEntry.delete(0,tk.END)
        self.PasswordEntry.delete(0,tk.END)
        
        self.FirstMeal.deselect()
        self.SecondMeal.deselect()
        self.ThirdMeal.deselect()
        self.SoftDrinks.set('')
        self.TotalBillEntry.config(state='normal')
        self.TotalBillEntry.delete(0,tk.END)
        self.TotalBillEntry.config(state='disabled')
        self.ExtraRiceVariable.set(0)

  def close(self):
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        self.destroy()

      
           
  
if __name__ == "__main__":
    app = JollyMcKing()
    app.mainloop()









