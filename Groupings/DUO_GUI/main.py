#Design A Tkinter Frame

import tkinter as tk
from tkinter import ttk  # Change this to 'from tkinter import ttk' to avoid errors
from tkinter import messagebox  # Change this to 'from tkinter import messagebox' to avoid errors
# Student Name (LABEL)(ENTRY)
# Units Enrolled (LABEL)(ENTRY)
# Year Level (LABEL)(ENTRY)
# Other Fees (LABEL)(CHECKBUTTON)
# Laboratory Fee (LABEL)(CHECKBUTTON)(200)
# Registration Fee (LABEL)(CHECKBUTTON)(50)
# Catalyst Fee (LABEL)(CHECKBUTTON)(50)
# Student Council Fee (LABEL)(CHECKBUTTON)(50)
# Student ID (LABEL)(CheckButton)(50)
# Other Miscellaneous Fee (LABEL)(CheckButton)(100)

# Scholarship Grant (LABEL)(RADIOBUTTON)
# Non-Scholar (RADIOBUTTON)
# Partial Scholar (RADIOBUTTON)
# Full Scholar (RADIOBUTTON)

# Total Amount (LABEL)(ENTRY)
# Clear (BUTTON)
# Compute (BUTTON)


from tkinter import messagebox, ttk  # Import messagebox and ttk

class APP(tk.Tk):
    def Compute(self):
        try:
            units_enrolled = int(self.UnitsEnrolled.get())  # Correctly retrieve and convert UnitsEnrolled to int
            if units_enrolled <= 0:
                raise ValueError("Units Enrolled must be greater than 0")
            year_level_fee = 0
            year_level = self.n.get().strip()
            if year_level:
                year_level = int(year_level[0])
                year_level_fee = year_level * 100

            other_fees = 0
            if self.LabFeeVar.get():
                other_fees += 200
            if self.RegCardVar.get():
                other_fees += 50
            if self.CatalystVar.get():
                other_fees += 50
            if self.StudentCouncilVar.get():
                other_fees += 50
            if self.StudentIDVar.get():
                other_fees += 50
            if self.OtherMiscVar.get():
                other_fees += 100

            scholar_type = self.var.get()
            if scholar_type == 1:  # Use integer comparison for scholar_type
                total_amount = units_enrolled * 10 + year_level_fee + other_fees
            elif scholar_type == 2:
                total_amount = (units_enrolled * 10 + year_level_fee + other_fees) / 2
            else:
                total_amount = units_enrolled * 10 + year_level_fee + other_fees  # Default case for non-scholars

            self.TotalAmount.delete(0, tk.END)
            self.TotalAmount.insert(0, total_amount)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "An unexpected error occurred")

    def Clear(self):
        self.StudentName.delete(0, tk.END)
        self.UnitsEnrolled.delete(0, tk.END)
        self.YearLevel.set('')  # Correctly clear the Combobox selection
        self.LabFee.deselect()
        self.RegCard.deselect()
        self.Catalyst.deselect()
        self.StudentCouncil.deselect()
        self.StudentID.deselect()
        self.OtherMisc.deselect()
        self.NonScholar.deselect()
        self.PartialScholar.deselect()
        self.FullScholar.deselect()
        self.TotalAmount.delete(0, tk.END)
        self.var.set(0)  # Reset the scholarship type to default

    def __init__(self):
        super().__init__()

        self.L1 = tk.Label(self, text="Student Number:")
        self.L1.pack()
        self.StudentName = tk.Entry(self, width=25, bg="#FFFFFF", fg="#000000")
        self.StudentName.pack()

        self.L2 = tk.Label(self, text="Units Enrolled:")
        self.L2.pack()
        self.UnitsEnrolled = tk.Entry(self, width=25, bg="#FFFFFF", fg="#000000")
        self.UnitsEnrolled.pack()

        self.L3 = tk.Label(self, text="Year Level:")
        self.L3.pack()
        self.n = tk.StringVar()
        self.YearLevel = ttk.Combobox(self, width=25, textvariable=self.n)
        self.YearLevel['values'] = ('1st Year', '2nd Year', '3rd Year', '4th Year', '5th Year')
        self.YearLevel.pack()

        self.L4 = tk.Label(self, text="Other Fees:")
        self.L4.pack()
        self.LabFeeVar = tk.BooleanVar()
        self.RegCardVar = tk.BooleanVar()
        self.CatalystVar = tk.BooleanVar()
        self.StudentCouncilVar = tk.BooleanVar()
        self.StudentIDVar = tk.BooleanVar()
        self.OtherMiscVar = tk.BooleanVar()
        self.LabFee = tk.Checkbutton(self, text="Laboratory Fee\tP200", onvalue=True, offvalue=False, variable=self.LabFeeVar)
        self.RegCard = tk.Checkbutton(self, text="Registration Card\tP50", onvalue=True, offvalue=False, variable=self.RegCardVar)
        self.Catalyst = tk.Checkbutton(self, text="Catalyst\tP50", onvalue=True, offvalue=False, variable=self.CatalystVar)
        self.StudentCouncil = tk.Checkbutton(self, text="Student Council\tP50", onvalue=True, offvalue=False, variable=self.StudentCouncilVar)
        self.StudentID = tk.Checkbutton(self, text="Student ID\tP50", onvalue=True, offvalue=False, variable=self.StudentIDVar)
        self.OtherMisc = tk.Checkbutton(self, text="Other Miscellaneous\tP100", onvalue=True, offvalue=False, variable=self.OtherMiscVar)
        self.LabFee.pack()
        self.RegCard.pack()
        self.Catalyst.pack()
        self.StudentCouncil.pack()
        self.StudentID.pack()
        self.OtherMisc.pack()

        self.L5 = tk.Label(self, text="Scholarship Grant")
        self.L5.pack()
        self.var = tk.IntVar(value=1)  # Initialize var as IntVar directly
        self.NonScholar = tk.Radiobutton(self, text='Non-Scholar', variable=self.var, value=1)
        self.PartialScholar = tk.Radiobutton(self, text='Partial Scholar', variable=self.var, value=2)
        self.FullScholar = tk.Radiobutton(self, text='Full Scholar', variable=self.var, value=3)
        self.NonScholar.pack()
        self.PartialScholar.pack()
        self.FullScholar.pack()

        self.L6 = tk.Label(self, text="Total Amount")
        self.L6.pack()
        self.TotalAmount = tk.Entry(self, width=25, bg="#FFFFFF", fg="#000000",state = 'readonly')
        self.TotalAmount.pack()

        self.CLEAR = tk.Button(self, text="CLEAR", command=self.Clear,)
        self.CLEAR.pack()
        self.COMPUTE = tk.Button(self, text="COMPUTE", command=self.Compute)
        self.COMPUTE.pack()

if __name__ == "__main__":
    app = APP()
    app.mainloop()