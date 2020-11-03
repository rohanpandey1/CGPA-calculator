from tkinter import *
import tkinter.messagebox as tmsg
# ####################################################### marks visualisation ####################################
def plot_sem1():
    import matplotlib.pyplot as plt
    x = [int(sub1ent.get()),int(sub2ent.get()),int(sub3ent.get()),int(sub4ent.get()),int(sub5ent.get()),int(sub6ent.get()),int(sub7ent.get())]
    index=range(len(x))
    plt.title("Marks of first sem")
    plt.bar(index,x,label="SEM 1")
    plt.xlabel("subjects")
    plt.ylabel("Marks")
    plt.title("Marks Comparision")
    plt.show()
def plot_sem2():
    import matplotlib.pyplot as plt
    x = [int(sub1ent2.get()),int(sub2ent2.get()),int(sub3ent2.get()),int(sub4ent2.get()),int(sub5ent2.get()),int(sub6ent2.get()),int(sub7ent2.get())]
    index=range(len(x))
    plt.title("Marks of first sem")
    plt.bar(index,x,label="SEM 2")
    plt.xlabel("subjects")
    plt.ylabel("Marks")
    plt.title("Marks Comparision")
    plt.show()
#
# ################################### to discard inputs ##########################################################
def entry_delete():
    sub1ent.delete(first=0,last=50)
    sub2ent.delete(first=0, last=50)
    sub3ent.delete(first=0, last=50)
    sub4ent.delete(first=0, last=50)
    sub5ent.delete(first=0, last=50)
    sub6ent.delete(first=0, last=50)
    sub7ent.delete(first=0, last=50)
    sub1ent2.delete(first=0, last=50)
    sub2ent2.delete(first=0, last=50)
    sub3ent2.delete(first=0, last=50)
    sub4ent2.delete(first=0, last=50)
    sub5ent2.delete(first=0, last=50)
    sub6ent2.delete(first=0, last=50)
    sub7ent2.delete(first=0, last=50)


root=Tk()
root.geometry("900x600")
root.config(bg='wheat3')

####################################################### frames used ################################################################
Label(root,text="CGPA-CALCULATOR",font="helvatica 25 bold italic",pady=15,fg="wheat3",bg="black").grid(row=2)

f4=Frame(root,borderwidth=3,relief=SUNKEN,bg="black")
f4.grid(row=3)

f2=Frame(root,borderwidth=3,relief=SUNKEN,bg="black")
f2.grid(row=5)

f3=Frame(root,borderwidth=3,relief=SUNKEN,bg="black")
f3.grid(row=6,column=7)
######################################################button for plotting #################################################
plot1=Label(f2,text="DO you want to see marks comparision among all subjects?",fg="wheat3",bg="black")
plot1.grid()
Button(f2,text="Click here for SEM 1",command=plot_sem1,fg="wheat3",bg="black",borderwidth=8).grid(row=1,column=0,pady=10)
Button(f2,text="Click here for SEM 2",command=plot_sem2,fg="wheat3",bg="black",borderwidth=8).grid(row=1,column=1,pady=10)
#################################################### function to calculate CGPA ################################################
def cgpa_calculator():
    if(len(sub1ent.get())==0 or len(sub2ent.get())==0 or len(sub3ent.get())==0 or len(sub4ent.get())==0 or len(sub5ent.get())==0 or len(sub6ent.get())==0 or len(sub7ent.get())==0 or len(sub1ent2.get())==0 or len(sub2ent2.get())==0 or len(sub3ent2.get())==0 or len(sub4ent2.get())==0 or len(sub5ent2.get())==0 or len(sub6ent2.get())==0 or len(sub7ent2.get())==0):
        tmsg.showwarning("Warning","Fill marks of all the subjects")


    tmsg.showinfo("msg","Write credits of first semester and second semester in console window")
    credit1=[]
    credit2 = []
    marks1 = [int(sub1ent.get()),int(sub2ent.get()),int(sub3ent.get()),int(sub4ent.get()),int(sub5ent.get()),int(sub6ent.get()),int(sub7ent.get())]
    marks2 = [int(sub1ent2.get()),int(sub2ent2.get()),int(sub3ent2.get()),int(sub4ent2.get()),int(sub5ent2.get()),int(sub6ent2.get()),int(sub7ent2.get())]

    tgpa1,first1,first2,i=0,0,0,0
    tgpa2,second1, second2,i1 =0,0,0,0
    print("Enter 7 credits of first semester")
    y=0
    while (y <7):
        credit= int(input(""))
        credit1.append(credit)
        y = y +1

    while (i < 7):
        first1 += credit1[i] * marks1[i]
        first2 += credit1[i]
        i = i + 1
    tgpa1=first1/first2

    print("Enter 7 credits of second semester")
    y1 = 0
    while (y1 < 7):
        credit = int(input(""))
        credit2.append(credit)
        y1 = y1 + 1
    print("Open gui window again")

    while (i1 < 7):
        second1 += credit2[i1] * marks2[i1]
        second2 += credit2[i1]
        i1 = i1 + 1
    tgpa2=second1/second2

    my_label.config(text=f"TGPA Of sem 1 is {int(tgpa1)}")
    my_label2.config(text=f"TGPA os sem 2 is {int(tgpa2)}")

    tmsg.askyesno(title="CGPA",message="Do you want to know CGPA?")
    cgpa=(tgpa1+tgpa2)//2
    grade=''
    if int(cgpa) == 10:
        grade='O'
    elif int(cgpa) ==  9:
        grade = 'A+'
    elif int(cgpa) ==  8:
        grade = 'A'
    elif int(cgpa) ==  7:
        grade = 'B+'
    elif int(cgpa) ==  6:
        grade = 'B'
    elif int(cgpa) ==  5:
        grade = 'C+'
    elif int(cgpa) ==  4:
        grade="congratulations! You have reappaer"
    else:
        grade="Great! You got fail"
    tmsg.showinfo("CGPA",f"CGPA is {cgpa} and grade is {grade}")


