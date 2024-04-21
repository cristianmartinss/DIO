menu = '''
====================
|| [d] Depositar  ||
|| [s] Sacar      ||
|| [e] Extrato    ||
|| [q] Sair       ||
===================
'''
saldo = 0
limite = 500
numero_saques = 0 
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        val = float(input('''
                            
============================================
|| Digite o valor que você vai depositar: ||
============================================       
                        '''))
        saldo = saldo + val
        print(f'''
=================================
|| Valor de R${val} depositado ||
=================================              
            ''')

    if opcao == "s":

        if numero_saques > LIMITE_SAQUES:
            print('''
==============================
|| Apenas 3 saques por dia: ||
==============================
''')
            continue

        val = float(input('''
========================================
|| Digite o valor que você vai sacar: ||
========================================
                        '''))
        
        if val <= saldo:
            if val <= 500:
                print(f'''
======================
|| Sacando R${val} ||
======================            
                      ''')
                numero_saques = numero_saques +1
                saldo = saldo - val

            else:
                print('''
=======================================
|| Valor máximo para Saque: R$500,00 ||
=======================================
                     ''')
                
        else:
            print(f'''
========================
|| Saldo Insuficiente ||
========================          
                  ''')
            
    if opcao == "e":
        print(f'''
==================================
|| Seu saldo é de R${saldo:.2f} ||
==================================        
              ''')
        
    if opcao == "q":
        print(f'''
====================
|| Ok, Encerrando ||
====================            
              ''')

        break