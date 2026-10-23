"""
Coletor Automático de Notícias e Documentos Oficiais (Crawler)
Monitora RSS de portais, Google News e endpoints governamentais a cada hora.
"""

import json
import logging
import time
from datetime import datetime
import hashlib
from config import FEEDS_RSS_NOTICIAS, FONTES_OFICIAIS, TODAS_CIDADES
from classifier import detectar_municipio, avaliar_conteudo_policial, categorizar_crime

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def gerar_hash_id(titulo: str, link: str) -> str:
    """Gera um identificador único para prevenir duplicatas de notícias."""
    conteudo = f"{titulo}_{link}".encode("utf-8")
    return hashlib.sha256(conteudo).hexdigest()[:16]

class RadarCrawler:
    def __init__(self, db_file="radar_noticias.json"):
        self.db_file = db_file
        self.noticias = self._carregar_banco()
        
    def _carregar_banco(self):
        try:
            with open(self.db_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _salvar_banco(self):
        with open(self.db_file, "w", encoding="utf-8") as f:
            json.dump(self.noticias, f, ensure_ascii=False, indent=2)

    def processar_item(self, titulo: str, resumo: str, link: str, fonte_nome: str, tipo_fonte: str, data_publicacao=None):
        """Valida se o item é relevante e grava no banco se aprovado."""
        cidade, regiao = detectar_municipio(f"{titulo} {resumo}")
        if not cidade:
            return None # Não pertence à RMC ou RMP
            
        if not avaliar_conteudo_policial(titulo, resumo):
            return None # Não é policial/investigativo
            
        item_id = gerar_hash_id(titulo, link)
        if any(item["id"] == item_id for item in self.noticias):
            return None # Já coletado anteriormente
            
        categoria = categorizar_crime(f"{titulo} {resumo}")
        
        novo_registro = {
            "id": item_id,
            "titulo": titulo.strip(),
            "resumo": resumo.strip(),
            "link": link,
            "fonte": fonte_nome,
            "tipo_fonte": tipo_fonte, # 'Notícia' ou 'Documento Oficial'
            "cidade": cidade,
            "regiao": regiao,
            "categoria": categoria,
            "coletado_em": datetime.now().isoformat(),
            "data_publicacao": data_publicacao or datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        
        self.noticias.insert(0, novo_registro)
        logging.info(f"NOVO REGISTRO APROVADO: [{cidade} - {regiao}] [{categoria}] {titulo[:60]}...")
        return novo_registro

    def executar_ciclo(self):
        """Executa um ciclo completo de varredura por todas as fontes."""
        logging.info("Iniciando varredura horária de fontes policiais...")
        novos_encontrados = 0
        
        # Em produção, aqui utiliza-se feedparser ou requests:
        # Exemplo com feedparser:
        # for feed_info in FEEDS_RSS_NOTICIAS:
        #     feed = feedparser.parse(feed_info["url"])
        #     for entry in feed.entries:
        #         item = self.processar_item(...)
        
        self._salvar_banco()
        logging.info(f"Varredura concluída. Total de notícias no banco: {len(self.noticias)}")
        return novos_encontrados

if __name__ == "__main__":
    crawler = RadarCrawler()
    crawler.executar_ciclo()
