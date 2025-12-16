import tkinter as tk  
from tkinter import messagebox 
from tkinter import ttk
import math

m=tk.Tk() #mainwindowcode start
m.title("CYPHR : Home")
m.geometry("950x800")
m.configure(background="midnightblue")

h1=tk.Label(m,text="welcome to",font=("Times New Roman",35,"bold"),fg="white",bg="midnightblue")
h1.place(x=340,y=200)
h2=tk.Label(m,text="C Y P H R",font=("Times New Roman",100,"bold"),fg="gold",bg="midnightblue")
h2.place(x=160,y=275)
h1=tk.Label(m,text="What cypher would you like to do?",font=("Times New Roman",35,"bold"),fg="white",bg="midnightblue")
h1.place(x=120,y=425)

def affine():
    m2=tk.Tk()
    m2.title("CYPHR : Affine")
    m2.geometry("950x800")
    m2.configure(background="tomato")

    hm=tk.Label(m2,text="AFFINE",font=("Times New Roman",96,"bold"),fg="red4",bg="tomato")
    hm.place(x=235,y=100)
    h=tk.Label(m2,text="ENTER YOUR TEXT",font=("Times New Roman",39,"bold"),fg="white",bg="tomato")
    h.place(x=230,y=240)
    h1=tk.Label(m2,text="entry:",font=("Times New Roman",24,"bold"),fg="white",bg="tomato")
    h1.place(x=340,y=300)
    h2=tk.Label(m2,text="a,b :",font=("Times New Roman",24,"bold"),fg="white",bg="tomato")
    h2.place(x=340,y=350)
    h3=tk.Label(m2,text="output:",font=("Times New Roman",24,"bold"),fg="white",bg="tomato")
    h3.place(x=340,y=390)

    e=tk.Entry(m2)
    e.place(x=435,y=315)
    eq=tk.Entry(m2)
    eq.place(x=420,y=360)
    o=tk.Label(m2, text = '')
    o.place(x=455,y=405)

    #define functions
    def encoaff():
        lis = eq.get().split(',')
        a = int(lis[0]) #first key
        b = int(lis[1])#second key
        str1 = e.get() #message
        if(math.gcd(a,26)==1 and b>=0 and b<=25):
            def crypt(a,b,str1):
                E = 0 #new letter index after encrypting
                capital = 0
                crypt_word="" #to store encrypted text
                for i in str1:
                    if i.isalpha():
                        alphabet = "abcdefghijklmnopqrstuvwxyz"
                        if i.lower() in alphabet:
                            if(i.isupper()):
                                capital += 1 # to check for uppercase :p
                            c = alphabet.index(i.lower()) #letter number
                            E = a*c + b #the affine equation
                            while (E >= 26): #only 26 letters in eng, so to fit it in that range for indexing
                                E %= 26
                            for j in alphabet:
                                if(alphabet[E] == j): #comparing the gotten alphabet and the alphabet
                                    if(capital != 1):
                                        crypt_word += alphabet[E]
                                    else:
                                        crypt_word += alphabet[E].upper()
                                        capital = 0#convert to upper when needed based on count
                    else:
                        crypt_word += i #in case of any punctuation, space etc.
                return crypt_word
        o.config(text = crypt(a,b,str1))
        e.delete(0,tk.END)

    def decoaff():
        lis = eq.get().split(',')
        a = int(lis[0]) #first key
        b = int(lis[1])#second key
        str2 = e.get()
        def decrypt(a,b,str2):
            D = 0
            d = 0
            cr = ""
            for i in str2: #Hjq H
                if i.isalpha(): #True
                    al = "abcdefghijklmnopqrstuvwxyz"
                    if i.lower() in al: #True
                        if(i.isupper()):
                            d+=1# to check for uppercase :p
                        c = al.index(i.lower()) #7
                        a_inv = pow(a, -1, 26)
                        D = ((a_inv)*(c - b))%26 
                        while (D >= 26): #only 26 letters in eng, so to fit it in that range for indexing
                            D %= 26
                        for j in al:
                            if(al[D] == j): #comparing the gotten alphabet and the alphabet
                                if(d != 0):
                                    cr += al[D].upper()
                                    d = 0
                                else:
                                    cr += al[D]
                else:
                    cr += i #in case of any punctuation, space etc.
            return cr
        o.config(text = decrypt(a,b,str2))
        e.delete(0,tk.END)

                

                    

    b11=tk.Button(m2,text="ENCODE", command = encoaff,bg="gold", width=20, height = 3)
    b11.place(x=300,y=500)
    b12=tk.Button(m2,text="DECODE", command = decoaff, bg="gold", width=20, height=3)
    b12.place(x=530,y=500)

    m2.mainloop()




