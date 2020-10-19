import tkinter as tk
from tkinter import filedialog,messagebox,ttk
from transclass import Translate


translate=Translate("","","",[])

def get_files():
    files = filedialog.askopenfilenames(filetypes=[('text files', '.jpg')])
    translate.file_paths=files
    if files:
        for file in files:
            text1.insert(tk.END, file + '\n')
            text1.update()
    else:
        print('你没有选择任何文件')
def set_result_path():
    result_path=filedialog.askdirectory()
    translate.result_root_path=result_path
    text2.insert(tk.END,result_path)

def translate_files():
    if translate.file_paths:
        translate.translate_files()
        tk.messagebox.showinfo("提示","搞定")
    else :
        tk.messagebox.showinfo("提示","无文件")


root=tk.Tk()
root.title("netease youdao translation test")
frm = tk.Frame(root)
frm.grid(padx='50', pady='50')
btn_get_file = tk.Button(frm, text='选择待翻译图片', command=get_files)
btn_get_file.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
text1 = tk.Text(frm, width='40', height='10')
text1.grid(row=0, column=1)
btn_get_result_path=tk.Button(frm,text='选择翻译结果路径',command=set_result_path)
btn_get_result_path.grid(row=1,column=0)
text2=tk.Text(frm,width='40', height='2')
text2.grid(row=1,column=1)

btn_sure=tk.Button(frm,text="翻译",command=translate_files)
btn_sure.grid(row=2,column=1)


root.mainloop()