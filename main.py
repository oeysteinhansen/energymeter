import time
import modbus_server


def main():
    s = modbus_server.Server(port=5020)
    s.start()
    s.set_coil(1,True)
    while True:
        time.sleep(1.0)

main()