from exportar_para_latex import exportar_df_colorido_para_latex
import pandas as pd
from data_frame_estilizado import generate_df_stylized
from loop_over_burned_fuses import (various_burned_fused_internal,
                                    calculate_bank_parameters,
                                    various_burned_fused_external,
                                    various_burned_fused_external_single_Y,
                                    various_burned_fused_internal_bridge_h)

###################################################################################
def master_internal_fuses(dicionario):
    # fazer com que o dicionário seja descompactado em variáveis
    # for k, v in dicionario.items():
    #     globals()[k] = v

    bank_parameters = calculate_bank_parameters(dicionario)
    data_internal_fused = various_burned_fused_internal(bank_parameters, dicionario)
    df_data_internal_fused = pd.DataFrame(data_internal_fused)

    ### TABELA DE SAIDA ###
    (df_stylized, 
     idx_mais_proximo_vcu,  
     idx_mais_proximo_vcu_work) = generate_df_stylized(df=df_data_internal_fused,
                                                       Vcu_max=1.1,
                                                       Vcu_max_work=1.1)
    
    df_subset = df_data_internal_fused[['f', 'Ve [pu]', 'Vcu [pu]', 'Vcu [pu_work]', 'Vln [pu]', 'Iu [pu]', 'Vng [pu]', 'Vng [V]', 'In [A]']]
    custom_headers = ['$f$', '$V_e$ [pu]', '$V_{cu}$ [pu]', '$V_{cu}$ [pu work]', '$V_{ln}$ [pu]', '$I_u$ [pu]', '$V_{ng}$ [pu]', '$V_{ng}$ [V]', '$I_n$ [A]']

    df_subset.columns = custom_headers
    exportar_df_colorido_para_latex(df_subset, 
                                    caminho_arquivo = "tex_files/df_subset.tex",
                                    idx_vcu_work = idx_mais_proximo_vcu_work, 
                                    idx_vcu = idx_mais_proximo_vcu)



    return df_stylized, idx_mais_proximo_vcu, idx_mais_proximo_vcu_work

###################################################################################
def master_external_fused_double_y(dicionario):

    bank_parameters = calculate_bank_parameters(dicionario)
    data_external_fused = various_burned_fused_external(bank_parameters, dicionario)
    df_data_external_fused = pd.DataFrame(data_external_fused)

    (df_stylized,
     idx_mais_proximo_vcu,  
     idx_mais_proximo_vcu_work) = generate_df_stylized(df=df_data_external_fused,
                                                       Vcu_max=1.1,
                                                       Vcu_max_work=1.1)

    df_subset = \
        df_data_external_fused[['n', 'Vcu [pu]', 'Vcu [pu_work]', 'Iu [pu]', 'Vng [pu]', 'Vng [V]', 'In [A]']]
    custom_headers = \
        ['$n$', '$V_{cu}$ [pu]', '$V_{cu}$ [pu work]', '$I_u$ [pu]', '$V_{ng}$ [pu]', '$V_{ng}$ [V]', '$I_n$ [A]']
    df_subset.columns = custom_headers

    exportar_df_colorido_para_latex(df_subset,
                                    caminho_arquivo=r"tex_files\df_subset.tex",
                                    idx_vcu_work=idx_mais_proximo_vcu_work,
                                    idx_vcu=idx_mais_proximo_vcu)

    return df_stylized, idx_mais_proximo_vcu, idx_mais_proximo_vcu_work

###################################################################################
def master_external_fused_single_y(f1,
                                   power_bank_rated,
                                   voltage_bank_rated,
                                   voltage_bank_work,
                                   S, n, Pt, G):
    (bank_current_rated,
     bank_reactance_rated,
     bank_capacitance_rated) = calculate_bank_parameters(f1,
                                                         power_bank_rated,
                                                         voltage_bank_rated)

    (data_external_fused,
     data_units_and_elements) = various_burned_fused_external_single_Y(base_voltage=voltage_bank_rated,
                                                              base_current=bank_current_rated,
                                                              voltage_bank_work=voltage_bank_work,
                                                              S=S, n=n, Pt=Pt, G=G)

    df_data_external_fused = pd.DataFrame(data_external_fused)
    (df_stylized, 
     idx_mais_proximo_vcu,  
     idx_mais_proximo_vcu_work) = generate_df_stylized(df=df_data_external_fused,
                                                       Vcu_max=1.1,
                                                       Vcu_max_work=1.1)

    return df_stylized, idx_mais_proximo_vcu, idx_mais_proximo_vcu_work


###################################################################################

###################################################################################
def master_internal_fuses_bridge_h(f1,
                          power_bank_rated,
                          voltage_bank_rated,
                          voltage_bank_work,
                          S, Pt, Pa, P, G, N, Su):
    (bank_current_rated,
     bank_reactance_rated,
     bank_capacitance_rated) = calculate_bank_parameters(f1,
                                                         power_bank_rated,
                                                         voltage_bank_rated)

    (data_report, 
     data_ieeec3799,
     data_units_and_elements) = various_burned_fused_internal_bridge_h(base_voltage=voltage_bank_rated,
                                                              base_current=bank_current_rated,
                                                              voltage_bank_work=voltage_bank_work,
                                                              S=S, Pt=Pt, Pa=Pa, P=P, G=G, N=N, Su=Su)

    data_report = pd.DataFrame(data_ieeec3799)
    (df_stylized, 
     idx_mais_proximo_vcu,  
     idx_mais_proximo_vcu_work) = generate_df_stylized(df=data_report,
                                                       Vcu_max=1.1,
                                                       Vcu_max_work=1.1)

    return df_stylized, idx_mais_proximo_vcu, idx_mais_proximo_vcu_work

###################################################################################

