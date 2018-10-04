from tkinter import *



janela= Tk();
L = "1200"
A = "800"
E = "100"
T = "100"
tamanho = str(L + "x" + A + "+" + E + "+" + T)
janela.geometry(tamanho)
janela.title("Calculo Financeiro")
janela["bg"] = "green"
corJanela = janela["bg"]

Label(janela,
      text="Calculos financeiros",
      bg=corJanela,
      font="Arial 12").place(500, 10)

Label(janela,
      bg=corJanela,
      text="Valor inicial: ").place(100, 50)

edtValorInicial = Entry(janela,
                        width=20); edtValorInicial.place(150, 50)

Button(janela,
       bg="blue",
       text="Calcular",
       command=lambda: calcular(0)).place(200, 50)

Label(janela,
      bg=corJanela,
      text="Tempo de aplicação: ").place(100, 80)

edtTempo = Entry(janela, 
                 width=20); edtTempo.place(150, 80)
Button(janela,
       bg="blue",
       text="Calcular",
       command=lambda: calcular(1)).place(200, 80)

Label(janela,
      bg=corJanela,
      text="Valor final: ").place(100, 110)

edtValorFinal = Entry(janela,
                      width = 20); edtValorFinal.place(150, 110)

Button(janela,
       bg="blue",
       text="Calcular",
       command=lambda: calcular(2)).place(200, 110)

Label(janela,
      bg=corJanela,
      text="% de juros: ").place(100, 140)

edtPercentJuros = Entry(janela,
                        bg=corJanela); edtPercentJuros.place(150,140)
Button(janela,
       bg="blue",
       text="Calcular",
       command=lambda: calcular(3)).place(200, 140)






