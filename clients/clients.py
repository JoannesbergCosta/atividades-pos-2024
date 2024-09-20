import requests
from tabulate import tabulate


API_BASE_URL = "https://suap.ifrn.edu.br/api/v2/"
API_KEY = "" 

def get_grades(year, semester):
    
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    
    boletim_url = f"{API_BASE_URL}minhas-informacoes/boletim/{year}/{semester}/"
    
    try:
        response = requests.get(boletim_url, headers=headers)
        response.raise_for_status()  
        boletim_data = response.json()

        
        formatted_grades = []
        for disciplina in boletim_data:
            
            nome_disciplina = disciplina['disciplina']
            notas = disciplina['notas']
            unidade1 = notas.get('1', {}).get('nota', '-')
            unidade2 = notas.get('2', {}).get('nota', '-')
            unidade3 = notas.get('3', {}).get('nota', '-')
            unidade4 = notas.get('4', {}).get('nota', '-')
            media_final = disciplina.get('media_final', '-')

          
            formatted_grades.append([nome_disciplina, unidade1, unidade2, unidade3, unidade4, media_final])

       
        headers = ["Disciplina", "Unidade 1", "Unidade 2", "Unidade 3", "Unidade 4", "Média Final"]

        
        print(tabulate(formatted_grades, headers, tablefmt="grid"))

    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter boletim: {e}")

if __name__ == "__main__":
    year = input("Digite o ano do boletim: ")  
    semester = input("Digite o semestre do boletim (1 ou 2): ")  
    get_grades(year, semester)
