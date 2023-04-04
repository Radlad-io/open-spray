### Raspberry Pi Pico Pin Out

| Purpose      | Use | Pin     |     | Pin          | Use  | Purpose      |
| ------------ | --- | ------- | --- | ------------ | ---- | ------------ |
| Audio Driver | A+  | GPIO_0  | -   | **VBUS**     |      |              |
| RotEncoder_1 |     | GPIO_01 | -   | **VSYS**     |      |              |
|              |     | **GND** | -   | **GND**      |      |              |
| RotEncoder_1 |     | GPIO_02 | -   | **3v3_EN**   |      |              |
| RotEncoder_1 |     | GPIO_03 | -   | **3V3(OUT)** |      |              |
| RotEncoder_1 |     | GPIO_04 | -   | **ADC_VREF** |      |              |
| RotEncoder_1 |     | GPIO_05 | -   | GPIO_28      |      | Trigger BTN  |
|              |     | **GND** | -   | **GND**      |      |              |
| RotEncoder_1 |     | GPIO_06 | -   | GPIO_27      |      | IR LED       |
| RotEncoder_2 |     | GPIO_07 | -   | GPIO_26      |      | RotEncoder_3 |
| RotEncoder_2 |     | GPIO_08 | -   | **RUN**      |      |              |
| RotEncoder_2 |     | GPIO_09 | -   | GPIO_22      |      | RotEncoder_3 |
|              |     | **GND** | -   | **GND**      |      |              |
| RotEncoder_2 |     | GPIO_10 | -   | GPIO_21      |      | RotEncoder_3 |
| RotEncoder_2 |     | GPIO_11 | -   | GPIO_20      | BL   | Display      |
| RotEncoder_2 |     | GPIO_12 | -   | GPIO_19      | MOSI | Display      |
| RotEncoder_3 |     | GPIO_13 | -   | GPIO_18      | SCK  | Display      |
|              |     | **GND** | -   | **GND**      | -    | Display      |
| RotEncoder_3 |     | GPIO_14 | -   | GPIO_17      | CS   | Display      |
| RotEncoder_3 |     | GPIO_25 | -   | GPIO_16      | DC   | Display      |

### Audio

Adafruit PAM8302 - https://www.adafruit.com/product/2130

https://learn.adafruit.com/mp3-playback-rp2040/pico-mp3

Hole Saw
https://www.homedepot.com/p/DIABLO-2-1-8-in-Carbide-Hole-Saw-with-2-3-8-in-Cutting-Depth-DHS2125CT/301697693
