import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import json
import os.path
window=tk.Tk()
window.geometry("1000x700")
window.title("Student Record Keeping Application")
window.configure(bg="white")

# **********START TOP FRAME ***************
top_frame=ttk.Frame(window,width=1000,height=100)

top_frame.pack(fill="x")

ttk.Label(top_frame,text ="EXPLORE",font = ("Times New Roman",22),foreground='#17141D',background='aliceblue').place(x=10,y=0)
ttk.Label(top_frame,text ="YOUR",font = ("Times New Roman",22),foreground='#17141D',background='azure').place(x=10,y=30)
ttk.Label(top_frame,text ="POTENTIAL",font = ("Times New Roman",22),foreground='#17141D',background='azure').place(x=10,y=60)

l8=ttk.Label(top_frame,text ="CHITKARA UNIVERSITY",font = ("Times New Roman",22),foreground='#17141D',background='azure').pack()
ttk.Label(top_frame,text ="STUDENT DATABASE",font = ("Times New Roman",22),foreground='#17141D',background='azure').pack(pady=20)

# logo=ImageTk.PhotoImage(Image.open('ck.jpg'))
# logo_label=ttk.Label(top_frame,image=logo)
# logo_label.pack(side="right")
# **********END TOP FRAME ***************
# MIDEL FRAME
midel_frame=ttk.Frame(window,width=1000,height=500)
midel_frame.pack(fill="x")

for i in range(3):
    midel_frame.columnconfigure(i,weight=1)

frame1=ttk.Frame(midel_frame,width=100,height=500)
frame2=ttk.Frame(midel_frame,width=800,height=500)
frame3=ttk.Frame(midel_frame,width=100,height=500)

frame1.grid(row=0,column=0,sticky="w")
frame2.grid(row=0,column=1,sticky="nsew")
frame3.grid(row=0,column=2,sticky="e")

for i in range(3):
    frame2.columnconfigure(i,weight=1)



my_notebook=ttk.Notebook(frame2)
my_notebook.grid(row=0,column=0,sticky="ew")

new_student_frame=ttk.Frame(my_notebook,width=800,height=500)
new_student_frame.grid(row=1,column=0,sticky="ew")

display_frame=ttk.Frame(my_notebook,width=800,height=500)
display_frame.grid(row=1,column=0,sticky="ew")


course_creation_frame=ttk.Frame(my_notebook,width=800,height=500)
course_creation_frame.grid(row=1,column=0,sticky="ew")

display_course_frame=ttk.Frame(my_notebook,width=800,height=500)
display_course_frame.grid(row=1,column=0,sticky="ew")

course_allocation_frame=ttk.Frame(my_notebook,width=800,height=500)
course_allocation_frame.grid(row=1,column=0,sticky="ew")

my_notebook.add(new_student_frame,text="New Student")
my_notebook.add(display_frame,text="Display")
my_notebook.add(course_creation_frame,text="Course Creation")
my_notebook.add(display_course_frame,text="Display Course")
my_notebook.add(course_allocation_frame,text="Course Allocation")

#ADD CONTENT IN NEW STUDENT FRAME******************
#LABELS FOR NEW STUDENT FRAME
enter_name_label=ttk.Label(new_student_frame,text="Enter Your Name", font=("Arial",12))
enter_name_label.grid(row=0,column=0,sticky="w",pady=20,padx=80)

enter_rollno_label=ttk.Label(new_student_frame,text="Enter Your Rollno", font=("Arial",12))
enter_rollno_label.grid(row=1,column=0,sticky="w",pady=20,padx=80)

chose_gender_label=ttk.Label(new_student_frame,text="Chose your Gender", font=("Arial",12))
chose_gender_label.grid(row=2,column=0,sticky="w",pady=20,padx=80)

address_label=ttk.Label(new_student_frame,text="Address for Correspondence", font=("Arial",12))
address_label.grid(row=3,column=0,sticky="w",pady=20,padx=80)

phone_label=ttk.Label(new_student_frame,text="Phone No", font=("Arial",12))
phone_label.grid(row=4,column=0,sticky="w",pady=20,padx=80)

your_batch_label=ttk.Label(new_student_frame,text="Your Batch", font=("Arial",12))
your_batch_label.grid(row=5,column=0,sticky="w",pady=20,padx=80)

hostel_label=ttk.Label(new_student_frame,text="Hostel[Y/N]", font=("Arial",12))
hostel_label.grid(row=6,column=0,sticky="w",pady=20,padx=80)

#ENTRY BOX FOR NEW STUDENT FRAME
name_var=tk.StringVar()
name_entry=ttk.Entry(new_student_frame,width=50,textvariable=name_var)
name_entry.focus()
name_entry.grid(row=0,column=2,sticky="e",pady=20)

roll_var=tk.StringVar()
roll_entry=ttk.Entry(new_student_frame,width=50,textvariable=roll_var)
roll_entry.grid(row=1,column=2,sticky="e",pady=20)

