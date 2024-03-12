import sys
import aioble
import bluetooth
import machine
import uasyncio as asyncio
from micropython import const

from modules.store import Store
from modules.display import Display

store = Store()
display = Display()

def uid():
    """ Return the unique id of the device as a string """
    return "{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}".format(
        *machine.unique_id())

DEVICE_NAME = "Bit Spray Remote"
MANUFACTURER_ID = const(0x02A29)
MODEL_NUMBER_ID = const(0x2A24)
SERIAL_NUMBER_ID = const(0x2A25)
HARDWARE_REVISION_ID = const(0x2A26)
BLE_VERSION_ID = const(0x2A28)

led = machine.Pin("LED", machine.Pin.OUT)

_DEVICE_INFO_UUID = bluetooth.UUID(0x180A) # Device Information
_GENERIC = bluetooth.UUID(0x1848)
_BUTTON_UUID = bluetooth.UUID(0x2A6E)
_BLE_APPEARANCE_GENERIC_REMOTE_CONTROL = const(384)
ADV_INTERVAL_MS = 250_000
BOUNCE_INTERVAL = 500 #In miliseconds
                              
connection = None
remote_service = aioble.Service(_GENERIC)
button_characteristic = aioble.Characteristic(remote_service, _BUTTON_UUID, read=True, notify=True)

print("Registering services")
aioble.register_services(remote_service)
connected = False
sync_required = True

data = None

async def remote_task():
    """ Task to handle remote control """
    global sync_required, data
    print("Waiting for Bluetooth connection...")
    while True:
        if not connected:
            await asyncio.sleep_ms(1000)
            continue
        if connected:
            if sync_required:
                data = store.get_values_as_json()
                button_characteristic.write(data)
                button_characteristic.notify(connection, data)
                sync_required = False
            await asyncio.sleep_ms(BOUNCE_INTERVAL)

async def peripheral_task():
    """ Task to handle peripheral """
    global connected, connection
    while True:
        connected = False
        async with await aioble.advertise(
            ADV_INTERVAL_MS,
            name=DEVICE_NAME,
            appearance=_BLE_APPEARANCE_GENERIC_REMOTE_CONTROL,
            services=[_GENERIC]
        ) as connection:
            print("Connection from, ", connection.device)
            connected = True
            display.home_screen()
            print("connected {connected}")
            await connection.disconnected(timeout_ms=None)
            connected = False
            display.boot_screen("Connection lost:", "Please reconnect", "using bluetooth")
            print("disconnected")

async def main():
    tasks = [
        asyncio.create_task(peripheral_task()),
        asyncio.create_task(remote_task()),
    ]
    await asyncio.gather(*tasks)

