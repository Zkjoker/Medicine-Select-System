import tkinter as tk
print_cal=0
class Cabinet():
    def __init__(self,cabinet_path,cabinet_name,floor_num):
        self.cabinet_path=cabinet_path
        self.cabinet_name=cabinet_name
        self.floor_name =[]
        self.cabinet=[]

        for current_number in range(floor_num):
            self.floor_name.append('place\\'+self.cabinet_path+'\\'+str(current_number+1)+'_floor.txt')
            current_floor_name=self.floor_name[current_number]
            with open(current_floor_name) as file_object:
                self.lines=file_object.readlines()
            floor=[]
            for line in self.lines:
                floor.append((line.strip()))
            self.cabinet.append(floor)


    def select(self,select_name):
        global print_cal
        self.stringshow=''
        for self.floors in self.cabinet:
            for self.medicine in self.floors:
                if select_name.lower() in self.medicine.lower():
                    self.flag=True
                    self.floornumber=self.cabinet.index(self.floors)
                    self.medicinenumber=self.floors.index(self.medicine)
                    print_cal+=1
                    if(print_cal<=10):
                        self.stringshow+= Cabinet.show_information(self)
        return self.stringshow
    def show_information(self):
        global print_cal

        self.show_string1 = (
                    "药物：" + self.medicine + ' 已经找到。' + '位于 ' + self.cabinet_name + " 的第 " + str(self.floornumber + 1) +
                    " 层," + "第 " + str(self.medicinenumber + 1) + ' 个。')
        self.show_string2 = "\n\n"
        self.show =self.show_string1 + self.show_string2
        # '该层药品依次为：\n'+self.medicines+'\n'
        return self.show

Front_A=Cabinet('front_A','前一柜',5)
Front_B=Cabinet('front_B','前二柜',5)
Behind_A=Cabinet('behind_A','后一柜',5)
Behind_B=Cabinet('behind_B','后二柜',5)
Left_A=Cabinet('left_A','左前柜',4)
Left_B=Cabinet('left_B','左中柜',4)
Left_C=Cabinet('left_C','左后柜',4)
Right_A=Cabinet('right_A','右前柜',6)
Right_B=Cabinet('right_B','右后柜',6)
Bottom_A=Cabinet('bottom_A','底一柜',3)
Bottom_B=Cabinet('bottom_B','底二柜',3)
Bottom_C=Cabinet('bottom_C','底三柜',3)


def hit_me():
    global print_cal
    print_cal=0
    m=input_med.get()
    m=m.strip()
    photo2 = tk.PhotoImage(file="bga.gif")
    theLabel2.config(image=photo2)
    theLabel2.image = photo2
    if m!='':
        strtotal=''
        strtotal+=Front_A.select(m)
        strtotal +=Front_B.select(m)
        strtotal +=Behind_A.select(m)
        strtotal += Behind_B.select(m)
        strtotal += Left_A.select(m)
        strtotal += Left_B.select(m)
        strtotal += Left_C.select(m)
        strtotal += Right_A.select(m)
        strtotal += Right_B.select(m)
        strtotal += Bottom_A.select(m)
        strtotal += Bottom_B.select(m)
        strtotal += Bottom_C.select(m)
        if strtotal=='':
            strtotal='无法找到'+m+'!\n请检查:\n1.输入是否正确\n2.是否将该药品加入服务器药品库'
        else:
            strtotal += '共找到' + str(print_cal) + '个结果。'
            if print_cal>10:
                strtotal +='仅显示前10个。\n'

    else:
        strtotal='请输入需要查找的内容！'
    var.set(strtotal)
def return_me():
    photo1 = tk.PhotoImage(file="bgp.gif")
    theLabel2.config(image=photo1)
    theLabel2.image = photo1
    var.set("")

window=tk.Tk()
photo1= tk.PhotoImage(file="bgp.gif")
window.title('百合山庄综合门诊药物查询系统')
window.geometry('1016x750')
theLabel1=tk.Label(window,text='百合山庄综合门诊药物查询系统',font=("黑体", 30),   
                   fg="black" )
theLabel1.pack()

var=tk.StringVar()
theLabel2 = tk.Label(window,textvariable=var,image=photo1, compound=tk.CENTER,font=("黑体", 20), fg="red")
theLabel2.pack()

input_med = tk.Entry(window,show=None)
input_med.pack()

mybutton1= tk.Button(window,
    text='查询',      
    width=20, height=2,
    command=hit_me)     
mybutton1.pack()

mybutton2= tk.Button(window,
    text='返回',      
    width=20, height=2,
    command=return_me)     
mybutton2.pack()

window.mainloop()