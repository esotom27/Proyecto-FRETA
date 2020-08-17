from tkinter import *
from tkinter.ttk import *
import time
from time import strftime
import sys

sys.path.append('C:\Python38\Lib\site-packages')


import cv2
import os
import imutils
import numpy as np
import numpy as np
import random 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time

root = Tk()
root.title('FRETA')
root.geometry("600x400")

lbl1= Label(root, text="Nombre:")
lbl1.place(x = 250, y = 300)
Nombre = Entry(root)
Nombre.place(x = 250, y = 325)

lblh= Label(root, text="Hora")
lblh.place(x = 25, y = 225)
lblm= Label(root, text="Minutos")
lblm.place(x = 25, y = 275)
lblam = Label(root, text = "AM o PM")
lblam.place(x = 25, y = 175)


date = strftime('%x')
datelb=Label(root, text=date)
datelb.pack(anchor = 'center', pady = 10)

        
Hour = Entry(root)
Hour.place(x = 25, y = 250)
Minute = Entry(root) 
Minute.place(x = 25, y = 300)
AM = Entry(root)
AM.place(x= 25, y = 200)

def time(): 
    string = strftime('%H:%M %p') 
    lbl.config(text = string) 
    lbl.after(1000, time)    
    
  
# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(root, font = ('calibri', 40, 'bold'), background = 'gray', foreground = 'white') 
  
# Placing clock at the centre 
# of the tkinter window 
lbl.pack(anchor = 'center', pady = 20)


def quitbutton():
    quitButton = Button(text="Exit",command=client_exit)
    quitButton.place(x=500, y=350)

def client_exit():
    exit()

def set_Alarm_button():
    Alertbutton = Button(root,text="Configurar Alarma",command=set_Alert)
    Alertbutton.place(x=25, y=350)

def set_Alert():
    h =(Hour.get())
    m = (Minute.get())
    ampm = (AM.get())

    if (h == strftime('%H'), m == strftime('%M') and ampm == strftime('%p')):
        button = Button(root,text="Dispense Pastillas",command=RF)
        button.place(x=300, y=250)

def RF():
    u=0
    dataPath = 'C:\Desktop\py2\Data' #Cambiar la ruta
    imagePaths = os.listdir(dataPath)
    print('imagePaths=',imagePaths)
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    face_recognizer.read('modeloEigenFace.xml')
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    while u==0:
        ret,frame = cap.read()
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)
            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            
            # EigenFaces
            if result[1] < 5700:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                x ='{}'.format(imagePaths[result[0]])
                u=2
                
                break
                
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                x ='Desconocido'
                u=2
                break
                
        
        cv2.imshow('frame',frame)
        k = cv2.waitKey(1)
        if k == 27:
            break
          
    cap.release()
    cv2.destroyAllWindows()

   

def set_user():
    
    userbutton = Button(root,text="Crear usuario",command=Captura)
    userbutton.place(x=250, y=350)

def entrenarRF ():
    dataPath = 'C:\Desktop\py2\Data'#Cambiar ruta
    peopleList = os.listdir(dataPath)
    print('Lista de personas: ', peopleList)
    labels = []
    facesData = []
    label = 0
    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        print('Leyendo las imágenes')
        for fileName in os.listdir(personPath):
            print('Rostros: ', nameDir + '/' + fileName)
            labels.append(label)
            facesData.append(cv2.imread(personPath+'/'+fileName,0))
        label = label + 1
    # Métodos para entrenar el reconocedor
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    face_recognizer.train(facesData, np.array(labels))
    # Almacenando el modelo obtenido
    face_recognizer.write('modeloEigenFace.xml')
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

def Captura():
        
    personName = (Nombre.get())
    dataPath = 'C:\Desktop\py2\Data'#Cambia a la ruta 
    personPath = dataPath + '/' + personName
    if not os.path.exists(personPath):
        print('Carpeta creada: ',personPath)
        os.makedirs(personPath)
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    #cap = cv2.VideoCapture('Video.mp4')
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    count = 0
    while True:
        
        ret, frame = cap.read()
        if ret == False: break
        frame =  imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count),rostro)
            count = count + 1
        cv2.imshow('frame',frame)
        k =  cv2.waitKey(1)
        if k == 27 or count >= 300:
            break
    cap.release()
    cv2.destroyAllWindows()
    entrenarRF()



    

time()
quitbutton()
set_Alarm_button()
set_user()

mainloop()



