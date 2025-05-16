import pandas as pd
import numpy as np
from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill


class CapacitorBank_ExternalFusedDoubleY:
    def __init__(self, S=4, n=2, Pt=14, Pa=8, G=1):

        self.S = S
        self.n = n
        self.Pt = Pt
        self.Pa = Pa
        self.G = G

        # Cálculos de capacitância
        self.Cg = self.__calculate_Cg()
        self.Cs = self.__calculate_Cs()
        self.Cp = self.__calculate_Cp()

        # Cálculos de tensão
        self.Vng = self.__calculate_Vng()
        self.Vln = self.__calculate_Vln()
        self.Vcu = self.__calculate_Vcu()

        # Cálculos de corrente
        self.Iu = self.__calculate_Iu()
        self.Iy = self.__calculate_Iy()
        self.Iph = self.__calculate_Iph()
        self.Ig = self.__calculate_Ig()
        self.In = self.__calculate_In()

    def __calculate_Cg(self):
        Cg = (self.Pa - self.n) / self.Pa
        return Cg

    def __calculate_Cs(self):
        num = self.S * self.Cg
        den = self.Cg * (self.S - 1) + 1
        Cs = num / den
        return Cs

    def __calculate_Cp(self):
        num = (self.Cs * self.Pa) + (self.Pt - self.Pa)
        Cp = num / self.Pt
        return Cp

    def __calculate_Vng(self):
        Vng = self.G * (3 / (2 + self.Cp) - 1)
        return Vng

    def __calculate_Vln(self):
        Vln = 1 + self.Vng
        return Vln

    def __calculate_Vcu(self):
        if self.Cg != 0:
            Vcu = (self.Vln * self.Cs) / self.Cg
        else:
            Vcu = self.Vln * self.S
        return Vcu

    def __calculate_Iu(self):
        Iu = self.Vcu * 1.0
        return Iu

    def __calculate_Iy(self):
        Iy = self.Vln * self.Cs
        return Iy

    def __calculate_Iph(self):
        Iph = self.Vln * self.Cp
        return Iph

    def __calculate_Ig(self):
        Ig = (1 - self.G) * (1 - self.Iph)
        return Ig

    def __calculate_In(self):
        In = 3 * self.Vng * self.G * (self.Pt - self.Pa) / self.Pt
        return In

class CapacitorBank_ExternalFusedSingleY:
    def __init__(self, S=4, n=2, Pt=8, G=1):

        self.S = S
        self.n = n
        self.Pt = Pt
        self.G = G

        # Cálculos de capacitância
        self.Cg = self.__calculate_Cg()
        self.Cp = self.__calculate_Cp()

        # Cálculos de tensão
        self.Vng = self.__calculate_Vng()
        self.Vln = self.__calculate_Vln()
        self.Vcu = self.__calculate_Vcu()

        # Cálculos de corrente
        self.Iu = self.__calculate_Iu()
        self.Iph = self.__calculate_Iph()
        self.Ig = self.__calculate_Ig()

    def __calculate_Cg(self):
        Cg = (self.Pt - self.n) / self.Pt
        return Cg

    def __calculate_Cp(self):
        num = self.S * self.Cg
        den = self.Cg * (self.S-1) + 1
        Cp = num / den
        return Cp

    def __calculate_Vng(self):
        Vng = self.G * (3 / (2 + self.Cp) - 1)
        return Vng

    def __calculate_Vln(self):
        Vln = 1 + self.Vng
        return Vln

    def __calculate_Vcu(self):
        Vcu = (self.Vln * self.Cp) / self.Cp
        return Vcu

    def __calculate_Iu(self):
        Iu = self.Vcu * 1
        return Iu

    def __calculate_Iph(self):
        Iph = self.Vln * self.Cp
        return Iph

    def __calculate_Ig(self):
        Ig = (1 - self.G) * (1 - self.Iph)
        return Ig

