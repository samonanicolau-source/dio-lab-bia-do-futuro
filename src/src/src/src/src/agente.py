import google.generativeai as genai
import pandas as pd
import json
from src.config import GOOGLE_API_KEY, DATA_PATH

class LumiAgente:
    def __init__(self):
        # Configura o Gemini
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Carrega a base de conhecimento local
        with open(f'{DATA_PATH}perfil_investidor.json', encoding='utf-8') as f:
            self.perfil = json.load(f)
        
        with open(f'{DATA_PATH}produtos_financeiros.json', encoding='utf-8') as f:
            self.produtos = json.load(f)

    def responder(self, pergunta):
        # O "Cérebro" da Lumi com as regras de Higiene Financeira
        system_prompt = f"""
        Você é a Lumi, mentora de Higiene Financeira em Angola.
        DADOS DO USUÁRIO: {self.perfil}
        PRODUTOS DISPONÍVEIS: {self.produtos}
        
        REGRAS:
        1. Fale 'Anti-Economês'.
        2. Foque em separar contas (BAI para gastos, Atlântico para metas).
        3. Priorize a meta do carro em 2027.
        """
        
        response = self.model.generate_content([system_prompt, pergunta])
        return response.text
