from tkinter import *

    
PayrollWin=Tk()
PayrollWin.title("Payroll")
PayrollWin.geometry("300x500")

GrossPay=IntVar()
Tax=DoubleVar()
Tax.set('0.0')
NatIns=DoubleVar()
NatIns.set('0.0')
Pension=DoubleVar()
Pension.set('0.0')
Deducts=DoubleVar()
Deducts.set('0.0')
NetPay=DoubleVar()
NetPay.set('0.0')

def CalcPay():

    Gross = float(GrossPay.get())
    Tax.set(round(Gross * 0.2, 2))
    NatIns.set(round(Gross * 0.14, 2))
    Pension.set(round(Gross * 0.08, 2))
    Deducts.set(round(Gross * 0.2 + Gross * 0.14 + Gross * 0.08, 2))
    NetPay.set(round(Gross - (Gross * 0.2 + Gross * 0.14 + Gross * 0.08), 2))
        
   
GrossPayLabel=Label(PayrollWin, text="Gross Pay").grid(row=3, column=0, sticky=W)
GrossPayEntry= Entry(PayrollWin, textvariable=GrossPay)
GrossPayEntry.grid(row=3,column=1)


b1= Button(PayrollWin, text=" Calculate ", command=CalcPay).grid(row=4)
 

TaxLabelText=Label(PayrollWin, text="Tax: ").grid(row=5, column=0, sticky=W)
TaxLabelValue=Label(PayrollWin, textvariable=Tax).grid(row=5, column=1, sticky=W)
NatInsLabelText =Label(PayrollWin, text="National Insurance: ").grid(row=6, column=0, sticky=W)
NatInsLabelValue=Label(PayrollWin, textvariable=NatIns).grid(row=6, column=1, sticky=W)
PensionLabeltext=Label(PayrollWin, text="Pension Contribution: " ).grid(row=7, column=0, sticky=W)
PensionLabelValue=Label(PayrollWin, textvariable=Pension).grid(row=7, column=1, sticky=W)
DeductsLabelText=Label(PayrollWin, text="Deductions: " ).grid(row=8, column=0, sticky=W)
DeductsLabelValue=Label(PayrollWin, textvariable=Deducts).grid(row=8, column=1, sticky=W)
NetPayLabelText=Label(PayrollWin, text="Net Pay: ").grid(row=9, column=0, sticky=W)
NetPayLabelValue=Label(PayrollWin, textvariable=NetPay).grid(row=9, column=1, sticky=W)


b2= Button(PayrollWin, text=" Back ", command=PayrollWin.destroy).grid(row=10)
   
    
PayrollWin.mainloop()
