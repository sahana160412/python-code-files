import os

def shutdown():
    os.system("shutdown /s /t 0" if os.name == 'nt' else "sudo shutdown now")
    
shutdown()