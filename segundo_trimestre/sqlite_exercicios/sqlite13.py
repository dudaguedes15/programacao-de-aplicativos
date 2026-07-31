import sqlite3 
 
def verificar_registros(): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
    cursor.execute("SELECT * FROM alunos") 
     
	
    print("Primeiro print:", cursor.fetchall()) 


    cursor.execute("SELECT * FROM alunos") 
    print("Segundo print:", cursor.fetchall()) 
     
    conexao.close() 

verificar_registros()

#o fetchall apaga todos os registro que a gente escreveu, fazendo com que oq a gente escrevu retorne em uma lista vazia