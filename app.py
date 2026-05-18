import os

senha_do_banco = os.genetv('SENHA_BANCO', 'NAO_CONFIGURADA')

print("--- SISTEMA DO BANCO DIGITAL ---")

if senha_do_banco == '12345':
    print("SENHA CORRETA!, acesso liberado ao cofre.")
else:
    print(" ACESSO NEGADO!, cahbe de segurança nao encontrada.")