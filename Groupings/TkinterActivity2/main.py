import tkinter as tk

class CalculatorApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.geometry("600x600")
    self.resizable(False, False)

####
    self.LABEL1 = tk.Label(self, text="Type Of Transaction")
    self.LABEL1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
####
    self.TypeRButton = tk.IntVar(value = "1")
    self.RButton1 = tk.Radiobutton(self, text="Default", variable=self.TypeRButton, value=1)
    self.RButton1.grid(row=0, column=1, padx=5, pady=2, sticky="w")
    self.RButton2 = tk.Radiobutton(self, text="Deposit", variable=self.TypeRButton, value=2,command=lambda: self.enable_entry(self.PrevBalEntry))
    self.RButton2.grid(row=0, column=2, padx=5, pady=2, sticky="w")
    self.RButton2 = tk.Radiobutton(self, text="Withdraw", variable=self.TypeRButton, value=3)
    self.RButton2.grid(row=0, column=3, padx=5, pady=2, sticky="w")


####
    self.PrevBal = tk.Label(self, text="Previous Balance:",)
    self.PrevBal.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    self.PrevBalEntry = tk.Entry(self, width=25, bg="#FFFFFF", fg="#000000",state='readonly')
    self.PrevBalEntry.grid(row=1, column=1, padx=5, pady=5)


#####
    self.Denomination = tk.Label(self, text="Denomination:")
    self.Denomination.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    self.NumberOfPieces = tk.Label(self, text="Number of Pieces:")
    self.NumberOfPieces.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    self.Amount = tk.Label(self, text="Amount")
    self.Amount.grid(row=2, column=2, padx=5, pady=5, sticky="w")
##

    self.DenoFee1 = tk.IntVar()
    self.DenoFee2 = tk.IntVar()
    self.DenoFee3 = tk.IntVar()
    self.DenoFee4 = tk.IntVar()

####
    self.Deno1 = tk.Checkbutton(self, text="1000", onvalue=1000, offvalue=0,variable = self.DenoFee1,command=lambda: self.enable_entry(self.Pieces1))
    self.Deno1.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    self.Deno2 = tk.Checkbutton(self, text="500", onvalue=500, offvalue=0,variable = self.DenoFee2,command=lambda: self.enable_entry(self.Pieces2))
    self.Deno2.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    self.Deno3 = tk.Checkbutton(self, text="200", onvalue=200, offvalue=0,variable = self.DenoFee3,command=lambda: self.enable_entry(self.Pieces3))
    self.Deno3.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    self.Deno4 = tk.Checkbutton(self, text="100", onvalue=100, offvalue=0,variable = self.DenoFee4,command=lambda: self.enable_entry(self.Pieces4))
    self.Deno4.grid(row=6, column=0, padx=5, pady=5, sticky="w")
#####
    self.Pieces1 = tk.Entry(self,state='readonly')
    self.Pieces1.grid(row = 3, column = 1, padx = 5, pady=5, stick="w")
    self.Pieces2 = tk.Entry(self,state='readonly')
    self.Pieces2.grid(row = 4, column = 1, padx = 5, pady=5, stick="w")
    self.Pieces3 = tk.Entry(self,state='readonly')
    self.Pieces3.grid(row = 5, column = 1, padx = 5, pady=5, stick="w")
    self.Pieces4 = tk.Entry(self,state='readonly')
    self.Pieces4.grid(row = 6, column = 1, padx= 5, pady=5, stick="w")
#####

    self.Amount1 = tk.Entry(self,state='readonly')
    self.Amount1.grid(row = 3, column = 2, padx = 5, pady=5, stick="w")
    self.Amount2 = tk.Entry(self,state='readonly')
    self.Amount2.grid(row = 4, column = 2, padx = 5, pady=5, stick="w")
    self.Amount3 = tk.Entry(self,state='readonly')
    self.Amount3.grid(row = 5, column = 2, padx = 5, pady=5, stick="w")
    self.Amount4 = tk.Entry(self,state='readonly')
    self.Amount4.grid(row = 6, column = 2, padx= 5, pady=5, stick="w")
    self.LTotalDeposit = tk.Label(self, text="Total Deposit:") 
    self.LTotalDeposit.grid(row = 7, column = 1, padx = 5, pady=5, stick="w")
    self.LTotalDepositEntry = tk.Entry(self,state='readonly')
    self.LTotalDepositEntry.grid(row = 7, column = 2, padx =5, pady=5, stick="w")

##########
    self.LCurrentBalance = tk.Label(self, text ="Current Balance")
    self.LCurrentBalance.grid(row = 8, column = 0, padx =5, pady=5, stick="w")
    self.ECurrentBalance = tk.Entry(self,state='readonly')
    self.ECurrentBalance.grid(row = 8, column = 1, padx =5, pady=5, stick="w")


##########
    self.Compute = tk.Button(self, text = "Compute")
    self.Compute.grid(row = 9, column=1, padx =5, pady =5, stick="w")

#######

  def enable_entry(self, entry):
        entry.configure(state="normal")
        entry.update()

  def disable_entry(self, entry):
        entry.configure(state="readonly")
        entry.update()



if __name__ == "__main__":
    calculator = CalculatorApp()
    calculator.mainloop()