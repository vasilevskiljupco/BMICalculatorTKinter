from tkinter import *
import math


def Evaluate():
    result = ""
    category = ""
    recommendation = ""
    try:
        ages = int(txtAges.get())
        if ages > 19 and ages <= 160:
            weight = float(txtWeight.get())
            height = float(txtHeight.get())/100
            index = round(weight/(height*height), 1)
            needToBe = round(25*(height*height), 1)
            if index < 16:
                category = "Severe Thinness"
                lblBMI.config(bg="red")
                lblRecommendation.config(bg="red")
            elif index >=16 and index < 17:
                category = "Moderate Thinness"
                lblBMI.config(bg="red")
                lblRecommendation.config(bg="red")
            elif index >=17 and index < 18.5:
                category = "Mild Thinness"
                lblBMI.config(bg="yellow")
                lblRecommendation.config(bg="yellow")
            elif index >=18.5 and index < 25:
                category = "Normal"
                lblBMI.config(bg="white")
                lblRecommendation.config(bg="white")
            elif index >= 25 and index < 30:
                category = "Overweight"
                lblBMI.config(bg="yellow")
                lblRecommendation.config(bg="yellow")
            elif index >= 30 and index < 35:
                category = "Obese Class I"
                lblBMI.config(bg="red")
                lblRecommendation.config(bg="red")
            elif index >= 35 and index < 40:
                category = "Obese Class II"
                lblBMI.config(bg="red")
                lblRecommendation.config(bg="red")
            else:
                category = "Obese Class III"
                lblBMI.config(bg="red")
                lblRecommendation.config(bg="red")

            result = str(index) + " - " + category
            if index >= 25:
                needToBe = round(25 * (height * height), 1)
                needToLose = str(round((weight - needToBe), 1))
                recommendation =  "You need to be " + str(needToBe) + "\nYou need to lose " + needToLose + "kg."
            elif index < 18.5:
                needToBe = round(18.5 * (height * height), 1)
                needToGain = str(round((needToBe - weight), 1))
                recommendation = "You need to be " + str(needToBe) + "\nYou need to gain " + needToGain + "kg."
            else:
                recommendation = "You weight is perfect. \nKeep going like this."
        elif ages <= 19:
            result = "BMI for children bellow 20 years cannot be estimated correctly"
            lblBMI.config(bg="red")
            lblRecommendation.config(bg="red")
        else:
            result = "Only Methuselah can live more than 160 years"
            lblBMI.config(bg="red")
            lblRecommendation.config(bg="red")
    except:
        result = "You must enter values in the fields."
        lblBMI.config(bg="red")
        lblRecommendation.config(bg="red")
    finally:
        lblBMI.configure(text=result)
        lblRecommendation.configure(text=recommendation)


def DrawCanvas():
    c.create_line(5, 25, 400, 25)
    c.create_line(5, 50, 400, 50)
    c.create_line(5, 75, 400, 75)
    c.create_line(5, 100, 400, 100)
    c.create_line(5, 125, 400, 125)
    c.create_line(5, 150, 400, 150)
    c.create_line(5, 175, 400, 175)
    c.create_line(5, 200, 400, 200)
    c.create_line(200, 5, 200, 220)
    c.create_text(100, 10, fill="darkblue", font="Helvetica 16 italic bold", text="Classification")
    c.create_text(300, 10, fill="darkblue", font="Helvetica 16 italic bold", text="BMI(kg/m)")
    c.create_text(100, 35, fill="blue", font="Helvetica 12 bold", text="Severe thinness")
    c.create_text(300, 35, fill="blue", font="Helvetica 12 bold", text="Bellow 16")
    c.create_text(100, 60, fill="blue", font="Helvetica 12 bold", text="Moderate thinness")
    c.create_text(300, 60, fill="blue", font="Helvetica 12 bold", text="16 - 16.99")
    c.create_text(100, 85, fill="blue", font="Helvetica 12 bold", text="Mild thinness")
    c.create_text(300, 85, fill="blue", font="Helvetica 12 bold", text="17 - 18.49")
    c.create_text(100, 110, fill="blue", font="Helvetica 12 bold", text="Normal")
    c.create_text(300, 110, fill="blue", font="Helvetica 12 bold", text="18.5-24.99")
    c.create_text(100, 135, fill="blue", font="Helvetica 12 bold", text="Overweight")
    c.create_text(300, 135, fill="blue", font="Helvetica 12 bold", text="25 - 29.99")
    c.create_text(100, 160, fill="blue", font="Helvetica 12 bold", text="Obese class I")
    c.create_text(300, 160, fill="blue", font="Helvetica 12 bold", text="30 - 34.99")
    c.create_text(100, 185, fill="blue", font="Helvetica 12 bold", text="Obese class II")
    c.create_text(300, 185, fill="blue", font="Helvetica 12 bold", text="35 - 39.99")
    c.create_text(100, 210, fill="blue", font="Helvetica 12 bold", text="Obese class III")
    c.create_text(300, 210, fill="blue", font="Helvetica 12 bold", text="40 and over")
#Create main window
top = Tk()
top.title("Body Mass Index Calculator")
top.configure(bg="lightblue")
w = 406
h = 450
ws = top.winfo_screenwidth()
hs = top.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
top.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Create Canvas
c = Canvas(top, bg="white", width=400, height=220)
c.grid(columnspan=2, row=0, column=0)
DrawCanvas()

# Create Entries
lblEmpty1 = Label(top, text=" ", bg="lightblue")
lblEmpty1.grid(row=1, column=0)
lblAges = Label(top, text="Ages: ", bg="lightblue")
lblAges.grid(row=2, column=0)
txtAges = Entry(top, bd=1, relief="solid", highlightcolor="blue")
txtAges.grid(row=2, column=1)
lblHeight = Label(top, text="Height(cm): ", bg="lightblue")
lblHeight.grid(row=3, column=0)
txtHeight = Entry(top, bd=1, relief="solid", highlightcolor="blue")
txtHeight.grid(row=3, column=1)
lblWeight = Label(top, text="Weight(kg): ", bg="lightblue")
lblWeight.grid(row=4, column=0)
txtWeight = Entry(top, bd=1, relief="solid", highlightcolor="blue")
txtWeight.grid(row=4, column=1)
lblEmpty2 = Label(top, text=" ", bg="lightblue")
lblEmpty2.grid(row=5, column=0)
btnCalculate = Button(top, text="CALCULATE", command=Evaluate, bd=0, bg='lightblue', fg='lightblue', relief="ridge")
btnCalculate.grid(columnspan=2, row=6, column=0)

lblBMI = Label(top, text="                          ", borderwidth=2, relief="groove", font="Helvetica 14 bold")
lblBMI.grid(columnspan=2, row=7, column=0)
lblRecommendation = Label(top, text="                          ", borderwidth=2, relief="groove")
lblRecommendation.grid(columnspan=2, row=8, column=0)

top.attributes("-topmost", True)
top.mainloop()