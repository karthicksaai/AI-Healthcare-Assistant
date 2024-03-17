import time
from bleak import BleakScanner, BleakClient

# Define the UUIDs of the service and characteristic you want to interact with
SERVICE_UUID = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"  # Replace with your service UUID
CHARACTERISTIC_UUID = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"  # Replace with your characteristic UUID

async def handle_data(sender, data):
    # This function will be called whenever new data is received from the smartwatch
    # Parse the received data and process it as needed for your ML model
    print("Received data:", data)

async def main():
    scanner = BleakScanner()

    # Start scanning for devices
    await scanner.start()

    # Wait for the smartwatch to be discovered
    while True:
        devices = await scanner.discover()
        for device in devices:
            if device.address == "DE:D8:72:B5:0A:98":  # Replace with your smartwatch's MAC address
                print("Smartwatch found!")
                await scanner.stop()
                break
        if not scanner.discovered_devices:
            await asyncio.sleep(1)
        else:
            break

    # Connect to the smartwatch
    async with BleakClient("DE:D8:72:B5:0A:98") as client:  # Replace with your smartwatch's MAC address
        print("Connected to smartwatch.")

        # Enable notifications for the characteristic
        await client.start_notify(CHARACTERISTIC_UUID, handle_data)

        print("Listening for data...")

        # Keep the script running to continue receiving data
        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
