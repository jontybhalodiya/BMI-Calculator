from setuptools import Command
import tkinter as tk
from cProfile import label
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("600x600")

#function for calculating BMI
def yrbmi():
    global bmi
    ht = float(box1.get())
    wt = float(box2.get())
    bmi = round(wt / (ht / 100)**2,2)
    finalr.config(text=f"Your BMI is: {bmi}")

#app.iconbitmap("jonty_dp_G1h_icon.ico")
label1 =tk.Label(app, text = "Enter your Height (m):",font = ("Arial", 10))
label1.place(x=13, y=70)
label2 =tk.Label(app, text = "Enter your Weight (Kg):",font = ("Arial", 10))
label2.place(x=10, y=130)
box1 = tk.Entry(app, font = ("Arial", 25), bg="#D3D3D3")
box1.place(x=150, y=60)
box2 = tk.Entry(app, font = ("Arial", 25), bg="#D3D3D3")
box2.place(x=150, y=120)
button1 = tk.Button(app , font=("Arial",15),bg ="Orange",text = "Calculate",command=yrbmi)  
button1.place(x=250 , y= 180 , width = 100)
finalr = tk.Label(app, font=("Arial", 15), fg="black",text="")
finalr.place(x= 50,y=240,width=500)
label3 =tk.Label(app, text = "BMI Categories:",font = ("Arial", 10))
label3.place(x=40, y=280)
label4 =tk.Label(app, text = "Underweight = <18.5",font = ("Arial", 10))
label4.place(x=40, y=300)
label5 =tk.Label(app, text = "Normal weight = 18.5–24.9",font = ("Arial", 10))
label5.place(x=40, y=320)
label6 =tk.Label(app, text = "Overweight = 25–29.9",font = ("Arial", 10))
label6.place(x=40, y=340)
label7 =tk.Label(app, text = "Obesity = BMI of 30 or greater",font = ("Arial", 10))
label7.place(x=40, y=360)
app.mainloop()