#atbash window
def atbash():
    m1=tk.Tk()
    m1.title("CYPHR : Atbash")
    m1.geometry("950x800")
    m1.configure(background="MediumPurple2")

    hm=tk.Label(m1,text="ATBASH",font=("Times New Roman",96,"bold"),fg="DeepPink4",bg="MediumPurple2")
    hm.place(x=235,y=100)
    h=tk.Label(m1,text="ENTER YOUR TEXT",font=("Times New Roman",39,"bold"),fg="white",bg="MediumPurple2")
    h.place(x=230,y=240)
    h1=tk.Label(m1,text="entry:",font=("Times New Roman",24,"bold"),fg="white",bg="MediumPurple2")
    h1.place(x=340,y=300)
    h2=tk.Label(m1,text="output:",font=("Times New Roman",24,"bold"),fg="white",bg="MediumPurple2")
    h2.place(x=340,y=350)

    e=tk.Entry(m1)
    e.place(x=435,y=315)
    o=tk.Label(m1, text = '')
    o.place(x=450,y=365)


    def encoatb():
        plaintext='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext='ZYXWVUTSRQPONMLKJIHGFEDCBA'
        encrypted_word=''
        decrypted_word=''
        w=''
        n=e.get() #getting the sentence from user
        n=n.upper()
        for w in n:
            if w==' ':
                encrypted_word=encrypted_word+' '
            else:
                ch=plaintext.index(w)
                f=ciphertext[ch]
                encrypted_word=encrypted_word+f
        o.config(text = encrypted_word)
        e.delete(0,tk.END)
    
    def decoatb():
        plaintext='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext='ZYXWVUTSRQPONMLKJIHGFEDCBA'
        encrypted_word=''
        decrypted_word=''
        w=''
        n=e.get()
        n=n.upper()
        for u in n:
            if u==' ':
                decrypted_word=decrypted_word+' '
            else:
                ch=ciphertext.index(u)
                f=plaintext[ch]
                decrypted_word=decrypted_word+f
        o.config(text = decrypted_word)
        e.delete(0,tk.END)
    
    b11=tk.Button(m1,text="ENCODE",command=encoatb,bg="orchid2", width=20, height=3)
    b11.place(x=300,y=450)
    b12=tk.Button(m1,text="DECODE",command=decoatb,bg="orchid2",width=20, height=3)
    b12.place(x=530,y=450)

    m1.mainloop()

#caesar window
def caesar():
    m3=tk.Tk()
    m3.title("CYPHR : Caesar")
    m3.geometry("950x800")
    m3.configure(background="deep sky blue")

    hm=tk.Label(m3,text="CAESAR",font=("Times New Roman",96,"bold"),fg="blue4",bg="deep sky blue")
    hm.place(x=235,y=100)
    h=tk.Label(m3,text="ENTER YOUR TEXT",font=("Times New Roman",39,"bold"),fg="white",bg="deep sky blue")
    h.place(x=230,y=240)
    h1=tk.Label(m3,text="entry:",font=("Times New Roman",24,"bold"),fg="white",bg="deep sky blue")
    h1.place(x=340,y=300)
    h2=tk.Label(m3,text="key  :",font=("Times New Roman",24,"bold"),fg="white",bg="deep sky blue")
    h2.place(x=340,y=350)
    h3=tk.Label(m3,text="output:",font=("Times New Roman",24,"bold"),fg="white",bg="deep sky blue")
    h3.place(x=340,y=390)

    e=tk.Entry(m3)
    e.place(x=435,y=315)
    eq=tk.Entry(m3)
    eq.place(x=420,y=360)
    o=tk.Label(m3, text = '')
    o.place(x=455,y=405)

    #define functions
    def encocae():
        t=e.get()
        k=int(eq.get())
        letters ='abcdefghijklmnopqrstuvwxyz'
        num_letters= 26

        def encrypt(plaintext,key):
            ciphertext=''
            for letter in plaintext:
                letter = letter.lower()
                if not letter == ' ':
                    index = letters.find(letter)
                    if index == -1:
                        ciphertext += letter
                    else:
                        new_index = index + key
                        if new_index >= 26:
                            new_index -=26
                        ciphertext += letters[new_index]
            return ciphertext
        o.config(text = encrypt(t,k))
        e.delete(0,tk.END)
    
    def decocae():
        t=e.get()
        k=int(eq.get())
        letters ='abcdefghijklmnopqrstuvwxyz'
        num_letters= len(letters)
        def decrypt(ciphertext,key):
            plaintext =''
            for letter in ciphertext:
                letter = letter .lower()
                if not letter == ' ':
                    index = letters.find(letter)
                    if index == -1:
                        plaintext += letter
                    else:
                        new_index = index - key
                        if new_index < 0 :
                            new_index += num_letters
                        plaintext += letters[new_index]
            return plaintext
        o.config(text = decrypt(t,k))
        e.delete(0,tk.END)
        

    b11=tk.Button(m3,text="ENCODE", command = encocae, bg="DodgerBlue3",width = 20, height=3)
    b11.place(x=300,y=450)
    b12=tk.Button(m3,text="DECODE",command = decocae, bg="DodgerBlue3", width =20, height=3)
    b12.place(x=530,y=450)


    m3.mainloop()



