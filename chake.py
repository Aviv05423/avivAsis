import tkinter as tk
import winsound
from time import sleep
from tkinter import *
from tkinter import messagebox, ttk




def root(linkButtoncommand, processing_label_text):
    root = tk.Tk()  # המסך הראשי
    # root.configure(background="#800000") # Recommended red
    root.configure(background="#f3b605")
    root.title("היי אביב")
    ttk.Style(root).configure('myStyle.TRadiobutton', background="#f3b605", foreground='white', font = ("rubik", 9))
    ttk.Style(root).configure('pickupPopup.TRadiobutton', background="#23964e", foreground='white', font = ("rubik", 9))
    ttk.Style(root).configure('W.TButton', font =('rubik', 22,), justify="center", foreground = 'black')
    # root.iconbitmap(r'C:\Users\idanb\Documents\MEGAsync\App4Sale\Spider3D\BlackLogoRoundedPNG.ico', )#לא בטוח למה צריך את הr
    # root.iconbitmap(r'Assets/StickerApp.ico')#לא בטוח למה צריך את הr

    canvas = tk.Canvas(root, height=130, width=300, bg="#f3b605", highlightbackground="#f3b605")
    canvas.pack()
    # endregion הגדרות טקינטר

    # region כפתור "המשך" לתחילת פעולה
    linkButtonSaver = tk.Frame(root, bg="#f3b605")  # כפתור שמירת קישור ותחילת עבודה
    linkButtonSaver.place(relx=0.25, rely=0.3, height=130, width=160, )
    linkButton = ttk.Button(linkButtonSaver, text="היי אביב", style="W.TButton", command=linkButtoncommand).pack()# command=main_starter


    # region שדה מס' הזמנה
    # entry_link_Frame = tk.Frame(root, bg="#f3b605")  # שדה טקסט לקישור
    # entry_link_Frame.place(relx=0.25, rely=0.38, height=30, width=184, )
    # orderLinkField = ttk.Entry(entry_link_Frame, font=("rubik", 14 ), width=30, justify="center")
    # orderLinkField.pack()
    # endregion שדה מס' הזמנה
    # איסוף עצמי "27695"
    # "25560" # Eyal Biton הזמנה עבור
    # כולל הערות + כמות גבוהה # "27692"

    # region שדה מס' אריזות
    # entry_pack_Frame = tk.Frame(root, bg="#f3b605")  # שדה טקסט כמות חבילות
    # entry_pack_Frame.place(relx=0.87, rely=0.38, height=30, width=33, )
    # packNum = ttk.Entry(entry_pack_Frame, font=("rubik", 14 ), width=33, justify="center")
    # packNum.pack()
    # packNum.insert(0, "1")
    # endregion

    # region כותרת "הכנס מס' הזמנה"
    ## Official green V1. #23964e
    global Main_label

    main_label_frame = tk.Frame(root, bg="#f3b605")  # טקסט המלצה לווידוא פרטים
    main_label_frame.place(relx=0.00, rely=0.05, height=25, width=300, )
    Main_label = Label(main_label_frame, text="", font=("rubik", 12, "bold"), bg="#f3b605", fg="white")
    Main_label.pack()

    global processing_label

    processing_label_frame = tk.Frame(root, bg="#f3b605")  # טקסט המלצה לווידוא פרטים
    processing_label_frame.place(relx=0.4, rely=0.75, height=30, width=160, )
    processing_label = Label(processing_label_frame, text="", font=("rubik", 12, "bold"), bg="#f3b605", fg="white")
    # processing_label.configure(text="8")
    processing_label.pack()


    # blue style #234795
    # driverTextFrame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
    # driverTextFrame.place(relx=0.04, rely=0.88, height=20, width=150, )
    # driverTextLabel = Label(driverTextFrame, text="מס' כרום דרייבר", font=("rubik", 9), bg="#23964e", fg="white").pack()
    # endregion "כותרת "הכנס מס' הזמנה

    root.mainloop()

def Main_label_confi(printComm):
    Main_label.configure(text=printComm)

def processing_label_confi(printComm):
    processing_label.configure(text=printComm)