gender_var=tk.StringVar()
gender_mail_radio=ttk.Radiobutton(new_student_frame,text="Male",value="Male",variable=gender_var)
gender_mail_radio.grid(row=2,column=2,sticky="w",pady=20)
gender_female_radio=ttk.Radiobutton(new_student_frame,text="Female",value="Female",variable=gender_var)
gender_female_radio.grid(row=2,column=2,sticky="e",pady=20)

address_var=tk.StringVar()
address_entry=ttk.Entry(new_student_frame,width=50,textvariable=address_var)
address_entry.grid(row=3,column=2,sticky="e",pady=20)

phone_var=tk.IntVar()
phone_entry=ttk.Entry(new_student_frame,width=50,textvariable=phone_var)
phone_entry.grid(row=4,column=2,sticky="e",pady=20)

batch_var=tk.StringVar()
batch_combo=ttk.Combobox(new_student_frame,width=50,textvariable=batch_var,state="readonly")
batch_combo["values"]=("Batch 2019","Batch 2020","Batch 2021")
batch_combo.current(0)
batch_combo.grid(row=5,column=2,sticky="e",pady=20)

hostel_check_var=tk.IntVar()
hostel_checkbox=ttk.Checkbutton(new_student_frame,text="Click if you need Hostel Faciality",variable=hostel_check_var)
hostel_checkbox.grid(row=6,column=2,sticky="e",pady=20)

#FUNCTION FOR SAVE STUDENT DATA
def saveData():
    name=name_var.get()
    roll=roll_var.get()
    gender=gender_var.get()
    address=address_var.get()
    phone=phone_var.get()
    batch=batch_var.get()
    if hostel_check_var.get()==0:
        hostel="false"
    else:
        hostel="true"
    data={"Rollno": roll, "Name": name, "Gender":gender, "address": address,
                    "Phone no": phone, "Batch": batch,"Hostel":hostel}
    with open('student.json') as f:
        json_str_data=f.read()
    json_data=eval(json_str_data)
    list_student=json_data['Students']
    list_student.append(data)
    with open('student.json','w') as file1:
        json.dump(json_data,file1)
    reload_fun()

    messagebox.showinfo("Save","Your record has been saved")
    return
def clear_student_data():
    name_entry.delete(0,tk.END)
    roll_entry.delete(0,tk.END)
    address_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)

save_new_studentdata=ttk.Button(new_student_frame,text="Save",command=saveData)
save_new_studentdata.grid(row=7,column=2,sticky="w",pady=20)

clear_new_studentdata=ttk.Button(new_student_frame,text="Clear",command=clear_student_data)
clear_new_studentdata.grid(row=7,column=2,sticky="e",pady=20)

#DISPLAY FRAME **********
with open("student.json") as f:
    json_str_data=f.read()
json_data=eval(json_str_data)
list_student=json_data['Students']

    
treestyle=ttk.Style()
treestyle.configure("mystyle.Treeview.Heading",font=("Georgia",10))
treestyle.layout("mystyle.Treeview",[("mystyle.Treeview.treearea",{'sticky':'ewns'})])

display_treeview=ttk.Treeview(display_frame,style="mystyle.Treeview")
display_treeview["columns"]=("name","gender","address","phone","batch","hostel")
display_treeview.column("#0",width=50,minwidth=25)
display_treeview.column("name",width=50,minwidth=25)
display_treeview.column("gender",width=50,minwidth=25)
display_treeview.column("address",width=50,minwidth=25)
display_treeview.column("phone",width=50,minwidth=25)
display_treeview.column("batch",width=50,minwidth=25)
display_treeview.column("hostel",width=50,minwidth=25)

display_treeview.heading("#0",text="Rollno",anchor="center")
display_treeview.heading("name",text="Name",anchor="center")
display_treeview.heading("gender",text="Gender",anchor="center")
display_treeview.heading("address",text="Address",anchor="center")
display_treeview.heading("phone",text="PhoneNo",anchor="center")
display_treeview.heading("batch",text="Batch",anchor="center")
display_treeview.heading("hostel",text="Hosteel",anchor="center")


for i in list_student:
    txt=i["Rollno"]
    name=i["Name"]
    gender=i["Gender"]
    address=i["address"]
    phone=i["Phone no"]
    batch=i["Batch"]
    hostel=i["Hostel"]
    display_treeview.insert(parent="",index="end",text=txt,values=(name,gender,address,phone,batch,hostel))
def reload_fun():
    name=name_var.get()
    roll=roll_var.get()
    gender=gender_var.get()
    address=address_var.get()
    phone=phone_var.get()
    batch=batch_var.get()
    display_treeview.insert(parent="",index="end",text=roll,values=(name,gender,address,phone,batch,hostel))
    
display_treeview.pack(fill="both")


#ADD CONTENT IN COURSES FRAME**********
#LABEL
courseId_label=ttk.Label(course_creation_frame,text="Course ID", font=("Arial",12))
courseId_label.grid(row=0,column=0,sticky="w",pady=20,padx=80)

courseName_label=ttk.Label(course_creation_frame,text="Course Name", font=("Arial",12))
courseName_label.grid(row=1,column=0,sticky="w",pady=20,padx=80)

