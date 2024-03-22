# LIDAR_LD06_python_loder
This code can use  Lidar's LD06 (LDS06) provided by LDROBOT from python. and It displays the acquired point cloud in real time in matplotlib.

## How to use
1. Clone this repository and change `Serial(port='/dev/tty.usbserial-0001'...)` in main.py to your own port.
2. Run `pip install -r requirements.txt` in venv environment.
3. Run `python main.py`.
4. Press the E key to exit.

## About LD06(LDS06)
- Sales page https://www.inno-maker.com/product/lidar-ld06/
- Datasheet http://wiki.inno-maker.com/display/HOMEPAGE/LD06

## Docker build

```bash
docker build -t lidar_ld06_python_loader .
```

## Docker run

```bash
docker run -it --rm --device=/dev/ttyUSB0:/dev/ttyUSB0 lidar_ld06_python_loader
```

With nvidia runtime:
```bash
docker run -it --rm --device=/dev/ttyUSB0:/dev/ttyUSB0 \ 
--runtime=nvidia \
--gpus=all \
--env="NVIDIA_DRIVER_CAPABILITIES=all" \
--env="NVIDIA_VISIBLE_DEVICES=all" \
--env="DISPLAY=$DISPLAY" \
lidar_ld06_python_loader
```

## LICENSE
Please see [LICENSE](https://github.com/henjin0/LIDAR_LD06_python_loder/blob/main/LICENSE).
