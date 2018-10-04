from math import *

class calculo():
    def __init__(self, vInicial, tempo, vFinal, pJuros):
        self.tempo = tempo;
        self.vFinal = vFinal;
        self.pJuros = pJuros;
        self.vInicial = vInicial;

    def setTempo(self, tempo):
        self.tempo = tempo
    def getTempo(self):
        return self.tempo

    def setvFinal(self, vFinal):
        self.vFinal = vFinal
    def getFinal(self):
        return self.vFinal


    def setvInicial(self, vInicial):
        self.vInicial = vInicial
    def getvInicial(self):
        return self.vInicial

    def setpJuros(self, pJuros):
        self.pJuros = pJuros
    def getpJuros(self):
        return self.pJuros

    def calculaTempo(self, isComposto):
        if(isComposto):
            if(self.tempo == None and self.pJuros != None and self.vInicial != None and self.vFinal != None):
                self.tempo = log1p(self.vFinal/self.vInicial)/log1p(1+ (self.pJuros/100))
                arrReturn = {"a.a": self.tempo/360,
                             "a.m": self.tempo/12}
            else:
                return "Somente o campo 'Tempo de aplicação' pode ficar em branco'"

        else:
            if (self.tempo == None and self.pJuros != None and self.vInicial != None and self.vFinal != None):
                self.tempo = self.vFinal-self.vInicial/(self.vInicial*self.pJuros)
                arrReturn = {"a.a": self.tempo/360,
                             "a.m": self.tempo/12}

        return arrReturn

    def calculaMontante(self, isComposto):
        if (isComposto):
            if (self.tempo != None and self.pJuros == None and self.vInicial != None and self.vFinal == None):
                self.tempo = log1p(self.vFinal / self.vInicial) / log1p(1 + (self.pJuros / 100))
                arrReturn = {"a.a": self.tempo / 360,
                             "a.m": self.tempo / 12}
            else:
                return "Somente o campo 'Tempo de aplicação' pode ficar em branco'"

        else:
            if (self.tempo == None and self.pJuros != None and self.vInicial != None and self.vFinal == None):
                self.tempo = self.vFinal - self.vInicial / (self.vInicial * self.pJuros)
                arrReturn = {"a.a": self.tempo / 360,
                             "a.m": self.tempo / 12}

        return arrReturn

    def calculaValInicial(self, isComposto):
        if(isComposto):
            self.vInicial = self.v




