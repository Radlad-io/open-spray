import sys
import aioble
import bluetooth
import machine
import uasyncio as asyncio

from micropython import const
from pimoroni import Button

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
# button_y = Button(15)



def uid():
    """ Return the unique id of the device as a string """
    return "{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}".format(
        *machine.unique_id())

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
                              
connection = None
remote_service = aioble.Service(_GENERIC)
button_characteristic = aioble.Characteristic(
    remote_service, _BUTTON_UUID, read=True, notify=True)

print("Registering services")
aioble.register_services(remote_service)
connected = False

constructed = b'{"rgba": "[255,255,255]", "sprayIndex": "0","layerIndex": "0" }'
async def remote_task():
    """ Task to handle remote control """
    while True:
        if not connected:
            print("Not Connected")
            await asyncio.sleep_ms(1000)
            continue
        if button_a.read():
            print(f"Button A pressed, connection is: {connection}")
            button_characteristic.write(b"a")
            # button_characteristic.notify(connection, constructed)
        elif button_b.read():
            print(f"Button B pressed, connection is: {connection}")
            button_characteristic.write(b"b")
            # button_characteristic.notify(connection, b"b")
        elif button_x.read():
            print(f"Button X pressed, connection is: {connection}")
            button_characteristic.write(b"x")
            # button_characteristic.notify(connection, b"x")
        else:
            button_characteristic.write(b"!")
            # button_characteristic.notify(connection, b"!")
        await asyncio.sleep_ms(10)

async def peripheral_task():
    """ Task to handle peripheral """
    global connected, connection
    while True:
        connected = False
        async with await aioble.advertise(
            ADV_INTERVAL_MS,
            name="BitSprayRemote",
            appearance=_BLE_APPEARANCE_GENERIC_REMOTE_CONTROL,
            services=[_GENERIC]
        ) as connection:
            print("Connection from, ", connection.device)
            connected = True
            print("connected {connected}")
            await connection.disconnected()
            print("disconnected")

async def blink_task():
    """ Task to blink LED """
    toggle = True
    while True:
        led.value(toggle)
        toggle = not toggle
        blink = 1000
        if connected:
            blink = 1000
        else:
            blink = 250
        await asyncio.sleep_ms(blink)


def test (self):
    print("sending test")
    button_characteristic.notify(connection, b"test")

machine.Pin(15).irq(handler=test, trigger=machine.Pin.IRQ_RISING)

async def main():
    tasks = [
        asyncio.create_task(peripheral_task()),
        asyncio.create_task(remote_task()),
        asyncio.create_task(blink_task()),
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())