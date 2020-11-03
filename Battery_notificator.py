import psutil
from win10toast import ToastNotifier
import getpass
import os

USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


add_to_startup()

battery = psutil.sensors_battery()
percent = battery.percent

toast = ToastNotifier()

if percent < 31:
    toast.show_toast("Your battery status is getting low!;)", "Please connect your device to electricity", duration=100,
                     icon_path="Battery_icon.ico")
