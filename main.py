from tkinter import *

root=Tk()
root.geometry('200x200')
root.title('Calculadora')
root.config(bg='black')
root.iconbitmap('img/icono.ico')
root.resizable(0, 0)
miframe=Frame(root, bg='black')
miframe.pack()

#---------pantalla
varpantalla=StringVar()
#varpantalla.set('0')
pantalla=Entry(miframe, bg='black', fg='white', textvariable=varpantalla, justify='center')
pantalla.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

# 1era fila de botones

#logica
resultado=''
def mostrar_num(n):
	varpantalla.set(pantalla.get()+str(n))

def CE():
	varpantalla.set(' ')
#operaciones
def mostrar_resul():
	global resultado
	try:
		resultado=eval(pantalla.get())
		varpantalla.set(resultado)
	except ZeroDivisionError:
		varpantalla.set('no se puede divir entre cero')  



boton_parenetesis_1=Button(miframe, text='(', width=3, command=lambda:mostrar_num('('), bg='black', fg='white')
boton_parenetesis_1.grid(row=1, column=0)

boton_parenetesis_2=Button(miframe, text=')', width=3, command=lambda:mostrar_num(')'), bg='black',fg='white')
boton_parenetesis_2.grid(row=1, column=1)

boton_divicion=Button(miframe, text='÷', width=3, command=lambda:mostrar_num('/'), bg='black',fg='white')
boton_divicion.grid(row=1, column=3)

boton_limpiar=Button(miframe, text='CE', width=3, command=lambda:CE(), bg='black',fg='white')
boton_limpiar.grid(row=1, column=2)



boton_7=Button(miframe, text='7', width=3, command=lambda:mostrar_num('7'), bg='black', fg='white')
boton_7.grid(row=2, column=0)

boton_8=Button(miframe, text='8', width=3, command=lambda:mostrar_num('8'), bg='black',fg='white')
boton_8.grid(row=2, column=1)

boton_9=Button(miframe, text='9', width=3, command=lambda:mostrar_num('9'), bg='black',fg='white')
boton_9.grid(row=2, column=2)

boton_mult=Button(miframe, text='x', width=3, command=lambda:mostrar_num('*'), bg='black',fg='white')
boton_mult.grid(row=2, column=3)

#2da fila de botones
boton_4=Button(miframe, text='4', width=3, command=lambda:mostrar_num('4'), bg='black',fg='white')
boton_4.grid(row=3, column=0)

boton_5=Button(miframe, text='5', width=3, command=lambda:mostrar_num('5'), bg='black',fg='white')
boton_5.grid(row=3, column=1)

boton_6=Button(miframe, text='6', width=3, command=lambda:mostrar_num('6'), bg='black',fg='white')
boton_6.grid(row=3, column=2)

boton_res=Button(miframe, text='-', width=3, command=lambda:mostrar_num('-'), bg='black',fg='white')
boton_res.grid(row=3, column=3)

#3ra fila de botones
boton_1=Button(miframe, text='1', width=3, command=lambda:mostrar_num('1'), bg='black',fg='white')
boton_1.grid(row=4, column=0)

boton_2=Button(miframe, text='2', width=3, command=lambda:mostrar_num('2'), bg='black',fg='white')
boton_2.grid(row=4, column=1)

boton_3=Button(miframe, text='3', width=3, command=lambda:mostrar_num('3'), bg='black',fg='white')
boton_3.grid(row=4, column=2)

boton_sum=Button(miframe, text='+', width=3,command=lambda:mostrar_num('+'), bg='black',fg='white')
boton_sum.grid(row=4, column=3)

#4ta fila de botones
boton_0=Button(miframe, text='0', width=3, command=lambda:mostrar_num('0'), bg='black',fg='white')
boton_0.grid(row=5, column=0)

boton_coma=Button(miframe, text=',', width=3, command=lambda:mostrar_num(','), bg='black',fg='white')
boton_coma.grid(row=5, column=1)

boton_igual=Button(miframe, text='=', width=8, bg='blue',fg='white', command=mostrar_resul)
boton_igual.grid(row=5, column=2, columnspan=3, padx=3)


root.mainloop()
