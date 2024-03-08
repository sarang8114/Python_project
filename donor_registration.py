from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
# from tkcalendar import Calendar
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'organ_donation_project.settings')
django.setup()

from organ_donation_app.models import Donor

# Donor registration screen

def RegisterForOrganDonation():
    global window1

    # On Adding Donor
    def onAddDonor():
        fname=e1.get()
        mname=e2.get()
        lname=e3.get()
        age=e4.get()
        contact=e5.get()
        email=e6.get()
        address=e7.get("1.0", END).strip()
        gender=gender_radio_used()
        blood_grp=bloodType.get()
        organ=organToDonate.get()
        medCondition=medical_condition()
        prevSurgeries=previous_surgeries_entry.get("1.0", END).strip()
        medEntries=medications_entry.get("1.0", END).strip()
        allergies=allergies_entry.get("1.0", END).strip()
        smokingCheck=lifestyle_info_used()
        alcConsumptionStatus=alcoholConsumption.get()
        
        new_donor = Donor(firstName=fname,middleName=mname,lastName=lname,ageOfDonor=age,contact_number=contact,
                          emailIdOfDonor=email,addressOfDonor=address,genderOfDonor=gender,bloodGrp=blood_grp,
                          organ_to_donate=organ,medicalConditions=medCondition,previousSurgery=prevSurgeries,
                          medicationEntries=medEntries,allergyEntries=allergies,smokingPercentage=smokingCheck,
                          alcoholConsumptionStatus=alcConsumptionStatus)
        new_donor.save()
        messagebox.showinfo("Donor Added", f"{fname} has been successfully added to database!")
        # window1.after(100, window1.destroy)
    
    # function to read gender from radiobutton
    def gender_radio_used():
        radio = gender_var.get()
        if radio == 0:
            return 'Male'
        elif radio==1:
            return 'Female'
        else:
            return 'Other'
    
    #function to health condition from checkbutton 
    def medical_condition():
        checkbox=medicalCondition.get()
        if checkbox==0:
            return 'Diabetes'
        elif checkbox==1:
            return 'Asthma'
        elif checkbox==2:
            return 'Cataract'
        else:
            return 'Arthritis'
        
    # function to check lifestyle status
    def lifestyle_info_used():
        val=smoking.get()
        if val==1:
            return 'Regular'
        elif val==2:
            return 'Occassional'
        else:
            return 'Never'
              
    # function to upload document
    def UploadDoc():
        global file_path
        global file_label
        file_path = filedialog.askopenfilename(initialdir="/", title="Select Document", filetypes=(("All Files", ".png;.jpg;.jpeg;.txt"), ("all files", ".*")))
        if file_path:
            file_label.config(text=f"File Selected: {file_path}")

    # Donor Form Window Geometry
            
    window1 = Tk()
    window1.title('Donor Registration')
    window1.geometry('1600x1500')
    window1.config(bg='Light gray')

    # Frame of Donor Form

    frame1 = Frame(window1, width=700, height=1400, highlightbackground='black', highlightthickness=1.5)
    frame1.grid(padx=200, pady=10)

    # Section 1 - Personal Information

    Label(frame1, text='Personal information', font=('Helvetica', 10, 'bold')).grid(row=0, columnspan=10,pady=(10,0))
    Label(frame1, text='First Name').grid(row=3)
    Label(frame1, text='Middle Name').grid(row=4)
    Label(frame1, text='Last Name').grid(row=5)
    Label(frame1, text='Age').grid(row=6)
    Label(frame1, text='Contact number').grid(row=7)
    Label(frame1, text='Email id').grid(row=8)
    Label(frame1, text='Address').grid(row=9,sticky='n')
    Label(frame1, text='Gender').grid(row=11)

    global gender_var
    gender_var = IntVar()
    Radiobutton(frame1, text='Male', value=0,command=gender_radio_used).grid(row=11, column=1,sticky='w', pady=(5, 0))
    Radiobutton(frame1, text='Female', value=1,command=gender_radio_used).grid(row=11, column=2,sticky='w', pady=(5, 0))
    Radiobutton(frame1, text='Other',value=2,command=gender_radio_used).grid(row=11, column=3,sticky='w',pady=(5, 0))

    e1 = Entry(frame1,width=60)
    e1.grid(row=3, column=1,sticky='w',pady=(5, 0))
    e2 = Entry(frame1,width=60)
    e2.grid(row=4, column=1,sticky='w',pady=(5, 0))
    e3 = Entry(frame1,width=60)
    e3.grid(row=5, column=1,sticky='w',pady=(5, 0))
    e4=Spinbox(frame1,width=3,from_= 0, to = 100)
    e4.grid(row=6,column=1,sticky='w',pady=(5, 0))
    e5 = Entry(frame1,width=60)
    e5.grid(row=7, column=1,sticky='w',pady=(5, 0))
    e6 = Entry(frame1,width=60)
    e6.grid(row=8, column=1,sticky='w',pady=(5, 0))
    e7 = Text(frame1, height=2, width=45)
    e7.grid(row=9,column=1,sticky='w',pady=(5, 0))

    # Section 2 - Medical Information

    Label(frame1, text='Medical information', font=('Helvetica', 10, 'bold')).grid(row=12, columnspan=10, pady=(10, 0))
    Label(frame1, text='Blood Type').grid(row=13, column=0)
    Label(frame1, text='Organ to Donate').grid(row=14, column=0)
    Label(frame1, text='Medical Conditions').grid(row=15, column=0)

    global bloodType
    bloodType = StringVar()
    bloodType_options = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    bloodType_dropdown = OptionMenu(frame1, bloodType, *bloodType_options)
    bloodType_dropdown.grid(row=13, column=1,sticky='w')

    bloodType_label = Label(frame1, text='')
    bloodType_label.grid(row=13, column=2,sticky='w')

    def update_selected_blood_type(*args):
        selectedBloodType = bloodType.get()
        bloodType_label.config(text=selectedBloodType)

    bloodType.trace_add('write', update_selected_blood_type)

    global organToDonate
    organToDonate = StringVar()
    organ_options = ['Heart', 'Liver', 'Kidney', 'Lung', 'Pancreas', 'Intestine','Eyes']
    organToDonate_dropdown = OptionMenu(frame1, organToDonate, *organ_options)
    organToDonate_dropdown.grid(row=14, column=1,sticky='w')

    organToDonate_label = Label(frame1, text='')
    organToDonate_label.grid(row=14, column=2,sticky='w')

    def update_selected_organ(*args):
        selectedOrgan = organToDonate.get()
        organToDonate_label.config(text=selectedOrgan)

    organToDonate.trace_add('write', update_selected_organ)

    global medicalCondition
    medicalCondition=IntVar()
    Checkbutton(frame1, text='Diabetes', command=medical_condition, onvalue='Diabetes', offvalue='').grid(row=15, column=1, sticky='w',padx=(0, 5))
    Checkbutton(frame1, text='Asthma', command=medical_condition, onvalue='Asthma', offvalue='').grid(row=15, column=2,sticky='w',padx=(0, 5))
    Checkbutton(frame1, text='Cataract', command=medical_condition, onvalue='Cataract', offvalue='').grid(row=15, column=3,sticky='w',padx=(0, 5))
    Checkbutton(frame1, text='Arthritis',command=medical_condition, onvalue='Arthritis', offvalue='').grid(row=15, column=4,sticky='w',padx=(0, 5))

    Label(frame1, text='Previous Surgeries').grid(row=16, column=0,pady=(10, 0))
    previous_surgeries_entry = Text(frame1, height=2, width=50)
    previous_surgeries_entry.grid(row=16, column=1, columnspan=2,sticky='w')

    Label(frame1, text='Medications Currently Taking').grid(row=17, column=0, pady=(10, 0))
    medications_entry = Text(frame1, height=2, width=50)
    medications_entry.grid(row=17, column=1, columnspan=2, pady=(10, 0),sticky='w')

    Label(frame1, text='Allergies').grid(row=18, column=0, pady=(10, 0))
    allergies_entry = Text(frame1, height=2, width=50)
    allergies_entry.grid(row=18, column=1, columnspan=2, pady=(10, 0),sticky='w')

    # Section 3 - Lifestyle Information

    Label(frame1, text='Lifestyle information', font=('Helvetica', 10, 'bold')).grid(row=19, columnspan=10,pady=(10,0))
    Label(frame1, text='Percentage of Alcohol Consumption').grid(row=20, column=0)
    Label(frame1, text='Smoking').grid(row=21, column=0)

    global alcoholConsumption
    alcoholConsumption = IntVar()
    Scale(frame1, from_=0, to=100, orient=HORIZONTAL,variable=alcoholConsumption).grid(row=20,column=1,sticky='w')

    global smoking
    smoking = IntVar()
    Radiobutton(frame1,text='Regular',value=0,command=lifestyle_info_used).grid(row=21,column=1,sticky='w')
    Radiobutton(frame1,text='Occassional',value=1,command=lifestyle_info_used).grid(row=21,column=2,sticky='w')
    Radiobutton(frame1,text='Never',value=2,command=lifestyle_info_used).grid(row=21,column=3,sticky='w')

    # Upload and Submit Buttons

    uploadDocument=Button(frame1,text='Upload Death Certificate', font=('Helvetica', 10, 'bold'), fg='Black', bg='Medium Purple',command=UploadDoc,width=20)
    uploadDocument.grid(row=22,column=1,pady=20,padx=40)

    submitButton = Button(frame1,text='Submit', font=('Helvetica', 10, 'bold'), fg='Black', bg='Medium Purple',
                          command= onAddDonor,width=20)
    submitButton.grid(row=22,column=2,pady=20,padx=40)

    mainwindow.withdraw()


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