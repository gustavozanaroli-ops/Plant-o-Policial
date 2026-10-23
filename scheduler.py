"""
Agendador de Tarefas (Daemon de Execução a cada 1 hora)
"""

import time
import schedule
from crawler import RadarCrawler

def tarefa_varredura():
    print(f"\n[{time.strftime('%Y-%m-%d %H:%M:%S')}] Executando varredura programada...")
    crawler = RadarCrawler()
    crawler.executar_ciclo()

def main():
    print("=" * 60)
    print("Radar Policial RMC & RMP - Serviço de Monitoramento Ativo")
    print("Frequência: Execução a cada 60 minutos")
    print("=" * 60)
    
    # Executa a primeira varredura imediatamente na inicialização
    tarefa_varredura()
    
    # Agenda para rodar exatamente a cada 1 hora
    schedule.every(1).hours.do(tarefa_varredura)
    
    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()
