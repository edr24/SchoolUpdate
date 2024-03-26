from tkinter import *
from tkinter import messagebox

# Creating the main application window
add_pupil_win = Tk()
add_pupil_win.title("Add Pupil")
add_pupil_win.geometry("300x300")

# Function to create and layout a label and entry, returning the entry's StringVar
def create_label_entry(parent, label_text, row):
    Label(parent, text=label_text).grid(row=row, column=0, sticky=W)
    var = StringVar()
    entry = Entry(parent, textvariable=var)
    entry.grid(row=row, column=1, sticky=W)
    return var

# Correct placement: Define frame1 before creating label and entry widgets
frame1 = Frame(add_pupil_win)
frame1.pack()

# Now we use frame1 properly for label and entry creation
pupil_id_var = create_label_entry(frame1, "PupilID", 0)
firstname_var = create_label_entry(frame1, "Firstname", 1)
surname_var = create_label_entry(frame1, "Surname", 2)
form_class_var = create_label_entry(frame1, "Form Class", 3)
dob_var = create_label_entry(frame1, "DoB", 4)

# Save pupil function with improved validation and file handling
def save_pupil():
    pupil_id = pupil_id_var.get().strip()
    firstname = firstname_var.get().strip()
    surname = surname_var.get().strip()
    form_class = form_class_var.get().strip()
    dob = dob_var.get().strip()

    # Validate pupil ID is not empty
    if not pupil_id:
        messagebox.showinfo("Error", "Pupil ID cannot be blank")
        return

    # Validate first name does not contain digits
    if any(char.isdigit() for char in firstname):
        messagebox.showinfo("Error", "First name cannot contain numbers")
        return

    # Justify and concatenate pupil details
    details = [pupil_id.ljust(50), firstname.ljust(50), surname.ljust(50), 
               form_class.ljust(50), dob.ljust(50)]

    # Save to file
    with open("PupilDetails.txt", "a") as file:
        file.write("".join(details) + "\n")
    messagebox.showinfo("Confirmation", "Pupil details successfully saved")

# Layout for buttons
buttons_frame = Frame(add_pupil_win)
buttons_frame.pack(pady=(10, 0))  # Add some padding above the buttons frame
Button(buttons_frame, text="Back", command=add_pupil_win.destroy).pack(side=LEFT, padx=5)
Button(buttons_frame, text="Save", command=save_pupil).pack(side=LEFT)

# Start the Tkinter event loop
add_pupil_win.mainloop()
