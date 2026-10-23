"""
Configurações de Fontes e Cidades para o Radar Policial RMC e RMP
"""

# Lista oficial dos 20 municípios da Região Metropolitana de Campinas (RMC)
CIDADES_RMC = [
    "Campinas", "Americana", "Artur Nogueira", "Cosmópolis", "Engenheiro Coelho",
    "Holambra", "Hortolândia", "Indaiatuba", "Itatiba", "Jaguariúna",
    "Monte Mor", "Morungaba", "Nova Odessa", "Paulínia", "Pedreira",
    "Santa Bárbara d'Oeste", "Santo Antônio de Posse", "Sumaré", "Valinhos", "Vinhedo"
]

# Lista oficial dos 24 municípios da Região Metropolitana de Piracicaba (RMP)
CIDADES_RMP = [
    "Piracicaba", "Águas de São Pedro", "Analândia", "Araras", "Capivari",
    "Charqueada", "Conchal", "Cordeirópolis", "Corumbataí", "Elias Fausto",
    "Ipeúna", "Iracemápolis", "Leme", "Limeira", "Mombuca",
    "Pirassununga", "Rafard", "Rio Claro", "Rio das Pedras", "Saltinho",
    "Santa Cruz da Conceição", "Santa Gertrudes", "Santa Maria da Serra", "São Pedro"
]

TODAS_CIDADES = CIDADES_RMC + CIDADES_RMP

# Palavras-chave obrigatórias do nicho policial e investigativo
KEYWORDS_POLICIA = [
    "polícia", "policia civil", "policia militar", "pm", "baep", "deic", "gaeco",
    "investigação", "inquérito", "mandado de prisão", "mandado de busca",
    "homicídio", "homicidio", "assassinato", "latrocínio", "latrocinio",
    "tráfico de drogas", "entorpecentes", "apreensão", "flagrante",
    "prisão preventiva", "preso", "presa", "foragido", "roubo de carga",
    "sequestro", "perícia técnica", "polícia científica", "tribunal de justiça",
    "ministério público", "mpsp", "boletim de ocorrência", "delegacia", "dise", "dig"
]

# Termos a descartar (para evitar falsos positivos de esportes, política comum ou trânsito leve)
KEYWORDS_EXCLUSAO = [
    "futebol", "campeonato", "política partidária", "eleições municipais",
    "receita de bolo", "horóscopo", "carnaval", "show", "ingresso"
]

# Feeds RSS e Endpoints de busca
FEEDS_RSS_NOTICIAS = [
    {
        "nome": "G1 Campinas e Região (Polícia)",
        "url": "https://g1.globo.com/sp/campinas-regiao/rss.xml",
        "regiao": "RMC"
    },
    {
        "nome": "G1 Piracicaba e Região (Polícia)",
        "url": "https://g1.globo.com/sp/piracicaba-regiao/rss.xml",
        "regiao": "RMP"
    },
    {
        "nome": "Google News RSS - Polícia RMC",
        "url": "https://news.google.com/rss/search?q=policia+investigacao+Campinas+OR+Americana+OR+Sumare+OR+Hortolandia&hl=pt-BR&gl=BR&ceid=BR:pt-419",
        "regiao": "RMC"
    },
    {
        "nome": "Google News RSS - Polícia RMP",
        "url": "https://news.google.com/rss/search?q=policia+investigacao+Piracicaba+OR+Limeira+OR+Rio+Claro+OR+Araras&hl=pt-BR&gl=BR&ceid=BR:pt-419",
        "regiao": "RMP"
    }
]

# Endpoints de Documentos Oficiais
FONTES_OFICIAIS = [
    {
        "nome": "Diário Oficial do Estado de SP (DOE)",
        "tipo": "DOE",
        "base_url": "https://www.imprensaoficial.com.br",
        "termo_busca": "Segurança Pública Campinas Piracicaba"
    },
    {
        "nome": "Secretaria da Segurança Pública (SSP-SP)",
        "tipo": "SSP",
        "url_noticias": "https://www.ssp.sp.gov.br/noticias",
        "url_estatisticas": "https://www.ssp.sp.gov.br/estatistica"
    },
    {
        "nome": "Ministério Público de São Paulo (MPSP - GAECO)",
        "tipo": "MPSP",
        "url_noticias": "https://www.mpsp.mp.br/noticias"
    }
]
