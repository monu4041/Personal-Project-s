from tkinter import *
from tkinter import ttk,messagebox
import webbrowser
import speech_recognition
from pygame import mixer

mixer.init()

def search():
    if questionField.get() !='':
        if temp.get() == 'google':
            webbrowser.open(f'https://www.google.com/search?q={questionField.get()}')

        if temp.get() == 'duck':
             webbrowser.open(f'https://duckduckgo.com/?va={questionField.get()}')

        if temp.get() == 'amazon':
             webbrowser.open(f"https://www.amazon.in/s?k={questionField.get()}&ref=nb_sb_noss")
            
        if temp.get() == 'youtube':
             webbrowser.open(f"https://www.youtube.com/results?search_query={questionField.get()}")
    else:
        messagebox.showerror("Error There is nothing to be searched ")
        
def voice():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr=speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
       try:
           sr.adjust_for_ambient_noise(m, duration=0.2)
           audio=sr.listen(m)
           message = sr.recognize_google(audio)
           mixer.music.load('music2.mp3')
           mixer.music.play()
           questionField.delete(0,END)
           questionField.insert(0,message)
           search()
           
       except:
           pass 
    
        
root = Tk()

root.geometry('660x70+100+100')
root.title('Universal Search Bar')
root.iconbitmap('E:\\pythan Training\Project_File\Search Bar\icon.ico') # create in mic icon
root.config(bg='lightgrey') # window bg colors create
root.resizable(0,0) # maximize button is of....
temp = StringVar()  # defined for temp

style = ttk.Style()
style.theme_use('default')

# search bar and Query window ....
queryLabel=Label(root,text='Query',font=('arial',14,'bold'),bg='lightgrey')
queryLabel.grid(row=0,column=0)

# search line create...
questionField=Entry(root,width=45,font=('arial',14,'bold'),bd=4,relief=SUNKEN)
questionField.grid(padx=10,row=0,column=1)

# mic icon create...
micImage=PhotoImage(file='E:\\pythan Training\Project_File\Search Bar\mic.png')
micButTon=Button(root,image=micImage,bg='lightgrey',bd=0,cursor='hand2',activebackground='lightgrey',command=voice)
micButTon.grid(row=0,column=2)

# search icon create...
#searchImage=PhotoImage(file='search.png')
searchImage=PhotoImage(file='E:\\pythan Training\Project_File\Search Bar\search.png')
searchButton=Button(root,image=searchImage,bd=0,cursor='hand2',bg='lightgrey',activebackground='lightgrey',command= search)
searchButton.grid(row=0,column=3,padx=5)

# create Google radio buttons...
googleRadioButton=ttk.Radiobutton(root,text='Google',value='google',variable=temp)
googleRadioButton.place(x=75,y=40)

# create Duck radio buttons...
duckRadioButton=ttk.Radiobutton(root,text='Duck Duck Go',value='duck',variable=temp)
duckRadioButton.place(x=200,y=40)

# create Amazon radio buttons...
amazonRadioButton=ttk.Radiobutton(root,text='Amazon',value='amazon',variable=temp)
amazonRadioButton.place(x=380,y=40)

# create Youtube radio buttons...
youtubeRadioButton=ttk.Radiobutton(root,text='Youtube',value='youtube',variable=temp)
youtubeRadioButton.place(x=510,y=40)

def enter_function(value):
    searchButton.invoke()
root.bind('<Return>',enter_function)
temp.set('google')
    

root.mainloop()



