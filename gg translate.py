from tkinter import *
from tkinter import ttk
#lớp TK được dùng để tạo cửa sổ
from googletrans import Translator, LANGUAGES

root = Tk()
#Tạo cửa sổ Tkinter

root.geometry('1055x320')
#kích thước cửa sổ Tkinter (ngangxdọc)

root.resizable(None,None)
#làm cho ô cửa số gốc không thể thay đổi kích thước

root.iconbitmap('translator.ico')
root ['bg']= 'pink'
#đặt biểu tượng cho cửa sổ ứng dụng
#màu background hồng

root.title('Translator of Huy n Linh')
Label(root, text = "Languague Translator", font = " Arial 20 bold").pack()
#Tạo bảng tiện ích gán với tiêu đề title mình cho trước với kích thước

Label(root,text = "Nhập văn bản", font = 'arial 13 bold', bg = 'white smoke').place(x=160, y=90)
# tạo tiện ích nhãn với văn bản và phông chữ được chỉ định và thêm nó vào cửa sổ gốc bằng trình quản lý hình học place().
# Phương thức place() được sử dụng để đặt vị trí của tiện ích nhãn trên cửa sổ. Trong trường hợp này, nhãn được đặt tại tọa độ (165, 90) trên cửa sổ
# x - trái sang phải
# y - trên xuống dưới

input_text = Entry(root, width=60)
input_text.place(x=40, y = 130)
input_text.focus()
input_text.get()
#tạo tiện ích mục nhập có chiều rộng 60 ký tự
# Cho tiện ích đó ở tọa độ (40,130)

Label(root, text = "Bản dịch văn bản", font = 'arial 13 bold', bg = 'white smoke').place(x = 770, y=90)
output_text = Text(root, font = 'arial 10',height = 3, wrap = WORD, padx = 5, pady= 5, width= 50)
output_text.place(x= 650, y = 130)
# tạo 1 bảng có chữ và biểu thị vị trí của nó
# tạo 1 ô cửa sổ đầu ra sẽ trả kết quả mình dịch ra được
# padx, pady: Nó đại diện cho số lượng pixel bên ngoài đường viền của gidget.

language = list(LANGUAGES.values())
# gán các ngôn ngữ của thư viện vào language

dest_lang = ttk.Combobox(root, values = language, width = 22)
dest_lang.place(x=765, y=230)
dest_lang.set('choose language')

# Dịch

def Translate():
    translator = Translator()
    translated= translator.translate(text=input_text.get(), dest = dest_lang.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)
trans_btn = Button(root, text = 'Translate', font = 'arial 12 bold', pady = 5, command= Translate, bg= 'orange', activebackground='green')
trans_btn.place (x=472, y =180)

root.mainloop()
