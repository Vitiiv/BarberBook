from app.database.database import engine

try:
    conexao = engine.connect()
    print("-------------------------------------------------")
    print("SUCESSO! O Python conectou no banco barberbook!")
    print("--------------------------------------------------")
    conexao.close()
except Exception as e:
    print(" ERRO:", e)
    
    