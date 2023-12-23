from win10toast import ToastNotifier 
import time
from win32com.client import Dispatch

hours=int(input('enter hourse to set:'))
minutes=int(input("enter minutes to set:"))
sec=int(input('enter seconds to set:'))

total=sec+(minutes*60)+(hours*60*60)

while True:
    time.sleep(total)
    noti=ToastNotifier()
    noti.show_toast('its time to grink water')



