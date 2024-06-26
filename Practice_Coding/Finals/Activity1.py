import tkinter as tk
from tkinter import StringVar, ttk, messagebox, END
from tkinter import Label, Checkbutton, IntVar, Entry
# Function Definitions
def clear():
    EBox.set(0)
    IBox.set(0)
    WBox.set(0)
    EverydayComboB.set(" ")
    IntegComboB.set(" ")
    WondersComboB.set(" ")
    EverdayQEntry.delete(0, END)
    IntegQEntry.delete(0, END)
    WondersQEntry.delete(0, END)
    Choice1.set("")
    SubTotal1.set("")
    Choice2.set("")
    SubTotal2.set("")
    Choice3.set("")
    SubTotal3.set("")
    TotalAmount.set("")

def updateBtn():
    if EBox.get() == 1:
        EverydayComboB.config(state="readonly")
        EverdayQEntry.config(state="normal")
    else:
        EverydayComboB.config(state="disabled")
        EverydayComboB.set(" ")
        Choice1.set("")
        SubTotal1.set("")
        EverdayQEntry.delete(0, END)
        EverdayQEntry.config(state="disabled")

    if IBox.get() == 1:
        IntegComboB.config(state="readonly")
        IntegQEntry.config(state="normal")
    else:
        IntegComboB.config(state="disabled")
        IntegComboB.set(" ")
        Choice2.set("")
        SubTotal2.set("")
        IntegQEntry.delete(0, END)
        IntegQEntry.config(state="disabled")

    if WBox.get() == 1:
        WondersComboB.config(state="readonly")
        WondersQEntry.config(state="normal")
    else:
        WondersComboB.config(state="disabled")
        WondersComboB.set(" ")
        Choice3.set("")
        SubTotal3.set("")
        WondersQEntry.delete(0, END)
        WondersQEntry.config(state="disabled")

def unitPriceUpdate(event):
    if EverydayComboB.get() == 'NURSERY':
        Choice1.set("150.00")
    elif EverydayComboB.get() == 'KINDER':
        Choice1.set("200.00")
    elif EverydayComboB.get() == 'PREP':
        Choice1.set("250.00")

    if IntegComboB.get() == 'NURSERY':
        Choice2.set("150.00")
    elif IntegComboB.get() == 'KINDER':
        Choice2.set("200.00")
    elif IntegComboB.get() == 'PREP':
        Choice2.set("250.00")

    if WondersComboB.get() == 'NURSERY':
        Choice3.set("150.00")
    elif WondersComboB.get() == 'KINDER':
        Choice3.set("200.00")
    elif WondersComboB.get() == 'PREP':
        Choice3.set("250.00")

def compute():
    try:
        subj1 = int(EverdayQEntry.get() ) * float(Choice1.get() or 0)
        subj2 = int(IntegQEntry.get() ) * float(Choice2.get() or 0)
        subj3 = int(WondersQEntry.get()) * float(Choice3.get() or 0)

        if EBox.get() == 1 and EverdayQEntry.get() == "":
            messagebox.showerror("Error!", "Please input valid quantity for Everyday English")
        elif IBox.get() == 1 and IntegQEntry.get() == "":
            messagebox.showerror("Error!", "Please input valid quantity for Integrated Mathematics")
        elif WBox.get() == 1 and WondersQEntry.get() == "":
            messagebox.showerror("Error!", "Please input valid quantity for Wonders of Science")
        else:
            SubTotal1.set(f"{subj1:.2f}" if subj1 else "")
            SubTotal2.set(f"{subj2:.2f}" if subj2 else "")
            SubTotal3.set(f"{subj3:.2f}" if subj3 else "")

            totalAmount = subj1 + subj2 + subj3
            TotalAmount.set(f"{totalAmount:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid values for book quantities.")

# Main Tkinter GUI Code
frame = tk.Tk()
frame.title("Book Store")
frame.geometry("1150x300")

MainTitle = Label(frame, text="MJN Book Store")
MainTitle.grid(row=0, column=2, padx=40, pady=2)

BookTitle = Label(frame, text="Book Title")
BookTitle.grid(row=1, column=1, padx=40, pady=2)

EBox = IntVar()
EverydayCheckB = Checkbutton(frame, text="Everyday English", variable=EBox, onvalue=1, offvalue=0, command=updateBtn, bg="white")
EverydayCheckB.grid(row=2, column=1, padx=40, pady=5)

