from tkinter import *
from calculo import *


def calcular(opt, entry):

    if (opt == 0):
        valorInicial = None
        valorFinal = float(edtValorFinal.get())
        taxaJuros = float(edtPercentJuros.get())
        tempoApli = float(edtTempo.get())
        if (varTipo.get() == 1):
            tempoApli = (tempoApli / 360) / 100
        else:
            tempoApli = (tempoApli / 12) / 100
        cCapital = calculo.calculo(valorInicial, tempoApli, valorFinal, taxaJuros)
        entry["text"] = cCapital.calculaValInicial(var.get())
        entry.place(x=200, y=50)

    elif (opt == 1):
        valorInicial = float(edtValorInicial.get())
        valorFinal = float(edtValorFinal.get())
        taxaJuros = float(edtPercentJuros.get())
        tempoApli = None
        cTempo = calculo(valorInicial, tempoApli, valorFinal, taxaJuros)

        if (varTipo.get() == 1):
            entry["text"] = cTempo.calculaTempo(var.get(), varTipo.get())
            entry.place(x=200, y=80)
        else:
            entry["text"] = cTempo.calculaTempo(var.get(), varTipo.get())
            entry.place(x=200, y=80)

    elif (opt == 2):
        valorInicial = float(edtValorInicial.get())
        valorFinal = None
        taxaJuros = float(edtPercentJuros.get())
        tempoApli = float(edtTempo.get())
        if (varTipo.get() == 1):
            tempoApli = (tempoApli / 360) / 100
        else:
            tempoApli = (tempoApli / 12) / 100
        cMontante = calculo.calculo(valorInicial, tempoApli, valorFinal, taxaJuros)
        entry["text"] = cMontante.calculaMontante(var.get())
        entry.place(x=200, y=110)

    elif (opt == 3):
        valorInicial = float(edtValorInicial.get())
        valorFinal = float(edtValorFinal.get())
        taxaJuros = None
        tempoApli = float(edtTempo.get())

        if (varTipo.get() == 1):
            tempoApli = tempoApli/360
        else:
            tempoApli = tempoApli / 12

        cTaxa = calculo(valorInicial, tempoApli, valorFinal, taxaJuros)
        entry["text"] = cTaxa.calculapJuros(var)
        entry.place(x=200, y=140)
        # s["text"] = "valor: "+str(cTaxa.calculapJuros(var))
        # s.place(x=500, y= 200)

    else:
        s["text"] = "A opção selecionada é inválida"
        s.place(x=200, y=170)


janela = Tk();
L = "1200"
A = "800"
E = "100"
T = "100"
tamanho = str(L + "x" + A + "+" + E + "+" + T)
janela.geometry(tamanho)
janela.title("Calculo Financeiro")
janela["bg"] = "green"
corJanela = janela["bg"]

var = IntVar()
varTipo = IntVar()
R1 = Radiobutton(janela, bg=corJanela, text="Juros Composto", variable=var, value=1)
R2 = Radiobutton(janela, bg=corJanela, text="Juros Simples", variable=var, value=2)

R1.place(x=100, y=170)
R2.place(x=100, y=200)

Label(janela, bg=corJanela, text="Tipo de taxa: ").place(x=300, y=170)
R1 = Radiobutton(janela, bg=corJanela, text="a.a", variable=varTipo, value=1)
R2 = Radiobutton(janela, bg=corJanela, text="a.m", variable=varTipo, value=2)

R1.place(x=300, y=200)
R2.place(x=300, y=230)

Label(janela,
      text="Calculos financeiros",
      bg=corJanela,
      font="Arial 12").place(x=500, y=10)

Label(janela,
      bg=corJanela,
      text="Valor inicial: ").place(x=80, y=50)

edtValorInicial = Entry(janela,
                        width=20);
edtValorInicial.place(x=200, y=50)

Button(janela,
       bg="blue",
       text="Calcular",
       command=lambda: calcular(0, edtValorInicial)).place(x=350, y=50)

Label(janela,
      bg=corJanela,
      text="Tempo de aplicação: ").place(x=80, y=80)

edtTempo = Entry(janela,
                 width=20);
edtTempo.place(x=200, y=80)
Button(janela,
       bg="blue",
       text="Calcular",
       command=lambda: calcular(1, edtTempo)).place(x=350, y=80)

Label(janela,
      bg=corJanela,
      text="Valor final: ").place(x=80, y=110)

edtValorFinal = Entry(janela,
                      width=20);
edtValorFinal.place(x=200, y=110)

Button(janela,
       bg="blue",
       text="Calcular",
       command=lambda: calcular(2, edtValorFinal)).place(x=350, y=110)

Label(janela,
      bg=corJanela,
      text="% de juros: ").place(x=80, y=140)

edtPercentJuros = Entry(janela,
                        width=20);
edtPercentJuros.place(x=200, y=140)
Button(janela,
       bg="blue",
       text="Calcular",
       command=lambda: calcular(3, edtPercentJuros)).place(x=350, y=140)

s = Label(janela, bg=corJanela)

janela.mainloop()
