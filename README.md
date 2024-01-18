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
2. plug device to PC with cable taht supports data transfer (`USB C`, `micro USB)

## 🏁 Quickstart Guide
1. download [Thonny app](https://thonny.org) on computer
2. right corner, select port for that device (e.g. `ESP32 /dev/cu.usbserial-0001` on Mac/Linux, `COM*` on Windows)
3. if that didn't connect the device (green play button should appear if it's connected/detected):
   1. try clicking on the red stop button in the Thonny
   2. try selecting another device for that same chip (e.g. ESP32 or ESP8266)
   3. sometimes it takes few seconds for computer to detect device (restart from `step 1`)
4. change `main.py` file with libraries from `src/common` folder, use `src/examples`for examples and quickstart
5. (optional) change `src/common` libraries if needed to fit your design
