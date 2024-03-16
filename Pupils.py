from tkinter import *
from tkinter import messagebox
    
AddPupilWin=Tk()
AddPupilWin.title("Add Pupil")
AddPupilWin.geometry("300x300")




def SavePupil() :

    PupilIDSave = PupilIDVar.get()
    if PupilIDSave.strip() == "":
        messagebox.showinfo("Error","Blank username and password")
    else:
       PupilIDSave = PupilIDSave.ljust(50)
   
       FirstnameSave = FirstnameVar.get()
       if any(char.isdigit() for char in FirstnameSave):
            FirstnameSave = FirstnameSave.ljust(50)
            messagebox.showinfo("Error","Number in Pupil Name")
       else:
    
            SurnameSave = SurnameVar.get()
            SurnameSave = SurnameSave.ljust(50)
        
            FormClassSave = FormClassVar.get()
            FormClassSave = FormClassSave.ljust(50)
        
            DoBSave = DoBVar.get()
            DoBSave = DoBSave.ljust(50)
            
        
            fileObject = open("PupilDetails.txt","a")
            
            fileObject.write(PupilIDSave + FirstnameSave + SurnameSave + FormClassSave + DoBSave + "\n")
            fileObject.close()
            
            messagebox.showinfo("Confirmation","Pupil details successfully saved")



frame1=Frame(AddPupilWin)
frame1.pack()

   
Label(frame1, text="PupilID").grid(row=3, column=0, sticky=W)
PupilIDVar=StringVar()
PupilIDVar= Entry(frame1, textvariable=PupilIDVar)
PupilIDVar.grid(row=3,column=1,sticky=W)

Label(frame1, text="Firstname").grid(row=4, column=0, sticky=W)
FirstnameVar=StringVar()
FirstnameVar= Entry(frame1, textvariable=FirstnameVar)
FirstnameVar.grid(row=4,column=1,sticky=W)

Label(frame1, text="Surname").grid(row=5, column=0, sticky=W)
SurnameVar=StringVar()
SurnameVar= Entry(frame1, textvariable=SurnameVar)
SurnameVar.grid(row=5,column=1,sticky=W)

Label(frame1, text="Address").grid(row=6, column=0, sticky=W)
FormClassVar=StringVar()
FormClassVar= Entry(frame1, textvariable=FormClassVar)
FormClassVar.grid(row=6,column=1,sticky=W)

Label(frame1, text="DoB").grid(row=7, column=0, sticky=W)
DoBVar=StringVar()
DoBVar= Entry(frame1, textvariable=DoBVar)
DoBVar.grid(row=7,column=1,sticky=W)

frame2 = Frame(AddPupilWin)
frame2.pack()
b1= Button(frame2, text=" Back ", command=AddPupilWin.destroy)
b2= Button(frame2, text=" Save ", command=SavePupil)
b1.pack(side=LEFT); b2.pack(side=LEFT)


    
AddPupilWin.mainloop()
