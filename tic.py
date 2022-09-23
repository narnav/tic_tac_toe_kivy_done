import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

class Grid_LayoutApp(App):
	x_turn=True
	row1=[]
	row2=[]
	row3=[]

	def play(self,instance):
		if instance.text == '-': #if text = '-' we can play
			if self.x_turn:
				instance.text ="X"
			else:
				instance.text ="O"
			self.x_turn =not self.x_turn
		if self.chk_win(instance):
			if self.x_turn:
				popup = Popup(title='win msg', content=Label(text='O won'),auto_dismiss=False)
			else:
				popup = Popup(title='win msg', content=Label(text='X won'),auto_dismiss=False)
			popup.open()
			print (f'{self.x_turn} won')

	def chk_win(self,instance):
		win =False
		# rows
		if self.row1[0].text != '-':
		 	if self.row1[0].text  == self.row1[1].text and self.row1[2].text  == self.row1[1].text: win =True
		if self.row2[0].text != '-':
			if self.row2[0].text  == self.row2[1].text and self.row2[2].text  == self.row2[1].text: win =True
		if self.row3[0].text != '-':
			if self.row3[0].text  == self.row3[1].text and self.row3[2].text  == self.row3[1].text: win =True

		# cols
		if self.row1[0].text != '-':
		 	if self.row1[0].text  == self.row2[0].text and self.row1[0].text  == self.row3[0].text: win =True
		if self.row2[1].text != '-':
			if self.row1[1].text  == self.row2[1].text and self.row1[1].text  == self.row3[1].text: win =True
		if self.row3[2].text != '-':
			if self.row1[2].text  == self.row2[2].text and self.row1[2].text  == self.row3[2].text: win =True


		# Diagonal
		if self.row1[0].text != '-':
		 	if self.row1[0].text  == self.row2[1].text and self.row1[0].text  == self.row3[2].text: win =True
		if self.row3[0].text != '-':
			if self.row1[2].text  == self.row2[1].text and self.row1[2].text  == self.row3[0].text: win =True

		return win
	
	def build(self):
		layout = GridLayout(cols =3)
		
		self.row1 =[Button(text ='-',on_press=self.play),Button(text ='-',on_press=self.play),Button(text ='-',on_press=self.play)]
		self.row2 =[Button(text ='-',on_press=self.play),Button(text ='-',on_press=self.play),Button(text ='-',on_press=self.play)]
		self.row3 =[Button(text ='-',on_press=self.play),Button(text ='-',on_press=self.play),Button(text ='-',on_press=self.play)]
		layout.add_widget(self.row1[0])
		layout.add_widget(self.row1[1])
		layout.add_widget(self.row1[2])
		layout.add_widget(self.row2[0])
		layout.add_widget(self.row2[1])
		layout.add_widget(self.row2[2])
		layout.add_widget(self.row3[0])
		layout.add_widget(self.row3[1])
		layout.add_widget(self.row3[2])
		return layout

root = Grid_LayoutApp()
root.run()
