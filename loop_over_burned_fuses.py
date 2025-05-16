import numpy as np
import capacitor_bank_protection_internal_fused as cbpif
import capacitor_bank_protection_external_fused as cbpefyy
import capacitor_bank_protection_internal_fused_bridge_h as cbpifh


def various_burned_fused_internal(bank_parameters, dicionario):
    bank_current_work = bank_parameters['bank_current_work']

    voltage_bank_rated = dicionario['voltage_bank_rated']
    voltage_bank_work = dicionario['voltage_bank_work']
    S = dicionario['S']
    Pt = dicionario['Pt']
    Pa = dicionario['Pa']
    P = dicionario['P']
    G = dicionario['G']
    N = dicionario['N']
    Su = dicionario['Su']

    casas_decimais = 4
    fear_factor = voltage_bank_rated / voltage_bank_work
    data_ieeec3799 = []
    f_values = np.arange(0, N, 1)

    for f in f_values:
        bank = cbpif.CapacitorBank_InternalFused(S=S, Pt=Pt, Pa=Pa, P=P, G=G, N=N, Su=Su, f=f)
        row = {
            'f': f,
            'Ci [pu]': round(bank.Ci, casas_decimais),
            'Cu [pu]': round(bank.Cu, casas_decimais),
            'Cg [pu]': round(bank.Cg, casas_decimais),
            'Cs [pu]': round(bank.Cs, casas_decimais),
            'Cp [pu]': round(bank.Cp, casas_decimais),
            'Vng [pu]': round(bank.Vng, casas_decimais),
            'Vln [pu]': round(bank.Vln, casas_decimais),
            'Vcu [pu]': round(bank.Vcu, casas_decimais),
            'Vcu [pu_work]': round(bank.Vcu / fear_factor, casas_decimais),
            'Vg [pu]': round(bank.Vg, casas_decimais),
            'Ve [pu]': round(bank.Ve, casas_decimais),
            'Iu [pu]': round(bank.Iu, casas_decimais),
            'Ist [pu]': round(bank.Ist, casas_decimais),
            'Iph [pu]': round(bank.Iph, casas_decimais),
            'Ig [pu]': round(bank.Ig, casas_decimais),
            'In [pu]': round(bank.In, casas_decimais),
            'In [A]': round(bank_current_work * bank.In, casas_decimais),
            'Vng [V]': round(voltage_bank_work / np.sqrt(3) * bank.Vng, casas_decimais)
        }
        data_ieeec3799.append(row)

    return data_ieeec3799

##########################################################################################################

def calculate_bank_parameters(dicionario):
    power_bank_rated = dicionario["power_bank_rated"]
    voltage_bank_rated = dicionario["voltage_bank_rated"]
    power_bank_work = dicionario["power_bank_work"]
    voltage_bank_work = dicionario["voltage_bank_work"]
    f1 = dicionario["f1"]

    angular_frequency = 2 * np.pi * f1

    bank_current_rated = power_bank_rated / (np.sqrt(3) * voltage_bank_rated)
    bank_reactance_rated = voltage_bank_rated ** 2 / power_bank_rated
    bank_capacitance_rated = 1 / (angular_frequency * bank_reactance_rated)

    bank_current_work = power_bank_work / (np.sqrt(3) * voltage_bank_work)
    bank_reactance_work = voltage_bank_work ** 2 / power_bank_work
    bank_capacitance_work = 1 / (angular_frequency * bank_reactance_work)

    bank_parameters = {
        "bank_current_rated": bank_current_rated,
        "bank_reactance_rated": bank_reactance_rated,
        "bank_capacitance_rated": bank_capacitance_rated,
        "bank_current_work": bank_current_work,
        "bank_reactance_work": bank_reactance_work,
        "bank_capacitance_work": bank_capacitance_work
    }

    return bank_parameters


# External Fused Double Y
def various_burned_fused_external(bank_parameters, dicionario):
    bank_current_work = bank_parameters['bank_current_work']
    voltage_bank_rated = dicionario['voltage_bank_rated']
    voltage_bank_work = dicionario['voltage_bank_work']
    S = dicionario['S']
    Pt = dicionario['Pt']
    Pa = dicionario['Pa']
    G = dicionario['G']

    casas_decimais = 4
    fear_factor = voltage_bank_rated / voltage_bank_work
    data_ieeec3799 = []
    n_values = np.arange(0, Pa, 1)

    for n in n_values:
        bank = cbpefyy.CapacitorBank_ExternalFusedDoubleY(S=S, n=n, Pt=Pt, Pa=Pa, G=G)
        row = {
            'n': n,
            'Cg [pu]': round(bank.Cg, casas_decimais),
            'Cs [pu]': round(bank.Cs, casas_decimais),
            'Cp [pu]': round(bank.Cp, casas_decimais),
            'Vng [pu]': round(bank.Vng, casas_decimais),
            'Vln [pu]': round(bank.Vln, casas_decimais),
            'Vcu [pu]': round(bank.Vcu, casas_decimais),
            'Vcu [pu_work]': round(bank.Vcu / fear_factor, casas_decimais),
            'Iu [pu]': round(bank.Iu, casas_decimais),
            'Iy [pu]': round(bank.Iy, casas_decimais),
            'Iph [pu]': round(bank.Iph, casas_decimais),
            'Ig [pu]': round(bank.Ig, casas_decimais),
            'In [pu]': round(bank.In, casas_decimais),
            'In [A]': round(bank_current_work * bank.In, casas_decimais),
            'Vng [V]': round(bank_current_work / np.sqrt(3) * bank.Vng, casas_decimais)
        }
        data_ieeec3799.append(row)

    return data_ieeec3799



