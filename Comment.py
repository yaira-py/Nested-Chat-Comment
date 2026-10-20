import tkinter as tk

class NestedComments:
    def __init__(self,root):
        self.root=root
        self.root.title('Nested Chat Comments')
        self.root.geometry('450x500')
        self.root.configure(bg='white')
        
        self.top_frame=tk.Frame(self.root)
        self.top_frame.pack(fill='x',padx=10,pady=10)

        self.top_entry=tk.Entry(self.top_frame,width=8)
        self.top_entry.pack(side='left',fill='x',expand=True,padx=5,ipady=4)
        self.top_entry.insert(0,'add text here')
        self.top_entry.bind('<FocusIn>',self.clear_top)
        self.top_entry.bind('<FocusOut>',self.add_top)

        self.top_btn=tk.Button(self.top_frame,text='Submit',command= self.submit_top)
        self.top_btn.pack(side='right')

        self.main_area= tk.Frame(self.root,bg='white')
        self.main_area.pack(fill='both',expand=True,padx=10)

    def clear_top(self,e):
        if self.top_entry.get()=='add text here':
            self.top_entry.delete(0,'end')
            self.top_entry.config(fg='black')

    def add_top(self,e):
        if not self.top_entry.get():
            self.top_entry.insert(0,'add text here')
            self.top_entry.config(fg='grey')

    def create_comment(self,parent,text,indent):
        if indent>80:
            indent=80
        comment_frame= tk.Frame(parent,bg='white')
        comment_frame.pack(fill='x',pady=1,padx=(indent,0))

        bubble= tk.Label(comment_frame,bg='white')
        bubble.pack(fill='x')

        tk.Label(bubble,text=text,bg='white',anchor='w').pack(fill='x',padx=10)

        reply_area =tk.Frame(comment_frame,bg='white')
        reply_area.pack(fill='x')

        def show_reply_box():
            for child in reply_area.winfo_children():
                if isinstance(child,tk.Frame):
                    return


        row=tk.Frame(comment_frame,bg='white')
        row.pack(fill='x',pady=2,padx=10)

        entry=tk.Entry(row,width=17)
        entry.pack(side='left',padx=8)
        entry.focus_set()
            

        btn=tk.Button(row,text='>',command= lambda: self.submit_reply(entry,reply_area,indent))
        btn.pack(side='left')

        #tk.Button(comment_frame,text='Reply',fg='blue',bd=0,bg='white',command=show_reply_box).pack(anchor='w',padx=10)

        


    def submit_top(self):
        txt= self.top_entry.get().strip()
        if  not txt:
            return 
        self.create_comment(self.main_area,txt,0)
        self.top_entry.delete(0,'end')
        self.top_entry.insert(0,'add text here')
        self.top_entry.config(fg='grey')

    def submit_reply(self,entry_widget,reply_area,indent):
        text= entry_widget.get().strip()
        if not text:
          return

        if indent>150:
            indent=50
        self.create_comment(reply_area,text,indent+1)
        entry_widget.destroy()
        entry_widget.master.destroy()
        

        
            
                    
        




if __name__=='__main__':
    window= tk.Tk()
    app= NestedComments(window)
    window.mainloop()