#ENTRY BOX
courseId_var=tk.StringVar()
courseId_entry=ttk.Entry(course_creation_frame,width=50,textvariable=courseId_var)
courseId_entry.focus()
courseId_entry.grid(row=0,column=1,sticky="e",pady=20)

courseName_var=tk.StringVar()
courseName_entry=ttk.Entry(course_creation_frame,width=50,textvariable=courseName_var)
courseName_entry.grid(row=1,column=1,sticky="e",pady=20)

#save & clear
#function for save course data
def courseData():
    courseid=courseId_var.get()
    coursename1=courseName_var.get()
    courseDict={"CourseID": courseid, "CourseName": coursename1}

    with open('course.json') as f:
        json_str_data=f.read()
    json_data=eval(json_str_data)
    list_student=json_data['Courses']
    list_student.append(courseDict)
    with open('course.json','w') as file1:
        json.dump(json_data,file1)
    messagebox.showinfo("Save","Your record has been saved")
    reload_course()
    return
def clear_course():
    courseId_entry.delete(0,tk.END)
    courseName_entry.delete(0,tk.END)
    return

save_course_data=ttk.Button(course_creation_frame,text="Save",command=courseData)
save_course_data.grid(row=3,column=1,sticky="w",pady=20)

clear_course_data=ttk.Button(course_creation_frame,text="Clear",command=clear_course)
clear_course_data.grid(row=3,column=1,sticky="e",pady=20)

#DISPLAY COURSES



display_course_treeview=ttk.Treeview(display_course_frame,style="mystyle.Treeview")
display_course_treeview["columns"]=("coursename","n")
display_course_treeview.column("#0",width=10)
display_course_treeview.column("coursename",width=100,minwidth=50)
display_course_treeview.column("n",width=100,minwidth=50)

display_course_treeview.heading("#0",text="")
display_course_treeview.heading("coursename",text="CourseID",anchor="w")
display_course_treeview.heading("n",text="Course Name",anchor="w")

filename1="course.json"
if os.path.isfile(filename1):
    with open(filename1) as f:
        json_str_course_data=f.read()
        json_course_data=json.loads(json_str_course_data)
    list_course=json_course_data["Courses"]
    for i in list_course:
        txt1=i["CourseID"]
        
        
        display_course_treeview.insert(parent="",index="end",text='',values=(i["CourseID"],i["CourseName"]))

def reload_course():
    courseid=courseId_var.get()
    coursename1=courseName_var.get()
    display_course_treeview.insert(parent="",index="end",text="",values=(courseid,coursename1))
    return
display_course_treeview.pack(fill="both")

#START FOR COURSE ALLOCATION FRAME************
#LABELS FOR ALLOCATION FRAME
allocate_student_rollno_label=ttk.Label(course_allocation_frame,text="Student Rollno", font=("Arial",12))
allocate_student_rollno_label.grid(row=0,column=0,sticky="w",pady=20,padx=80)

allocate_courseName_label=ttk.Label(course_allocation_frame,text="Course Name", font=("Arial",12))
allocate_courseName_label.grid(row=1,column=0,sticky="w",pady=20,padx=80)

#ENTRY FOR ALLOCATION FRAME
allocate_studentroll_var=tk.StringVar()
allocate_studentroll_entry=ttk.Entry(course_allocation_frame,width=50,textvariable=allocate_studentroll_var)
allocate_studentroll_entry.focus()
allocate_studentroll_entry.grid(row=0,column=1,sticky="e",pady=20)

courses=[]
filename="course.json"
if os.path.isfile(filename):
    with open(filename) as f:
        temp=f.read()
        data=json.loads(temp)
    listof_course=data["Courses"]
    for i in listof_course:
        courses.append(i["CourseName"])
    

allocate_courseName_var=tk.StringVar()
allocate_courseName_menu=ttk.OptionMenu(course_allocation_frame,allocate_courseName_var,*courses)
allocate_courseName_menu.config(width=40)
allocate_courseName_menu.grid(row=1,column=1,sticky="e",pady=20)

#save & clear for allocation frame
def allocateData():
    studentroll=allocate_studentroll_var.get()
    studentcourse=allocate_courseName_var.get()

    with open("course.json") as f:
        json_str_data=f.read()
    json_data=eval(json_str_data)
    list_student=json_data["Courses"]
    for i in list_student:
        if i["CourseName"]==studentcourse:
            course_id=i["CourseID"]
    allocationDict={"Rollno": studentroll, "CourseID":course_id } 
    with open('allocation.json') as f:
        json_str_data=f.read()
    json_data=eval(json_str_data)
    list_student=json_data['Stu_Course']
    list_student.append(allocationDict)
    with open('allocation.json','w') as file1:
        json.dump(json_data,file1)
    messagebox.showinfo("Allocate","Your record has been Allocated!!")

allocate_course=ttk.Button(course_allocation_frame,text="Allocate",command=allocateData)
allocate_course.grid(row=2,column=1,sticky="w",pady=20)

#START DISPLAY FRAME***************


#BOTTTOM FRAME 
bottom_frame=ttk.Frame(window,width=1000,height=100)
bottom_frame.pack(fill="both")


window.mainloop()