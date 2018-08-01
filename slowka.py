from tkinter import *
from tkinter import ttk
import time,random




def czytanie():
	global ile
	plik = open('slowka.txt')
	try:
		slowka = plik.read().split("\n")
	finally:
		plik.close()
	ile = int(slowka[4])
	
	for i in range (len(slowka)-5):
		slowka[i] = slowka[len(slowka)-i-1]
	for i in range (5):
		slowka.pop()
	return slowka

def reset():
	global count,tabela,do_resetu,poprawne,czy_koniec,index
	poprawne=[]
	count = [0 for i in range (len(tabela))]
	tabela=[]
	for i in do_resetu:
		tabela.append(i)
	
	czy_koniec=len(tabela)
	index=random.randint(0,dlugosc-1)
	button1.grid_remove()
	label4.config(text="")
	label3.config(text=tabela[index][1])
	inpt.config(state='enabled')
	
tabela=[]	
do_resetu=[]

ile=0 #wartosc mowiaca o tym ile razy program pyta o slowo. ustawiana w czytanie()
"""
for i in czytanie():
	tabela.append(i.split("#"))
"""
tabela = [i.split("#") for i in czytanie()]

for i in tabela:
	do_resetu.append(i)
	
count = [0 for i in range (len(tabela))]
poprawne=[]
program=1
czy_koniec=len(tabela)
dlugosc = len(tabela)

index=random.randint(0,dlugosc-1)

def wez(event):
	global guess,index,tabela,dlugosc,count,reset,poprawne,czy_koniec
	if index in poprawne:
		pass

	else:
		#jesli to slowo zostalo podane poprawnie var ile razy to zamienia sie na "". I jesli jest "" to program idzie do nastepneo
		if tabela[index]=="":
			pass
		
		else:
		
			guess = inpt.get()
			inpt.delete(0,len(str(guess)))
			
			if guess==tabela[index][0] and count[index]!=ile:
				label4.config(text="Correct")
				count[index]+=1
			
				if count[index] == ile:
					tabela[index]=""
					czy_koniec-=1
					poprawne.append(index)
			else:
				label4.config(text=f"False. Correct = {tabela[index][0]}")
				count[index]=0
			
		while True:
			index=random.randint(0,dlugosc-1)
			
			if index in poprawne and czy_koniec==0:
				inpt.config(state='disabled')
				button1.grid(row=3,sticky=E)
				break
				
			elif index in poprawne:
				pass
				
			else:
				label3.config(text=tabela[index][1])
				break

LARGE_FONT= ("Verdana", 8)
LARGER_FONT= ("Verdana", 10)

root = Tk()

myvar = StringVar(root)

label1 = ttk.Label(root, text="English:", font=LARGE_FONT)
label2 = ttk.Label(root, text="Polish:", font=LARGE_FONT)
label3 = ttk.Label(root, text=tabela[index][1],font=LARGER_FONT,borderwidth=2,relief="sunken",takefocus=True)
label4 = ttk.Label(root, text="", font=LARGE_FONT)
button1 = ttk.Button(root,text="Again?",command=reset)
				
label1.grid(padx=35,pady=4,row=0, column=0)
label2.grid(padx=35,pady=4,row=0, column=1)
label3.grid(padx=10,pady=5,row=1, column=0,sticky=W)
label4.grid(padx=10,pady=5,row=2, column=1)
label4.grid(padx=10,pady=5,row=2, column=1)
root.grid_columnconfigure(0, minsize=40)
button1.grid(row=3,sticky=E)
button1.grid_remove()
inpt = ttk.Entry(root,font=LARGER_FONT)

inpt.bind('<Return>',wez)
inpt.grid(padx=5,pady=6,row=1,column=1)

root.title("Slowka v1.0")
root.mainloop()