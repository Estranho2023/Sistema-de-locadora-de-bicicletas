import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("ADM ")
        #setting window size
        width=863
        height=632
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        entray_1=tk.Entry(root)
        entray_1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entray_1["font"] = ft
        entray_1["fg"] = "#333333"
        entray_1["justify"] = "center"
        entray_1["text"] = "Entry"
        entray_1.place(x=50,y=180,width=70,height=25)

        butao_1=tk.Button(root)
        butao_1["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        butao_1["font"] = ft
        butao_1["fg"] = "#000000"
        butao_1["justify"] = "center"
        butao_1["text"] = "Button"
        butao_1.place(x=120,y=180,width=70,height=25)
        butao_1["command"] = self.butao_1_command

        label_1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        label_1["font"] = ft
        label_1["fg"] = "#333333"
        label_1["justify"] = "center"
        label_1["text"] = "label"
        label_1.place(x=80,y=150,width=70,height=25)

        entray_2=tk.Entry(root)
        entray_2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entray_2["font"] = ft
        entray_2["fg"] = "#333333"
        entray_2["justify"] = "center"
        entray_2["text"] = "Entry"
        entray_2.place(x=240,y=180,width=70,height=25)

        butao_2=tk.Button(root)
        butao_2["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        butao_2["font"] = ft
        butao_2["fg"] = "#000000"
        butao_2["justify"] = "center"
        butao_2["text"] = "Button"
        butao_2.place(x=310,y=180,width=70,height=25)
        butao_2["command"] = self.butao_2_command

        label_2=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        label_2["font"] = ft
        label_2["fg"] = "#333333"
        label_2["justify"] = "center"
        label_2["text"] = "label"
        label_2.place(x=270,y=150,width=70,height=25)

        entray_3=tk.Entry(root)
        entray_3["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entray_3["font"] = ft
        entray_3["fg"] = "#333333"
        entray_3["justify"] = "center"
        entray_3["text"] = "Entry"
        entray_3.place(x=430,y=180,width=70,height=25)

        butao_3=tk.Button(root)
        butao_3["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        butao_3["font"] = ft
        butao_3["fg"] = "#000000"
        butao_3["justify"] = "center"
        butao_3["text"] = "Button"
        butao_3.place(x=500,y=180,width=70,height=25)
        butao_3["command"] = self.butao_3_command

        label_3=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        label_3["font"] = ft
        label_3["fg"] = "#333333"
        label_3["justify"] = "center"
        label_3["text"] = "label"
        label_3.place(x=460,y=150,width=70,height=25)

        entray_4=tk.Entry(root)
        entray_4["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entray_4["font"] = ft
        entray_4["fg"] = "#333333"
        entray_4["justify"] = "center"
        entray_4["text"] = "Entry"
        entray_4.place(x=50,y=350,width=70,height=25)

        label_4=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        label_4["font"] = ft
        label_4["fg"] = "#333333"
        label_4["justify"] = "center"
        label_4["text"] = "label"
        label_4.place(x=80,y=320,width=70,height=25)

        butao_4=tk.Button(root)
        butao_4["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        butao_4["font"] = ft
        butao_4["fg"] = "#000000"
        butao_4["justify"] = "center"
        butao_4["text"] = "Button"
        butao_4.place(x=120,y=350,width=70,height=25)
        butao_4["command"] = self.butao_4_command

        entray_5=tk.Entry(root)
        entray_5["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entray_5["font"] = ft
        entray_5["fg"] = "#333333"
        entray_5["justify"] = "center"
        entray_5["text"] = "Entry"
        entray_5.place(x=240,y=350,width=70,height=25)

        butao_5=tk.Button(root)
        butao_5["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        butao_5["font"] = ft
        butao_5["fg"] = "#000000"
        butao_5["justify"] = "center"
        butao_5["text"] = "Button"
        butao_5.place(x=310,y=350,width=70,height=25)
        butao_5["command"] = self.butao_5_command

        label_5=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        label_5["font"] = ft
        label_5["fg"] = "#333333"
        label_5["justify"] = "center"
        label_5["text"] = "label"
        label_5.place(x=280,y=320,width=70,height=25)

        entray_6=tk.Entry(root)
        entray_6["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entray_6["font"] = ft
        entray_6["fg"] = "#333333"
        entray_6["justify"] = "center"
        entray_6["text"] = "Entry"
        entray_6.place(x=430,y=350,width=70,height=25)

        butao_6=tk.Button(root)
        butao_6["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        butao_6["font"] = ft
        butao_6["fg"] = "#000000"
        butao_6["justify"] = "center"
        butao_6["text"] = "Button"
        butao_6.place(x=500,y=350,width=70,height=25)
        butao_6["command"] = self.butao_6_command

        label_6=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        label_6["font"] = ft
        label_6["fg"] = "#333333"
        label_6["justify"] = "center"
        label_6["text"] = "label"
        label_6.place(x=460,y=320,width=70,height=25)

        b_alugadas=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        b_alugadas["font"] = ft
        b_alugadas["fg"] = "#333333"
        b_alugadas["justify"] = "center"
        b_alugadas["text"] = "BICICLETAS ALUGADAS "
        b_alugadas.place(x=650,y=40,width=168,height=30)

        alugadas=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        alugadas["font"] = ft
        alugadas["fg"] = "#333333"
        alugadas["justify"] = "center"
        alugadas["text"] = "Alugadas agora:"
        alugadas.place(x=650,y=90,width=91,height=30)

        GLabel_403=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_403["font"] = ft
        GLabel_403["fg"] = "#333333"
        GLabel_403["justify"] = "center"
        GLabel_403["text"] = "label"
        GLabel_403.place(x=760,y=90,width=70,height=25)

        receita=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        receita["font"] = ft
        receita["fg"] = "#333333"
        receita["justify"] = "center"
        receita["text"] = "RECEITA GERADA"
        receita.place(x=670,y=160,width=132,height=30)

        GLabel_35=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_35["font"] = ft
        GLabel_35["fg"] = "#333333"
        GLabel_35["justify"] = "center"
        GLabel_35["text"] = "label"
        GLabel_35.place(x=700,y=210,width=70,height=25)

    def butao_1_command(self):
        print("command")


    def butao_2_command(self):
        print("command")


    def butao_3_command(self):
        print("command")


    def butao_4_command(self):
        print("command")


    def butao_5_command(self):
        print("command")


    def butao_6_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
