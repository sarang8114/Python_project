from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

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
        
        new_donor = Donor(firstName=fname,middleName=mname,lastName=lname,ageOfDonor=age,contact_number=contact,
                          emailIdOfDonor=email,addressOfDonor=address,genderOfDonor=gender,bloodGrp=blood_grp,
                          organ_to_donate=organ,medicalConditions=medCondition,previousSurgery=prevSurgeries,
                          medicationEntries=medEntries,allergyEntries=allergies,smokingStatus=smokingCheck,
                          )
        new_donor.save()
        messagebox.showinfo("Donor Added", f"{fname} has been successfully added to database!")
        window1.after(100, window1.destroy)
    
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
        if val==0:
            return 'Regular'
        elif val==1:
            return 'Occassional'
        else:
            return 'Never'
              
    # function to upload document
    # def UploadDoc():
    #     global file_path
    #     global file_label
    #     file_path = filedialog.askopenfilename(initialdir="/", title="Select Document", filetypes=(("All Files", ".png;.jpg;.jpeg;.txt"), ("all files", ".*")))
    #     if file_path:
    #         file_label.config(text=f"File Selected: {file_path}")

    # Donor Form Window Geometry
            
    window1 = Tk()
    window1.title('Donor Registration')
    window1.geometry('1600x1500')
    window1.config(bg='Light gray')

    # Frame of Donor Form

    frame1 = Frame(window1, width=300, height=900, highlightbackground='black', highlightthickness=1.5)
    frame1.grid(padx=290, pady=60)

    # Section 1 - Personal Information

    Label(frame1, text='Personal information : ', font=('Helvetica', 10, 'bold')).grid(row=0, columnspan=10)
    Label(frame1, text='First Name : ').grid(row=3)
    Label(frame1, text='Middle Name : ').grid(row=4)
    Label(frame1, text='Last Name : ').grid(row=5)
    Label(frame1, text='Age : ').grid(row=6)
    Label(frame1, text='Contact number : ').grid(row=7)
    Label(frame1, text='Email id : ').grid(row=8)
    Label(frame1, text='Address : ').grid(row=9,sticky='n')
    Label(frame1, text='Gender : ').grid(row=11)

    global gender_var
    gender_var = IntVar()
    Radiobutton(frame1, text='Male', variable=gender_var,value=0,command=gender_radio_used).grid(row=11, column=1,sticky='w')
    Radiobutton(frame1, text='Female',variable=gender_var, value=1,command=gender_radio_used).grid(row=11, column=2,sticky='w')
    Radiobutton(frame1, text='Other',variable=gender_var,value=2,command=gender_radio_used).grid(row=11, column=3,sticky='w')

    e1 = Entry(frame1,width=60)
    e1.grid(row=3, column=1,sticky='w',pady=(3, 0))
    e2 = Entry(frame1,width=60)
    e2.grid(row=4, column=1,sticky='w',pady=(3, 0))
    e3 = Entry(frame1,width=60)
    e3.grid(row=5, column=1,sticky='w',pady=(3, 0))
    e4=Spinbox(frame1,width=3,from_= 0, to = 100)
    e4.grid(row=6,column=1,sticky='w',pady=(3, 0))
    e5 = Entry(frame1,width=60)
    e5.grid(row=7, column=1,sticky='w',pady=(3, 0))
    e6 = Entry(frame1,width=60)
    e6.grid(row=8, column=1,sticky='w',pady=(3, 0))
    e7 = Text(frame1, height=2, width=45)
    e7.grid(row=9,column=1,sticky='w',pady=(3, 0))

    # Section 2 - Medical Information

    Label(frame1, text='Medical information', font=('Helvetica', 10, 'bold')).grid(row=12, columnspan=10)
    Label(frame1, text='Blood Type : ').grid(row=13, column=0)
    Label(frame1, text='Organ to Donate : ').grid(row=14, column=0)
    Label(frame1, text='Medical Conditions : ').grid(row=15, column=0)

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
    Checkbutton(frame1, text='Diabetes', command=medical_condition, onvalue='Diabetes').grid(row=15, column=1,sticky='w')
    Checkbutton(frame1, text='Asthma', command=medical_condition, onvalue='Asthma').grid(row=15, column=2,sticky='w')
    Checkbutton(frame1, text='Cataract', command=medical_condition, onvalue='Cataract').grid(row=15, column=3,sticky='w')
    Checkbutton(frame1, text='Arthritis',command=medical_condition, onvalue='Arthritis').grid(row=15, column=4,sticky='w')

    Label(frame1, text='Previous Surgeries :').grid(row=16, column=0)
    previous_surgeries_entry = Text(frame1, height=2, width=50)
    previous_surgeries_entry.grid(row=16, column=1, columnspan=2,pady=(3, 0),sticky='w')

    Label(frame1, text='Medications Currently Taking : ').grid(row=17, column=0)
    medications_entry = Text(frame1, height=2, width=50)
    medications_entry.grid(row=17, column=1, columnspan=2,pady=(3, 0),sticky='w')

    Label(frame1, text='Allergies : ').grid(row=18, column=0)
    allergies_entry = Text(frame1, height=2, width=50)
    allergies_entry.grid(row=18, column=1, columnspan=2,pady=(3, 0),sticky='w')

    # Section 3 - Lifestyle Information

    Label(frame1, text='Lifestyle information : ', font=('Helvetica', 10, 'bold')).grid(row=19, columnspan=10,pady=(10,0))
    Label(frame1, text='Smoking : ').grid(row=21, column=0)

    # Checkbutton(frame1).grid(row=22,column=0,sticky='e')
    # Label(frame1, text='I accept the Terms and Conditions of the Donor Registration Agreement and the National Organ Donation Committee policy').grid(row=22, column=1)

    global smoking
    smoking = IntVar()
    Radiobutton(frame1,text='Regular',variable=smoking,value=0,command=lifestyle_info_used).grid(row=21,column=1,sticky='w')
    Radiobutton(frame1,text='Occassional',variable=smoking,value=1,command=lifestyle_info_used).grid(row=21,column=2,sticky='w')
    Radiobutton(frame1,text='Never',variable=smoking,value=2,command=lifestyle_info_used).grid(row=21,column=3,sticky='w')

    # Upload and Submit Buttons

    # uploadDocument=Button(frame1,text='Upload Death Certificate', font=('Helvetica', 10, 'bold'), fg='Black', bg='Medium Purple',command=UploadDoc,width=20)
    # uploadDocument.grid(row=23,column=1,pady=20)

    submitButton = Button(frame1,text='Submit', font=('Helvetica', 10, 'bold'), fg='Black', bg='Medium Purple',
                          command= onAddDonor,width=20)
    submitButton.grid(row=25,column=1,columnspan=2)

    mainwindow.withdraw()


