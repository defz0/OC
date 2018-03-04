import tkinter as tk
import pickle

class Main(tk.Frame):
	def __init__(self, root):
		super().__init__(root)
		self.init_main()

	def init_main(self):
		btn_syr = tk.Button(root, text = "Споровые взвеси", command = self.open_syr, bg = "green", width = 40)
		btn_syr.pack()
		btn_incub = tk.Button(root, text = "Инкубация", command = self.open_incub, bg = "green", width = 40)
		btn_incub.pack()
		btn_fruit = tk.Button(root, text = "Плодоношение", command = self.open_fruit, bg = "green", width = 40)
		btn_fruit.pack()

	def open_syr(self):
		syr()
	def open_incub(self):
		incub()
	def open_fruit(self):
		fruit()

class syr(tk.Toplevel):

	def __init__(self):
		super().__init__(root)
		self.init_syr()

	def open_add_syr(self):
		add_syr()
		syr.destroy(self)

	def init_syr(self):
		self.title("История споровых взвесей")
		self.geometry("450x310+300+200")
		self.resizable(False, False)

		self.grab_set()
		self.focus_set()

		listbox_syr = tk.Listbox(self, height=17, width=72)
		try:
			file = open('syr.wb','rb')
			load = pickle.load(file)
			file.close()
		except IOError as e:
			load = ['Пока ничего нет!']
		for i in load:
			listbox_syr.insert(tk.END, i)
		listbox_syr.pack()
		
		btn_addsyr = tk.Button(self, text = "Добавить споровую взвесь", command = self.open_add_syr, bg = "green", width = 40)
		btn_addsyr.pack()

class add_syr(tk.Toplevel):

	def __init__(self):
		super().__init__(root)
		self.init_add_syr()

	def init_add_syr(self):
		self.title("Добавить позицию")
		self.geometry("300x180+300+200")
		self.resizable(False, False)

		self.grab_set()
		self.focus_set()
		def write(event):
			try:
				file = open('syr.wb','rb')
			except IOError as e:
				file = open('syr.wb','wb')
				pickle.dump(["|Дата:" + entry_date.get() + "|  |Маркировка:" + entry_mark.get() + "|  |Время регидратации:" + entry_time.get() + "|"], file)
				file.close()
				add_syr.destroy(self)
				syr()
			else:
				load = pickle.load(file)
				file.close()
				new_index = "|Дата:" + entry_date.get() + "|  |Маркировка:" + entry_mark.get() + "|  |Время регидратации:" + entry_time.get() + "|"
				load.append(new_index)
				print(load)
				file = open('syr.wb','wb')
				pickle.dump(load, file)
				file.close()
				add_syr.destroy(self)
				syr()

		entry_date_L = tk.Label(self, text = "Дата")
		entry_date_L.pack()
		entry_date = tk.Entry(self, width = 40, bd = 5)
		entry_date.pack()
		entry_mark_L = tk.Label(self, text = "Маркировка")
		entry_mark_L.pack()
		entry_mark = tk.Entry(self, width = 40, bd = 5)
		entry_mark.pack()
		entry_time_L = tk.Label(self, text = "Время регидратации")
		entry_time_L.pack()
		entry_time = tk.Entry(self, width = 40, bd = 5)
		entry_time.pack()
		btn_add_position = tk.Button(self, text = "OK", bg = "green", width = 17)
		btn_add_position.bind("<Button-1>", write)
		btn_add_position.pack()

class incub(tk.Toplevel):

	def __init__(self):
		super().__init__(root)
		self.init_incub()

	def open_add_incub(self):
		add_incub()
		incub.destroy(self)

	def init_incub(self):
		self.title("История инкубаций")
		self.geometry("450x310+300+200")
		self.resizable(False, False)

		self.grab_set()
		self.focus_set()

		listbox_syr = tk.Listbox(self, height=17, width=72)
		try:
			file = open('incub.wb','rb')
			load = pickle.load(file)
			file.close()
		except IOError as e:
			load = ['Пока ничего нет!']
		for i in load:
			listbox_syr.insert(tk.END, i)
		listbox_syr.pack()

		btn_addsyr = tk.Button(self, text = "Добавить инкубационный образец", command = self.open_add_incub, bg = "green", width = 40)
		btn_addsyr.pack()

