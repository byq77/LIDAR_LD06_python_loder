#!/usr/bin/env python3
"""
LIDAR LD06 test program
"""
import serial
import binascii
from CalcLidarData import CalcLidarData
import matplotlib.pyplot as plt
import math
import argparse
import os

PORT = os.getenv("LD06_PORT", "/dev/ttyUSB0")


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument(
        "--print", action="store_true", help="print the data to the console"
    )

    args = args.parse_args()

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="polar")
    ax.set_title("lidar (exit: Key E)", fontsize=18)

    plt.connect("key_press_event", lambda event: exit(1) if event.key == "e" else None)

    with serial.Serial(
        port=PORT,
        baudrate=230400,
        timeout=5.0,
        bytesize=8,
        parity="N",
        stopbits=1,
    ) as ser:

        tmpString = ""
        lines = list()
        angles = list()
        distances = list()

        i = 0
        while True:
            loopFlag = True
            flag2c = False

            if i % 40 == 39:
                if "line" in locals():
                    line.remove()
                line = ax.scatter(angles, distances, c="pink", s=5)

                ax.set_theta_offset(math.pi / 2)
                plt.pause(0.01)
                angles.clear()
                distances.clear()
                i = 0

            while loopFlag:
                b = ser.read()
                tmpInt = int.from_bytes(b, "big")

                if tmpInt == 0x54:
                    tmpString += b.hex() + " "
                    flag2c = True
                    continue

                elif tmpInt == 0x2C and flag2c:
                    tmpString += b.hex()

                    if not len(tmpString[0:-5].replace(" ", "")) == 90:
                        tmpString = ""
                        loopFlag = False
                        flag2c = False
                        continue

                    lidarData = CalcLidarData(tmpString[0:-5])
                    angles.extend(lidarData.Angle_i)
                    distances.extend(lidarData.Distance_i)

                    if args.print:
                        print(tmpString[-5:], end=" ")
                        print(tmpString[:-5], flush=True)

                    tmpString = ""
                    loopFlag = False
                else:
                    tmpString += b.hex() + " "

                flag2c = False

            i += 1


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