# Hospital Screen
def HospitalScreen():
    global window2

    def find_matching_donors():
        organ_required = organ_var.get()
        blood_type = blood_type_var.get()

        if organ_required and blood_type:
            matching_donors = Donor.objects.filter(organ_to_donate=organ_required, bloodGrp=blood_type)

            eligible_donor_window = Tk()
            eligible_donor_window.title('Eligible Donors')
            eligible_donor_window.geometry('800x600')

            canvas = Canvas(eligible_donor_window)
            canvas.pack(side=LEFT, fill=BOTH, expand=True)

            scrollbar = Scrollbar(eligible_donor_window, orient=VERTICAL, command=canvas.yview)
            scrollbar.pack(side=RIGHT, fill=Y)

            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

            inner_frame = Frame(canvas)
            canvas.create_window((0, 0), window=inner_frame, anchor='nw')

            Label(inner_frame, text='Eligible Donors:', font=('Helvetica', 16, 'bold')).pack()

            for donor in matching_donors:
                details_frame = Frame(inner_frame, bd=1, relief=SOLID)
                details_frame.pack(pady=10, padx=10, fill=X)

                Label(details_frame, text=f"Name: {donor.firstName} {donor.middleName} {donor.lastName}", font=('Helvetica', 12, 'bold')).pack(anchor='w')
                Label(details_frame, text=f"Age: {donor.ageOfDonor}", font=('Helvetica', 10)).pack(anchor='w')
                Label(details_frame, text=f"Contact Number: {donor.contact_number}", font=('Helvetica', 10)).pack(anchor='w')
                Label(details_frame, text=f"Email: {donor.emailIdOfDonor}", font=('Helvetica', 10)).pack(anchor='w')
                Label(details_frame, text=f"Address: {donor.addressOfDonor}", font=('Helvetica', 10)).pack(anchor='w')
                Label(details_frame, text=f"Gender: {donor.genderOfDonor}", font=('Helvetica', 10)).pack(anchor='w')
                Label(details_frame, text=f"Blood Group: {donor.bloodGrp}", font=('Helvetica', 10)).pack(anchor='w')
                Label(details_frame, text=f"Organ to Donate: {donor.organ_to_donate}", font=('Helvetica', 10)).pack(anchor='w')
                Label(details_frame, text=f"Medical Conditions: {donor.medicalConditions}", font=('Helvetica', 10)).pack(anchor='w')
                Label(details_frame, text=f"Previous Surgeries: {donor.previousSurgery}", font=('Helvetica', 10)).pack(anchor='w')
                Label(details_frame, text=f"Medications: {donor.medicationEntries}", font=('Helvetica', 10)).pack(anchor='w')
                Label(details_frame, text=f"Allergies: {donor.allergyEntries}", font=('Helvetica', 10)).pack(anchor='w')
                Label(details_frame, text=f"Smoking Status: {donor.smokingStatus}", font=('Helvetica', 10)).pack(anchor='w')

            canvas.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

            eligible_donor_window.mainloop()
        else:
            messagebox.showerror("Error", "Please select both organ required and blood type.")


    window2 = Tk()
    window2.title('Hospital Screen')
    window2.geometry('600x400')

    Label(window2, text='Organ Required:').pack()
    organ_options = ['Heart', 'Liver', 'Kidney', 'Lung', 'Pancreas', 'Intestine', 'Eyes']
    organ_var = StringVar()
    organ_dropdown = OptionMenu(window2, organ_var, *organ_options)
    organ_dropdown.pack()

    Label(window2, text='Blood Type of Patient:').pack()
    blood_type_options = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    blood_type_var = StringVar()
    blood_type_dropdown = OptionMenu(window2, blood_type_var, *blood_type_options)
    blood_type_dropdown.pack()

    find_button = Button(window2, text='Find Donors', command=find_matching_donors)
    find_button.pack()

    window2.mainloop()


# Main Screen 

mainwindow = Tk()
mainwindow.title('Organ Donation')
mainwindow.geometry('1000x1000')

mainImagePath="img2.jpg"
img=Image.open(mainImagePath)
img=img.resize((1000,1000))

img_tk = ImageTk.PhotoImage(img)

img_label = Label(mainwindow, image=img_tk)
img_label.place(x=0, y=0, relwidth=1, relheight=1) 

img_label.image = img_tk
    
btn1 = Button(text='Register for Organ Donation', fg='white', bg='blue', font=('Helvetica', 12),
              command=RegisterForOrganDonation)
btn1.place(x=500, y=300)

btn2 = Button(text='Get Eligible Organ Donors', fg='white', bg='blue', font=('Helvetica', 12),
              command=HospitalScreen)
btn2.place(x=750, y=300)

mainwindow.mainloop()