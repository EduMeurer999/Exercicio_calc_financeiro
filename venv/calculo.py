from math import *

class calculo():
    def __init__(self, vInicial, tempo, vFinal, pJuros):
        self.tempo = tempo
        self.vFinal = vFinal
        self.pJuros = pJuros
        self.vInicial = vInicial

    def calculaTempo(self, isComposto, isAA):
        if(isComposto == 1):
            
            if(self.tempo == None and self.pJuros != None and self.vInicial != None and self.vFinal != None):
                if(isAA):
                    self.tempo = log10(self.vFinal/self.vInicial)/log10((self.pJuros/100)+1)
                    arrReturn = self.tempo/360
                else:
                    self.tempo = log10(self.vFinal / self.vInicial) / log10(1 + (self.pJuros / 100))
                    arrReturn = self.tempo
            else:
                return "Somente o campo 'Tempo de aplicação' pode ficar em branco'"

        else:
            if (self.tempo == None and self.pJuros != None and self.vInicial != None and self.vFinal != None):
                self.tempo = (self.vFinal-self.vInicial)/(self.vInicial*(self.pJuros/100))
                arrReturn = self.tempo

        return arrReturn

    def calculaMontante(self, isComposto):
        if (self.tempo != None and self.pJuros != None and self.vInicial != None and self.vFinal == None):
            if (isComposto == 1):
                self.vFinal = self.vInicial*(1+self.pJuros)**self.tempo
                arrReturn = self.vFinal
            else:
                self.vFinal = self.vInicial + (1+(self.pJuros*self.tempo))
                arrReturn = self.vFinal
        else:
            return "Somente o campo 'Montante' pode ficar em branco'"

    def calculaValInicial(self, isComposto):
        if (self.tempo != None and self.pJuros != None and self.vInicial == None and self.vFinal != None):
            if(isComposto == 1):
                self.vInicial = self.vFinal/(1+self.pJuros)**self.tempo
                arrReturn = self.vInicial
            else:
                self.vInicial = self.vFinal - (1+(self.pJuros*self.tempo))
                arrReturn = self.vInicial
            return arrReturn
        else:
            return "Somente o campo 'Valor inicial' pode ficar em branco'"

    def calculapJuros(self, isComposto):
        if (self.tempo != None and self.pJuros == None and self.vInicial != None and self.vFinal != None):
            if(isComposto == 1):
                self.pJuros = self.tempo//(self.vFinal/self.vInicial)-1

                return self.pJuros
            else:
                self.pJuros = (self.vFinal-self.vInicial-1)/self.tempo
                return self.pJuros
        else:
            return "Somente o campo 'Taxa de juros' pode ficar em branco"






