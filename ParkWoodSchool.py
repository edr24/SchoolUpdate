from tkinter import *
from tkinter import messagebox
import os

# Renamed function to follow Python's snake_case convention
def open_add_teacher_window():
    def save_teacher():
        # Condensed the process of getting values and justifying them for file saving
        details = [teacher_id_var.get().ljust(50), firstname_var.get().ljust(50), 
                   surname_var.get().ljust(50), address_var.get().ljust(50), 
                   postcode_var.get().ljust(50), qualification_var.get().ljust(50)]
        # Using 'with' ensures the file is properly closed after writing
        with open("TeacherDetails.txt", "a") as file:
            file.write("".join(details) + "\n")
        messagebox.showinfo("Confirmation", "Teacher details successfully saved")
        # Destroys the window after saving, to prevent multiple open windows
        add_teacher_window.destroy()

    # Using Toplevel instead of Tk() for secondary windows
    add_teacher_window = Toplevel()
    add_teacher_window.title("Add Teacher")
    add_teacher_window.geometry("300x300")

    # Simplified label and entry creation using a loop
    fields = ["TeacherID", "Firstname", "Surname", "Address", "Postcode", "Qualification"]
    vars = []
    for i, field in enumerate(fields, start=1):
        Label(add_teacher_window, text=field).grid(row=i, column=0, sticky=W)
        var = StringVar()
        Entry(add_teacher_window, textvariable=var).grid(row=i, column=1, sticky=W)
        vars.append(var)

    # Direct unpacking of variables for clarity
    teacher_id_var, firstname_var, surname_var, address_var, postcode_var, qualification_var = vars

    # Positioning back and save buttons more logically
    Button(add_teacher_window, text="Back", command=add_teacher_window.destroy).grid(row=len(fields)+1, column=0)
    Button(add_teacher_window, text="Save", command=save_teacher).grid(row=len(fields)+1, column=1)

def open_payroll_window():
    os.system('python Payroll.py')  # No change here

def open_add_pupil_window():
    os.system('python Pupils.py')  # No change here

def open_add_user_window():
    def save_user():
        # Simplified getting values and stripping whitespace
        user_id = user_id_var.get().strip()
        password = password_var.get().strip()
        # Using 'with' for proper file handling
        with open("data.dat", "a") as file:
            file.write(f"{user_id} {password}\n")
        messagebox.showinfo("Confirmation", "Password successfully saved")
        # Closing the window after saving
        add_user_window.destroy()

    # Using Toplevel for this window as well
    add_user_window = Toplevel()
    add_user_window.title("Add User")
    add_user_window.geometry("300x300")

    # Simplified label and entry setup
    Label(add_user_window, text="UserID").grid(row=1, column=0, sticky=W)
    user_id_var = StringVar()
    Entry(add_user_window, textvariable=user_id_var).grid(row=1, column=1, sticky=W)

    Label(add_user_window, text="Password").grid(row=2, column=0, sticky=W)
    password_var = StringVar()
    Entry(add_user_window, textvariable=password_var).grid(row=2, column=1, sticky=W)

    # More logical button placement and clear action indication
    Button(add_user_window, text="Back", command=add_user_window.destroy).grid(row=3, column=0)
    Button(add_user_window, text="Save", command=save_user).grid(row=3, column=1)

# Renamed to follow snake_case convention
def open_main_menu_window():
    main_menu_window = Tk()
    main_menu_window.title("Main Menu")
    main_menu_window.geometry("200x200")

    # Grouped buttons together for cleaner setup
    buttons = [("Add Teacher", open_add_teacher_window), 
               ("Payroll", open_payroll_window), 
               ("Add User", open_add_user_window), 
               ("Add Pupil", open_add_pupil_window), 
               ("Logout", main_menu_window.destroy),  # Logout now correctly destroys the main menu window
               ("Exit", main_menu_window.quit)]  # Exit quits the application

    for text, command in buttons:
        Button(main_menu_window, text=text, command=command).pack()

    main_menu_window.mainloop()

# Ensuring the script runs only when directly executed
if __name__ == "__main__":
    open_main_menu_window()
