from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import Calendar
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'organ_donation_project.settings')
django.setup()

from organ_donation_app.models import Donor



# Donor registration screen

def RegisterForOrganDonation():

    # On Adding Donor
    def onAddDonor():
        fname=e1.get()
        mname=e2.get()
        lname=e3.get()
        age=e4.get()
        contact=e5.get()
        email=e6.get()
        address=e7.get()
        gender=gender_radio_used()
        blood_grp=bloodType.get()
        organ=organToDonate.get()
        
        new_donor = Donor(firstName=fname,middleName=mname,lastName=lname,ageOfDonor=age,contact_number=contact,emailIdOfDonor=email,addressOfDonor=address,genderOfDonor=gender,bloodGrp=blood_grp,organ_to_donate=organ)
        new_donor.save()
        messagebox.showinfo("Donor Added", f"{fname} has been successfully added to database!")
        window1.after(100, window1.destroy)
    
    # command for radio button
    def gender_radio_used():
        radio = gender_var.get()
        if radio == 0:
            return 'Male'
        else:
            return 'Female'
               
    # function to upload document
    def UploadDoc():
        pass

    window1 = Tk()
    window1.title('Donor Registration')
    window1.geometry('1600x1500')
    window1.config(bg='Light gray')

    frame1 = Frame(window1, width=1200, height=800, highlightbackground='black', highlightthickness=1.5)
    frame1.grid(padx=350, pady=50, ipadx=30, ipady=30)

    Label(frame1, text='Personal information', font=('Helvetica', 10, 'bold')).grid(row=0, columnspan=4)
    Label(frame1, text='First Name').grid(row=2)
    Label(frame1, text='Middle Name').grid(row=3)
    Label(frame1, text='Last Name').grid(row=4)
    Label(frame1, text='Age').grid(row=5)
    Label(frame1, text='Contact number').grid(row=6)
    Label(frame1, text='Email id').grid(row=7)
    Label(frame1, text='Address').grid(row=8)
    Label(frame1, text='Gender').grid(row=9, column=0, sticky='e')


    global gender_var
    gender_var = IntVar()
    Radiobutton(frame1, text='Male', variable=gender_var, value=0,command=gender_radio_used).grid(row=9, column=1)
    Radiobutton(frame1, text='Female', variable=gender_var, value=1,command=gender_radio_used).grid(row=9, column=2)

    Label(frame1, text='Medical information', font=('Helvetica', 10, 'bold')).grid(row=10, columnspan=4)
    Label(frame1, text='Blood Type').grid(row=11, column=0, sticky='e')
    Label(frame1, text='Organ to Donate').grid(row=12, column=0, sticky='e')

    global bloodType
    bloodType = StringVar()
    bloodType_options = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    bloodType_dropdown = OptionMenu(frame1, bloodType, *bloodType_options)
    bloodType_dropdown.grid(row=11, column=1)

    global organToDonate
    organToDonate = StringVar()
    organ_options = ['Heart', 'Liver', 'Kidney', 'Lung', 'Pancreas', 'Intestine','Eyes']
    organToDonate_dropdown = OptionMenu(frame1, organToDonate, *organ_options)
    organToDonate_dropdown.grid(row=12, column=1)

    bloodType_label = Label(frame1, text='')
    bloodType_label.grid(row=11, column=2)

    organToDonate_label = Label(frame1, text='')
    organToDonate_label.grid(row=12, column=2)

    def update_selected_blood_type(*args):
        selectedBloodType = bloodType.get()
        bloodType_label.config(text=selectedBloodType)

    def update_selected_organ(*args):
        selectedOrgan = organToDonate.get()
        organToDonate_label.config(text=selectedOrgan)

    bloodType.trace_add('write', update_selected_blood_type)
    organToDonate.trace_add('write', update_selected_organ)

    e1 = Entry(frame1)
    e1.grid(row=2, column=1)
    e2 = Entry(frame1)
    e2.grid(row=3, column=1)
    e3 = Entry(frame1)
    e3.grid(row=4, column=1)
    e4=Entry(frame1)
    e4.grid(row=5,column=1)
    e5 = Entry(frame1)
    e5.grid(row=6, column=1)
    e6 = Entry(frame1)
    e6.grid(row=7, column=1)
    e7 = Entry(frame1)
    e7.grid(row=8, column=1)

    uploadDocument=Button(frame1,text='Upload Death Certificate', font=('Helvetica', 8, 'bold'), fg='Black', bg='Medium Purple',
                          command=UploadDoc)
    uploadDocument.grid(row=13,column=1,pady=20,padx=40)

    submitButton = Button(frame1,text='Submit', font=('Helvetica', 8, 'bold'), fg='Black', bg='Medium Purple',
                          command= onAddDonor)
    submitButton.grid(row=13,column=2,pady=20,padx=40)



# Main Screen
    
mainwindow = Tk()
mainwindow.title('Organ Donation')
mainwindow.geometry('1000x1000')
    
btn1 = Button(text='Register for Organ Donation', fg='white', bg='blue', font=('Helvetica', 12),
              command=RegisterForOrganDonation)
btn1.place(x=300, y=300)


btn2 = Button(text='Find Hospital Details', fg='white', bg='blue', font=('Helvetica', 12))
btn2.place(x=550, y=300)



mainwindow.mainloop()