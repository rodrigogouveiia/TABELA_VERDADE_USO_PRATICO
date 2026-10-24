# PARTE 1 
# CADASTRO E VALIDAÇÃO DOS DADOS (ENTRADA DO USUÁRIO)

print("====INSTALAÇÃO DO SISTEMA DE VALIDAÇÃO BANCÁRIA====")
P_user = idade_do_cliente= int(input("Digite sua idade: "))
Q_user = biometria_valida= input("A biometria facil foi aprovada? (S/N): ").upper() == 'S'
# =='S' pega a resposta digitada (S/N) e testa se é igual a 'S' (True). Qualquer resposta contrária a 'S' é transformada em False e guardada na variável.  
R_user = conta_foi_criada= input("O banco conseguiu gerar o número da conta? (S/N): ").upper() == 'S'
#==========================================================================================================
# PARTE 2 
# TRANFORMAÇÃO DOS DADOS EM VALORES PROPOSICIONAIS ( P, Q, R)
P_user = idade_do_cliente >= 18 #PROPOSIÇÃO 'P': IDADE É MAIOR OU IGUAL A 18?
Q_user = biometria_valida #PROPOSIÇÃO 'Q': BIOMETRIA É VÁLIDA?
R_user = conta_foi_criada #PROPOSIÇÃO 'R': CONTA FOI ABERTA?
#==========================================================================================================
# PARTE 3
# EXIBIÇÃO DA TABELA VERDADE 100% COMPLETA
print("\n========TABELA VERDADE DE AUDITORIA========")
print(f"{'Idade(P)':<9} | {'Bio(Q)':<7} | {'Conta(R)':<9} | {'P ^ Q':<6} | {'¬(P ^ Q)':<9} | {'(P ^ Q) → R':<13} | Status do Sistema")
print("-" * 100)

# OS TRÊS LOOPS TESTAM AS 8 (2³) COMBINAÇÕES DE TRUE E FALSE
for P in [True, False]:
    for Q in [True, False]:
        for R in [True, False]:

            # OPERAÇÕES LÓGICAS DA TABELA VERDADE
            p_e_q= P and Q  #CONJUNÇÃO (E) 
            negacao = not p_e_q  #NEGAÇÃO (NÃO) 
            implicacao = negacao or R #IMPLICAÇÃO (SE ... ENTÃO)    

            # FORMATAÇÃO DE TEXTO PARA SIMPLIFICAÇÃO NO TERMINAL
            v_p = 'V' if P else 'F'
            v_q = 'V' if Q else 'F'
            v_r = 'V' if R else 'F'
            v_e = 'V' if p_e_q else 'F'
            v_nao = 'V' if negacao else 'F'
            v_seta = 'V' if implicacao else 'F' 

            # REGRA DA VALIDAÇÃO BANCÁRIA
            status = "SISTEMA OK" if implicacao else "ERRO DO BANCO!"
            
            # MAPEAMENTO DO SEU STATUS ATUAL 
            if P == P_user and Q == Q_user and R == R_user:
                marcador = "<------- TESTE ATUAL"
            else:
                marcador= ""
            #EXIBE NO TERMINAL
            print(f"{v_p:<9} | {v_q:<7} | {v_r:<9} | {v_e:<6} | {v_nao:<9} | {v_seta:<13} | {status:<15} {marcador}")  
print("-" * 100)
