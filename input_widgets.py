import streamlit as st
import pandas as pd


def get_capacitor_bank_inputs_for_internal_fused(selected_option):
    col1, col2, col3 = st.columns(3)

    # Coluna 1
    with col1:
        S = st.number_input(
            label="Unidades Série - S:",
            min_value=1,
            max_value=100,
            value=3,
            step=1,
            format="%d"
        )
        Pt = st.number_input(
            label="Unidades Paralelas - Pt:",
            min_value=1,
            max_value=100,
            value=2,
            step=1,
            format="%d"
        )
        Pa = st.number_input(
            label="Un. Paralelas da Fase Afetada - Pa:",
            min_value=1,
            max_value=100,
            value=1
        )
        P = st.number_input(
            label="Un. Paralelas na String Afetada - P:",
            min_value=1,
            max_value=100,
            value=1
        )

    with col2:
        G = st.number_input(
            label="Aterrado (0) Isolado (1) - G:",
            min_value=0,
            max_value=1,
            value=1
        )
        N = st.number_input(
            label="Paralelos dentro da Unidade - N:",
            min_value=1,
            max_value=100,
            value=9
        )
        Su = st.number_input(
            label="Elementos em Série - Su:",
            min_value=1,
            max_value=100,
            value=6
        )
        f1 = st.number_input(
            label="Frequência Fundamental - Hz:",
            min_value=40,
            max_value=70,
            value=60
        )

    with col3:
        voltage_bank_work = 1e3 * st.number_input(
            label="kV de Trabalho do Banco:",
            min_value=1.0,
            max_value=1000.0,
            value=34.5
        )
        power_bank_work = 1e6 * st.number_input(
            label="MVAr de Trabalho do Banco:",
            min_value=0.1,
            max_value=100.0,
            value=10.0
        )

        voltage_bank_rated = 1e3 * st.number_input(
            label="kV Nominal do Banco:",
            min_value=1.0,
            max_value=1000.0,
            value=1.3e-3*voltage_bank_work
        )
        power_bank_rated = 1e6 * st.number_input(
            label="MVAr Nominal do Banco:",
            min_value=0.1,
            max_value=100.0,
            value=1e-6*power_bank_work*((voltage_bank_rated/voltage_bank_work)**2),
            disabled=True
        )

    dicionario = {"f1": f1,
                  "power_bank_rated": power_bank_rated,
                  "voltage_bank_rated": voltage_bank_rated,
                  "power_bank_work": power_bank_work,
                  "voltage_bank_work": voltage_bank_work,
                  "S": S,
                  "Pt": Pt,
                  "Pa": Pa,
                  "P": P,
                  "G": G,
                  "N": N,
                  "Su": Su}

    return dicionario


def get_capacitor_bank_inputs_for_external_fused_double_y(selected_option):
    # Criar cinco colunas
    col1, col2, col3 = st.columns(3)

    # Coluna 1
    with col1:
        S = st.number_input(
            label="Quantidade Série de Unidades - S:",
            min_value=3,
            max_value=100,
            value=4
        )

        Pt = st.number_input(
            label="Total de Unidades Paralelas - Pt:",
            min_value=1,
            max_value=100,
            value=32
        )

        Pa = st.number_input(
            label="Unidades Paralelas da Fase Afetada - Pa:",
            min_value=1,
            max_value=100,
            value=16
        )

        G = st.number_input(
            label="Aterrado (0) Isolado (1) - G:",
            min_value=0,
            max_value=1,
            value=1
        )

    with col2:
        f1 = st.number_input(
            label="Frequência Fundamental - Hz:",
            min_value=40,
            max_value=70,
            value=60
        )

        with col3:
            voltage_bank_work = 1e3 * st.number_input(
                label="kV de Trabalho do Banco:",
                min_value=1.0,
                max_value=1000.0,
                value=34.5
            )
            power_bank_work = 1e6 * st.number_input(
                label="MVAr de Trabalho do Banco:",
                min_value=0.1,
                max_value=100.0,
                value=10.0
            )

            voltage_bank_rated = 1e3 * st.number_input(
                label="kV Nominal do Banco:",
                min_value=1.0,
                max_value=1000.0,
                value=1.3e-3 * voltage_bank_work
            )
            power_bank_rated = 1e6 * st.number_input(
                label="MVAr Nominal do Banco:",
                min_value=0.1,
                max_value=100.0,
                value=1e-6 * power_bank_work * ((voltage_bank_rated / voltage_bank_work) ** 2),
                disabled=True
            )

    dicionario = {"f1": f1,
                  "power_bank_rated": power_bank_rated,
                  "voltage_bank_rated": voltage_bank_rated,
                  "power_bank_work": power_bank_work,
                  "voltage_bank_work": voltage_bank_work,
                  "S": S,
                  "Pt": Pt,
                  "Pa": Pa,
                  "G": G
                  }


    return dicionario


