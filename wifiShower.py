import subprocess
from tkinter import * 
from tkinter import ttk
class wifiextractor :
    def __init__(self):
        self.createWindow()
    def createWindow(self):
        self.root= Tk()
        self.root.geometry("700x300")
        self.table = ttk.Treeview(self.root)
        self.table['columns'] = ('password')
        self.table.heading('#0', text='WiFi Name')
        self.table.column('#0', width=350, stretch=True)
        self.table.heading('password', text='Password')
        self.table.column('password', width=350, stretch=True)
        self.table.pack()
        btn = Button(self.root,text = "Get WiFi",command=self.getWifi)
        btn.pack()
        self.root.mainloop()
    def getWifi(self):
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        allProfiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in allProfiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 
                                'key=clear']).decode('utf-8').split('\n')

            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            self.table.insert(parent='', index='end',text=i, values=(results[0]))

app = wifiextractor()