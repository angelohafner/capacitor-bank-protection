class CapacitorBank_InternalFused:
    def __init__(self, S=4, Pt=11, Pa=6, P=3, G=0, N=14, Su=3, f=0):

        self.S = S
        self.Pt = Pt
        self.Pa = Pa
        self.P = P
        self.G = G
        self.N = N
        self.Su = Su
        self.f = f

        # Cálculos de capacitância
        self.Ci = self.__calculate_Ci()
        self.Cu = self.__calculate_Cu()
        self.Cg = self.__calculate_Cg()
        self.Cs = self.__calculate_Cs()
        self.Cp = self.__calculate_Cp()

        # Cálculos de tensão (ajustada a ordem)
        self.Vng = self.__calculate_Vng()
        self.Vln = self.__calculate_Vln()
        self.Vcu = self.__calculate_Vcu()
        self.Vg = self.__calculate_Vg()
        self.Ve = self.__calculate_Ve()

        # Cálculos de corrente
        self.Iu = self.__calculate_Iu()
        self.Ist = self.__calculate_Ist()
        self.Iph = self.__calculate_Iph()
        self.Ig = self.__calculate_Ig()
        self.In = self.__calculate_In()
        self.Id = self.__calculate_Id()

    def __calculate_Ci(self):
        Ci = (self.N - self.f) / self.N
        return Ci

    def __calculate_Cu(self):
        num = self.Su * self.Ci
        den = self.Ci * (self.Su - 1) + 1
        Cu = num / den
        return Cu

    def __calculate_Cg(self):
        num = self.P - 1 + self.Cu
        Cg = num / self.P
        return Cg

    def __calculate_Cs(self):
        num = self.S * self.Cg
        den = self.Cg * (self.S - 1) + 1
        Cs = num / den
        return Cs

    def __calculate_Cp(self):
        num = (self.Cs * self.P) + self.Pt - self.P
        Cp = num / self.Pt
        return Cp

    def __calculate_Vng(self):
        Vng = self.G * (3 / (2 + self.Cp) - 1)
        return Vng

    def __calculate_Vln(self):
        Vln = 1 + self.Vng
        return Vln

    def __calculate_Vcu(self):
        num = self.Vln * self.Cs
        Vcu = num / self.Cg
        return Vcu

    def __calculate_Vg(self):
        num = self.Su * self.N
        den = (self.Su-1)*(self.N-self.f) + self.N
        Vg = num / den
        return Vg

    def __calculate_Ve(self):
        Ve = self.Vcu * self.Vg
        return Ve

    def __calculate_Iu(self):
        Iu = self.Vcu * self.Cu
        return Iu

    def __calculate_Ist(self):
        Ist = self.Vln * self.Cs
        return Ist

    def __calculate_Iph(self):
        Iph = self.Vln * self.Cp
        return Iph

    def __calculate_Ig(self):
        Ig = (1 - self.G) * (1 - self.Iph)
        return Ig

    def __calculate_In(self):
        In = 3 * self.Vng * self.G * (self.Pt - self.Pa) / self.Pt
        return In

    def __calculate_Id(self):
        Id = self.Vln * (1 - self.Cp)
        return Id


