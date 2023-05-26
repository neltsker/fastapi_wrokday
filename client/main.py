from tkinter import *
from tkinter import ttk

import requests

"""
FastApiWorkDay Client app.
windows tkinter
Created by:
Kurbanov Roman PE-01b
Ivanov Oleg PE-01b
Evdokimov Sergey PE-01b

"""

#class MainWindow(Tk):
    
class LoginFrame(Frame):
    
    def __init__(self, root):
        super().__init__()
        self.setFrame()
    
    def setFrame(self):
        
        self.login = Entry(self)
        self.password = Entry(self)
        self.sendButton = Button(self, text="get login", command=self.get_Login)
        self.login.pack()
        self.password.pack()
        self.sendButton.pack()
        
        
        
    def get_Login(self):
        #data = {'username'=self.login.get(), "password" = self.password.get()}
        data = {'username': self.login.get(), 'password': self.password.get()}
        print(data)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        req = requests.post(url="http://127.0.0.1:8000/auth/token", data=data, headers=headers)
        print(req.status_code, req.json())
        if req.status_code==200:
            global token
            token = req.json()["access_token"]
            self.succesLogin()
        
    def succesLogin(self):
        
        for widget in self.winfo_children():
           widget.destroy()
        self.exitLogin = Button(self, text="exit login", command=self.setFrame)
        global token
        self.tokenLabel = Label(self, text=token)
        self.exitLogin.pack()
        self.tokenLabel.pack()
        
        
        
class WorkFrame(Frame):
    def __init__(self, root):
        super().__init__()
        self.setFrame()
        
        
    def get_tasks(self):
        global token
        #data = {'username': self.login.get(), 'password': self.password.get()}
        #print(data)
        headers = {'accept': 'application/json', 'Authorization': 'Bearer '+token}
        #headers = {'accept': 'application/json', 'Authorization': 'Bearer': token}
        req = requests.get(url="http://127.0.0.1:8000/task/list?id="+self.dep.get()+'&active=True', headers=headers)
        print(req.status_code, req.json())
        self.tasks = req.json()['tasks']
        #print(self.tasks)
        self.taskList.delete(0,END)
        for i in self.tasks:
            self.taskList.insert(0,i['name'])
        
        #self.taskList['listvariable'] =self.tasks
        
        
    def end_task(self):
        global token
        value=str((self.taskList.get(ACTIVE)))
        print(value)
        #data = {'username': self.login.get(), 'password': self.password.get()}
        #print(data)
        headers = {'accept': 'application/json', 'Authorization': 'Bearer '+token}
        #headers = {'accept': 'application/json', 'Authorization': 'Bearer': token}
        req = requests.get(url="http://127.0.0.1:8000/task/task/end/?name="+value+'&dep_id='+self.dep.get(), headers=headers)
        print(req.status_code, req.json())
        for widget in self.winfo_children():
           widget.destroy()
        self.setFrame()
        #self.task_name['text']=req.json()['task']['name']
        #self.task_creator['text']=req.json()['task']['creator']
        #self.task_descripton['text']=req.json()['task']['description']
        
    def updateTask(self, evt):
        global token
        value=str((self.taskList.get(ACTIVE)))
        print(value)
        #data = {'username': self.login.get(), 'password': self.password.get()}
        #print(data)
        headers = {'accept': 'application/json', 'Authorization': 'Bearer '+token}
        #headers = {'accept': 'application/json', 'Authorization': 'Bearer': token}
        req = requests.get(url="http://127.0.0.1:8000/task/task/?name="+value+'&dep_id='+self.dep.get(), headers=headers)
        print(req.status_code, req.json())
        
        self.task_name['text']=req.json()['task']['name']
        #self.task_creator['text']=req.json()['task']['creator']
        self.task_descripton['text']=req.json()['task']['description']
        #self.task_name['text']=req.json()['task']['name']
        
        #self.tasks = req.json()['tasks']
        #print(self.tasks)
        #self.taskList.delete(0,END)
        #for i in self.tasks:
        #    self.taskList.insert(0,i['name'])
        
            
            
    def setFrame(self):
        
        #self.get_tasks()
        self.taskList=Listbox(self, selectmode=SINGLE)
        self.taskList.bind('<<ListboxSelect>>',self.updateTask)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command = self.taskList.yview)
        self.taskList.pack(anchor=W)
        self.dep = Entry(self, text="dep_id")
        self.dep.pack(anchor=W)
        self.getBut = Button(self, text="get", command=self.get_tasks)
        self.getBut.pack(anchor=W)
        self.task_name=Label(self, text="task name")
        self.task_creator=Label(self, text="task creator")
        self.task_descripton=Label(self, text='task desc')
        self.task_end=Button(self, text="end", command=self.end_task)
        self.task_name.pack(anchor=NE)
        self.task_creator.pack(anchor=NE)
        self.task_descripton.pack(anchor=NE)
        self.task_end.pack(anchor=NE)

root = Tk()
root.title("METANIT.COM")
root.geometry("1280x720") 
# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
 
# создаем пару фреймвов
LOGINFRAME = LoginFrame(notebook)
WORKFRAME = WorkFrame(notebook)

LOGINFRAME.pack(fill=BOTH, expand=True)
WORKFRAME.pack(fill=BOTH, expand=True)
 
# добавляем фреймы в качестве вкладок
notebook.add(LOGINFRAME, text="login")
notebook.add(WORKFRAME, text="work area")
#frame1 = LoginFrame()

#frame1.pack()
#frame1.setFrame()
 

root.mainloop()
