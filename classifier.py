"""
Motor de Classificação e Filtragem Rigorosa
Garante que apenas notícias policiais e investigativas das regiões RMC e RMP sejam aprovadas.
"""

import re
import unicodedata
from config import CIDADES_RMC, CIDADES_RMP, TODAS_CIDADES, KEYWORDS_POLICIA, KEYWORDS_EXCLUSAO

def normalizar_texto(texto: str) -> str:
    """Remove acentos e converte para minúsculas para correspondência imune a diacríticos."""
    if not texto:
        return ""
    texto_norm = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    return texto_norm.lower()

def detectar_municipio(texto: str):
    """
    Identifica se o texto cita algum município de RMC ou RMP.
    Retorna uma tupla (nome_cidade, regiao) ou (None, None).
    """
    texto_busca = normalizar_texto(texto)
    
    # Busca primeiro nas cidades de RMC
    for cidade in CIDADES_RMC:
        padrao = r'\b' + re.escape(normalizar_texto(cidade)) + r'\b'
        if re.search(padrao, texto_busca):
            return cidade, "RMC"
            
    # Busca nas cidades de RMP
    for cidade in CIDADES_RMP:
        padrao = r'\b' + re.escape(normalizar_texto(cidade)) + r'\b'
        if re.search(padrao, texto_busca):
            return cidade, "RMP"
            
    return None, None

def avaliar_conteudo_policial(titulo: str, corpo: str) -> bool:
    """
    Avalia se o conteúdo é estritamente policial e de investigação criminal.
    Exclui ruídos de esportes, celebridades, etc.
    """
    conteudo = normalizar_texto(f"{titulo} {corpo}")
    
    # 1. Verifica termos de exclusão forte
    for exc in KEYWORDS_EXCLUSAO:
        if re.search(r'\b' + re.escape(normalizar_texto(exc)) + r'\b', conteudo):
            return False
            
    # 2. Contabiliza termos policiais
    hits = 0
    for kw in KEYWORDS_POLICIA:
        if re.search(r'\b' + re.escape(normalizar_texto(kw)) + r'\b', conteudo):
            hits += 1
            
    # Título tem peso duplo
    titulo_norm = normalizar_texto(titulo)
    for kw in KEYWORDS_POLICIA:
        if re.search(r'\b' + re.escape(normalizar_texto(kw)) + r'\b', titulo_norm):
            hits += 2
            
    # Requer pelo menos 2 ocorrências ou 1 no título
    return hits >= 2

def categorizar_crime(texto: str) -> str:
    """Determina a categoria criminal principal para organização em tags."""
    t = normalizar_texto(texto)
    if any(k in t for k in ["homicidio", "assassinato", "latrocinio", "morte", "corpo encontrado"]):
        return "Homicídios / Latrocínios"
    if any(k in t for k in ["trafico", "drogas", "cocaina", "maconha", "entorpecentes"]):
        return "Tráfico de Drogas"
    if any(k in t for k in ["gaeco", "operacao", "organizacao criminosa", "faccoes", "deic"]):
        return "Operações & Crime Organizado"
    if any(k in t for k in ["mandado", "prisao preventiva", "foragido", "capturado", "captura"]):
        return "Mandados de Prisão"
    if any(k in t for k in ["roubo de carga", "furto", "assalto", "estelionato", "golpe"]):
        return "Patrimônio & Roubo de Carga"
    if any(k in t for k in ["pericia", "policia cientifica", "laudo", "iml", "instituto criminalistica"]):
        return "Perícia Técnica / IML"
    return "Geral Policial"
