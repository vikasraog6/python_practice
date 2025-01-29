import os
choice = input ("shutdown your computer? (Y or N) ")
if choice == 'Y' or choice == 'y':
    os.system("sudo shutdown -r now")
else:
    print("Exiting the program")