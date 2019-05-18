
# Frontend

from tkinter import *
import tkinter.messagebox
import stdDatabase_BackEnd05



class Student:
    
    def __init__(self,root,var):
        
        self.var = var
        self.root = root
        self.root.title("Student Database Management Systems")
        self.root.geometry("1050x600")
        self.root.config(bg ="cadet blue")

        # 定义 tkinter 类型的字符创变量
        StdID = tkinter.StringVar()
        Firstname = tkinter.StringVar()
        Surname = tkinter.StringVar()
        DoB = tkinter.StringVar()
        Age = tkinter.StringVar()
        Gender = tkinter.StringVar()
        Address = tkinter.StringVar()
        Mobile = tkinter.StringVar()
        #===============================Function=========================================================================

        # 退出窗口
        def iExit():
            iExit = tkinter.messagebox.askyesno("Students Database Management Systems","如果你想退出请点击确定")
            if iExit >0:
                root.destroy()
                return

        # 清除
        def ClearData():
            self.txtStdID.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtSna.delete(0,END)
            self.txtDoB.delete(0,END)
            self.txtAge.delete(0,END)
            self.txtGender.delete(0,END)
            self.txtAdr.delete(0,END)
            self.txtMobile.delete(0,END)
        
        # 添加数据
        def addData():
            if(len(StdID.get())!=0):
                stdDatabase_BackEnd05.addStdRec(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),\
                                              Address.get(),Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),\
                                             Address.get(),Mobile.get()))

        # 显示数据
        def DisplayData():
            studentlist.delete(0,END)
            for row in stdDatabase_BackEnd05.viewDate():
                studentlist.insert(END,row,str(""))

        # 事件函数（不懂是干嘛的）
        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtSna.delete(0,END)
            self.txtSna.insert(END,sd[3])
            self.txtDoB.delete(0,END)
            self.txtDoB.insert(END,sd[4])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END,sd[5])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END,sd[6])
            self.txtAdr.delete(0,END)
            self.txtAdr.insert(END,sd[7])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,sd[8])
        
        # 删除函数有问题
        def DeleteData():
            if (len(StdID.get())!=0):
                stdDatabase_BackEnd05.deleteRec(sd[0])
                ClearData()
                # stdDatabase_BackEnd05.deleteRec(StdID.get())
                DisplayData()

        # 查找函数
        def searchDatabase():
            studentlist.delete(0,END)
            for rows in stdDatabase_BackEnd05.searchData(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),\
                                              Address.get(),Mobile.get()):
                studentlist.insert(END,rows,str(""))

        def updata():
            if(len(StdID.get())!=0):
                stdDatabase_BackEnd05.deleteRec(sd[0])

            if(len(StdID.get())!=0):
                stdDatabase_BackEnd05.addStdRec(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),\
                                              Address.get(),Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),\
                                        Address.get(),Mobile.get()))

        def showdata():
            pass



        #===============================Frames===========================================================================
        MainFrame = tkinter.Frame(self.root,bg="cadet blue")
        MainFrame.grid()

        
        # 标题框架
        TitFrame = tkinter.Frame(MainFrame, bd=2,padx = 54,pady=8,bg="Ghost White",relief = 'ridge')
        TitFrame.pack(side=TOP)
        
        
        # 标签（依附在标题框架上面）
        self.lblTit = Label(TitFrame,font =('Calibri',45,'bold'),text=var,bg="Ghost White")
        self.lblTit.grid()

        # Button 框架
        ButtonFrame =Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg="Ghost White",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        # 数据框架
        DataFrame = Frame(MainFrame,bd=2,width=1300,height=400,padx=20,pady=20,relief=RIDGE,bg="cadet blue")
        DataFrame.pack(side=LEFT)

        # 左边数据框架
        DataFromeLEFT = LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,relief=RIDGE,bg="Ghost White",
                                  font=('Calibri',20,'bold'),text="信息输入\n")
        DataFromeLEFT.pack(side=LEFT)

        # 右边数据框架
        DataFrameRIGHT = LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3,relief=RIDGE,bg='Ghost White',
                                    font=('Calibri',20,'bold'),text="信息详情\n")
        DataFrameRIGHT.pack(side=RIGHT)

        #===============================Lables and Entry Widget======================================================================
        # 标签 和 输入框

        self.lblStdID = Label(DataFromeLEFT,font =('Calibri',20,'bold'),text="学院:",padx =2,pady=2,bg="Ghost White")
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID = Entry(DataFromeLEFT,font=('Calibri',20,'bold'),textvariable = StdID,width=39)
        self.txtStdID.grid(row=0,column=1)

        self.lblfna = Label(DataFromeLEFT,font =('Calibri',20,'bold'),text="专业:",padx =2,pady=2,bg="Ghost White")
        self.lblfna.grid(row=1,column=0,sticky=W)
        self.txtfna = Entry(DataFromeLEFT,font=('Calibri',20,'bold'),textvariable=Firstname,width=39)
        self.txtfna.grid(row=1,column=1)

        self.lblSna = Label(DataFromeLEFT,font =('Calibri',20,'bold'),text="班主任:",padx =2,pady=2,bg="Ghost White")
        self.lblSna.grid(row=2,column=0,sticky=W)
        self.txtSna = Entry(DataFromeLEFT,font=('Calibri',20,'bold'),textvariable=Surname,width=39)
        self.txtSna.grid(row=2,column=1)

        self.lblDoB = Label(DataFromeLEFT,font =('Calibri',20,'bold'),text="年级:",padx =2,pady=2,bg="Ghost White")
        self.lblDoB.grid(row=3,column=0,sticky=W)
        self.txtDoB = Entry(DataFromeLEFT,font=('Calibri',20,'bold'),textvariable=DoB,width=39)
        self.txtDoB.grid(row=3,column=1)

        self.lblAge = Label(DataFromeLEFT,font =('Calibri',20,'bold'),text="班级人数:",padx =2,pady=2,bg="Ghost White")
        self.lblAge.grid(row=4,column=0,sticky=W)
        self.txtAge = Entry(DataFromeLEFT,font=('Calibri',20,'bold'),textvariable=Age,width=39)
        self.txtAge.grid(row=4,column=1)

        self.lblGender = Label(DataFromeLEFT,font =('Calibri',20,'bold'),text="班长:",padx =2,pady=2,bg="Ghost White")
        self.lblGender.grid(row=5,column=0,sticky=W)
        self.txtGender = Entry(DataFromeLEFT,font=('Calibri',20,'bold'),textvariable=Gender,width=39)
        self.txtGender.grid(row=5,column=1)

        self.lblAdr = Label(DataFromeLEFT,font =('Calibri',20,'bold'),text="班主任电话:",padx =2,pady=2,bg="Ghost White")
        self.lblAdr.grid(row=6,column=0,sticky=W)
        self.txtAdr = Entry(DataFromeLEFT,font=('Calibri',20,'bold'),textvariable=Address,width=39)
        self.txtAdr.grid(row=6,column=1)

        self.lblMobile = Label(DataFromeLEFT,font =('Calibri',20,'bold'),text="班长电话:",padx =2,pady=2,bg="Ghost White")
        self.lblMobile.grid(row=7,column=0,sticky=W)
        self.txtMobile = Entry(DataFromeLEFT,font=('Calibri',20,'bold'),textvariable=Mobile,width=39)
        self.txtMobile.grid(row=7,column=1)



        #===============================ListBox & ScrollBar Widget=================================================================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        studentlist = Listbox(DataFrameRIGHT,width=41,height=18,font=('Calibri',12,'bold'),yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command = studentlist.yview)



        #===============================Button Widget==============================================================================
        # 按钮部件
        self.btnAddDate = Button(ButtonFrame,text="添加",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=addData)
        self.btnAddDate.grid(row=0,column=0)

        self.btnDisplayData = Button(ButtonFrame,text="显示",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=DisplayData)
        self.btnDisplayData.grid(row=0,column=1)

        self.btnClearData = Button(ButtonFrame,text="清除",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=ClearData)
        self.btnClearData.grid(row=0,column=2)

        self.btnDeleteData = Button(ButtonFrame,text="删除",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0,column=3)

        self.btnSearchData = Button(ButtonFrame,text="搜索",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0,column=4)

        self.btnUpdateData = Button(ButtonFrame,text="修改",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=updata)
        self.btnUpdateData.grid(row=0,column=5)

        self.btnShowData = Button(ButtonFrame,text="示图",font = ('Calibri',20,'bold'),height=1,width=10,bd=4,command='')
        self.btnShowData.grid(row=0,column=6)

        self.btnEixt = Button(ButtonFrame,text="退出",font=('Calibri',20,'bold'),height=1,width=10,bd=4,command=iExit)
        self.btnEixt.grid(row=0,column=7)


# if __name__ == '__main__':
#      root = tkinter.Tk()
#      application = Student(root)
#      root.mainloop()

def main():
    tx="班级管理"
    root = tkinter.Tk()
    application = Student(root,tx)
    root.mainloop() 

