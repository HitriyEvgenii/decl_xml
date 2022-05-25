import sqlite3
import tkinter as tk
import tkinter.ttk as ttk


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)


        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)

class App_filter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame_top = tk.Frame(self)
        self.frame_top.pack()
        self.frame_bottom = tk.Frame(self)
        self.frame_bottom.pack()

        self.label_2 = tk.Label(self.frame_top, text="Граница", width=7, height=1, bg='yellow')
        self.label_2.pack(side=tk.LEFT, anchor=tk.W)
        self.input_2 = tk.StringVar()
        border = list(set(row[0] for row in data))
        border.sort()
        self.input_1 = ttk.Combobox(self.frame_top, width=25, values=border) #, postcommand=self.post_border
        self.input_1.bind("<<ComboboxSelected>>", self.data_update_border)
        self.input_1.pack(side=tk.LEFT, anchor=tk.W)

        self.label_2 = tk.Label(self.frame_top, text="Город", width=7, height=1, bg='green')
        self.label_2.pack(side=tk.LEFT, anchor=tk.W)
        self.input_2 = tk.StringVar()
        border = list(set(row[1] for row in data))
        border.sort()
        self.input_2 = ttk.Combobox(self.frame_top, width=25, values=border)
        self.input_2.bind("<<ComboboxSelected>>", self.data_update_city)
        self.input_2.pack(side=tk.LEFT, anchor=tk.W)

        self.button = Table(self.frame_bottom, headings=('Пункт перехода', 'Город назначения', 'Стоимость'), rows=data)
        self.button.pack(expand=tk.YES, fill=tk.BOTH)

    def data_update_border(self, event):
        value = self.input_1.get()
        cursor.execute(f"SELECT border, city, transport_cost FROM routs where border = '{str(value)}'")
        data = list(row for row in cursor.fetchall())
        self.button.destroy()
        self.button = Table(self.frame_bottom, headings=('Пункт перехода', 'Город назначения', 'Стоимость'), rows=data)
        self.button.pack(expand=tk.YES, fill=tk.BOTH)
        self.input_2['values'] = ['*'] + [row[1] for row in data if row[0] == value]
        return self.frame_bottom.update()

    def data_update_city(self, event):
        value = self.input_2.get()
        cursor.execute(f"SELECT border, city, transport_cost FROM routs where city = '{str(value)}'")
        data = list(row for row in cursor.fetchall())
        self.button.destroy()
        self.button = Table(self.frame_bottom, headings=('Пункт перехода', 'Город назначения', 'Стоимость'), rows=data)
        self.button.pack(expand=tk.YES, fill=tk.BOTH)


        return self.frame_bottom.update()




#data = (,)
connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()
cursor.execute("SELECT border, city, transport_cost FROM routs")
#data = (row for row in cursor.fetchall())
data = set(row for row in cursor.fetchall())
cursor.execute("SELECT border FROM routs order by border")


data1 = list(set(row[0] for row in cursor.fetchall()))
#print(data1)

if __name__ == "__main__":
    root = App_filter()


    root.mainloop()