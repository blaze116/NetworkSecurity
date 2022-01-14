import tkinter as tk

'''
    This is the code for a message encryption and decryption 
    desktop application using python tkinter. 
'''

light_gray = "#cce2f1"

class Converter:                            
    def __init__(self):
        self.window= tk.Tk()              # This is to create a basic window
        self.window.geometry("700x350")  # this is for the size of the window
        # self.window.resizable(0,0)        # comment out this line to make window size fixed
        self.window.title("Message Encryption-Decryption")    # Window title
        self.design_frame = self.make_design()
        self.display_frame = self.create_display()
        self.lab1, self.lab2 = self.create_lab()
        self.button_frame = self.create_button()
        self.plain, self.cipher = self.create_txt()
        self.but1, self.but2 = self.make_button()


    def encipherfun(self):                  # Function to encrypt the message
        res= self.plain.get("1.0",tk.END)
        s=""

        for i in res:
            if(i==' ' or i=='\n'):
                s+=i
            elif(i>='a' and i<='z'):
                s+=chr(ord('a')+ord('z')-ord(i))
            elif(i>='A' and i<='Z'):
                s+=chr(ord('A')+ord('Z')-ord(i))
        self.cipher.delete("1.0", tk.END)
        self.cipher.insert(tk.END,s)

    def decipherfun(self):                      # Function to decrypt the message
        res= self.cipher.get("1.0",tk.END)
        s=""

        for i in res:
            if(i==' ' or i=='\n'):
                s+=i
            elif(i>='a' and i<='z'):
                s+=chr(ord('a')+ord('z')-ord(i))
            elif(i>='A' and i<='Z'):
                s+=chr(ord('A')+ord('Z')-ord(i))
        self.plain.delete("1.0", tk.END)
        self.plain.insert(tk.END,s)


    def make_button(self):                         # 
        but1 = tk.Button(self.window, text="Encipher", bg="#29A9D3", fg="white", height=1, width=10,font=("Cipsta",12,"bold"), command=self.encipherfun)
        but1.place(x=10, y=275)
        but2 = tk.Button(self.window, text="Decipher", bg="#29A9D3", fg="white", height=1, width=10,font=("Cipsta",12,"bold"), command=self.decipherfun)
        but2.place(x=360, y=275)
        return but1, but2

    def create_txt(self):
        plain = tk.Text(width=40, height=10, bg="#A6BBC3", padx=5, pady=5,font=("Courier",10, "bold"))
        plain.place(x=10, y=60)

        cipher = tk.Text(width=40, height=10, bg="#A6BBC3", padx=5, pady=5,font=("Courier",10, "bold"))
        cipher.place(x=360, y=60)

        return plain,cipher

         
    def create_lab(self):
        lab1 = tk.Label(self.display_frame, text="PLAINTEXT", bg="#cce2f1", padx=10, font=("Times",16,"bold italic"))
        lab1.pack(expand="True", fill="both")
        lab1.place(x=70,y=10)

        lab2 = tk.Label(self.display_frame, text="CIPHERTEXT", bg="#cce2f1", padx=10, font=("Times",16,"bold italic"))
        lab2.place(x=450,y=10)

        return lab1,lab2
        

    def make_design(self):                                              # creating design frame
        frame = tk.Frame(master=self.window, height=20,bg="#32AFF8")
        frame.pack(fill=tk.X,side= tk.TOP)
        return frame

    def create_display(self):                                           # This is to create frame for input fields
        frame = tk.Frame(master=self.window,height=300,bg=light_gray)
        frame.pack(expand="True", fill="both")
        return frame 

    def create_button(self):                                               # This is for creating frame for input fields
        frame = tk.Frame(master=self.window, bg=light_gray)
        frame.pack(expand="True", fill="both")
        return frame

    def run(self):
        self.window.mainloop()

if __name__=='__main__':
    solver = Converter()                        # Creating class object
    solver.run()