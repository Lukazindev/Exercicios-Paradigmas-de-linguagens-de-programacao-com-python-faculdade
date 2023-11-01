import threading
import time

# Função que será executada pela primeira thread
def thread1_function():
    time.sleep(3)
    print("Thread 1 executada")

# Função que será executada pela segunda thread
def thread2_function():
    time.sleep(2)
    print("Thread 2 executada")

# Crie as threads
thread1 = threading.Thread(target=thread1_function)
thread2 = threading.Thread(target=thread2_function)

# Inicie as threads
thread1.start()
thread2.start()

# Aguarde o término das threads
thread1.join()
thread2.join()

print("Ambas as threads terminaram a execução")
