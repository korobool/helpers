from Tkinter import *
from sql_processor import sql_processor

class Application(Frame):              
    def __init__(self, master=None):
        Frame.__init__(self, master)   
        self.grid()                    
        self.createWidgets()

    def createWidgets(self):
#        self.quitButton = Button ( self, text='Quit',
#            command=self.quit )
        self.text_area_sql = Text()
        self.text_area_result = Text()

        self.text_area_sql.config(state=NORMAL)

        self.okButton = Button ( self, text='Ok',
            command = self.myCommand )

        self.text_area_sql.grid()
        self.text_area_result.grid()
        self.okButton.grid()

    def myCommand(self):
        request = self.text_area_sql.get(1.0, END)
        processor = sql_processor()
        self.text_area_result.delete(1.0, END)
        try:
            tuples = processor.process(request)


            self.text_area_result.insert(1.0, self.format_tuples(tuples))
        except:
            self.text_area_result.insert(1.0, "ERROR")



    def format_tuples(self, tuples):
        formatted_table = ''
        for i in tuples:
            temp = ''
            for j in i:
                temp = temp + ' | ' + str(j).center(20)
            formatted_table = formatted_table + temp + ' | ' '\n'
        return formatted_table

app = Application()                    
app.master.title("Sample application")

app.mainloop()  