#railfence window
def railfence():
    m4=tk.Tk()
    m4.title("CYPHR : Railfence")
    m4.geometry("950x800")
    m4.configure(background="hot pink")

    hm=tk.Label(m4,text="RAILFENCE",font=("Times New Roman",96,"bold"),fg="medium violet red",bg="hot pink")
    hm.place(x=100,y=100)
    h=tk.Label(m4,text="ENTER YOUR TEXT",font=("Times New Roman",39,"bold"),fg="white",bg="hot pink")
    h.place(x=230,y=240)
    h1=tk.Label(m4,text="entry:",font=("Times New Roman",24,"bold"),fg="white",bg="hot pink")
    h1.place(x=340,y=300)
    h2=tk.Label(m4,text="rails:",font=("Times New Roman",24,"bold"),fg="white",bg="hot pink")
    h2.place(x=340,y=350)
    h3=tk.Label(m4,text="output:",font=("Times New Roman",24,"bold"),fg="white",bg="hot pink")
    h3.place(x=340,y=390)

    e=tk.Entry(m4)
    e.place(x=435,y=315)
    eq=tk.Entry(m4)
    eq.place(x=420,y=360)
    o=tk.Label(m4, text = '')
    o.place(x=455,y=405)

    #define functions
    def encorail():
        text = e.get()
        n = int(eq.get())
        fence=[""]*n
        r=0
        step=1
        for ch in text:
            fence[r]+=ch
            r+=step
            if r==n-1:
                step=-1
            if r==0:
                step=1
        cipher="".join(fence)
        
        o.config(text = cipher)
        e.delete(0,tk.END)

    def decorail():
        text = e.get()
        n = int(eq.get())
        pattern=[]
        for i in range(n):
            row=[]
            for j in range(len(text)):
                row.append("")
            pattern.append(row)
        r=0
        step=1
        for i in range(len(text)):
            pattern[r][i]="*"
            r+=step
            if r==n-1:
                step=-1
            if r==0:
                step=1
        index=0
        for rr in range(n):
            for cc in range(len(text)):
                if pattern[rr][cc]=="*":
                    pattern[rr][cc]=text[index]
                    index+=1
        result=""
        rail=0
        step=1
        for c in range(len(text)):
            result+=pattern[rail][c] 
            rail+=step
            if rail==n-1:
                step=-1
            if rail==0:
                step=1

        o.config(text = result)
        e.delete(0,tk.END)
    
    b111=tk.Button(m4,text="ENCODE", command = encorail,bg="deep pink",width=20, height=3)
    b111.place(x=300,y=450)
    b122=tk.Button(m4,text="DECODE", command = decorail, bg="deep pink",width=20, height=3)
    b122.place(x=530,y=450)


    m4.mainloop()


b1=tk.Button(m,text="AFFINE",command=affine,bg="tomato") #SlateBlue1
b1.place(x=330,y=500)
b2=tk.Button(m,text="ATBASH",command=atbash,bg="MediumPurple2")
b2.place(x=420,y=500)
b3=tk.Button(m,text="CAESAR",command=caesar,bg="DodgerBlue3")
b3.place(x=520,y=500)
b4=tk.Button(m,text="RAILFENCE",command=railfence,bg="hot pink")
b4.place(x=610,y=500)


m.mainloop()
