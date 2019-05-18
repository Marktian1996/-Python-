

import tkinter as tk
import tkinter.messagebox
import pickle

# 引入三个文件
import admin_c
import teacher_c
import student_c


def main_window(): # 显示主窗口（管理员窗口）函数
    admin_c.main()
    

def teacher_window_function(): # 显示教师窗口函数
    teacher_c.main()
    

def student_window_funciton(): # 显示学生窗口函数
    student_c.main()

# （1）创建窗口
window = tk.Tk()
window.title('welcome')
window.geometry('450x300')
window.config(bg='cadet blue')

# （2）加载图片，创建画布
canvas = tk.Canvas(window,height=300,width=500,bg='cadet blue',bd=0)
canvas.config()

image_file=tk.PhotoImage(file='welcome.png') # 得到图片路径
image = canvas.create_image(100,30,anchor='nw',image=image_file) # 创建图片对象，放置图片位置
canvas.pack(side ='top') # 放置画布位置 

# （3）建立 2 个标签
tk.Label(window,text='User name:',bd=2).place(x=50,y=150)
tk.Label(window,text='Password:',bd=2).place(x=50,y=190)

# （4）输入框 2 个
var_usr_name=tk.StringVar()
var_usr_name.set('请输入用户名') # 设置输入框默认显示
var_usr_pwd=tk.StringVar()


entry_usr_name = tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=150)
entry_usr_pwd = tk.Entry(window,textvariable=var_usr_pwd,show ='*')
entry_usr_pwd.place(x=160,y=190)

# （5）登陆，注册按钮
def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info,usr_file)

    #if usr_name in usrs_info:
    if((usr_name in usrs_info)and(usr_name == 'admin')):

        if usr_pwd == usrs_info[usr_name]: # 以管理员身份登陆
            window.destroy()
            main_window() # 调用主窗口显示函数
            

            # tk.messagebox.showinfo(title='welcome',message='How are you?' + usr_name) # 将这个地方改变为：数据显示窗口


        else:
            tk.messagebox.showerror(message='Error,Password error, please try again！')

    elif((usr_name in usrs_info) and (usr_name == 'Teacher')):# 以教师身份登陆
        
        window.destroy()
        teacher_window_function() # 调用教师窗口显示函数

    elif(usr_name in usrs_info): # 以学生身份登陆
        window.destroy()
        student_window_funciton()
        

    else:
        is_sign_up = tk.messagebox.askyesno('Welcome','You have not registered yet, do you need to register?')

        if is_sign_up:
            usr_sign_up()


def usr_sign_up(): # 注册窗口设置

    # 注册后台，与主要操作
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        with open('usrs_info.pickle','rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)


        if (np != npf ):
            tk.messagebox.showerror('错误!','Password input is different!')
        elif np == '':
            tk.messagebox.showerror('错误!','The password is empty!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('错误!','User already exists!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo('welcome','You have already registered successfully')
            window_sign_up.destroy()


    # 创建注册窗口
    window_sign_up =tk.Toplevel(window)
    window_sign_up.title('注册')
    window_sign_up.geometry('350x200')
    

    # 创建标签与输入框
    # 用户名与输入框
    new_name = tk.StringVar()
    new_name.set('please enter user name')
    tk.Label(window_sign_up,text='User name:').place(x=10,y=10)
    entry_new_name = tk.Entry(window_sign_up,textvariable = new_name)
    entry_new_name.place(x=150,y=10)

    # 密码与输入框
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up,text='Password:').place(x=10,y=50)
    entry_new_usr_pwd=tk.Entry(window_sign_up,textvariable = new_pwd,show ='*')
    entry_new_usr_pwd.place(x=150,y=50)

    # 用户名再次输入，与输入框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up,text="Confirm password:").place(x=10,y=99)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*')
    entry_usr_pwd_confirm.place(x=150,y=90)

    # 再次确认密码按钮
    btn_confirm_sign_up = tk.Button(window_sign_up,text = '注册',command = sign_to_Mofan_Python)
    btn_confirm_sign_up.place(x=150,y=130)





# 登陆（login）窗口按钮

btn_login = tk.Button(window,text='登陆',command = usr_login)
btn_login.place(x=170,y=230)

btn_sign_up = tk.Button(window,text = '注册', command = usr_sign_up)
btn_sign_up.place(x=270,y=230)

window.mainloop()
