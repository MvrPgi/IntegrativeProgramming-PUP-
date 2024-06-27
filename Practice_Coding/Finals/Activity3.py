    
import tkinter as tk
from tkinter import messagebox

class TravelTours(tk.Tk):
   def __init__(self):
    super().__init__()
    self.geometry("500x500")
    self.resizable(False, False)

    self.labelFrame = tk.Frame(self)
    self.labelFrame.grid(row=0, column=0, padx=10, pady=10)
    self.travelABC = tk.Label(self.labelFrame, text="ABC PH TRAVEL AND TOURS")
    self.travelABC.grid(row=0, column=5)

    self.guestFrame = tk.Frame(self)
    self.guestFrame.grid(row=1, column=0, padx=10, pady=10)
    self.guestName = tk.Label(self.guestFrame, text="Guest Name:")
    self.guestName.grid(row=1, column=0,pady= 2)

    self.guestNameEntry = tk.Entry(self.guestFrame, width=25)
    self.guestNameEntry.grid(row=1, column=1,pady= 2)

    self.guestContactNumber = tk.Label(self.guestFrame, text="Contact Number:")
    self.guestContactNumber.grid(row=2, column=0,pady= 2)
    self.guestContactNumberEntry = tk.Entry(self.guestFrame, width=25)
    self.guestContactNumberEntry.grid(row=2, column=1,pady= 2)


    self.Packages = tk.Frame(self)
    self.Packages.grid(row=2, column=0,padx=10, pady=10)

#BORACAY

    self.tPack = tk.Label(self.Packages, text="Tour Packages:")
    self.tPack.grid(row=0, column=0,pady= 2)

    self.boracayTripVariable = tk.BooleanVar()
    self.boracayTrip = tk.Checkbutton(self.Packages, text="Boracay Trip", onvalue=True, offvalue=False, variable=self.boracayTripVariable,command =self.Toggle)
    self.boracayTrip.grid(row=2, column=0)

    self.boracayPax = tk.Label(self.Packages, text="PAX")
    self.boracayPax.grid(row=2, column=1)

    self.boracayCapacity = tk.Entry(self.Packages, width=5,state='disabled')
    self.boracayCapacity.grid(row=2, column=2)

    self.boracayDate = tk.Entry(self.Packages, width=25,state='disabled')
    self.boracayDate.grid(row=2, column=4)

#ILOILO

    self.IloIloTripVariable = tk.BooleanVar()
    self.IloIloTrip = tk.Checkbutton(self.Packages, text="IloIlo Trip", onvalue=True, offvalue=False, variable=self.IloIloTripVariable,command =self.Toggle)
    self.IloIloTrip.grid(row=3, column=0)

    self.IloIloPax = tk.Label(self.Packages, text="PAX")
    self.IloIloPax.grid(row=3, column=1)

    self.IloIloTripCapacity = tk.Entry(self.Packages, width=5, state='disabled')
    self.IloIloTripCapacity.grid(row=3, column=2)

    self.IloIloTripDate = tk.Entry(self.Packages, width=25,state='disabled')
    self.IloIloTripDate.grid(row=3, column=4)

#CEBU
    self.CebuTripVariable = tk.BooleanVar()
    self.CebuTrip = tk.Checkbutton(self.Packages, text="Cebu Trip", onvalue=True, offvalue=False, variable=self.CebuTripVariable,command =self.Toggle)
    self.CebuTrip.grid(row=4, column=0)

    self.CebuPax = tk.Label(self.Packages, text="PAX")
    self.CebuPax.grid(row=4, column=1)

    self.CebuTripCapacity = tk.Entry(self.Packages, width=5,state='disabled')
    self.CebuTripCapacity.grid(row=4, column=2)

    self.CebuTripDate = tk.Entry(self.Packages, width=25,state='disabled')
    self.CebuTripDate.grid(row=4, column=4)

#CEBU BOHOL
    self.CebuBoholTripVariable = tk.BooleanVar()
    self.CebuBoholTrip = tk.Checkbutton(self.Packages, text="CebuBohol Trip", onvalue=True, offvalue=False, variable=self.CebuBoholTripVariable,command =self.Toggle)
    self.CebuBoholTrip.grid(row=5, column=0)

    self.CebuBoholPax = tk.Label(self.Packages, text="PAX")
    self.CebuBoholPax.grid(row=5, column=1)

    self.CebuBoholTripCapacity = tk.Entry(self.Packages, width=5,state='disabled')
    self.CebuBoholTripCapacity.grid(row=5, column=2)

    self.CebuBoholTripDate = tk.Entry(self.Packages, width=25,state='disabled')
    self.CebuBoholTripDate.grid(row=5, column=4)

#ILOCOS
    self.IlocosTripVariable = tk.BooleanVar()
    self.IlocoslTrip = tk.Checkbutton(self.Packages, text="Ilocos Trip", onvalue=True, offvalue=False, variable=self.IlocosTripVariable,command=self.Toggle)
    self.IlocoslTrip.grid(row=6, column=0)

    self.IlocosPax = tk.Label(self.Packages, text="PAX")
    self.IlocosPax.grid(row=6, column=1)

    self.IlocosTripCapacity = tk.Entry(self.Packages, width=5,state='disabled')
    self.IlocosTripCapacity.grid(row=6, column=2)

    self.IlocosTripDate = tk.Entry(self.Packages, width=25,state='disabled')
    self.IlocosTripDate.grid(row=6, column=4)