# various_burned_fused_external_single_Y
def various_burned_fused_external_single_Y(base_voltage,
                                  base_current,
                                  voltage_bank_work,
                                  S=4, n=2, Pt=8, G=1):
    casas_decimais = 4
    fear_factor = base_voltage / voltage_bank_work
    data_ieeec3799 = []
    n_values = np.arange(0, n, 1)

    for n in n_values:
        bank = cbpefyy.CapacitorBank_ExternalFusedSingleY(S=S, n=n, Pt=Pt, G=G)
        row = {
            'n': n,
            'Cg [pu]': round(bank.Cg, casas_decimais),
            'Cp [pu]': round(bank.Cp, casas_decimais),
            'Vng [pu]': round(bank.Vng, casas_decimais),
            'Vln [pu]': round(bank.Vln, casas_decimais),
            'Vcu [pu]': round(bank.Vcu, casas_decimais),
            'Vcu [pu_work]': round(bank.Vcu / fear_factor, casas_decimais),
            'Iu [pu]': round(bank.Iu, casas_decimais),
            'Iph [pu]': round(bank.Iph, casas_decimais),
            'Ig [pu]': round(bank.Ig, casas_decimais),
            'Ig [A]': round(base_current * bank.Ig, casas_decimais),
            'Vng [V]': round(base_voltage / np.sqrt(3) * bank.Vng, casas_decimais)
        }
        data_ieeec3799.append(row)

        data_units_and_elements = [
            {'series group line to neutral - S': S},
            {'total parallels units per phase - Pt': Pt},
            {'(0=grounded, 1=ungrounded) - G': G},
        ]

    return data_ieeec3799, data_units_and_elements

##########################################################################################################

def various_burned_fused_internal_bridge_h(base_voltage, base_current, voltage_bank_work,
                                           S=7, St=3, Pt=9, Pa=5, P=2, G=0, N=16, Su=3):
    casas_decimais = 4
    fear_factor = base_voltage / voltage_bank_work
    data_ieeec3799 = []
    data_report = []
    f_values = np.arange(0, N, 1)

    for f in f_values:
        bank = cbpifh.CapacitorBank_InternalFused_Bridge_H(S=S, St=St, Pt=Pt, Pa=Pa, P=P, G=G, N=N, Su=Su, f=f)
        row = {
            'f': f,
            'Cu [pu]':  round(bank.Cu, casas_decimais),
            'Chn [pu]': round(bank.Chn, casas_decimais),
            'Cp [pu]':  round(bank.Cp, casas_decimais),
            'Vng [pu]': round(bank.Vng, casas_decimais),
            'Vng [V]':  round(base_voltage / np.sqrt(3) * bank.Vng, casas_decimais),
            'Vln [pu]': round(bank.Vln, casas_decimais),
            'Vh [pu]':  round(bank.Vh, casas_decimais),
            'Ih [pu]':  round(bank.Ih, casas_decimais),
            'Ih [A]':   round(bank.Ih*base_current, casas_decimais),
            'Vcu [pu]': round(bank.Vcu, casas_decimais),
            'Vcu [pu_work]': round(bank.Vcu / fear_factor, casas_decimais),
            'Ve [pu]': round(bank.Ve, casas_decimais),
            'Iu [pu]': round(bank.Iu, casas_decimais),
        }
        data_ieeec3799.append(row)
        row = {
            ('Elementos Perdidos', 'f'): f,
            
            ('Tensão na Unidade', 'Vcu [pu]'):      round(bank.Vcu, casas_decimais),
            ('Tensão na Unidade', 'Vcu_work [pu]'): round(bank.Vcu / fear_factor, casas_decimais),
            ('Tensão nos elementos', 'Ve [pu]'): round(bank.Ve, casas_decimais),
            ('Tensão de fase', 'Vln [pu]'):   round(bank.Vln, casas_decimais),
            ('Tensão no h', 'Vh [pu]'):       round(bank.Vh, casas_decimais),
            ('Tensão no h', 'Vh [V]'):        round(base_voltage / np.sqrt(3) * bank.Vh, casas_decimais),

            ('Corrente no h','Ih [pu]'): round(bank.Ih, casas_decimais),
            ('Corrente no h','Ih [A]'):  round(base_current * bank.Ih, casas_decimais),
            
            'Iu [pu]': round(bank.Iu, casas_decimais),
        }

        data_report.append(row)

        data_units_and_elements = [
            {'series group line to neutral - S': S},
            {'series groups, H leg to neutral - St': St},
            {'parallels units per phase - Pt': Pt},
            {'parallels units on left side of H - Pa': Pa},
            {'parallels units in affected string - P': P},
            {'(0=grounded, 1=ungrounded) - G': G},
            {'parallels elements inside a unit - N': N},
            {'series elements inside a unit - Su': Su}
        ]

    return data_report, data_ieeec3799, data_units_and_elements