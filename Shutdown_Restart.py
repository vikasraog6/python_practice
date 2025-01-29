import os
choice = input ("shutdown your computer? (Y or N) ")
if choice == 'Y' or choice == 'y':
    os.system("Shutdown /h")
else:
    print("Exiting the program")