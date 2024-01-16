# Winterevent 2024 Embedded Talk

## 🔦 Firmware Flash 

- Supported chips: `esp32`, `esp8266`, `esp32s2`

- Images [Micropython source](https://micropython.org/download):
  - `esp32`: [firmware/ESP32_GENERIC-20240105-v1.22.1.bin](firmware/ESP32_GENERIC-20240105-v1.22.1.bin)
  - `esp32s2`: [firmware/LOLIN_S2_MINI-20240105-v1.22.1.bin](firmware/LOLIN_S2_MINI-20240105-v1.22.1.bin)
  - `esp8266`: [firmware/ESP8266_GENERIC-20240105-v1.22.1.bin](firmware/ESP8266_GENERIC-20240105-v1.22.1.bin)

- Steps:
  1. install `esptool` for flashing: `pip install esptool`
  2. find port (macOS): `l /dev/cu.* `
  3. execute (e.g. port: `/dev/cu.usbmodem01`, image: `firmware/ESP32_GENERIC-20240105-v1.22.1.bin`, chip: see supported chips)
        ```
        source scripts/<chip>_firmware_flash.sh <port> <image>
        ```

## ⚙️ Setting Up
1. create `secrets.py` file and add Wi-Fi connection details, variables: `SSID`, `PASSWORD` (`.gitignore` ignores file)
2. 
