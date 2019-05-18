
import tkinter
import uer_d
import class_d
import course_d
import student_d
import teacher_d


class Student_www:
    
    def __init__(self,root,var):
        
        self.var=var
        self.root = root
        self.root.geometry('590x700')
        self.root.title(self.var)
        self.root.config(bg='cadet blue')

        # 框架
        ButtonFrame=tkinter.Frame(self.root,bd=4,width=100,height=500,padx=10,pady=27,bg="Ghost White")
        ButtonFrame.place(x=20,y=55)

        # =========================================标签=====================================================
        T_table = tkinter.Label(root,text='欢迎进入管理员界面',font=('Calibri',20),height=1,width=50,bd=4,bg="Ghost White").grid()

        # ========================================文本框======================================================
        t = tkinter.Text(self.root,bd=4)
        t.place(x=170,y=55,width=400,height=450) 
        
        # =======================================函数=========================================================
        # 用户管理模块
        def add_user():
            #root.destroy()
            uer_d.main()

        # 教师管理
        def add_teacher():
            #root.destroy()
            teacher_d.main()

        # 学生管理
        def add_student():
            #root.destroy()
            student_d.main()

        # 班级管理
        def add_class():
            #root.destroy()
            class_d.main()

        # 课程管理
        def add_course():
            #root.destroy()
            course_d.main()
                        

        # 专业管理    
        def add_profession():
            pass    
            


        # ========================================按钮==========================================================
        l_admin1=tkinter.Label(ButtonFrame,text="用户管理",font=('Calibri',15,),height=1,width=10,bd=4,bg='Ghost White')
        l_admin1.grid(row=0,column=0)
        btnAddDate = tkinter.Button(ButtonFrame,text="添加用户",font=('Calibri',13,),height=1,width=10,bd=4,command=add_user)
        btnAddDate.grid(row=1,column=0)
        btnAddDate = tkinter.Button(ButtonFrame,text="用户管理",font=('Calibri',13,),height=1,width=10,bd=4,command=add_user)
        btnAddDate.grid(row=2,column=0)

        l_admin1=tkinter.Label(ButtonFrame,text="教师管理",font=('Calibri',15,),height=1,width=10,bd=4,bg='Ghost White')
        l_admin1.grid(row=3,column=0)
        btnAddDate = tkinter.Button(ButtonFrame,text="添加教师",font=('Calibri',13,),height=1,width=10,bd=4,command=add_teacher)
        btnAddDate.grid(row=4,column=0)
        btnAddDate = tkinter.Button(ButtonFrame,text="教师管理",font=('Calibri',13,),height=1,width=10,bd=4,command=add_teacher)
        btnAddDate.grid(row=5,column=0)

        l_admin1=tkinter.Label(ButtonFrame,text="学生管理",font=('Calibri',15,),height=1,width=10,bd=4,bg='Ghost White')
        l_admin1.grid(row=6,column=0)
        btnAddDate = tkinter.Button(ButtonFrame,text="学生添加",font=('Calibri',13,),height=1,width=10,bd=4,command=add_student)
        btnAddDate.grid(row=7,column=0)
        btnAddDate = tkinter.Button(ButtonFrame,text="学生管理",font=('Calibri',13,),height=1,width=10,bd=4,command=add_student)
        btnAddDate.grid(row=8,column=0)

        l_admin1=tkinter.Label(ButtonFrame,text="班级管理",font=('Calibri',15,),height=1,width=10,bd=4,bg='Ghost White')
        l_admin1.grid(row=9,column=0)
        btnAddDate = tkinter.Button(ButtonFrame,text="添加班级",font=('Calibri',13,),height=1,width=10,bd=4,command=add_class)
        btnAddDate.grid(row=10,column=0)
        btnAddDate = tkinter.Button(ButtonFrame,text="管理班级",font=('Calibri',13,),height=1,width=10,bd=4,command=add_class)
        btnAddDate.grid(row=11,column=0)

        l_admin1=tkinter.Label(ButtonFrame,text="课程管理",font=('Calibri',15,),height=1,width=10,bd=4,bg='Ghost White')
        l_admin1.grid(row=12,column=0)
        btnAddDate = tkinter.Button(ButtonFrame,text="添加课程",font=('Calibri',13,),height=1,width=10,bd=4,command=add_course)
        btnAddDate.grid(row=13,column=0)
        btnAddDate = tkinter.Button(ButtonFrame,text="管理课程",font=('Calibri',13,),height=1,width=10,bd=4,command=add_course)
        btnAddDate.grid(row=14,column=0)

        ''' l_admin1=tkinter.Label(ButtonFrame,text="专业管理",font=('Calibri',15,),height=1,width=10,bd=4,bg='Ghost White')
        l_admin1.grid(row=15,column=0)
        btnAddDate = tkinter.Button(ButtonFrame,text="添加专业",font=('Calibri',13,),height=1,width=10,bd=4)
        btnAddDate.grid(row=16,column=0)
        btnAddDate = tkinter.Button(ButtonFrame,text="管理专业",font=('Calibri',13,),height=1,width=10,bd=4)
        btnAddDate.grid(row=17,column=0)
 '''

def main():
    root = tkinter.Tk()
    var='管理员'
    application = Student_www(root,var)
    root.mainloop()
