import tkinter as tk
from tkinter import END, W, ttk
from tkinter import messagebox

class JollyMcKing(tk.Tk):
  def __init__(self):
      super().__init__()
      self.geometry("400x300")
      self.resizable(False,False)
      



      self.frame = tk.Frame(self)
      self.frame.grid(row=0, column=0, padx=0, pady=10,sticky='nsew')

      self.Username = tk.Label(self.frame, text = "Username:")
      self.Username.grid(row=1, column = 1)
      self.UsernameEntry = tk.Entry(self.frame, width= 25)
      self.UsernameEntry.grid(row=1, column = 2)
      self.Password = tk.Label(self.frame, text = "Password ")
      self.Password.grid(row= 2,column = 1)
      self.PasswordEntry = tk.Entry(self.frame, width= 25,show='*')
      self.PasswordEntry.grid(row= 2,column = 2)
      self.ButtonLogin = tk.Button(self.frame, text= "OK",command=self.Login)
      self.ButtonLogin.grid(row= 2, column=3)

      self.frame2 = tk.Frame(self)
      self.frame2.grid(row=1, column = 0, padx =10,pady=10,sticky='nsew')

      self.OrderLabel = tk.Label(self.frame2, text = "Choose Your Order")
      self.OrderLabel.grid(row=2, column =0)

      self.FirstMealVariable = tk.BooleanVar()
      self.FirstMeal = tk.Checkbutton(self.frame2, text= "Value Meal #1 P25.00",onvalue=True, offvalue=False, variable= self.FirstMealVariable)
      self.FirstMeal.grid(row=3, column =0)

      self.SecondMealVariable = tk.BooleanVar()
      self.SecondMeal = tk.Checkbutton(self.frame2, text= "Value Meal #2 P30.00",onvalue=True, offvalue=False, variable= self.SecondMealVariable)
      self.SecondMeal.grid(row=4, column =0)

      self.ThirdMealVariable = tk.BooleanVar()
      self.ThirdMeal = tk.Checkbutton(self.frame2, text= "Value Meal #3 P30.00",onvalue=True, offvalue=False, variable= self.ThirdMealVariable)
      self.ThirdMeal.grid(row=5, column =0)

      self.SoftDrinksVariable = tk.StringVar()
      self.SoftDrinks = ttk.Combobox(self.frame2, width= 25, textvariable=self.SoftDrinksVariable)

  
      self.SoftDrinks['values']=('Coke','Sprite','RootBeer')
      self.SoftDrinks.grid(row=5, column =1)

      self.ExtraRiceVariable = tk.IntVar()
      self.ExtraRice = tk.Radiobutton(self.frame2, text="Extra Rice", variable= self.ExtraRiceVariable, value =1)
      self.ExtraRice.grid(row=6, column = 0)

      self.NoExtraRice = tk.Radiobutton(self.frame2, text="No Extra Rice", variable= self.ExtraRiceVariable, value =0)
      self.NoExtraRice.grid(row=6, column = 1)

    
      self.TotalBill = tk.Label(self.frame2, text="Total Bill Is:")
      self.TotalBillEntry = tk.Entry(self.frame2,width=25)
      self.TotalBill.grid(row =7, column =0)
      self.TotalBillEntry.grid(row = 7, column =1)



      self.ComputeButton = tk.Button(self.frame2, text="Compute"
                                    ,command=self.Compute)
      self.ComputeButton.grid(row = 6, column =3)
      
      self.ClearButton = tk.Button(self.frame2, text="Clear"  
                                  ,command=self.Clear)
      self.ClearButton.grid(row= 8, column=0)
          
      self.CloseButton = tk.Button(self.frame2, text="Close"  
                                  ,command=self.close)
      self.CloseButton.grid(row= 8, column=1)


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
        elif password != "AlwynPythonGods":
           messagebox.showinfo("Invalid Action", "Wrong Password")
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









