from tkinter import*
'''
create window 
widegets
action 
'''
# creat main window

root = Tk()
root.title("First Program")
root.geometry("500x500")


def buttonfunc():
    INPUTusername = username.get()
    if(INPUTusername =="Ali Abdelhakem"):
        INPUTpass = password.get()
        Outputpass.place(relx=0.1 , rely=0.3)
        if(INPUTpass == "123"):
            Outputpass.insert(0,'Hello Ali                          ')
            Pin0Output.place(relx=0.65 , rely=0.1)
            Pin0Input.place(relx=0.85 , rely=0.1)
            pin0label.place(relx=0.5 , rely=0.1)
            Pin1Output.place(relx=0.65 , rely=0.15)
            Pin1Input.place(relx=0.85 , rely=0.15)
            pin1label.place(relx=0.5 , rely=0.15)
            Pin2Output.place(relx=0.65 , rely=0.2)
            Pin2Input.place(relx=0.85 , rely=0.2)
            pin2label.place(relx=0.5 , rely=0.2)
            Pin3Output.place(relx=0.65 , rely=0.25)
            Pin3Input.place(relx=0.85 , rely=0.25)
            pin3label.place(relx=0.5 , rely=0.25)
            Pin4Output.place(relx=0.65 , rely=0.3)
            Pin4Input.place(relx=0.85 , rely=0.3)
            pin4label.place(relx=0.5 , rely=0.3)
            Pin5Output.place(relx=0.65 , rely=0.35)
            Pin5Input.place(relx=0.85 , rely=0.35)
            pin5label.place(relx=0.5 , rely=0.35)
            Pin6Output.place(relx=0.65 , rely=0.4)
            Pin6Input.place(relx=0.85 , rely=0.4)
            pin6label.place(relx=0.5 , rely=0.4)
            Pin7Output.place(relx=0.65 , rely=0.45)
            Pin7Input.place(relx=0.85 , rely=0.45)
            pin7label.place(relx=0.5 , rely=0.45)
            button.place(relx=0.75 , rely=0.5)
        else:
            Outputpass.insert( 0,'Wrong Password            ')
    else:
        Outputpass.insert(0,'Wrong Username            ')
        Outputpass.place(relx=0.1 , rely=0.3)
                

def selection():
    global DDRA
    DDRA='0b'
    Pin0selec=Pin0Variable.get()
    Pin1selec=Pin1Variable.get()
    Pin2selec=Pin2Variable.get()
    Pin3selec=Pin3Variable.get()
    Pin4selec=Pin4Variable.get()
    Pin5selec=Pin5Variable.get()
    Pin6selec=Pin6Variable.get()
    Pin7selec=Pin7Variable.get()
    DDRA= DDRA+str(Pin0selec)+str(Pin1selec)+str(Pin2selec)+str(Pin3selec)+str(Pin4selec)+str(Pin5selec)+str(Pin6selec)+str(Pin7selec)
    
def Generate():
  file1 = open("E:\\ITI\\03-python\\Simple GUI Project\\DDRAfile.txt",'w+')
  file1.write("void Init_PORTA_DIR (void)\n{")
  file1.write("\n\nDDRA = ")
  file1.write(DDRA)
  file1.write("\n\n")
  file1.write("}")
  label = Label(root,text="File Generated, Thanks")
  label.pack(side="bottom")
    

#creat lables
label = Label(root,text="AVR Project")
label.pack(side="top")

usernamelabel = Label(root,text="Enter Username")
usernamelabel.place(relx=0.1 , rely=0.05)
username =Entry(root  )
username.place(relx=0.1 , rely=0.1)

passlabel = Label(root,text="Enter Password")
passlabel.place(relx=0.1 , rely=0.15)
password =Entry(root,show='*')
password.place(relx=0.1 , rely=0.2)

#create button
button = Button(root , text="Enter",command=lambda:buttonfunc())
button.place(relx=0.1 , rely=0.25)

Outputpass = Entry(root,  bg = "light cyan")


Pin0Variable = IntVar()
Pin1Variable = IntVar()
Pin2Variable = IntVar()
Pin3Variable = IntVar()
Pin4Variable = IntVar()
Pin5Variable = IntVar()
Pin6Variable = IntVar()
Pin7Variable = IntVar()

pin0label =Label(root , text='Pin 0 Mode')
Pin0Output = Radiobutton(root,text ='Output' , variable=Pin0Variable , value =1, command=selection)
Pin0Input = Radiobutton(root ,text ='input' , variable=Pin0Variable , value =0, command=selection)

pin1label =Label(root , text='Pin 1 Mode')
Pin1Output = Radiobutton(root ,text ='Output' , variable=Pin1Variable , value =1, command=selection)
Pin1Input = Radiobutton(root ,text ='input' , variable=Pin1Variable , value =0, command=selection)

pin2label =Label(root , text='Pin 2 Mode')
Pin2Output = Radiobutton(root ,text ='Output' , variable=Pin2Variable , value =1, command=selection)
Pin2Input = Radiobutton(root ,text ='input' , variable=Pin2Variable , value =0, command=selection)

pin3label =Label(root , text='Pin 3 Mode')
Pin3Output = Radiobutton(root ,text ='Output' , variable=Pin3Variable , value =1, command=selection)
Pin3Input = Radiobutton(root ,text ='input' , variable=Pin3Variable , value =0, command=selection)

pin4label =Label(root , text='Pin 4 Mode')
Pin4Output = Radiobutton(root ,text ='Output' , variable=Pin4Variable , value =1, command=selection)
Pin4Input = Radiobutton(root ,text ='input' , variable=Pin4Variable , value =0, command=selection)

pin5label =Label(root , text='Pin 5 Mode')
Pin5Output = Radiobutton(root ,text ='Output' , variable=Pin5Variable , value =1, command=selection)
Pin5Input = Radiobutton(root ,text ='input' , variable=Pin5Variable , value =0, command=selection)

pin6label =Label(root , text='Pin 6 Mode')
Pin6Output = Radiobutton(root ,text ='Output' , variable=Pin6Variable , value =1, command=selection)
Pin6Input = Radiobutton(root ,text ='input' , variable=Pin6Variable , value =0, command=selection)

pin7label =Label(root , text='Pin 7 Mode')
Pin7Output = Radiobutton(root ,text ='Output' , variable=Pin7Variable , value =1, command=selection)
Pin7Input = Radiobutton(root ,text ='input' , variable=Pin7Variable , value =0, command=selection)

button = Button(root , text="Generate File",command=Generate)
root.mainloop()





