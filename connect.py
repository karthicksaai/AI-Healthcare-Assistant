import bluetooth
import time
devices = bluetooth.discover_devices(lookup_names=True)
for addr, name in devices:
    print(f"Found device: {name} ({addr})")
smartwatch_addr = "00:00:00:00:00:00"
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((smartwatch_addr,1))
while True:
    heartbeat_command = b"GET_HEARTBEAT"
    sock.send(heartbeat_command)
    heartbeat_data = sock.recv(1024)
    print("Heartbeat value:", heartbeat_data.decode())

    step_count_command = b"GET_STEP_COUNT"
    sock.send(step_count_command)
    step_count_data = sock.recv(1024)
    print("Step count:", step_count_data.decode())

    time.sleep(5)