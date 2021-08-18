# teste_ping_1

import os
hostname = "lichess.org"
response = os.system("ping -t " + hostname)
if response == 0:
    pingstatus = "Network Active"
else:
    pingstatus = "Network Error"