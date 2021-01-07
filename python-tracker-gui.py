from tkinter import Tk, Label, Button, Entry
from phonenumbers import *
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import phonenumbers 


class Location_Tracker:
    def __init__(self, App):
        self.window = App
        self.window.title("Phone number Tracker")
        self.window.geometry("500x400")
        self.window.configure(bg="#3f5efb")
        self.window.iconbitmap(r'C:\python\loc.ico')
        self.window.resizable(False, False) 

        #___________Application menu_____________
        Label(App, text="Enter a phone number",fg="white", font=("Times", 20), bg="#3f5efb").place(x=130,y= 30)
        self.phone_number = Entry(App,validate='all' , width=18, font=("Arial", 15), relief="flat")
        self.track_button = Button(App, text="Track Country", bg="#22c1c3", relief="sunken",font = ('Sans','10','bold'))
        self.country_label = Label(App,fg="white", font=("Times", 20), bg="#3f5efb")
        self.timezone_label = Label(App,fg="white", font=("Times", 20), bg="#3f5efb")
        self.svp_label = Label(App,fg="white", font=("Times", 20), bg="#3f5efb")
        self.clearbutton = Button(App,text="Clear", bg="#23d1c3",font = ('Sans','10','bold'),command=self.clearbtn)

        #___________Place widgets on the window______
        self.phone_number.place(x=150, y=120)
        self.phone_number.focus()
        self.track_button.place(x=200, y=170)
        self.country_label.place(x=200, y=230)
        self.timezone_label.place(x=200, y=275)
        self.svp_label.place(x=200, y=325)
        self.clearbutton.place(x=50,y=250)

        #__________Linking button with countries ________
        self.track_button.bind("<Button-1>", self.Track_location)
        #255757294146

    def Track_location(self,event):
        try:
            phone_number = self.phone_number.get()
            # country = "Country is Unknown"
            if phone_number is not None:
                
                #__________for country name______________
                mainNum = phonenumbers.parse(phone_number,"CH") 
                if mainNum:
                    tracked = geocoder.description_for_number(mainNum,"en") 
                else:
                    print("error")
                #__________For Timezone ______________
                phoneNumber = phonenumbers.parse(phone_number) 
                if phoneNumber: 
                    timeZone = timezone.time_zones_for_number(phoneNumber) 
                else:
                    print("error") 
                #__________for Service Provider name______________

                service_number = phonenumbers.parse(phone_number,"RO")
                if service_number:
                    svp = carrier.name_for_number(service_number,"en")
                else:
                    print("error")

                self.country_label.configure(text=tracked)
                self.timezone_label.configure(text=timeZone)
                self.svp_label.configure(text=svp)

            else:
                phone_number.focus_set()

        except:
            print("you must put a valid number")

    def clearbtn(self):
        self.phone_number.delete(0, 'end')
        # print("clear")

PhoneTracker = Tk()
MyApp = Location_Tracker(PhoneTracker)
PhoneTracker.mainloop()
