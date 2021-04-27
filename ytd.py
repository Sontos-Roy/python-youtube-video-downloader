from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")
    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#download video
def DownloadVideo():
    choice = ytdChoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,).first()

        elif(choice == choices[2]):
            select = yt.streams.filter(progressive=True,res="360p").first()

        elif(choice == choices[3]):
            select = yt.streams.filter(progressive=True,res="240p").last()

        elif(choice == choices[4]):
            select = yt.streams.filter(progressive=True,file_extension='mp4', res="144p").last()

        elif(choice == choices[5]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")
    # download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed !!")

root = Tk()

root.title("YTD Downloader")
root.geometry("350x450") #set window
root.columnconfigure(0,weight=1) #set all content in center

#YTD link Label
ytdLabel = Label(root, text="Enter the URL of the Video", font=("jost", 15))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Eroor Msg
ytdError = Label(root, text="Please wait for download", fg="red", font=("jost",15,"bold"))
ytdError.grid()

#Asking save file label
saveLabel = Label(root, text="Save the Video File", font=("jost",15,"bold"))
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error msg location
locationError = Label(root,text="Error msg of Path", fg="red", font=("jost",10))
locationError.grid()

#Download Quality
ytdQuality = Label(root, text="Select Quality",font=("jost",15))
ytdQuality.grid(column=0,rowspan=2, sticky=S, ipady=10)

#Combobox  //
choices = ["720p","480p", "360p", "240p", "144p", "only Audio"]
ytdChoices = ttk.Combobox(root,values=choices)
ytdChoices.grid()

#download btn
downloadclick = Label(root, text="Click here for download your video",font=("jost",15))
downloadclick.grid(row=9, column=0,rowspan=2, sticky=S, ipady=10)
downloadbtn = Button(root,text="Download", width=10,bg="red",fg="white", command=DownloadVideo)
downloadbtn.grid()

#developer label
developerlabel = Label(root,text="Sontos Sharma",font=("jost,15"))
developerlabel.grid(column=0,rowspan=2, sticky=S, ipady=20)

root.mainloop()