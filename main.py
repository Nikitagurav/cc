############################################CREATED BY ARMAN RUSHIKESH SAURABH VED #################################
from tkinter import *
import random
import requests
import datetime



# price of products
Shower_gel = 100
Liquid_Shampoop = 140
Face_Washp = 240
Body_Sprayp = 340
Conditionerp = 260
Wheatp = 100
Jowarp = 180
Daalp = 80
Ricep = 80
Saltp = 20
Mountain_Dewp = 40
Limkap = 50
Pepsip = 60
Sodap = 20
Saucesp = 20

 # url = 'http://miniproject1.atwebpages.com/billdata.csv'
 #url = 'https://armannakhwa.cf/Degree/Python/bills.txt'
whichserver2="http://localhost/Python/"
whichserver="https://armannakhwa.cf/Degree/Python/"
class My_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x900+0+0")
        self.root.maxsize(width=1300, height=700)
        self.root.minsize(width=1280, height=700)
        self.root.title(" Bill Management System")

        # For View All Bills
        def openNewWindow():
            newWindow = Toplevel(root)
            newWindow.title("View All Bills")
            newWindow.geometry("1000x500")
          
            # read Data From Server
            url = whichserver+'bills.txt'
            myobj = {'somekey': 'somevalue'}
            x = requests.post(url, data=myobj)
            rscroll_y = Scrollbar(newWindow, orient=VERTICAL)
            self.rtxt = Text(newWindow, yscrollcommand=rscroll_y.set)
            rscroll_y.pack(side=RIGHT, fill=Y)
            rscroll_y.config(command=self.rtxt.yview)
            self.rtxt.pack(fill=BOTH, expand=1)
            self.rtxt.insert(END, f"{x.text}")

            #Download File From Server
            url = whichserver+'billdata.csv'
            r = requests.get(url, allow_redirects=True)
            open('billdata.csv', 'wb').write(r.content)

             #Download File From Server for localhost
            url = whichserver2+'billdata.csv'
            r = requests.get(url, allow_redirects=True)
            open('billdata.csv', 'wb').write(r.content)


        # ====================Variables========================#
        self.cus_name = StringVar()
        self.cus_mail = StringVar()
        self.c_phone = StringVar()
        # For Generating Random Bill Numbers
        x = random.randint(1000, 9999)
        self.c_bill_no = StringVar()
        # Seting Value to variable
        self.c_bill_no.set(str(x))

        self.shower_gel = IntVar()
        self.liquid_shampoo = IntVar()
        self.face_wash = IntVar()
        self.body_spray = IntVar()
        self.conditioner = IntVar()
        self.rice = IntVar()
        self.daal = IntVar()
        self.jowar = IntVar()
        self.wheat = IntVar()
        self.salt = IntVar()
        self.mountain_due = IntVar()
        self.pepsi = IntVar()
        self.limka = IntVar()
        self.soda = IntVar()
        self.sauces = IntVar()
        self.total_cosmetics = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()
       
           #Date
        now = datetime.datetime.now()
        self.pdate=now.strftime("%Y-%m-%d %H:%M:%S")


        # ===================================
        bg_color = "purple"
        fg_color = "white"
        lbl_color = 'white'

        # Title of App
        title = Label(self.root, text=" Bill Management System", bd=12, relief=GROOVE, fg=fg_color, bg=bg_color,
                      font=("times new roman", 30, "bold"), pady=3).pack(fill=X)

        # ==========Customers Frame==========#
        F1 = LabelFrame(text="Customer Details", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color,
                        relief=GROOVE, bd=10)
        F1.place(x=0, y=80, relwidth=1)

        # ===============Customer Name===========#
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color,
                          font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=5)
        cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        # =================Customer Phone==============#
        cphon_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20)
        cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphon_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        # ====================Customer Bill No==================#
        cbill_lbl = Label(F1, text="Bill No.", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold"))
        cbill_lbl.grid(row=0, column=4, padx=20)
        cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

        # ====================Customer Email===============#
        cmail_lbl = Label(F1, text="Customer Mail", bg=bg_color, fg=fg_color,
                          font=("times new roman", 15, "bold")).grid(row=0, column=6, padx=5)
        cmail_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_mail)
        cmail_en.grid(row=0, column=7, ipady=2, padx=0, ipadx=2, pady=2)



        # ==================Cosmetics Frame=====================#
        F2 = LabelFrame(self.root, text='Cosmetics', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F2.place(x=5, y=180, width=345, height=380)

        # ===========Frame Content
        bath_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Shower Gel")
        bath_lbl.grid(row=0, column=0, padx=10, pady=20)
        bath_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.shower_gel)
        bath_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======Liquid Shampoo
        face_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Liquid Shampoo")
        face_lbl.grid(row=1, column=0, padx=10, pady=20)
        face_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.liquid_shampoo)
        face_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # ========Face Wash
        wash_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Face Wash")
        wash_lbl.grid(row=2, column=0, padx=10, pady=20)
        wash_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.face_wash)
        wash_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========Body Spray
        hair_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Body Spray")
        hair_lbl.grid(row=3, column=0, padx=10, pady=20)
        hair_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.body_spray)
        hair_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============Conditioner
        lot_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Conditioner")
        lot_lbl.grid(row=4, column=0, padx=10, pady=20)
        lot_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.conditioner)
        lot_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ==================Grocery Frame=====================#
        F2 = LabelFrame(self.root, text='Grocery', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F2.place(x=330, y=180, width=325, height=380)

        # ===========Frame Content
        rice_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rice")
        rice_lbl.grid(row=0, column=0, padx=10, pady=20)
        rice_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.rice)
        rice_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======
        oil_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Jowar")
        oil_lbl.grid(row=1, column=0, padx=10, pady=20)
        oil_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.jowar)
        oil_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # =======
        daal_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Daal")
        daal_lbl.grid(row=2, column=0, padx=10, pady=20)
        daal_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.daal)
        daal_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========
        wheat_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Wheat")
        wheat_lbl.grid(row=3, column=0, padx=10, pady=20)
        wheat_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.wheat)
        wheat_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============
        salt_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Salt")
        salt_lbl.grid(row=4, column=0, padx=10, pady=20)
        salt_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.salt)
        salt_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ==================Other Stuff=====================#

        F2 = LabelFrame(self.root, text='Others', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F2.place(x=655, y=180, width=325, height=380)

        # ===========Frame Content
        mountain_due_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color,
                                 text="Mountain dew")
        mountain_due_lbl.grid(row=0, column=0, padx=10, pady=20)
        mountain_due_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.mountain_due)
        mountain_due_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======
        cock_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Pepsi")
        cock_lbl.grid(row=1, column=0, padx=10, pady=20)
        cock_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.pepsi)
        cock_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # =======
        limka_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Limka")
        limka_lbl.grid(row=2, column=0, padx=10, pady=20)
        limka_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.limka)
        limka_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========
        cold_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Soda")
        cold_lbl.grid(row=3, column=0, padx=10, pady=20)
        cold_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.soda)
        cold_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============
        bis_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Sauces")
        bis_lbl.grid(row=4, column=0, padx=10, pady=20)
        bis_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.sauces)
        bis_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ===================Bill Aera================#
        F3 = Label(self.root, bd=10, relief=GROOVE)
        F3.place(x=960, y=180, width=325, height=380)
        # ===========
        bill_title = Label(F3, text="Bill Area", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        # ============
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txt = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # ===========Buttons Frame=============#
        F4 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F4.place(x=0, y=560, relwidth=1, height=145)

        # ===================
        cosm_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Cosmetics")
        cosm_lbl.grid(row=0, column=0, padx=10, pady=0)
        cosm_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_cosmetics)
        cosm_en.grid(row=0, column=1, ipady=2, ipadx=5)

        # ===================
        gro_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Grocery")
        gro_lbl.grid(row=1, column=0, padx=10, pady=5)
        gro_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_grocery)
        gro_en.grid(row=1, column=1, ipady=2, ipadx=5)

        # ================
        oth_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Others Total")
        oth_lbl.grid(row=2, column=0, padx=10, pady=5)
        oth_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_other)
        oth_en.grid(row=2, column=1, ipady=2, ipadx=5)

        # ================
        cosmt_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Cosmetics Tax")
        cosmt_lbl.grid(row=0, column=2, padx=30, pady=0)
        cosmt_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_cos)
        cosmt_en.grid(row=0, column=3, ipady=2, ipadx=5)

        # =================
        grot_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Grocery Tax")
        grot_lbl.grid(row=1, column=2, padx=30, pady=5)
        grot_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_groc)
        grot_en.grid(row=1, column=3, ipady=2, ipadx=5)

        # ==================
        otht_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Others Tax")
        otht_lbl.grid(row=2, column=2, padx=10, pady=5)
        otht_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_other)
        otht_en.grid(row=2, column=3, ipady=2, ipadx=5)

        # ====================
        total_btn = Button(F4, text="Total", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.total)
        total_btn.grid(row=1, column=4, ipadx=20, padx=5)

        # ========================
        genbill_btn = Button(F4, text="Generate Bill", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                             relief=GROOVE, command=self.bill_area)
        genbill_btn.grid(row=1, column=5, ipadx=20)

        # ====================
        clear_btn = Button(F4, text="Clear", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.clear)
        clear_btn.grid(row=1, column=6, ipadx=20, padx=5)

        # ======================
        exit_btn = Button(F4, text="Exit", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.exit)
        exit_btn.grid(row=1, column=7, ipadx=20)
        #========================
        bill_btn = Button(F4, text="View All Bills", bd=7, relief=GROOVE, font=("times new roman", 12, "bold"),
                          bg=bg_color, fg=fg_color, command=openNewWindow)
        bill_btn.grid(row=1, column=8, ipady=2, padx=2, ipadx=20)

    # Function to get total prices
    def total(self):
        # =================Total Cosmetics Prices
        self.total_cosmetics_prices = (
                (self.shower_gel.get() * Shower_gel) +
                (self.liquid_shampoo.get() * Liquid_Shampoop) +
                (self.face_wash.get() * Face_Washp) +
                (self.body_spray.get() * Body_Sprayp) +
                (self.conditioner.get() * Conditionerp)
        )
        self.total_cosmetics.set("Rs. " + str(self.total_cosmetics_prices))
        self.tax_cos.set("Rs. " + str(round(self.total_cosmetics_prices * 0.05)))
        # ====================Total Grocery Prices
        self.total_grocery_prices = (
                (self.wheat.get() * Wheatp) +
                (self.jowar.get() * Jowarp) +
                (self.daal.get() * Daalp) +
                (self.rice.get() * Ricep) +
                (self.salt.get() * Saltp)

        )
        self.total_grocery.set("Rs. " + str(self.total_grocery_prices))
        self.tax_groc.set("Rs. " + str(round(self.total_grocery_prices * 0.05)))
        # ======================Total Other Prices
        self.total_other_prices = (
                (self.mountain_due.get() * Mountain_Dewp) +
                (self.limka.get() * Limkap) +
                (self.pepsi.get() * Pepsip) +
                (self.soda.get() * Sodap) +
                (self.sauces.get() * Saucesp)
        )
        self.total_other.set("Rs. " + str(self.total_other_prices))
        self.tax_other.set("Rs. " + str(round(self.total_other_prices * 0.05)))

    # Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "       Welcome To FAMT's  store\n")
        self.txt.insert(END, "               Invoice\n")
        self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END, f"\nCustomer Mail : {str(self.cus_mail.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, f"\nDate. : {str(self.pdate)}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, "\nProduct          Qty         Price")
        self.txt.insert(END, "\n===================================")

    # Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0', END)

    # Add Product name , qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.shower_gel.get() != 0:
            self.txt.insert(END,
                            f"\nShower gel        {self.shower_gel.get()}           {self.shower_gel.get() * Shower_gel}")
        if self.liquid_shampoo.get() != 0:
            self.txt.insert(END,
                            f"\nLiquid Shampoo    {self.liquid_shampoo.get()}           {self.liquid_shampoo.get() * Liquid_Shampoop}")
        if self.face_wash.get() != 0:
            self.txt.insert(END,
                            f"\nFace Wash         {self.face_wash.get()}           {self.face_wash.get() * Face_Washp}")
        if self.body_spray.get() != 0:
            self.txt.insert(END,
                            f"\nBody  Spray       {self.body_spray.get()}           {self.body_spray.get() * Body_Sprayp}")
        if self.conditioner.get() != 0:
            self.txt.insert(END,
                            f"\nConditioner       {self.conditioner.get()}           {self.conditioner.get() * Conditionerp}")
        if self.wheat.get() != 0:
            self.txt.insert(END, f"\nWheat             {self.wheat.get()}           {self.wheat.get() * Wheatp}")
        if self.jowar.get() != 0:
            self.txt.insert(END, f"\nJowar             {self.jowar.get()}           {self.jowar.get() * Jowarp}")
        if self.daal.get() != 0:
            self.txt.insert(END, f"\nDaal              {self.daal.get()}           {self.daal.get() * Daalp}")
        if self.rice.get() != 0:
            self.txt.insert(END, f"\nRice              {self.rice.get()}           {self.rice.get() * Ricep}")
        if self.salt.get() != 0:
            self.txt.insert(END, f"\nSalt              {self.salt.get()}           {self.salt.get() * Saltp}")
        if self.mountain_due.get() != 0:
            self.txt.insert(END,
                            f"\nMountain Dew      {self.mountain_due.get()}           {self.mountain_due.get() * Mountain_Dewp}")
        if self.limka.get() != 0:
            self.txt.insert(END, f"\nPepsi             {self.limka.get()}           {self.limka.get() * Limkap}")
        if self.pepsi.get() != 0:
            self.txt.insert(END, f"\nLimka             {self.pepsi.get()}           {self.pepsi.get() * Pepsip}")
        if self.soda.get() != 0:
            self.txt.insert(END, f"\nSoda              {self.soda.get()}           {self.soda.get() * Sodap}")
        if self.sauces.get() != 0:
            self.txt.insert(END, f"\nSauces            {self.sauces.get()}           {self.sauces.get() * Saucesp}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END,
                        f"\n Total : {self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices + self.total_cosmetics_prices * 0.05 + self.total_grocery_prices * 0.05 + self.total_other_prices * 0.05}")

        # send Mail

        cname = f"{str(self.cus_name.get())}"
        cphone = f"{str(self.c_phone.get())}"
        

        print("****************************")
        print(cname + cphone)
        mailmsg = ""
        onlyproducts = ""

        mailmsg += f"       Welcome To FAMT's  store\n"
        mailmsg += "               Invoice\n"
        mailmsg += f"\nBill No. : {str(self.c_bill_no.get())}"
        mailmsg += f"\nCustomer Name : {str(self.cus_name.get())}"
        mailmsg += f"\nCustomer Mail : {str(self.cus_mail.get())}"
        mailmsg += f"\nPhone No. : {str(self.c_phone.get())}"
        mailmsg +=f"\nDate. : {str(self.pdate)}"
        mailmsg += "\n==================================="
        mailmsg += f"\nProduct          Qty         Price"
        mailmsg += f"\n==================================="
        if self.shower_gel.get() != 0:
            mailmsg += f"\nShower gel        {self.shower_gel.get()}           {self.shower_gel.get() * Shower_gel}"
            onlyproducts += f"/Shower gel        {self.shower_gel.get()}           {self.shower_gel.get() * Shower_gel}"
        if self.liquid_shampoo.get() != 0:
            mailmsg += f"\n Liquid Shampoo    {self.liquid_shampoo.get()}           {self.liquid_shampoo.get() * Liquid_Shampoop}"
            onlyproducts += f"/ Liquid Shampoo    {self.liquid_shampoo.get()}           {self.liquid_shampoo.get() * Liquid_Shampoop}"
        if self.face_wash.get() != 0:
            mailmsg += f"\n Face Wash         {self.face_wash.get()}           {self.face_wash.get() * Face_Washp}"
            onlyproducts+= f"/ Face Wash         {self.face_wash.get()}           {self.face_wash.get() * Face_Washp}"
        if self.body_spray.get() != 0:
            mailmsg += f"\n Body  Spray       {self.body_spray.get()}           {self.body_spray.get() * Body_Sprayp}"
            onlyproducts += f"/ Body  Spray       {self.body_spray.get()}           {self.body_spray.get() * Body_Sprayp}"
        if self.conditioner.get() != 0:
            mailmsg += f"\nConditioner       {self.conditioner.get()}           {self.conditioner.get() * Conditionerp}"
            onlyproducts += f"/ Conditioner       {self.conditioner.get()}           {self.conditioner.get() * Conditionerp}"
        if self.wheat.get() != 0:
            mailmsg += f"\nWheat             {self.wheat.get()}           {self.wheat.get() * Wheatp}"
            onlyproducts += f"/ Wheat             {self.wheat.get()}           {self.wheat.get() * Wheatp}"
        if self.jowar.get() != 0:
            mailmsg += f"\nJowar             {self.jowar.get()}           {self.jowar.get() * Jowarp}"
            onlyproducts += f"/ Jowar             {self.jowar.get()}           {self.jowar.get() * Jowarp}"
        if self.daal.get() != 0:
            mailmsg += f"\nDaal              {self.daal.get()}           {self.daal.get() * Daalp}"
            onlyproducts += f"/ Daal              {self.daal.get()}           {self.daal.get() * Daalp}"
        if self.rice.get() != 0:
            mailmsg += f"\nRice              {self.rice.get()}           {self.rice.get() * Ricep}"
            onlyproducts += f"/ Rice              {self.rice.get()}           {self.rice.get() * Ricep}"
        if self.salt.get() != 0:
            mailmsg += f"\nSalt              {self.salt.get()}           {self.salt.get() * Saltp}"
            onlyproducts += f"/ Salt              {self.salt.get()}           {self.salt.get() * Saltp}"
        if self.mountain_due.get() != 0:
            mailmsg += f"\nMountain Dew      {self.mountain_due.get()}           {self.mountain_due.get() * Mountain_Dewp}"
            onlyproducts+= f"/ Mountain Dew      {self.mountain_due.get()}           {self.mountain_due.get() * Mountain_Dewp}"
        if self.limka.get() != 0:
            mailmsg += f"\nPepsi             {self.limka.get()}           {self.limka.get() * Limkap}"
            onlyproducts += f"/ Pepsi             {self.limka.get()}           {self.limka.get() * Limkap}"
        if self.pepsi.get() != 0:
            mailmsg += f"\nLimka             {self.pepsi.get()}           {self.pepsi.get() * Pepsip}"
            onlyproducts += f"/ Limka             {self.pepsi.get()}           {self.pepsi.get() * Pepsip}"
        if self.soda.get() != 0:
            mailmsg += f"\nSoda              {self.soda.get()}           {self.soda.get() * Sodap}"
            onlyproducts += f"/ Soda              {self.soda.get()}           {self.soda.get() * Sodap}"
        if self.sauces.get() != 0:
            mailmsg += f"\nSauces            {self.sauces.get()}           {self.sauces.get() * Saucesp}"
            onlyproducts += f"/Sauces            {self.sauces.get()}           {self.sauces.get() * Saucesp}"
        # mailmsg= "<br>==================================="
        mailmsg += f"\n Total : {self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices + self.total_cosmetics_prices * 0.05 + self.total_grocery_prices * 0.05 + self.total_other_prices * 0.05}"
        mailmsg += f"\n\n\n"
        onlyproductsTotal= f"{self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices + self.total_cosmetics_prices * 0.05 + self.total_grocery_prices * 0.05 + self.total_other_prices * 0.05}"
        print(mailmsg)


     
        #for Server used

        resp = requests.head(whichserver+'mail.php?BillNO='+str(self.c_bill_no.get())+'&name='+str(self.cus_name.get())+'&Mobile='+str(self.c_phone.get())+'&email='+str(self.cus_mail.get())+'&Products='+onlyproducts+'&Totalamt='+onlyproductsTotal+'&Date='+str(self.pdate)+'&message='+mailmsg)
        print(str(self.pdate))
        print(resp.text)

        #for localhost
        resp = requests.head(whichserver2+'mail.php?BillNO='+str(self.c_bill_no.get())+'&name='+str(self.cus_name.get())+'&Mobile='+str(self.c_phone.get())+'&email='+str(self.cus_mail.get())+'&Products='+onlyproducts+'&Totalamt='+onlyproductsTotal+'&Date='+str(self.pdate)+'&message='+mailmsg)
       



    # Function to exit
    def exit(self):
        self.root.destroy()

    # Function To Clear All Fields


root = Tk()
object = My_App(root)
root.mainloop()

############################################CREATED Arman Rushikesh Saurabh Ved#################################