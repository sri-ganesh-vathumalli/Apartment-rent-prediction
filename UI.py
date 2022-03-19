from tkinter import *
from tkinter import messagebox
from main import Model
model=Model()
#main screen
screen=Tk()
screen.title('Steet Easy Rent Predictor')
screen.geometry('700x700')

#frame1
outer_frame11=Frame(screen)
outer_frame11.config(height=350,width=350,bg='lightgray')
outer_frame11.place(x=0,y=0)
outer_frame12=Frame(screen)
outer_frame12.config(height=350,width=350,bg='navy')
outer_frame12.place(x=0,y=350)
outer_frame21=Frame(screen)
outer_frame21.config(height=350,width=350,bg='navy')
outer_frame21.place(x=350,y=0)
outer_frame22=Frame(screen)
outer_frame22.config(height=350,width=350,bg='lightgray')
outer_frame22.place(x=350,y=350)
#frame 2
outer_frame2=Frame(screen)
outer_frame2.config(height=680,width=680,bg='black')
outer_frame2.place(x=10,y=10)

#TESTING WELCOME SCREEN

#
#frame 3
frame=Frame(screen)
frame.config(height=660,width=660,bg='lavender')
frame.place(x=20,y=20)

b='lavender'

#TITLE
name1=Label(screen)
name1.config(text='StreetEasy',fg='navy',font='times 26',bg=b)
name1.place(x=40,y=40)
name2=Label(screen)
name2.config(text='Apartment Rent prediction',fg='navy',font='times 26',bg=b)
name2.place(x=40,y=80)

#location
location=Label(screen)
location.config(text='Select Location',fg='red',bg=b,font='times 15')
location.place(x=500,y=50)
loc=StringVar()
choices={'Brooklyn','Queens','Manhattan'}
loc.set('Select')
drop=OptionMenu(screen,loc,*choices)
drop.config(bg=b,fg='navy',font='times 15')
drop.place(x=500,y=80)
#prediction button
def predict():
    if loc.get()=='Select':
        messagebox.showerror("Error", "Location is Mandatory \n Please select a valid location")
    else:
        try:
            accuracy1,accuracy2=model.train_model(loc.get())
            """"'bedrooms', 'bathrooms',
            'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee',
            'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator',
            'has_dishwasher', 'has_patio', 'has_gym"""
            options=[int(bedrooms_req.get()),int(bathrooms_req.get()),float(size_req.get()),float(subway_req.get()),int(floor_req.get()),
                         float(building_age_req.get()),maintenance_req.get(),rooftop_req.get(),washer_req.get(),doorman_req.get(),elevator_req.get(),
                         dishwasher_req.get(),patio_req.get(),gym_req.get()]
            for i in options:
                print(type(i))
            price1,price2=model.predict(options)

            print_prediction(price1[0],price2,accuracy1,accuracy2)
        except:
            messagebox.showerror('Invalid data','Few key is missing or invalid\n Please correct and then Retry')
button1=Button(screen)
button1.config(text='Predict',bg='springgreen2',fg='white',font='times 15',command=predict)
button1.place(x=400,y=600)
#
#labels
size=Label(screen)
size.config(bg=b,fg='green',text='Size in Sqft',font='times 14')
size.place(x=50,y=140)
bedrooms=Label(screen)
bedrooms.config(bg=b,fg='green',text='Bedrooms',font='times 14')
bedrooms.place(x=50,y=170)
subway=Label(screen)
subway.config(bg=b,fg='green',text='time to subway',font='times 14')
subway.place(x=50,y=200)
floor=Label(screen)
floor.config(bg=b,fg='green',text='floor',font='times 14')
floor.place(x=50,y=230)
building_age=Label(screen)
building_age.config(bg=b,fg='green',text='Building age',font='times 14')
building_age.place(x=50,y=290)
bathrooms=Label(screen)
bathrooms.config(bg=b,fg='green',text='Bathrooms',font='times 14')
bathrooms.place(x=50,y=260)
fee=Label(screen)
fee.config(bg=b,fg='green',text='Maintenance Fee',font='times 14')
fee.place(x=50,y=320)
rooftop=Label(screen)
rooftop.config(bg=b,fg='green',text='Rooftop',font='times 14')
rooftop.place(x=50,y=350)
washer=Label(screen)
washer.config(bg=b,fg='green',text='Washer/Laundry',font='times 14')
washer.place(x=50,y=380)
doorman=Label(screen)
doorman.config(bg=b,fg='green',text='Doorman',font='times 14')
doorman.place(x=50,y=410)
elevator=Label(screen)
elevator.config(bg=b,fg='green',text='Elevator',font='times 14')
elevator.place(x=50,y=440)
dishwasher=Label(screen)
dishwasher.config(bg=b,fg='green',text='Dishwasher',font='times 14')
dishwasher.place(x=50,y=470)
patio=Label(screen)
patio.config(bg=b,fg='green',text='Patio',font='times 14')
patio.place(x=50,y=500)
gym=Label(screen)
gym.config(bg=b,fg='green',text='Gym',font='times 14')
gym.place(x=50,y=530)
#
#entry boxes
size_req=Entry(screen)
size_req.config(bg='snow',font='times 14',width=20)
size_req.place(x=300,y=140)

