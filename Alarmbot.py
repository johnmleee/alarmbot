
import winsound
from win10toast import ToastNotifier

#building reminder within a toast notification
def timer (reminder,seconds):
    toaster = ToastNotifier()

    toaster.show_toast(title = ": alarmbot", msg = "New task: "+ str(words) +"\nYou will be notified in "+ str(seconds) + " minute(s).", icon_path = "C:/Users/lee/OneDrive - Kennesaw State University/Documents/GitHub/alarmbot/wrench.ico", duration = seconds*60)
    toaster.show_toast(title = ": alarmbot", msg = reminder, icon_path = "C:/Users/lee/OneDrive - Kennesaw State University/Documents/GitHub/Garage-Buddy/wrench.ico", duration = 15, threaded = True)

#alarm sound, still within "timer" function
    frequency = 905S
    duration = 500
    winsound.Beep(frequency,duration)
    frequency = 905
    duration = 200
    winsound.Beep(frequency,duration)
    frequency = 905
    duration = 200
    winsound.Beep(frequency,duration)
    frequency = 623
    duration = 400
    winsound.Beep(frequency,duration)
    frequency = 623
    duration = 400
    winsound.Beep(frequency,duration)

#user input and calling "timer" function
if __name__ == "__main__":
    words = input ("What would you like to be alarmed of? ")
    seconds = int(input("In how many minutes would you like to be alarmed? "))

    timer (words, seconds)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