# DESIRED DATE

    self.boracayDateLabel = tk.Label(self.Packages, text="Desired Date")
    self.boracayDateLabel.grid(row=2, column=3,padx=10, pady=10)

    self.IloIloTripDateLabel = tk.Label(self.Packages, text="Desired Date")
    self.IloIloTripDateLabel.grid(row=3, column=3,padx=10, pady=10)

    self.CebuTripDateLabel = tk.Label(self.Packages, text="Desired Date")
    self.CebuTripDateLabel.grid(row=4, column=3,padx=10, pady=10)

    self.CebuBoholTripDateLabel = tk.Label(self.Packages, text="Desired Date")
    self.CebuBoholTripDateLabel.grid(row=5, column=3,padx=10, pady=10)

    self.IlocosTripDateLabel = tk.Label(self.Packages, text="Desired Date")
    self.IlocosTripDateLabel.grid(row=6, column=3,padx=10, pady=10)



    self.lastFrame = tk.Frame(self)
    self.lastFrame.grid (row =3, column =0,padx=10, pady=10)
    self.Clear = tk.Button(self.lastFrame, text="Clear",command = self.ClearButton)
    self.Clear.grid(row =3 , column=0,padx=10, pady=10)
    self.Compute = tk.Button(self.lastFrame, text="Compute", command=self.ComputeButton)
    self.Compute.grid(row =3 , column=1,padx=10, pady=10)
    self.TotalAmount = tk.Label (self.lastFrame,text="Total Amount")
    self.TotalAmount.grid(row=3, column=2,padx=10, pady=10)
    self.totalAmountEntry = tk.Entry(self.lastFrame, width = 25)
    self.totalAmountEntry.grid(row=3, column = 3,padx=10, pady=10)
    
    self.totalAmountEntry.config(state='disable')




   def ComputeButton(self):
    try:  
      self.TotalPrice = 0
      if self.boracayTripVariable.get():
          self.TotalPrice += 4599 * int(self.boracayCapacity.get())
      if self.IloIloTripVariable.get():
          self.TotalPrice += 2999 *int(self.IlocosTripCapacity.get())
      if self.CebuTripVariable.get():
          self.TotalPrice += 1999 * int(self.CebuBoholTripCapacity.get())
      if self.CebuBoholTripVariable.get():
          self.TotalPrice += 3599 * int(self.CebuBoholTripCapacity.get())
      if self.IlocosTripVariable.get():
          self.TotalPrice += 3599 * int(self.IlocosTripCapacity.get())

      self.totalAmountEntry.config(state='normal')
      self.totalAmountEntry.delete(0,tk.END)
      self.totalAmountEntry.insert(0,self.TotalPrice)
      self.totalAmountEntry.config(state='readonly')


    except ValueError:
        messagebox.showerror("Invalid Input")

   def ClearButton(self):
     self.guestNameEntry.delete(0,tk.END)
     self.guestContactNumberEntry.delete(0,tk.END)
     self.boracayTrip.deselect()
     self.boracayCapacity.delete(0,tk.END)
     self.boracayDate.delete(0,tk.END)
     self.IloIloTrip.deselect()
     self.IloIloTripCapacity.delete(0,tk.END)
     self.IloIloTripDate.delete(0,tk.END)
     self.CebuTrip.deselect()
     self.CebuTripCapacity.delete(0,tk.END)
     self.CebuTripDate.delete(0,tk.END)
     self.CebuBoholTrip.deselect()
     self.CebuBoholTripCapacity.delete(0,tk.END)
     self.CebuTripDate.delete(0,tk.END)
     self.IlocoslTrip.deselect()
     self.IlocosTripCapacity.delete(0,tk.END)
     self.IlocosTripDate.delete(0,tk.END)

   def Toggle(self):
     if self.boracayTripVariable.get() == True:
        self.boracayCapacity.config(state='normal')
        self.boracayDate.config(state='normal')
     elif self.boracayTripVariable.get() == False:
        self.boracayCapacity.config(state='disabled')
        self.boracayDate.config(state='disabled')

     if self.IloIloTripVariable.get() == True:
        self.IloIloTripCapacity.config(state='normal')
        self.IloIloTripDate.config(state='normal')
     elif self.IloIloTripVariable.get() == False:
        self.IloIloTripCapacity.config(state='disabled')
        self.IloIloTripDate.config(state='disabled')

     if self.CebuTripVariable.get() == True:
        self.CebuTripCapacity.config(state='normal')
        self.CebuTripDate.config(state='normal')
     elif self.CebuTripVariable.get() == False:
        self.CebuTripCapacity.config(state='disabled')
        self.CebuTripDate.config(state='disabled')

     if self.CebuBoholTripVariable.get() == True:
        self.CebuBoholTripCapacity.config(state='normal')
        self.CebuBoholTripDate.config(state='normal')
     elif self.CebuBoholTripVariable.get() == False:
        self.CebuBoholTripCapacity.config(state='disabled')
        self.CebuBoholTripDate.config(state='disabled')
        
     if self.IlocosTripVariable.get() == True:
        self.IlocosTripCapacity.config(state='normal')
        self.IlocosTripDate.config(state='normal')
     elif self.IlocosTripVariable.get() == False:
        self.IlocosTripCapacity.config(state='disabled')
        self.IlocosTripDate.config(state='disabled')



 





if __name__ == "__main__":
  App = TravelTours()
  App.mainloop()