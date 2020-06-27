from tkinter import*
import datetime
import random,os
from tkinter import messagebox
from PIL import Image, ImageTk

class main:
    #================= Stationary Check_F ====================
    def chkg_pen(self):
        if (self.var1.get()==1):
            self.g_pen_en.configure(state = NORMAL)
            self.g_pen_en.focus()
            self.g_pen_en.delete('0',END)
            self.g_pen.set("")
        elif (self.var1.get()==0):
            self.g_pen_en.configure(state = DISABLED) 
            self.g_pen.set("0")
    def chkeraser(self):
        if (self.var2.get()==1):
            self.eraser_en.configure(state = NORMAL)
            self.eraser_en.focus()
            self.eraser_en.delete('0',END)
            self.eraser.set("")
        elif (self.var2.get()==0):
            self.eraser_en.configure(state = DISABLED)
            self.eraser.set("0")
    def chkmarker(self):
        if (self.var3.get()==1):
            self.marker_en.configure(state = NORMAL)
            self.marker_en.focus()
            self.marker_en.delete('0',END)
            self.marker.set("")
        elif (self.var3.get()==0):
            self.marker_en.configure(state = DISABLED)
            self.marker.set("0")
    def chkn_book(self):
        if (self.var4.get()==1):
            self.n_book_en.configure(state = NORMAL)
            self.n_book_en.focus()
            self.n_book_en.delete('0',END)
            self.n_book.set("")
        elif (self.var4.get()==0):
            self.n_book_en.configure(state = DISABLED)
            self.n_book.set("0")
    def chkg_box(self):
        if (self.var5.get()==1):
            self.g_box_en.configure(state = NORMAL)
            self.g_box_en.focus()
            self.g_box_en.delete('0',END)
            self.g_box.set("")
        elif (self.var5.get()==0):
            self.g_box_en.configure(state = DISABLED)
            self.g_box.set("0")
    def chkm_pencil(self):
        if (self.var6.get()==1):
            self.c_pencil_en.configure(state = NORMAL)
            self.c_pencil_en.focus()
            self.c_pencil_en.delete('0',END)
            self.c_pencil.set("")
        elif (self.var6.get()==0):
            self.c_pencil_en.configure(state = DISABLED)
            self.c_pencil.set("0")
    #================= Grocery Check_F ====================
    def chkrice(self):
        if (self.var7.get()==1):
            self.rice_en.configure(state = NORMAL)
            self.rice_en.focus()
            self.rice_en.delete('0',END)
            self.rice.set("")
        elif (self.var7.get()==0):
            self.rice_en.configure(state = DISABLED)
            self.rice.set("0")
    def chkbread(self):
        if (self.var8.get()==1):
            self.bread_en.configure(state = NORMAL)
            self.bread_en.focus()
            self.bread_en.delete('0',END)
            self.bread.set("")
        elif (self.var8.get()==0):
            self.bread_en.configure(state = DISABLED)
            self.bread.set("0")
    def chkflour(self):
        if (self.var9.get()==1):
            self.flour_en.configure(state = NORMAL)
            self.flour_en.focus()
            self.flour_en.delete('0',END)
            self.flour.set("")
        elif (self.var9.get()==0):
            self.flour_en.configure(state = DISABLED)
            self.flour.set("0")
    def chkfish(self):
        if (self.var10.get()==1):
            self.fish_en.configure(state = NORMAL)
            self.fish_en.focus()
            self.fish_en.delete('0',END)
            self.fish.set("")
        elif (self.var10.get()==0):
            self.fish_en.configure(state = DISABLED)
            self.fish.set("0")
    def chksugar(self):
        if (self.var11.get()==1):
            self.sugar_en.configure(state = NORMAL)
            self.sugar_en.focus()
            self.sugar_en.delete('0',END)
            self.sugar.set("")
        elif (self.var11.get()==0):
            self.sugar_en.configure(state = DISABLED)
            self.sugar.set("0")
    def chkcheese(self):
        if (self.var12.get()==1):
            self.cheese_en.configure(state = NORMAL)
            self.cheese_en.focus()
            self.cheese_en.delete('0',END)
            self.cheese.set("")
        elif (self.var12.get()==0):
            self.cheese_en.configure(state = DISABLED)
            self.cheese.set("0")
    #================= Drinks Check_F ====================
    def chkfanta(self):
        if (self.var13.get()==1):
            self.fanta_en.configure(state = NORMAL)
            self.fanta_en.focus()
            self.fanta_en.delete('0',END)
            self.fanta.set("")
        elif (self.var13.get()==0):
            self.fanta_en.configure(state = DISABLED)
            self.fanta.set("0")
    def chkreal(self):
        if (self.var14.get()==1):
            self.real_en.configure(state = NORMAL)
            self.real_en.focus()
            self.real_en.delete('0',END)
            self.real.set("")
        elif (self.var14.get()==0):
            self.real_en.configure(state = DISABLED)
            self.real.set("0")
    def chklimca(self):
        if (self.var15.get()==1):
            self.limca_en.configure(state = NORMAL)
            self.limca_en.focus()
            self.limca_en.delete('0',END)
            self.limca.set("")
        elif (self.var15.get()==0):
            self.limca_en.configure(state = DISABLED)
            self.limca.set("0")
    def chktuborg(self):
        if (self.var16.get()==1):
            self.tuborg_en.configure(state = NORMAL)
            self.tuborg_en.focus()
            self.tuborg_en.delete('0',END)
            self.tuborg.set("")
        elif (self.var16.get()==0):
            self.tuborg_en.configure(state = DISABLED)
            self.tuborg.set("0")
    def chkwine(self):
        if (self.var17.get()==1):
            self.wine_en.configure(state = NORMAL)
            self.wine_en.focus()
            self.wine_en.delete('0',END)
            self.wine.set("")
        elif (self.var17.get()==0):
            self.wine_en.configure(state = DISABLED)
            self.wine.set("0")
    def chkredbull(self):
        if (self.var18.get()==1):
            self.redbull_en.configure(state = NORMAL)
            self.redbull_en.focus()
            self.redbull_en.delete('0',END)
            self.redbull.set("")
        elif (self.var18.get()==0):
            self.redbull_en.configure(state = DISABLED)
            self.redbull.set("0")
    #=============== Membership ID =================
    def chkid(self):
        if (self.var19.get()==1):
            self.R3_en.configure(state = NORMAL)
            self.R3_en.focus()
            self.R3_en.delete('0',END)
            self.id.set("")
        elif (self.var19.get()==0):
            self.R3_en.configure(state = DISABLED)
            self.id.set("0")
    
    def set_0(self):
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)
        self.var9.set(0)
        self.var10.set(0)
        self.var11.set(0)
        self.var12.set(0)
        self.var13.set(0)
        self.var14.set(0)
        self.var15.set(0)
        self.var16.set(0)
        self.var17.set(0)
        self.var18.set(0)
        self.var19.set(0)
    def __init__(self, master):
        self.master = master
        self.master.title("Billing Software")
        self.master.geometry("1300x700+0+0")
        self.master.config(bg="black")
        self.master.resizable(0,0)
        bg_color = "#9F9F9F"
        T_frame = Frame(self.master)
        T_frame.pack(fill=X)
        title = Label(T_frame, text="B$B Mart", bd=12, relief=GROOVE, bg="#292929", fg="white", font=("times new roman",30,"bold"), pady=2)
        title.pack(fill=X)

        image1 = Image.open("logo.png")
        image1 = image1.resize((61, 40), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(image1)

        lbl_1 = Label(T_frame,image=photo1, bd=5, relief=GROOVE, bg="#4D006E")
        lbl_1.image1 = photo1
        lbl_1.place(x=460,y=12)

        image2 = Image.open("logo.png")
        image2 = image2.resize((61, 40), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(image2)

        lbl_2 = Label(T_frame,image=photo2, bd=5, relief=GROOVE, bg="#4D006E")
        lbl_2.image2 = photo2
        lbl_2.place(x=760,y=12)
        #--------- date -------------
        self.dt = datetime.date.today()
        date = Label(T_frame, text=self.dt, font=("times new roman",20,"bold"), bg="#292929", fg="white")
        date.place(x=1080, y=20)

        #====================================Variables========================================
        #-------------------- Stationary --------------------
        self.g_pen = IntVar()
        self.eraser = IntVar()
        self.marker = IntVar()
        self.n_book = IntVar()
        self.g_box = IntVar()
        self.c_pencil = IntVar()
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        #-------------------- Grocery --------------------
        self.rice = IntVar()
        self.bread = IntVar()
        self.flour = IntVar()
        self.fish = IntVar()
        self.sugar = IntVar() 
        self.cheese = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()
        self.var11 = IntVar()
        self.var12 = IntVar()
        #-------------------- Drinks --------------------
        self.fanta = IntVar()
        self.real = IntVar()
        self.limca = IntVar()
        self.tuborg = IntVar()
        self.wine = IntVar()
        self.redbull = IntVar()
        self.var13 = IntVar()
        self.var14 = IntVar()
        self.var15 = IntVar()
        self.var16 = IntVar()
        self.var17 = IntVar()
        self.var18 = IntVar()
        #------------------- Member ---------------------
        self.var19 = IntVar()
        #-------------- SET the variables '0' --------------
        self.set_0()
        #-------------------- Total Product Price and Tax Variable --------------------
        self.subtotal = StringVar()
        self.total_tax = StringVar()
        self.id = IntVar()
        self.discountamt = StringVar()
        self.grandttl = StringVar()
        self.received_amt = IntVar()

        #-------------------- Customer --------------------
        self.c_name = StringVar()
        self.c_mob = StringVar()
        self.receipt_no = StringVar()
        x = random.randint(1000,9999)
        self.receipt_no.set(str(x))
        self.search_receipt = StringVar()

        #================== Costumer Detail Frame ====================
        F1 = LabelFrame(self.master, text="Customer Details", font=("times new roman",15,"italic"), bd=12, relief=GROOVE, fg="gold", bg="#535353")
        F1.place(x=0, y=75, relwidth=1)

        name_l = Label(F1, text="Customer Name", bg="#535353",fg="white", font=("cambria",18,"bold"))
        name_l.pack(fill=BOTH, expand=True, side=LEFT)
        name_en=Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN)
        name_en.pack(fill=BOTH, expand=True, side=LEFT, pady=3)
        
        phn_l = Label(F1, text="Mobile No.", bg="#535353", fg="white", font=("times new roman",18,"bold"))
        phn_l.pack(fill=BOTH, expand=True, side=LEFT)
        phn_en = Entry(F1, width=15, textvariable=self.c_mob, font="arial 15", bd=7, relief=SUNKEN)
        phn_en.pack(fill=BOTH, expand=True, side=LEFT, pady=3)

        billno_l = Label(F1, text="Customer Bill No.", bg="#535353", fg="white", font=("times new roman",18,"bold"))
        billno_l.pack(fill=BOTH, expand=True, side=LEFT)
        billno_en =Entry(F1, width=15, textvariable=self.search_receipt, font="arial 15", bd=7, relief=SUNKEN)
        billno_en.pack(fill=BOTH, expand=True, side=LEFT, pady=3)
        
        search_btn = Button(F1, text="Search", command=self.find_receipt, width=10, bd=7, font="arial 12 bold")
        search_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=12, pady=3)

        #================== Receipt Area =========================
        F5 = Frame(self.master, bd=5, relief=GROOVE)
        F5.place(x=2, y=165, width=355, height=380)
        header = Label(F5, text="Receipt", font="arial 15 bold", bd=7, relief=GROOVE)
        header.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set, bg="#D5D5D5")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=True)

        #================== Stationary Frame ===================
        F2 = LabelFrame(self.master, text="Stationary", bd=8, relief=GROOVE, font=("times new roman",20,"bold","italic","underline"), fg="black", bg=bg_color)
        F2.place(x=361, y=165, width=325, height=380)

        g_pen_l = Checkbutton(F2, text="Gel Pen", font=("times new roman",16,"bold"),variable=self.var1, onvalue=1, offvalue=0, command=self.chkg_pen, bg=bg_color, fg="black")
        g_pen_l.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.g_pen_en = Entry(F2, textvariable=self.g_pen, width=9,state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.g_pen_en.grid(row=0, column=1, padx=10, pady=10)

        eraser_l = Checkbutton(F2, text="Eraser", font=("times new roman",16,"bold"),variable=self.var2, onvalue=1, offvalue=0, command=self.chkeraser, bg=bg_color, fg="black")
        eraser_l.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.eraser_en = Entry(F2, width=9, textvariable=self.eraser,state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.eraser_en.grid(row=1, column=1, padx=10, pady=10)

        marker_l = Checkbutton(F2, text="Marker", font=("times new roman",16,"bold"),variable=self.var3, onvalue=1, offvalue=0, command=self.chkmarker, bg=bg_color, fg="black")
        marker_l.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.marker_en = Entry(F2, width=9, textvariable=self.marker, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.marker_en.grid(row=2, column=1, padx=10, pady=10)

        n_book_l = Checkbutton(F2, text="Notebook", font=("times new roman",16,"bold"),variable=self.var4, onvalue=1, offvalue=0, command=self.chkn_book, bg=bg_color, fg="black")
        n_book_l.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.n_book_en = Entry(F2, width=9, textvariable=self.n_book, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.n_book_en.grid(row=3, column=1, padx=10, pady=10)

        g_box_l = Checkbutton(F2, text="Geometry Box", font=("times new roman",16,"bold"),variable=self.var5, onvalue=1, offvalue=0, command=self.chkg_box, bg=bg_color, fg="black")
        g_box_l.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.g_box_en = Entry(F2, width=9, textvariable=self.g_box, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.g_box_en.grid(row=4, column=1, padx=10, pady=10)

        c_pencil_l = Checkbutton(F2, text="Color Pencils", font=("times new roman",16,"bold"),variable=self.var6, onvalue=1, offvalue=0, command=self.chkm_pencil, bg=bg_color, fg="black")
        c_pencil_l.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.c_pencil_en = Entry(F2, width=9, textvariable=self.c_pencil, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.c_pencil_en.grid(row=5, column=1, padx=10, pady=10)
        


        #================== Grocery Frame =====================
        F3 = LabelFrame(self.master, text="Grocery", bd=8, relief=GROOVE, font=("times new roman",20,"bold","italic","underline"), fg="black", bg=bg_color)
        F3.place(x=691, y=165, width=325, height=380)

        rice_l = Checkbutton(F3, text="Rice", font=("times new roman",16,"bold"), variable=self.var7, onvalue=1, offvalue=0, command=self.chkrice, bg=bg_color, fg="black")
        rice_l.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.rice_en = Entry(F3, width=10, textvariable=self.rice, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.rice_en.grid(row=0, column=1, padx=10, pady=10)

        bread_l = Checkbutton(F3, text="Brown Bread", font=("times new roman",16,"bold"), variable=self.var8, onvalue=1, offvalue=0, command=self.chkbread, bg=bg_color, fg="black")
        bread_l.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.bread_en = Entry(F3, width=10, textvariable=self.bread, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.bread_en.grid(row=1, column=1, padx=10, pady=10)

        flour_l = Checkbutton(F3, text="Flour", font=("times new roman",16,"bold"), variable=self.var9, onvalue=1, offvalue=0, command=self.chkflour, bg=bg_color, fg="black")
        flour_l.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.flour_en = Entry(F3, width=10, textvariable=self.flour, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.flour_en.grid(row=2, column=1, padx=10, pady=10)

        fish_l = Checkbutton(F3, text="Fish", font=("times new roman",16,"bold"), variable=self.var10, onvalue=1, offvalue=0, command=self.chkfish, bg=bg_color, fg="black")
        fish_l.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.fish_en = Entry(F3, width=10, textvariable=self.fish, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.fish_en.grid(row=3, column=1, padx=10, pady=10)

        sugar_l = Checkbutton(F3, text="Sugar", font=("times new roman",16,"bold"), variable=self.var11, onvalue=1, offvalue=0, command=self.chksugar, bg=bg_color, fg="black")
        sugar_l.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.sugar_en = Entry(F3, width=10, textvariable=self.sugar, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.sugar_en.grid(row=4, column=1, padx=10, pady=10)

        cheese_l = Checkbutton(F3, text="Cheese", font=("times new roman",16,"bold"), variable=self.var12, onvalue=1, offvalue=0, command=self.chkcheese, bg=bg_color, fg="black")
        cheese_l.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.cheese_en = Entry(F3, width=10, textvariable=self.cheese, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.cheese_en.grid(row=5, column=1, padx=10, pady=10)
        

        #================== Drinks Frame ======================
        F4 = LabelFrame(self.master, text="Drinks", bd=8, relief=GROOVE, font=("times new roman",20,"bold","italic","underline"), fg="black", bg=bg_color)
        F4.place(x=1021, y=165, width=275, height=380)

        fanta_l = Checkbutton(F4, text="Fanta", font=("times new roman",16,"bold"), variable=self.var13, onvalue=1, offvalue=0, command=self.chkfanta, bg=bg_color, fg="black")
        fanta_l.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.fanta_en = Entry(F4, width=10, textvariable=self.fanta, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.fanta_en.grid(row=0, column=1, padx=10, pady=10)

        real_l = Checkbutton(F4, text="Real", font=("times new roman",16,"bold"), variable=self.var14, onvalue=1, offvalue=0, command=self.chkreal, bg=bg_color, fg="black")
        real_l.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.real_en = Entry(F4, width=10, textvariable=self.real, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.real_en.grid(row=1, column=1, padx=10, pady=10)

        limca_l = Checkbutton(F4, text="Limca", font=("times new roman",16,"bold"), variable=self.var15, onvalue=1, offvalue=0, command=self.chklimca, bg=bg_color, fg="black")
        limca_l.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.limca_en = Entry(F4, width=10, textvariable=self.limca, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.limca_en.grid(row=2, column=1, padx=10, pady=10)

        tuborg_l = Checkbutton(F4, text="Tuborg", font=("times new roman",16,"bold"), variable=self.var16, onvalue=1, offvalue=0, command=self.chktuborg, bg=bg_color, fg="black")
        tuborg_l.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.tuborg_en = Entry(F4, width=10, textvariable=self.tuborg, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.tuborg_en.grid(row=3, column=1, padx=10, pady=10)

        wine_l = Checkbutton(F4, text="Wine", font=("times new roman",16,"bold"), variable=self.var17, onvalue=1, offvalue=0, command=self.chkwine, bg=bg_color, fg="black")
        wine_l.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.wine_en = Entry(F4, width=10, textvariable=self.wine, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.wine_en.grid(row=4, column=1, padx=10, pady=10)

        redbull_l = Checkbutton(F4, text="Redbull", font=("times new roman",16,"bold"), variable=self.var18, onvalue=1, offvalue=0, command=self.chkredbull, bg=bg_color, fg="black")
        redbull_l.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.redbull_en = Entry(F4, width=10,textvariable=self.redbull, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        self.redbull_en.grid(row=5, column=1, padx=10, pady=10)

        #================== Button Frame ======================
        F6 = LabelFrame(self.master, text="Bill Menu", bd=8, relief=GROOVE, font=("times new roman",15,"italic"), fg="gold", bg="#535353")
        F6.place(x=0, y=548, relwidth=1, height=152)

        R1_l = Label(F6, text="Sub Total Amount", bg="#535353", fg="white", font=("times new roman",15,"bold"))
        R1_l.grid(row=0, column=0, padx=10, pady=1, sticky="w")
        R1_en = Entry(F6, textvariable=self.subtotal, width=16, font="arial 11 bold", bd=6, relief=SUNKEN)
        R1_en.grid(row=0, column=1, padx=10, pady=3)

        R2_l = Label(F6, text="Total Tax", bg="#535353", fg="white", font=("times new roman",14,"bold"))
        R2_l.grid(row=1, column=0, padx=10, pady=1, sticky="w")
        R2_en = Entry(F6, textvariable=self.total_tax, width=16, font="arial 11 bold", bd=6, relief=SUNKEN)
        R2_en.grid(row=1, column=1, padx=10, pady=1)

        R3_l = Checkbutton(F6, text="Membership ID No.", bg="#535353", fg="gold", font=("times new roman",15,"underline"), variable=self.var19, onvalue=1, offvalue=0, command=self.chkid)
        R3_l.grid(row=2, column=0, padx=10, pady=1, sticky="w")
        self.R3_en = Entry(F6, textvariable=self.id, width=16, font="arial 11 bold", state=DISABLED, bd=6, relief=SUNKEN)
        self.R3_en.grid(row=2, column=1, padx=10, pady=3)

        R4_l = Label(F6, text="Discount Amount", bg="#535353", fg="white", font=("times new roman",14,"bold"))
        R4_l.grid(row=0, column=2, padx=10, pady=1, sticky="w")
        R4_en = Entry(F6, textvariable=self.discountamt, width=16, font="arial 11 bold", bd=6, relief=SUNKEN)
        R4_en.grid(row=0, column=3, padx=10, pady=3)
       
        R5_l = Label(F6, text="Grand Total Amt", bg="#535353", fg="white", font=("times new roman",14,"bold"))
        R5_l.grid(row=1, column=2, padx=10, pady=1, sticky="w")
        R5_en = Entry(F6, textvariable=self.grandttl, width=16, font="arial 11 bold", bd=6, relief=SUNKEN)
        R5_en.grid(row=1, column=3, padx=10, pady=1)

        R6_l = Label(F6, text="Received Amount", bg="#535353", fg="white", font=("times new roman",14,"bold"))
        R6_l.grid(row=2, column=2, padx=10, pady=1, sticky="w")
        R6_en = Entry(F6, textvariable=self.received_amt, width=16, font="arial 11 bold", bd=6, relief=SUNKEN)
        R6_en.grid(row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=715, y=5, width=570, height=105)

        total_btn = Button(btn_F, text="Calculate", command=self.total, bg=bg_color, fg="black", pady=15, bd=2, width=10, font="arial 15 bold")
        total_btn.grid(row=0, column=0, padx=4, pady=10)
        Gbill_btn = Button(btn_F, text="Generate \nBill", command=self.receipt_area, bg=bg_color, fg="black", pady=3, bd=2, width=10, font="arial 15 bold")
        Gbill_btn.grid(row=0, column=1, padx=4, pady=5)
        Clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg=bg_color, fg="black", pady=15, bd=2, width=10, font="arial 15 bold")
        Clear_btn.grid(row=0, column=2, padx=4, pady=5)
        Exit_btn = Button(btn_F, text="Exit", command=self.Exit_app, bg=bg_color, fg="black", pady=15, bd=2, width=10, font="arial 15 bold")
        Exit_btn.grid(row=0, column=3, padx=4, pady=5)
        self.welcome_receipt()
    
    def total(self):
        self.s_gp_p = self.g_pen.get()*30
        self.s_e_p = self.eraser.get()*50
        self.s_m_p = self.marker.get()*50
        self.s_nb_p = self.n_book.get()*100
        self.s_gb_p = self.g_box.get()*450
        self.s_cp_p = self.c_pencil.get()*150
        self.total_stationary_price = float(
                                        self.s_gp_p+
                                        self.s_e_p+
                                        self.s_m_p+
                                        self.s_nb_p+
                                        self.s_gb_p+
                                        self.s_cp_p
                                        )

        self.g_r_p = self.rice.get()*2650
        self.g_b_p = self.bread.get()*80
        self.g_fl_p = self.flour.get()*350
        self.g_fi_p = self.fish.get()*500
        self.g_s_p = self.sugar.get()*72
        self.g_c_p = self.cheese.get()*200
        self.total_grocery_price = float(
                                        self.g_r_p+
                                        self.g_b_p+
                                        self.g_fl_p+
                                        self.g_fi_p+
                                        self.g_s_p+
                                        self.g_c_p
                                        )

        self.d_f_p = self.fanta.get()*220
        self.d_r_p = self.real.get()*180
        self.d_l_p = self.limca.get()*150
        self.d_t_p = self.tuborg.get()*340
        self.d_w_p = self.wine.get()*2100
        self.d_rb_p = self.redbull.get()*110
        self.total_drink_price = float(
                                        self.d_f_p+
                                        self.d_r_p+
                                        self.d_l_p+
                                        self.d_t_p+
                                        self.d_w_p+
                                        self.d_rb_p
                                        )

        self.subT = (round(
                            ((self.total_stationary_price)+
                            (self.total_grocery_price)+
                            (self.total_drink_price)),2)
                        )
        self.subtotal.set("Rs. "+str(self.subT))

        self.ttl_tax = (round(
                            ((self.total_stationary_price*0.05)+
                            (self.total_grocery_price*0.01)+
                            (self.total_drink_price*0.03)),2)
                        )
        self.total_tax.set("Rs. "+str(self.ttl_tax))

        self.ttl_amt = (round(
                            ((self.total_stationary_price)+
                            (self.total_grocery_price)+
                            (self.total_drink_price)+
                            (self.ttl_tax)),2)
                        )
        
        if self.id.get()!= 0 :
            self.discount = (round(
                                (0.05*self.ttl_amt),2)
                            )
            self.discountamt.set("Rs. "+str(self.discount))
        
            self.grand = (round(
                            (self.ttl_amt-self.discount),2)
            )
            self.grandttl.set("Rs. "+str(self.grand))
        else :
            self.grand = (
                            self.ttl_amt
            )
            self.grandttl.set("Rs. "+str(self.grand))

    def welcome_receipt(self):
        self.datetime = datetime.datetime.today().replace(microsecond=0)
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END, "\t    B$B Mart Pvt.Ltd \n\t\tBansbari\n")
        self.txtarea.insert(END, f"\n Bill No.  : {self.receipt_no.get()}")
        self.txtarea.insert(END, f"\n Customer  : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone No. : {self.c_mob.get()}")
        self.txtarea.insert(END, f"\n P.Time    : {self.datetime}")
        if self.id.get()!=0:
            self.txtarea.insert(END, f"\n Member ID : {self.id.get()}")
        self.txtarea.insert(END, f"\n----------------------------------------")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n----------------------------------------")

    def receipt_area(self):
        #======== calculate the amount to return =============
        self.received = self.received_amt.get()
        try:
            self.return_amt = (round(
                                (float(self.received) - 
                                self.grand),2)                    
                                )
        except AttributeError:
            messagebox.showerror("Error","Calculate the data first!")
        if self.c_name.get()=="" or self.c_mob.get()=="":
            messagebox.showerror("Error", "Customer Details are must")
        elif self.grandttl.get() == "" or self.grandttl.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        elif self.received_amt.get()==0:
            messagebox.showwarning("Reminder", "Please enter the received amount")
        else:
            self.welcome_receipt()

            #--------- Stationary ------------
            if self.g_pen.get() !=0:
                self.txtarea.insert(END, f"\n Gel Pen\t\t{self.g_pen.get()}\t\t{self.s_gp_p}")   
            if self.eraser.get() !=0:
                self.txtarea.insert(END, f"\n Eraser \t\t{self.eraser.get()}\t\t{self.s_e_p}")   
            if self.marker.get() !=0:
                self.txtarea.insert(END, f"\n Marker \t\t{self.marker.get()}\t\t{self.s_m_p}")   
            if self.n_book.get() !=0:
                self.txtarea.insert(END, f"\n Notebook\t\t{self.n_book.get()}\t\t{self.s_nb_p}")   
            if self.g_box.get() !=0:
                self.txtarea.insert(END, f"\n Geometry Box\t\t{self.g_box.get()}\t\t{self.s_gb_p}")   
            if self.c_pencil.get() !=0:
                self.txtarea.insert(END, f"\n Magic Pencils\t\t{self.c_pencil.get()}\t\t{self.s_cp_p}")

            #--------- Grocery ------------
            if self.rice.get() !=0:
                self.txtarea.insert(END, f"\n Rice    \t\t{self.rice.get()}\t\t{self.g_r_p}")   
            if self.bread.get() !=0:
                self.txtarea.insert(END, f"\n Bread   \t\t{self.bread.get()}\t\t{self.g_b_p}")   
            if self.flour.get() !=0:
                self.txtarea.insert(END, f"\n Flour   \t\t{self.flour.get()}\t\t{self.g_fl_p}")   
            if self.fish.get() !=0:
                self.txtarea.insert(END, f"\n Fish    \t\t{self.fish.get()}\t\t{self.g_fi_p}")   
            if self.sugar.get() !=0:
                self.txtarea.insert(END, f"\n Sugar   \t\t{self.sugar.get()}\t\t{self.g_s_p}")   
            if self.cheese.get() !=0:
                self.txtarea.insert(END, f"\n Cheese  \t\t{self.cheese.get()}\t\t{self.g_c_p}")

            #--------- Drinks ------------
            if self.fanta.get() !=0:
                self.txtarea.insert(END, f"\n Fanta   \t\t{self.fanta.get()}\t\t{self.d_f_p}")   
            if self.real.get() !=0:
                self.txtarea.insert(END, f"\n Real    \t\t{self.real.get()}\t\t{self.d_r_p}")   
            if self.limca.get() !=0:
                self.txtarea.insert(END, f"\n Limca   \t\t{self.limca.get()}\t\t{self.d_l_p}")   
            if self.tuborg.get() !=0:
                self.txtarea.insert(END, f"\n Tuborg  \t\t{self.tuborg.get()}\t\t{self.d_t_p}")   
            if self.wine.get() !=0:
                self.txtarea.insert(END, f"\n Wine    \t\t{self.wine.get()}\t\t{self.d_w_p}")   
            if self.redbull.get() !=0:
                self.txtarea.insert(END, f"\n Redbull \t\t{self.redbull.get()}\t\t{self.d_rb_p}") 

            self.txtarea.insert(END, f"\n----------------------------------------")
            if self.subtotal.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Subtotal Amount :\t\tRs. {self.subT}")
            self.txtarea.insert(END, f"\n Total Tax       :\t\tRs. {self.ttl_tax}")
            #if !=0 then..... use garne
            if self.id.get()!=0:
                try:
                    self.txtarea.insert(END, f"\n Discount Amount :\t\tRs. {self.discount}")
                except AttributeError:
                    messagebox.showerror("Error","Calculate the data and try again")
                    return
            self.txtarea.insert(END, f"\n----------------------------------------")
            self.txtarea.insert(END, f"\n Grand Total Amt :\t\tRs. {self.grand}")
            self.txtarea.insert(END, f"\n----------------------------------------")
            self.txtarea.insert(END, f"\n Received Amount :\t\tRs. {self.received}")
            self.txtarea.insert(END, f"\n Returned Amount :\t\tRs. {self.return_amt}")
            self.txtarea.insert(END, f"\n****************************************")
            self.txtarea.insert(END, "\n\t\tTHANK YOU!\n\t       VISIT AGAIN")
            self.txtarea.insert(END, f"\n****************************************")
            self.save_receipt()

    def save_receipt(self):
        op = messagebox.askyesno("Save Receipt", "Do you want to save the Bill?")
        if op>0:
            self.receipt_data = self.txtarea.get("1.0",END)
            f1 = open("bill3/"+str(self.receipt_no.get())+".txt","w")
            f1.write(self.receipt_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. {self.receipt_no.get()} saved successfully")
        else:
            return

    def find_receipt(self):
        present = "no"
        for i in os.listdir("bill3/"):
            if i.split('.')[0]==self.search_receipt.get():
                f1 = open(f"bill3/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error","Invalid Bill no.")

    def clear_data(self):
        op = messagebox.askyesno("Clear","Do you really want to Clear?")
        if op>0:
            self.set_0()
            self.chkg_pen()
            self.chkeraser()
            self.chkmarker()
            self.chkn_book()
            self.chkg_box()
            self.chkm_pencil()

            self.chkrice()
            self.chkbread()
            self.chkflour()
            self.chkfish()
            self.chksugar()
            self.chkcheese()

            self.chkfanta()
            self.chkreal()
            self.chklimca()
            self.chktuborg()
            self.chkwine()
            self.chkredbull()

            self.chkid()
            #------ Customer Details -------------
            self.c_name.set("")
            self.c_mob.set("")
            self.receipt_no.set("")
            x = random.randint(1000,9999)
            self.receipt_no.set(str(x))
            self.search_receipt.set("")
            #==================== Total Product Price and Tax Variable =================================
            self.subtotal.set("")
            self.total_tax.set("")
            self.id.set(0)
            self.discountamt.set("")
            self.grandttl.set("")
            self.received_amt.set(0)

            self.welcome_receipt()

    def Exit_app(self):
        op = messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.master.destroy()



GUI = Tk()
bis = main(GUI)
GUI.mainloop()
