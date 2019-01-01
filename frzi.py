import time
from threading import Timer
timeout=10
t=Timer(timeout, print, ['Sorry, times up'])
t.start()
prompt="You got 10 seconds to answer"
answer=input(prompt)
t.cancel()
print(answer)