########################################################### heading and labels used #############################################################
Label(f4,text="Enter Grades of first Semester and second Semester",fg="wheat3",bg="black",font="helvatica 20 bold italic").grid(row=0,column=1)
Label(f4,text="Sem 1(0-10)",fg="wheat3",bg="black").grid(row=1,column=1)
Label(f4,text="Sem 2(0-10)",fg="wheat3",bg="black").grid(row=1,column=2)
sub1=Label(f4,text="CSE211",fg="wheat3",bg="black")
sub2=Label(f4,text="CSE205",fg="wheat3",bg="black")
sub3=Label(f4,text="CSE320",fg="wheat3",bg="black")
sub4=Label(f4,text="INT213",fg="wheat3",bg="black")
sub5=Label(f4,text="INT306",fg="wheat3",bg="black")
sub6=Label(f4,text="MTH401",fg="wheat3",bg="black")
sub7=Label(f4,text="PEL135",fg="wheat3",bg="black")
sub1.grid(row=2,column=0)
sub2.grid(row=3,column=0)
sub3.grid(row=4,column=0)
sub4.grid(row=5,column=0)
sub5.grid(row=6,column=0)
sub6.grid(row=7,column=0)
sub7.grid(row=8,column=0)
##################################################variable for sem 1###########################################
sub1val=StringVar()
sub2val=StringVar()
sub3val=StringVar()
sub4val=StringVar()
sub5val=StringVar()
sub6val=StringVar()
sub7val=StringVar()
#############################################entry widget for sem1 #############################################
sub1ent=Entry(f4,textvariable=sub1val,fg="wheat3",bg="black",insertbackground='wheat3')
sub2ent=Entry(f4,textvariable=sub2val,fg="wheat3",bg="black",insertbackground='wheat3')
sub3ent=Entry(f4,textvariable=sub3val,fg="wheat3",bg="black",insertbackground='wheat3')
sub4ent=Entry(f4,textvariable=sub4val,fg="wheat3",bg="black",insertbackground='wheat3')
sub5ent=Entry(f4,textvariable=sub5val,fg="wheat3",bg="black",insertbackground='wheat3')
sub6ent=Entry(f4,textvariable=sub6val,fg="wheat3",bg="black",insertbackground='wheat3')
sub7ent=Entry(f4,textvariable=sub7val,fg="wheat3",bg="black",insertbackground='wheat3')
sub1ent.grid(row=2,column=1)
sub2ent.grid(row=3,column=1)
sub3ent.grid(row=4,column=1)
sub4ent.grid(row=5,column=1)
sub5ent.grid(row=6,column=1)
sub6ent.grid(row=7,column=1)
sub7ent.grid(row=8,column=1)


##################################################variable for sem2 ######################################
sub1val2=StringVar()
sub2val2=StringVar()
sub3val2=StringVar()
sub4val2=StringVar()
sub5val2=StringVar()
sub6val2=StringVar()
sub7val2=StringVar()
############################################3 entry widget for sem 2########################################
sub1ent2=Entry(f4,textvariable=sub1val2,fg="wheat3",bg="black",insertbackground='wheat3')
sub2ent2=Entry(f4,textvariable=sub2val2,fg="wheat3",bg="black",insertbackground='wheat3')
sub3ent2=Entry(f4,textvariable=sub3val2,fg="wheat3",bg="black",insertbackground='wheat3')
sub4ent2=Entry(f4,textvariable=sub4val2,fg="wheat3",bg="black",insertbackground='wheat3')
sub5ent2=Entry(f4,textvariable=sub5val2,fg="wheat3",bg="black",insertbackground='wheat3')
sub6ent2=Entry(f4,textvariable=sub6val2,fg="wheat3",bg="black",insertbackground='wheat3')
sub7ent2=Entry(f4,textvariable=sub7val2,fg="wheat3",bg="black",insertbackground='wheat3')
sub1ent2.grid(row=2,column=2)
sub2ent2.grid(row=3,column=2)
sub3ent2.grid(row=4,column=2)
sub4ent2.grid(row=5,column=2)
sub5ent2.grid(row=6,column=2)
sub6ent2.grid(row=7,column=2)
sub7ent2.grid(row=8,column=2)


##########################################################discard and click to cpga button #####################################################
my_button = Button(f4,text="Click! to find CGPA", command=cgpa_calculator ,bg="black",fg="wheat3",borderwidth=8)
my_label = Label(f4,text="TGPA SEM 1",bg="black",fg="wheat3")
my_label2 = Label(f4,text="TGPA sem 2",bg="black",fg="wheat3")
my_label.grid(row=9,column=1)
my_label2.grid(row=9,column=2)
my_button.grid(row=10,column=1)
B=Button(f4, text="Discard values", command=entry_delete,bg="black",fg="wheat3",borderwidth=8)
B.grid(row=10,column=2,pady=23,padx=23)
root.mainloop()