from multiprocessing import Process, Pipe
from os import getpid
from time import sleep

###### Вариант №1
def work(receiver, sender, response):
    sender.send('')
    while True:
        msg = receiver.recv()
        print(f"Process{getpid()} got message: {msg}")
        sleep(2)
        sender.send(response)


if __name__ == "__main__":
    sender_conn, receiver_conn = Pipe()
    process1 = Process(target=work, args=(
        sender_conn, receiver_conn, 'ping'))
    process2 = Process(target=work, args=(
        sender_conn, receiver_conn, 'pong'))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

#############Вариант №2

# def work(receiver, sender, response):
#
#     while True:
#         receiver.send(response)
#         print(f"Process {getpid()} got message: {response}")
#         sleep(2)
#         sender.send(response)
#
#
# if __name__ == "__main__":
#      sender_conn_1, receiver_conn_1 = Pipe()
#      sender_conn_2, receiver_conn_2 = Pipe()
#
#      process_1 = Process(target=work, args=(receiver_conn_1, sender_conn_2, "Ping"))
#      process_2 = Process(target=work, args=(receiver_conn_2, sender_conn_1, "Pong"))
#      process_1.start()
#      process_2.start()
#      process_1.join()
#      process_2.join()
