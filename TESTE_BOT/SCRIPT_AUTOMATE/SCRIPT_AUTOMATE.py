#Como Agendar Scripts Python & Execução Paralela #DevAprender
#LINK DO TUTORIAL: https://www.youtube.com/watch?v=PAnrHMQBB-Y


import schedule
import time

def FazerTarefaImportante():
    print(1)

#schedule.cada.tempo.fazer
schedule.every(1).seconds.do(FazerTarefaImportante)

while 1:
    schedule.run_pending()
    time.sleep(1)