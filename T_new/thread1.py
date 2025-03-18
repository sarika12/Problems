import threading
# def print_number():
#     for i in range(5):
#         print(f"print number {i}")
#
# t=threading.Thread(target=print_number())
# t.start()
# t.join()
lock=threading.Lock()

# def critical_sections():
#     with lock:
#         print("Critical sectios")
#         print("xyz")
#
# a=critical_sections()

event = threading.Event()

def waiter():
    print("Waiting for event...")
    event.wait()
    print("Event received!")
    event.wait()
    print("Event received!")
threading.Thread(target=waiter).start()
event.set()








