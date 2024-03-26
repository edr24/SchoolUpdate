from tkinter import *

# Create the main application window
payroll_win = Tk()
payroll_win.title("Payroll")
payroll_win.geometry("300x500")

# Initialize variables for payroll calculations
gross_pay = DoubleVar() #Changed from IntVar to DoubleVar to accurately handle decimal values in gross pay
tax = DoubleVar(value=0.0)
nat_ins = DoubleVar(value=0.0)
pension = DoubleVar(value=0.0)
student_loan = DoubleVar(value=0.0)  # Variable for student loan deduction
deducts = DoubleVar(value=0.0)
net_pay = DoubleVar(value=0.0)

# Function to calculate payroll details
def calc_pay():
    gross = gross_pay.get()
    tax.set(round(gross * 0.22, 2)) #changed from 20%
    nat_ins.set(round(gross * 0.085, 2)) #changed as per task
    pension.set(round(gross * 0.08, 2))
    student_loan.set(round(gross * 0.10, 2))  # Calculation for student loan
    total_deductions = sum([tax.get(), nat_ins.get(), pension.get(), student_loan.get()])
    deducts.set(round(total_deductions, 2))
    net_pay.set(round(gross - total_deductions, 2))

# Creating and placing widgets in a more structured manner
Label(payroll_win, text="Gross Pay").grid(row=0, column=0, sticky=W)
Entry(payroll_win, textvariable=gross_pay).grid(row=0, column=1)

Button(payroll_win, text="Calculate", command=calc_pay).grid(row=1, pady=5)

Label(payroll_win, text="Tax:").grid(row=2, column=0, sticky=W)
Label(payroll_win, textvariable=tax).grid(row=2, column=1, sticky=W)

Label(payroll_win, text="National Insurance:").grid(row=3, column=0, sticky=W)
Label(payroll_win, textvariable=nat_ins).grid(row=3, column=1, sticky=W)

Label(payroll_win, text="Pension Contribution:").grid(row=4, column=0, sticky=W)
Label(payroll_win, textvariable=pension).grid(row=4, column=1, sticky=W)

Label(payroll_win, text="Student Loan Deduction:").grid(row=5, column=0, sticky=W)
Label(payroll_win, textvariable=student_loan).grid(row=5, column=1, sticky=W)

Label(payroll_win, text="Total Deductions:").grid(row=6, column=0, sticky=W)
Label(payroll_win, textvariable=deducts).grid(row=6, column=1, sticky=W)

Label(payroll_win, text="Net Pay:").grid(row=7, column=0, sticky=W)
Label(payroll_win, textvariable=net_pay).grid(row=7, column=1, sticky=W)

Button(payroll_win, text="Back", command=payroll_win.destroy).grid(row=8, pady=5)

# Running the application's main loop
payroll_win.mainloop()