IBox = IntVar()
IntegCheckB = Checkbutton(frame, text="Integrated Mathematics", variable=IBox, onvalue=1, offvalue=0, command=updateBtn, bg="white")
IntegCheckB.grid(row=3, column=1, padx=40, pady=5)

WBox = IntVar()
WondersCheckB = Checkbutton(frame, text="Wonders Of Science", variable=WBox, onvalue=1, offvalue=0, command=updateBtn, bg="white")
WondersCheckB.grid(row=4, column=1, padx=40, pady=5)

Level = Label(frame, text="Level")
Level.grid(row=1, column=2, padx=40, pady=2)
choices = ["NURSERY", "KINDER", "PREP"]

EverydayComboB = ttk.Combobox(frame, values=choices, state="disabled")
EverydayComboB.grid(row=2, column=2, padx=40, pady=2)
EverydayComboB.bind("<<ComboboxSelected>>", unitPriceUpdate)

IntegComboB = ttk.Combobox(frame, values=choices, state="disabled")
IntegComboB.grid(row=3, column=2, padx=40, pady=2)
IntegComboB.bind("<<ComboboxSelected>>", unitPriceUpdate)

WondersComboB = ttk.Combobox(frame, values=choices, state="disabled")
WondersComboB.grid(row=4, column=2, padx=40, pady=2)
WondersComboB.bind("<<ComboboxSelected>>", unitPriceUpdate)

UnitPrice = Label(frame, text="Unit Price")
UnitPrice.grid(row=1, column=3, padx=40, pady=2)

Choice1 = StringVar()
Choice2 = StringVar()
Choice3 = StringVar()

EverdayUEntry = Entry(frame, state="readonly", textvariable=Choice1)
EverdayUEntry.grid(row=2, column=3, padx=40, pady=2)

IntegUEntry = Entry(frame, state="readonly", textvariable=Choice2)
IntegUEntry.grid(row=3, column=3, padx=40, pady=2)

WondersUEntry = Entry(frame, state="readonly", textvariable=Choice3)
WondersUEntry.grid(row=4, column=3, padx=40, pady=2)

Quantity = Label(frame, text="Quantity")
Quantity.grid(row=1, column=4, padx=40, pady=2)

Quantity1 = StringVar()
Quantity2 = StringVar()
Quantity3 = StringVar()

EverdayQEntry = Entry(frame, state="disabled", textvariable=Quantity1)
EverdayQEntry.grid(row=2, column=4, padx=40, pady=2)

IntegQEntry = Entry(frame, state="disabled", textvariable=Quantity2)
IntegQEntry.grid(row=3, column=4, padx=40, pady=2)

WondersQEntry = Entry(frame, state="disabled", textvariable=Quantity3)
WondersQEntry.grid(row=4, column=4, padx=40, pady=2)

SubTotal = Label(frame, text="Sub-Total")
SubTotal.grid(row=1, column=5, padx=40, pady=2)

SubTotal1 = StringVar()
SubTotal2 = StringVar()
SubTotal3 = StringVar()

EverdaySEntry = Entry(frame, state="readonly", textvariable=SubTotal1)
EverdaySEntry.grid(row=2, column=5, padx=40, pady=2)

IntegSEntry = Entry(frame, state="readonly", textvariable=SubTotal2)
IntegSEntry.grid(row=3, column=5, padx=40, pady=2)

WondersSEntry = Entry(frame, state="readonly", textvariable=SubTotal3)
WondersSEntry.grid(row=4, column=5, padx=40, pady=2)

TotalAmount = StringVar()
TotalAmountLabel = Label(frame, text="Total Amount:")
TotalAmountLabel.grid(row=5, column=4, padx=40, pady=2)
TotalEAmount = Entry(frame, state="readonly", textvariable=TotalAmount)
TotalEAmount.grid(row=5, column=5, padx=40, pady=2)

ComputerButton = tk.Button(frame, text="Compute", command=compute)
ComputerButton.grid(row=6, column=2, padx=40, pady=2)
ClearButton = tk.Button(frame, text = "Clear", command = clear)
ClearButton.grid(row = 6, column = 3,padx=40, pady=2)

frame.mainloop()















