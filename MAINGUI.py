

from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, ttk

import cv2

def center_window(w,h):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
def read_input():
    print("inside read_input")

    
 
    lat1=textBox1.get()
    long1=textBox2.get()
    lat2=textBox3.get()
    long2=textBox4.get()
    date=textBox5.get()
   
    print("lat1  ",lat1)
    print("long1  ",long1)
    print("lat2  ",lat2)
    print("long2  ",long2)
    print("date  ",date)
    co_ordinates=lat1+","+long1+","+lat2+","+long2
   # co_ordinates='39.705062,-121.818724,41.188645,-120.327158' # Lat1,Long1,Lat2,Long2
    import  ImageMapPulling
    mapvalue=ImageMapPulling.getImage(date, co_ordinates)
    if(mapvalue==1):
        print("Image is pulled from NASA Reporsitory")
        import SVM_Test
        image_path="Input_map.jpg"
        print("Image is Pulled ")
        resultstr=SVM_Test.isFireDetected(image_path)
        if(resultstr=="Fire Detected"):
                
            print("SVM output is: ",resultstr)
            messagebox.showinfo("Fire Detection Result",resultstr)
            print("Calling to YOLO Now")
            import YOLO_Detection
            detect_value=YOLO_Detection.startDetection(image_path)   
            if(detect_value==1):
                # image = cv2.imread('Yolo_Detected.jpg')
                from PIL import Image
                img = Image.open('Yolo_Detected.jpg')
                img.show()

                import FireSpreadModel
                FireSpreadModel.draw_future_fire("Yolo_Detected.jpg")
          
                
                
            else:
                messagebox.showinfo("Fire Detection Result","Error in YOLO Model \n Please Try again")  
                
                
            
        else:
            messagebox.showinfo("Fire Detection Result",resultstr)  
            print("Ending the process here ....................")
        
    else:
        print("Error in pulling image")
    
   
    
    
   

    
root=Tk()
root.configure(background='#6495ED')
root.title("WILD FIRE CLASSFICATION,DETECTION AND TRACKING SYSTEM")
center_window(900, 600)
image = Image.open("model/main_img.jpg")

# Resize the image using resize() method
resize_image = image.resize((1200, 900))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()


username = Label(root,text = "WILD FIRE CLASSFICATION,DETECTION AND TRACKING SYSTEM", font=("Courier", 20,'bold'),fg='#f00',bg='#6495ED').place(x = 20,y = 40)


# code to create label 
label1 = Label(root,text = "Latitude 1: ",bg='#6495ED',font=("Ariel", 10)).place(x = 150,y = 130)
label2 = Label(root, text = "Longitude 1 : ",bg='#6495ED',font=("Ariel", 10)).place(x = 150,y = 200)  
label3 = Label(root, text = "Latitude 2 : ",bg='#6495ED',font=("Ariel", 10)).place(x = 150,y = 270)  
label4 = Label(root, text = "Longitude 2 : ",bg='#6495ED',font=("Ariel", 10)).place(x = 150,y = 340)  
label5 = Label(root, text = "Date : ",bg='#6495ED',font=("Ariel", 10)).place(x = 150,y = 410)  




   


#code to insert textbox
textBox1 = tk.Entry(root, width = 40)
textBox1.place(x = 250,y = 130,height=30)

textBox2 = tk.Entry(root, width = 40)
textBox2.place(x = 250,y = 200,height=30)

textBox3 = tk.Entry(root, width = 40)
textBox3.place(x = 250,y = 270,height=30) # N

textBox4 = tk.Entry(root, width = 40)       #P
textBox4.place(x = 250,y = 340,height=30)

textBox5 = tk.Entry(root, width = 40)  #K
textBox5.place(x = 250,y = 410,height=30)





#command=lambda: retrieve_input() >>> just means do this when i press the button
button=Button(root, height=1, width=13, font=("Ariel", 10,'bold'),text="SUBMIT", command=lambda: read_input()).place(x=150,y=500)

# Button for closing
exit_button = Button(root, height=1, width=13, font=("Ariel", 10,'bold'),text="Exit", command=root.destroy).place(x=350,y=500)


mainloop()

