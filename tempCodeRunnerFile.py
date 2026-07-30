from tkinter import *
import tkinter.messagebox
from tkinter import font
from tkinter import ttk
import csv

# ---------- Create Main window ----------
window = Tk()
window.title("Health Analysis & Calculation")
width = 700
height = 600
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
x = (window_width // 2) - (width // 2)
y = (window_height // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")
window.resizable(False, False)

# ---------- Create Function ----------
count = 0
times = -1
name, age, sex, h, w, activ = [], [], [], [], [], []
def saveinfomation():
    global name, age, sex, h, w, activ, count, times
    data = [str(entName.get()), int(entAge.get()), str(Sex.get()),
    int(entHeight.get()), float(entWeight.get()), str(Activity.get())]
    filepath = "UserData.csv"
    with open(filepath, "a", encoding="utf-8", newline="") as f:
        fw = csv.writer(f, delimiter="|")
        fw.writerow(data)
    name.append(data[0])
    age.append(data[1])
    sex.append(data[2])
    h.append(data[3])
    w.append(data[4])
    activ.append(data[5])
    times += 1
    count = 1

def clearinfomation():
    global name, age, sex, h, w, activ, count, times
    count = 0
    times = -1
    name, age, sex, h, w, activ = [], [], [], [], [], []

user_info = None
def info():
    global user_info, count
    if user_info is None or not user_info.winfo_exists():
        user_info = Toplevel(window)
        user_info.title("User Information")
        user_info.geometry(f"360x400+{x}+{y}")
        user_info.resizable(False, False)
        user_info.columnconfigure((0,1,2,3,4), weight=1, uniform="a")
        user_info.rowconfigure((0,1,2,3,4,5,6,7), weight=1, uniform="a")
        if count == 0:
            Label(user_info, text="รายการข้อมูลผู้ใช้", font=font4, bg="#FFEA62").grid(row=0, columnspan=5, sticky="nsew")
            Label(user_info, text="ไม่มีข้อมูล", font=font3, fg="grey").grid(row=3, columnspan=5, sticky="s")
        if count != 0:
            Label(user_info, text="รายการข้อมูลผู้ใช้", font=font4, bg="#FFEA62").grid(row=0, columnspan=5, sticky="nsew")
            Label(user_info, text="------------------------------------------", font=font3, fg="#C1BCBC").grid(row=1, columnspan=5, sticky="n")
            Label(user_info, text=f"ชื่อผู้ใช้: {name[times]}", font=font3).grid(row=1, columnspan=5, sticky="s")
            Label(user_info, text="------------------------------------------", font=font3, fg="#C1BCBC").grid(row=2, columnspan=5, sticky="n")
            Label(user_info, text=f"อายุ/เพศ: {age[times]} ปี / {sex[times]}", font=font3).grid(row=2, columnspan=5, sticky="s")
            Label(user_info, text="------------------------------------------", font=font3, fg="#C1BCBC").grid(row=3, columnspan=5, sticky="n")
            Label(user_info, text=f"ส่วนสูง: {h[times]} เซนติเมตร", font=font3).grid(row=3, columnspan=5, sticky="s")
            Label(user_info, text="------------------------------------------", font=font3, fg="#C1BCBC").grid(row=4, columnspan=5, sticky="n")
            Label(user_info, text=f"น้ำหนัก: {w[times]} กิโลกรัม", font=font3).grid(row=4, columnspan=5, sticky="s")
            Label(user_info, text="------------------------------------------", font=font3, fg="#C1BCBC").grid(row=5, columnspan=5, sticky="n")
            Label(user_info, text="กิจกรรมของคุณ:", font=font3).grid(row=5, columnspan=5, sticky="s")
            Label(user_info, text=f"{activ[times]}", font=font3).grid(row=6, columnspan=6, sticky="n")
            Label(user_info, text="------------------------------------------", font=font3, fg="#C1BCBC").grid(row=6, columnspan=5, sticky="s")
            Label(user_info, text="*ข้อมูลล่าสุด", font=font2, fg="#C1BCBC").grid(row=7, columnspan=5, sticky="n")
    else:
        user_info.lift()
        user_info.focus_force()

help_info = None
def helpMenu():
    global help_info
    if help_info is None or not help_info.winfo_exists():
        help_info = Toplevel(window)
        help_info.title("Help")
        help_info.geometry(f"400x500+{x}+{y}")
        help_info.resizable(False, False)
        Label(help_info, text="Help")
    else:
        help_info.lift()
        help_info.focus_force()

def exitProgram():
    confirm = tkinter.messagebox.askokcancel("Exit", "คุณต้องการปิดโปรแกรมนี้หรือไม่?")
    if confirm is True:
        window.destroy()

def comfirmBmi():
    confirm = tkinter.messagebox.askokcancel("Calculate BMI", "คุณต้องการคำนวณ BMI ใช่หรือไม่?")
    if confirm is True:
        if not (name and age and sex and h and w and activ):
            tkinter.messagebox.showinfo("Fail Information", "กรุณากรอกข้อมูลให้ถูกต้องและบันทึก")
        else:
            calBMI()

def comfirmBmr():
    confirm = tkinter.messagebox.askokcancel("Calculate BMR", "คุณต้องการคำนวณ BMR ใช่หรือไม่?")
    if confirm is True:
        if not (name and age and sex and h and w and activ):
            tkinter.messagebox.showinfo("Fail Information", "กรุณากรอกข้อมูลให้ถูกต้องและบันทึก")
        else:
            calBMR()

def comfirmTdee():
    confirm = tkinter.messagebox.askokcancel("Calculate TDEE", "คุณต้องการคำนวณ TDEE ใช่หรือไม่?")
    if confirm is True:
        if not (name and age and sex and h and w and activ):
            tkinter.messagebox.showinfo("Fail Information", "กรุณากรอกข้อมูลให้ถูกต้องและบันทึก")
        else:
            calTDEE()

def Name_focus_in(event):
    if entName.get() == "กรอกชื่อผู้ใช้...":
        entName.delete(0, 'end')
        entName.config(fg="black")

def Name_focus_out(event):
    if entName.get() == "":
        entName.insert(0, "กรอกชื่อผู้ใช้...")
        entName.config(fg="grey")

def Age_focus_in(event):
    if entAge.get() == "กรอกอายุ...":
        entAge.delete(0, 'end')
        entAge.config(fg="black")

def Age_focus_out(event):
    if entAge.get() == "":
        entAge.insert(0, "กรอกอายุ...")
        entAge.config(fg="grey")

def H_focus_in(event):
    if entHeight.get() == "กรอกส่วนสูง...":
        entHeight.delete(0, "end")
        entHeight.config(fg="black")

def H_focus_out(event):
    if entHeight.get() == "":
        entHeight.insert(0, "กรอกส่วนสูง...")
        entHeight.config(fg="grey")

def W_focus_in(event):
    if entWeight.get() == "กรอกน้ำหนัก...":
        entWeight.delete(0,"end")
        entWeight.config(fg="black")

def W_focus_out(event):
    if entWeight.get() == "":
        entWeight.insert(0, "กรอกน้ำหนัก...")
        entWeight.config(fg="grey")

def select(event):
    event.widget.config(style="TCombobox", foreground="black")

# ---------- Create Calculation for Function ----------
def BMI():
    height_user = h[times] * 0.01
    bmi = w[times] / (height_user ** 2)
    condition = bmi
    if condition >= 30:
        con1 = "โรคอ้วนระดับ 2"
    elif condition >= 25:
        con1 = "โรคอ้วนระดับ 1"
    elif condition >= 23:
        con1 = "น้ำหนักเกิน"
    elif condition >= 18.5:
        con1 = "สมส่วน"
    else:
        con1 = "น้ำหนักน้อย"
    return bmi, con1

def BMR():
    if sex[times] == "ชาย":
        bmr = (10 * w[times]) + (6.25 * h[times]) - (5 * age[times]) + 5
    elif sex[times] == "หญิง":
        bmr = (10 * w[times]) + (6.25 * h[times]) - (5 * age[times]) - 161
    else:
        tkinter.messagebox.showinfo("Fail Information", "กรุณาเลือกเพศและบันทึก")
    con2 = "เทียบตามด้านล่าง"
    return bmr, con2

def TDEE():
    if activ[times] == "ไม่ออกกำลังกายเลยหรือน้อยมาก":
        bmrx = 1.2
    elif activ[times] == "ออกกำลังกายเบาๆ 1-3 วัน/สัปดาห์":
        bmrx = 1.375
    elif activ[times] == "ออกกำลังกายปานกลาง 3-5 วัน/สัปดาห์":
        bmrx = 1.55
    elif activ[times] == "ออกกำลังกายหนัก 6-7 วัน/สัปดาห์":
        bmrx = 1.725
    elif activ[times] == "นักกีฬา/ออกกำลังกายหนัก":
        bmrx = 1.9
    else:
        tkinter.messagebox.showinfo("Fail Information", "กรุณาเลือกกิจกรรมและบันทึก")
    bmr_before, non = BMR()
    tdee =  float(bmr_before) * float(bmrx)
    con3 = "เทียบตามด้านล่าง"
    return tdee, con3

calbmi_info = None
def calBMI():
    global calbmi_info
    bmi, cont1 = BMI()
    if calbmi_info is None or not calbmi_info.winfo_exists():
        calbmi_info = Toplevel(window)
        calbmi_info.title("BMI Calculate")
        calbmi_info.geometry(f"400x520+{x}+{y}")
        calbmi_info.resizable(False, False)
        calbmi_info.columnconfigure((0,1,2,3,4), weight=1, uniform="a")
        calbmi_info.rowconfigure((0,1,2,3,4,5,6,7), weight=1, uniform="a")
        Label(calbmi_info, text="______________________________________", font=font3, fg="#C1BCBC").grid(row=0, columnspan=5, sticky="n")
        Label(calbmi_info, text=" ", font=font3, bg="#FFEF83").grid(row=0, columnspan=5, sticky="ew")
        Label(calbmi_info, text=f"BMI ของคุณ {name[times]}: {bmi:.2f}",font=font4, bg="#FFEF83").grid(row=0, columnspan=5, sticky="esw")
        Label(calbmi_info, text=f"ผลลัพธ์เกณฑ์: {cont1}", font=font4, bg="#FFEF83").grid(row=1, columnspan=5, sticky="enw")
        Label(calbmi_info, text=" ", font=font3, bg="#FFEF83").grid(row=1, columnspan=5, sticky="ew")
        Label(calbmi_info, text="------------------------------------------", font=font3, fg="#C1BCBC").grid(row=1, columnspan=5, sticky="s")

        Label(calbmi_info, text="น้ำหนักต่ำกว่าเกณฑ์ (น้อยกว่า 18.5)", font=font3).grid(row=2, columnspan=5)
        Label(calbmi_info, text="- มีความเสี่ยงเกิดโรคขาดสารอาหาร", font=font3, fg="grey").grid(row=2, columnspan=5, sticky="s")
        Label(calbmi_info, text="น้ำหนักสมส่วน (18.5 - 22.9)", font=font3).grid(row=3, columnspan=5)
        Label(calbmi_info, text="- มีโอกาสเกิดโรคแทรกซ้อนน้อยที่สุด", font=font3, fg="grey").grid(row=3, columnspan=5, sticky="s")
        Label(calbmi_info, text="น้ำหนักเกินมาตรฐาน (23.0 - 24.9)", font=font3).grid(row=4, columnspan=5)
        Label(calbmi_info, text="- น้ำหนักเกินเริ่มต้น เริ่มมีโรคแทรกซ้อนเล็กน้อย", font=font3, fg="grey").grid(row=4, columnspan=5, sticky="s")
        Label(calbmi_info, text="เป็นโรคอ้วนระดับที่ 1 (25.0 - 29.9)", font=font3).grid(row=5, columnspan=5)
        Label(calbmi_info, text="- น้ำหนักเกินมาก มีโรคแทรกซ้อนระยะอ้วนเริ่มต้น", font=font3, fg="grey").grid(row=5, columnspan=5, sticky="s")
        Label(calbmi_info, text="เป็นโรคอ้วนระดับที่ 2 (มากกว่า 30)", font=font3).grid(row=6, columnspan=5)
        Label(calbmi_info, text="- มีโอกาสเป็นโรคเบาหวาน, ความดันโลหิตสูง,", font=font3, fg="grey").grid(row=6, columnspan=5, sticky="s")
        Label(calbmi_info, text="โรคหลอดเลือดสมอง, โรคหลอดเลือดหัวใจ", font=font3, fg="grey").grid(row=7, columnspan=5, sticky="n")
    else:
        calbmi_info.lift()
        calbmi_info.focus_force()

calbmr_info = None
def calBMR():
    global calbmr_info
    bmr, cont2 = BMR()
    if calbmr_info is None or not calbmr_info.winfo_exists():
        calbmr_info = Toplevel(window)
        calbmr_info.title("BMR Calculate")
        calbmr_info.geometry(f"400x520+{x}+{y}")
        calbmr_info.resizable(False, False)
        calbmr_info.columnconfigure((0,1,2,3,4), weight=1, uniform="a")
        calbmr_info.rowconfigure((0,1,2,3,4,5,6,7), weight=1, uniform="a")
        Label(calbmr_info, text="______________________________________", font=font3, fg="#C1BCBC").grid(row=0, columnspan=5, sticky="n")
        Label(calbmr_info, text=" ", font=font3, bg="#FFEF83").grid(row=0, columnspan=5, sticky="ew")
        Label(calbmr_info, text=f"BMR ของคุณ {name[times]}: {bmr:.2f} kcal",font=font4, bg="#FFEF83").grid(row=0, columnspan=5, sticky="esw")
        Label(calbmr_info, text=f"ข้อเสนอแนะ: {cont2}", font=font4, bg="#FFEF83").grid(row=1, columnspan=5, sticky="enw")
        Label(calbmr_info, text=" ", font=font3, bg="#FFEF83").grid(row=1, columnspan=5, sticky="ew")
        Label(calbmr_info, text="------------------------------------------", font=font3, fg="#C1BCBC").grid(row=1, columnspan=5, sticky="s")

        Label(calbmr_info, text="BMR (Basal Metabolic Rate)", font=font3).grid(row=3, columnspan=5, sticky="n")
        Label(calbmr_info, text="พลังงานที่ร่างกายใช้เพื่อรักษาการทำงาน", font=font3, fg="grey").grid(row=3, columnspan=5)
        Label(calbmr_info, text="พื้นฐานของอวัยวะต่างๆ เช่น การหายใจ", font=font3, fg="grey").grid(row=3, columnspan=5, sticky="s")
        Label(calbmr_info, text="คำแนะนำเบื้องต้น", font=font3).grid(row=4, columnspan=5, sticky="s")
        Label(calbmr_info, text="“BMR = พลังงานขั้นต่ำที่ร่างกายใช้ตอนพัก”", font=font3, fg="grey").grid(row=5, columnspan=5, sticky="n")
        Label(calbmr_info, text="ไม่แนะนำให้กินต่ำกว่า BMR อย่างต่อเนื่อง", font=font3, fg="grey").grid(row=5, columnspan=5)
        Label(calbmr_info, text="เพราะร่างกายอาจจะสูญเสียมวลกล้ามเนื้อ", font=font3, fg="grey").grid(row=5, columnspan=5, sticky="s")

        Label(calbmr_info, text="______________________________________", font=font3, fg="#C1BCBC").grid(row=7, columnspan=5)
    else:
        calbmr_info.lift()
        calbmr_info.focus_force()

caltdee_info = None
def calTDEE():
    global caltdee_info
    tdee, cont3 = TDEE()
    if caltdee_info is None or not caltdee_info.winfo_exists():
        caltdee_info = Toplevel(window)
        caltdee_info.title("TDEE Calculate")
        caltdee_info.geometry(f"400x520+{x}+{y}")
        caltdee_info.resizable(False, False)
        caltdee_info.columnconfigure((0,1,2,3,4), weight=1, uniform="a")
        caltdee_info.rowconfigure((0,1,2,3,4,5,6,7), weight=1, uniform="a")
        Label(caltdee_info, text="____________________________________", font=font3, fg="#C1BCBC").grid(row=0, columnspan=5, sticky="n")
        Label(caltdee_info, text=" ", font=font3, bg="#FFEF83").grid(row=0, columnspan=5, sticky="ew")
        Label(caltdee_info, text=f"TDEE ของคุณ {name[times]}: {tdee:.2f} kcal",font=font4, bg="#FFEF83").grid(row=0, columnspan=5, sticky="esw")
        Label(caltdee_info, text=f"ข้อเสนอแนะ: {cont3}",font=font4, bg="#FFEF83").grid(row=1, columnspan=5, sticky="enw")
        Label(caltdee_info, text=" ", font=font3, bg="#FFEF83").grid(row=1, columnspan=5, sticky="ew")
        Label(caltdee_info, text="------------------------------------------", font=font3, fg="#C1BCBC").grid(row=1, columnspan=5, sticky="s")

        Label(caltdee_info, text="TDEE (Total Daily Energy Expenditure)", font=font3).grid(row=3, columnspan=5, sticky="n")
        Label(caltdee_info, text="พลังงานรวมทั้งหมดที่ร่างกายใช้ในแต่ละวัน", font=font3, fg="grey").grid(row=3, columnspan=5)
        Label(caltdee_info, text="ซึ่งรวมถึง BMR และการทำกิจกรรมต่างๆ", font=font3, fg="grey").grid(row=3, columnspan=5, sticky="s")
        Label(caltdee_info, text="คำแนะนำและเป้าหมาย", font=font3).grid(row=4, columnspan=5, sticky="s")
        Label(caltdee_info, text="อยากลดน้ำหนักช้าๆ: TDEE - 10%", font=font3, fg="grey").grid(row=5, columnspan=5, sticky="n")
        Label(caltdee_info, text="อยากคงน้ำหนักไว้: เท่ากับ TDEE", font=font3, fg="grey").grid(row=5, columnspan=5)
        Label(caltdee_info, text="อยากเพิ่มน้ำหนัก/กล้าม: TDEE + 10%", font=font3, fg="grey").grid(row=5, columnspan=5, sticky="s")

        Label(caltdee_info, text="____________________________________", font=font3, fg="#C1BCBC").grid(row=7, columnspan=5)
    else:
        caltdee_info.lift()
        caltdee_info.focus_force()

# ---------- Create Font ---------
fontHeading = font.Font(size=18)
fontHeadingsmall = font.Font(size=16)
font2 = font.Font(size=12)
font3 = font.Font(size=13)
font4 = font.Font(size=14)

# ---------- Create Widget Label & Variable ----------
window.columnconfigure((0,1,2,3,4), weight=1, uniform="a")
window.rowconfigure((0,1,2,3,4,5,6,7), weight=1, uniform="a")

Lb1 = Label(window, text="Welcome To Health Analysis & Calculation", font=fontHeading)
Lb1.grid(row=0, columnspan=5)
Lb2 = Label(window, text="* หากคุณยังไม่เคยกรอกข้อมูลส่วนตัว แนะนำให้กรอกในช่องด้านล่าง", font=font2)
Lb2.grid(row=0, columnspan=5, sticky=S)
LbName = Label(window, text="ชื่อผู้ใช้", font=font3).grid(row=1, column=1, sticky="w", padx=2)
LbAge = Label(window, text="อายุ", font=font3).grid(row=1, column=3, sticky="w", padx=5)
LbSex = Label(window, text='เพศ', font=font3).grid(row=2, column=1, sticky="w")
LbHeight = Label(window, text="ส่วนสูง", font=font3).grid(row=2, column=2, sticky="w", padx=2)
LbWeight = Label(window, text="น้ำหนัก", font=font3).grid(row=2, column=3, sticky="w", padx=5)
LbActivity = Label(window, text="กิจกรรม", font=font3).grid(row=3, column=1, columnspan=3, sticky="w")
LbCatagory = Label(window, text="Choose a Health Topic", font=fontHeading).grid(row=5, columnspan=5, sticky="s")
LbCatagory2 = Label(window, text="* เลือกหัวข้อที่จะคำนวณ", font=font2)
LbCatagory2.grid(row=6, columnspan=5, sticky="n")
Label(window, text="_____________________________________________________________________________________", font=font2, fg="#C1BCBC").grid(row=5, columnspan=5, sticky="n")
Label(window, text="คำนวณ", font=font3).grid(row=6, column=1, sticky="s")
Label(window, text="คำนวณ", font=font3).grid(row=6, column=2, sticky="s")
Label(window, text="คำนวณ", font=font3).grid(row=6, column=3, sticky="s")



txtName = StringVar()
entName = Entry(window, textvariable=txtName, font=font3, fg="grey")
entName.grid(row=1, column=1, columnspan=2, sticky="sew", padx=2)
entName.insert(0, "กรอกชื่อผู้ใช้...")
entName.bind("<FocusIn>", Name_focus_in) 
entName.bind("<FocusOut>", Name_focus_out)
entName.focus()

txtAge = StringVar()
entAge = Entry(window, textvariable=txtAge, font=font3, fg="grey")
entAge.grid(row=1, column=3, sticky="sw", padx=5)
entAge.insert(0, "กรอกอายุ...")
entAge.bind("<FocusIn>", Age_focus_in)
entAge.bind("<FocusOut>", Age_focus_out)

style1 = ttk.Style()
style1.configure("1.TCombobox", foreground="grey")
Sex = ttk.Combobox(window, style="1.TCombobox", font=font3)
Sex.set("กรุณาเลือก")
Sex["values"] = ["ชาย", "หญิง"]
Sex.grid(row=2, column=1, sticky="sw")
Sex.bind("<<ComboboxSelected>>", select)

txtHeight = StringVar()
entHeight = Entry(window, textvariable=txtHeight, font=font3, fg="grey")
entHeight.grid(row=2, column=2, sticky="sw", padx=4)
entHeight.insert(0, "กรอกส่วนสูง...")
entHeight.bind("<FocusIn>", H_focus_in)
entHeight.bind("<FocusOut>", H_focus_out)

txtWeight = StringVar()
entWeight = Entry(window, textvariable=txtWeight, font=font3, fg="grey")
entWeight.grid(row=2, column=3, sticky="sw", padx=3)
entWeight.insert(0, "กรอกน้ำหนัก...")
entWeight.bind("<FocusIn>", W_focus_in)
entWeight.bind("<FocusOut>", W_focus_out)

style2 = ttk.Style()
style2.configure("2.TCombobox", foreground="grey")
Activity = ttk.Combobox(window, style="2.TCombobox", font=font3)
Activity.set("กรุณาเลือก")
Activity["values"] = ["ไม่ออกกำลังกายเลยหรือน้อยมาก",
                    "ออกกำลังกายเบาๆ 1-3 วัน/สัปดาห์",
                    "ออกกำลังกายปานกลาง 3-5 วัน/สัปดาห์",
                    "ออกกำลังกายหนัก 6-7 วัน/สัปดาห์",
                    "นักกีฬา/ออกกำลังกายหนัก"]
Activity.grid(row=3, column=1, columnspan=3, sticky="sew")
Activity.bind("<<ComboboxSelected>>", select)

Btn = Button(window, text="บันทึกข้อมูล", font=font3, width=12, bg="white", command=saveinfomation).grid(row=4, column=2)
Btn2 = Button(window, text="BMI", font=font3, width=15, bg="white", command=comfirmBmi).grid(row=7, column=1, sticky="n")
Btn3 = Button(window, text="BMR", font=font3, width=15, bg="white", command=comfirmBmr).grid(row=7, column=2, sticky="n")
Btn4 = Button(window, text="TDEE", font=font3, width=15, bg="white", command=comfirmTdee).grid(row=7, column=3, sticky="n")



# ---------- Create Menu ----------
menubar = Menu()
window.config(menu=menubar)

menuitem = Menu()
menuitem.add_command(label="User Information", command=info)
menuitem.add_command(label="Clear Information", command=clearinfomation)
menuitem.add_command(label="Exit Program", command=exitProgram)

menubar.add_cascade(label="More", menu=menuitem)
menubar.add_cascade(label="Help")

window.mainloop()

# Last Update 25/09/2025
# ศุภวิชญ์ ยุยงค์ Section.7 6804062662215
# ภวิษย์พร สุวรรณสันติสุข Section.7 6804062662193