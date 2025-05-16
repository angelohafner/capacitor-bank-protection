class CapacitorBank_InternalFused_Bridge_H:
    def __init__(self, S=7, St=3, Pt=9, Pa=5, P=2, G=0, N=16, Su=3, f=0):
        # Dados de entrada
        self.S = S
        self.St = St
        self.Pt = Pt
        self.Pa = Pa
        self.P = P
        self.G = G
        self.N = N
        self.Su = Su
        self.f = f

        # Cálculos de capacitância
        self.Cu  = self.__calculate_Cu()
        self.Chn = self.__calculate_Chn()
        self.Cp  = self.__calculate_Cp()
        # Cp0 = value of Cp when f=0
        # since analytically Cp0 = Pt/S
        self.Cp0 = self.Pt / self.S
        # Cálculos de tensão (ajustada a ordem)
        self.Vng = self.__calculate_Vng()
        self.Vln = self.__calculate_Vln()
        self.Vh  = self.__calculate_Vh()
        self.Vcu = self.__calculate_Vcu()
        self.Ve  = self.__calculate_Ve()

        # Cálculos de corrente
        self.Ih  = self.__calculate_Ih()
        self.Iu = self.__calculate_Iu()

    def __calculate_Cu(self):
        num = self.Su * (self.N - self.f)
        den = (self.N-self.f) * (self.Su-1) + self.N
        Cu = num / den
        return Cu

    def __calculate_Chn(self):
        num1 = (self.Cu+self.P-1)*self.P
        den1 = (self.Cu+self.P-1)*(self.St-1)+self.P
        num2 = self.Pt-self.P
        den2 = self.St
        Chn = num1/den1 + num2/den2
        return Chn
    
    
    def __calculate_Cp(self):
        num = self.Chn * self.Pt
        den = self.Chn * (self.S - self.St) + self.Pt
        Cp = num / den
        return Cp

    def __calculate_Vng(self):
        Vng = self.G * (3 / (2 + self.Cp/self.Cp0) - 1)
        return Vng

    def __calculate_Vln(self):
        Vln = 1 + self.Vng
        return Vln
    
    def __calculate_Vh(self):
        Vh = self.Cp / self.Chn
        return Vh
    
    def __calculate_Ih(self):
        termo_2 = self.St/self.S - self.Vh
        termo_3 = 1/(self.S-self.St) + 1/self.St
        termo_4 = self.S*(self.Pt-self.Pa)/self.Pt
        return -self.Vln*termo_2*termo_3*termo_4

    def __calculate_Vcu(self):
        num = self.Vln * self.Vh * self.P * self.S
        den = self.P + (self.St-1) * (self.Cu+self.P-1)
        Vcu = num / den
        return Vcu

    def __calculate_Ve(self):
        num = self.Vcu * self.Su * self.N
        den = self.Su * (self.N-self.f) + self.f
        Ve = num / den
        return Ve

    def __calculate_Iu(self):
        Iu = self.Vcu * self.Cu
        return Iu