class add_incub(tk.Toplevel):

	def __init__(self):
		super().__init__(root)
		self.init_add_incub()

	def init_add_incub(self):
		self.title("Добавить позицию")
		self.geometry("300x225+300+200")
		self.resizable(False, False)

		self.grab_set()
		self.focus_set()
		def write(event):
			try:
				file = open('incub.wb','rb')
			except IOError as e:
				file = open('incub.wb','wb')
				pickle.dump(["|Дата:" + entry_date.get() + "|  |Маркировка:" + entry_mark.get() + "|  |Время инкубации:" + entry_time.get() + "|  |Статус:" + entry_status.get() + "|"], file)
				file.close()
				add_incub.destroy(self)
				incub()
			else:
				load = pickle.load(file)
				file.close()
				new_index = "|Дата:" + entry_date.get() + "|  |Маркировка:" + entry_mark.get() + "|  |Время инкубации:" + entry_time.get() + "|  |Статус:" + entry_status.get() + "|"
				load.append(new_index)
				print(load)
				file = open('incub.wb','wb')
				pickle.dump(load, file)
				file.close()
				add_incub.destroy(self)
				incub()

		entry_date_L = tk.Label(self, text = "Дата")
		entry_date_L.pack()
		entry_date = tk.Entry(self, width = 40, bd = 5)
		entry_date.pack()
		entry_mark_L = tk.Label(self, text = "Маркировка")
		entry_mark_L.pack()
		entry_mark = tk.Entry(self, width = 40, bd = 5)
		entry_mark.pack()
		entry_time_L = tk.Label(self, text = "Время инкубации")
		entry_time_L.pack()
		entry_time = tk.Entry(self, width = 40, bd = 5)
		entry_time.pack()
		entry_status_L = tk.Label(self, text = "Статус")
		entry_status_L.pack()
		entry_status = tk.Entry(self, width = 40, bd = 5)
		entry_status.pack()
		btn_add_position = tk.Button(self, text = "OK", bg = "green", width = 17)
		btn_add_position.bind("<Button-1>", write)
		btn_add_position.pack()

class fruit(tk.Toplevel):

	def __init__(self):
		super().__init__(root)
		self.init_fruit()

	def open_add_fruit(self):
		add_fruit()
		fruit.destroy(self)

	def init_fruit(self):
		self.title("История плодоношений")
		self.geometry("450x310+300+200")
		self.resizable(False, False)

		self.grab_set()
		self.focus_set()

		listbox_syr = tk.Listbox(self, height=17, width=72)
		try:
			file = open('fruit.wb','rb')
			load = pickle.load(file)
			file.close()
		except IOError as e:
			load = ['Пока ничего нет!']
		for i in load:
			listbox_syr.insert(tk.END, i)
		listbox_syr.pack()

		btn_addsyr = tk.Button(self, text = "Добавить историю плодоношения", command = self.open_add_fruit, bg = "green", width = 40)
		btn_addsyr.pack()

class add_fruit(tk.Toplevel):

	def __init__(self):
		super().__init__(root)
		self.init_add_fruit()

	def init_add_fruit(self):
		self.title("Добавить позицию")
		self.geometry("300x325+300+200")
		self.resizable(False, False)

		self.grab_set()
		self.focus_set()
		def write(event):
			try:
				file = open('fruit.wb','rb')
			except IOError as e:
				file = open('fruit.wb','wb')
				pickle.dump(["|Дата:" + entry_date.get() + "|  |Маркировка:" + entry_mark.get() + "|  |Время инкубации:" + entry_time.get() + "|  |Волна:" + entry_wave.get() + "|  |Урожай:" + entry_weight.get() + "|  |Статус:" + entry_status.get() + "|"], file)
				file.close()
				add_fruit.destroy(self)
				fruit()
			else:
				load = pickle.load(file)
				file.close()
				new_index = "|Дата:" + entry_date.get() + "|  |Маркировка:" + entry_mark.get() + "|  |Время инкубации:" + entry_time.get() + "|  |Волна:" + entry_wave.get() + "|  |Урожай:" + entry_weight.get() + "|  |Статус:" + entry_status.get() + "|"
				load.append(new_index)
				print(load)
				file = open('fruit.wb','wb')
				pickle.dump(load, file)
				file.close()
				add_fruit.destroy(self)
				fruit()

		entry_date_L = tk.Label(self, text = "Дата")
		entry_date_L.pack()
		entry_date = tk.Entry(self, width = 40, bd = 5)
		entry_date.pack()
		entry_mark_L = tk.Label(self, text = "Маркировка")
		entry_mark_L.pack()
		entry_mark = tk.Entry(self, width = 40, bd = 5)
		entry_mark.pack()
		entry_time_L = tk.Label(self, text = "Время инкубации")
		entry_time_L.pack()
		entry_time = tk.Entry(self, width = 40, bd = 5)
		entry_time.pack()
		entry_wave_L = tk.Label(self, text = "Волна")
		entry_wave_L.pack()
		entry_wave = tk.Entry(self, width = 40, bd = 5)
		entry_wave.pack()
		entry_weight_L = tk.Label(self, text = "Общий урожай")
		entry_weight_L.pack()
		entry_weight = tk.Entry(self, width = 40, bd = 5)
		entry_weight.pack()
		entry_status_L = tk.Label(self, text = "Статус")
		entry_status_L.pack()
		entry_status = tk.Entry(self, width = 40, bd = 5)
		entry_status.pack()
		btn_add_position = tk.Button(self, text = "OK", bg = "green", width = 17)
		btn_add_position.bind("<Button-1>", write)
		btn_add_position.pack()


if __name__ == "__main__":
	root = tk.Tk()
	app = Main(root)
	app.pack()
	root.title("Shroomer history")
	root.geometry("300x80+300+200")
	root.resizable(False, False)
	root.mainloop()