def get_capacitor_bank_inputs_for_external_fused_single_y():
    # Criar cinco colunas
    col1, col2, col3, col4, col5 = st.columns(5)
    # Coluna 1
    with col1:
        S = st.number_input(
            label="Quantidade Série de Unidades - S:",
            min_value=3,
            max_value=100,
            value=4
        )
        Pt = st.number_input(
            label="Total de Unidades Paralelas - Pt:",
            min_value=1,
            max_value=100,
            value=8
        )

    # Coluna 2
    with col2:
        st.write("Pa = Pt")
    # Coluna 3
    with col3:
        G = st.number_input(
            label="Aterrado (0) Isolado (1) - G:",
            min_value=0,
            max_value=1,
            value=1
        )

    # Coluna 4
    with col4:
        f1 = st.number_input(
            label="Frequência Fundamental - Hz:",
            min_value=40,
            max_value=70,
            value=60
        )

    # Coluna 5
    with col5:
        power_bank_rated = 1e6 * st.number_input(
            label="Potência Nominal do Banco - MVAr:",
            min_value=0.1,
            max_value=100.0,
            value=10.0
        )
        voltage_bank_rated = 1e3 * st.number_input(
            label="Tensão Nominal do Banco - kV:",
            min_value=1.0,
            max_value=1000.0,
            value=54.8
        )
        voltage_bank_work = 1e3 * st.number_input(
            label="Tensão de Trabalho do Banco - kV:",
            min_value=1.0,
            max_value=1000.0,
            value=34.5
        )
    # f1 = 60
    # power_bank_rated = 10e6
    # voltage_bank_rated = 34.5e3
    # voltage_bank_work = 1.3*voltage_bank_rated
    # S = 4
    # Pt = 64
    # G = 1

    return {
        "f1": f1,
        "power_bank_rated": power_bank_rated,
        "voltage_bank_rated": voltage_bank_rated,
        "voltage_bank_work": voltage_bank_work,
        "S": S,
        "n": Pt,
        "Pt": Pt,
        "G": G,
    }


def get_capacitor_bank_inputs_for_internal_fused_bridge_h():
    # Criar cinco colunas
    col1, col2, col3, col4, col5 = st.columns(5)
    # Coluna 1
    with col1:
        S = st.number_input(
            label="Quantidade Série de Unidades - S:",
            min_value=1,
            max_value=100,
            value=7
        )
        St = st.number_input(
            label="Quantidade Série H-neutro - St:",
            min_value=1,
            max_value=100,
            value=3
        )


    # Coluna 2
    with col2:
        Pt = st.number_input(
            label="Unidades Paralelas - Pt:",
            min_value=1,
            max_value=100,
            value=9
        )
        Pa = st.number_input(
            label="Paralelas do lado esquerdo - Pa:",
            min_value=1,
            max_value=100,
            value=5
        )
        P = st.number_input(
            label="Unidades paralelas na string afetada - P:",
            min_value=1,
            max_value=100,
            value=2
        )        
    # Coluna 3
    with col3:
        N = st.number_input(
            label="Elementos paralelos na célula - N:",
            min_value=1,
            max_value=100,
            value=16
        )
        Su = st.number_input(
            label="Elementos série na célula - Su:",
            min_value=1,
            max_value=100,
            value=3
        )        
        G = st.number_input(
            label="Aterrado (0) Isolado (1) - G:",
            min_value=0,
            max_value=1,
            value=1
        )

    # Coluna 4
    with col4:
        f1 = st.number_input(
            label="Frequência Fundamental - Hz:",
            min_value=40,
            max_value=70,
            value=60
        )

    # Coluna 5
    with col5:
        power_bank_rated = 1e6 * st.number_input(
            label="Potência Nominal do Banco - MVAr:",
            min_value=0.1,
            max_value=100.0,
            value=10.0
        )
        voltage_bank_rated = 1e3 * st.number_input(
            label="Tensão Nominal do Banco - kV:",
            min_value=1.0,
            max_value=1000.0,
            value=54.8
        )
        voltage_bank_work = 1e3 * st.number_input(
            label="Tensão de Trabalho do Banco - kV:",
            min_value=1.0,
            max_value=1000.0,
            value=34.5
        )
    # f1 = 60
    # power_bank_rated = 10e6
    # voltage_bank_rated = 34.5e3
    # voltage_bank_work = 1.3*voltage_bank_rated
    # S = 4
    # Pt = 64
    # G = 1

    return {
        "f1": f1,
        "power_bank_rated": power_bank_rated,
        "voltage_bank_rated": voltage_bank_rated,
        "voltage_bank_work": voltage_bank_work,
        "S": S,
        "Pt": Pt,
        "Pa": Pa,
        "P": P,
        "G": G,
        "N": N,
        "Su": Su,                
    }