bedrooms_req=Spinbox(screen)
bedrooms_req.config(bg='snow',font='times 14',from_=1,to=30)
bedrooms_req.place(x=300,y=170)

subway_req=Entry(screen)
subway_req.config(bg='snow',font='times 14',width=20)
subway_req.place(x=300,y=200)

floor_req=Spinbox(screen)
floor_req.config(bg='snow',font='times 14',from_=0,to=100)
floor_req.place(x=300,y=230)

bathrooms_req=Spinbox(screen)
bathrooms_req.config(bg='snow',font='times 14',from_=1,to=30)
bathrooms_req.place(x=300,y=260)

building_age_req=Entry(screen)
building_age_req.config(bg='snow',font='times 14',width=20)
building_age_req.place(x=300,y=290)

maintenance_req=IntVar()
r1=Radiobutton(screen,text='no fee',value=1,var=maintenance_req,font='times 14',bg=b)
r1.place(x=450,y=320)
r2=Radiobutton(screen,text='fee applicable',value=0,var=maintenance_req,font='times 14',bg=b)
r2.place(x=300,y=320)

rooftop_req=IntVar()
r3=Radiobutton(screen,text='has rooftop',value=1,var=rooftop_req,font='times 14',bg=b)
r3.place(x=300,y=350)
r4=Radiobutton(screen,text='no rooftop',value=0,var=rooftop_req,font='times 14',bg=b)
r4.place(x=450,y=350)

washer_req=IntVar()
r5=Radiobutton(screen,text='has washer',value=1,var=washer_req,font='times 14',bg=b)
r5.place(x=300,y=380)
r6=Radiobutton(screen,text='no washer',value=0,var=washer_req,font='times 14',bg=b)
r6.place(x=450,y=380)

doorman_req=IntVar()
r7=Radiobutton(screen,text='has doorman',value=1,var=doorman_req,font='times 14',bg=b)
r7.place(x=300,y=410)
r8=Radiobutton(screen,text='no doorman',value=0,var=doorman_req,font='times 14',bg=b)
r8.place(x=450,y=410)

elevator_req=IntVar()
r9=Radiobutton(screen,text='has elevator',value=1,var=elevator_req,font='times 14',bg=b)
r9.place(x=300,y=440)
r10=Radiobutton(screen,text='no elevator',value=0,var=elevator_req,font='times 14',bg=b)
r10.place(x=450,y=440)

dishwasher_req=IntVar()
r11=Radiobutton(screen,text='has dishwasher',value=1,var=dishwasher_req,font='times 14',bg=b)
r11.place(x=300,y=470)
r12=Radiobutton(screen,text='no dishwasher',value=0,var=dishwasher_req,font='times 14',bg=b)
r12.place(x=450,y=470)

patio_req=IntVar()
r13=Radiobutton(screen,text='has patio',value=1,var=patio_req,font='times 14',bg=b)
r13.place(x=300,y=500)
r14=Radiobutton(screen,text='no patio',value=0,var=patio_req,font='times 14',bg=b)
r14.place(x=450,y=500)

gym_req=IntVar()
r15=Radiobutton(screen,text='has gym',value=1,var=gym_req,font='times 14',bg=b)
r15.place(x=300,y=530)
r16=Radiobutton(screen,text='no gym',value=0,var=gym_req,font='times 14',bg=b)
r16.place(x=450,y=530)

#prediction price label
def print_prediction(price1,price2,accuracy1,accuracy2):
    if accuracy1-accuracy2 >=10 or accuracy2-accuracy1>=10:
        if accuracy1>accuracy2:
            accuracy=accuracy1
            price=price1
        else:
            accuracy=accuracy2
            price=price2
    else:
        price=(price2+price1)/2
        accuracy=max([accuracy2,accuracy1])

    if price>4000:
        c='red'
    if price>3000 and price<4000:
        c='orange'
    if price<3000:
        c='green'
    rent=Label(screen)
    rent.config(bg=b,fg='navy',font='times 20',text='Rent\npredicted')
    rent.place(x=50,y=590)
    pred=Label(screen)
    pred.config(bg=b,fg=c,font='times 25',text='$ '+str(round(price)))
    pred.place(x=200,y=600)
    acu=Label(screen)
    acu.config(bg=b,fg='steelblue',text='The predicted accuracy for the price is {}%'.format(round(accuracy*100,2)))
    acu.place(x=170,y=650)
#print_prediction(3320,0.77)
screen.mainloop()


