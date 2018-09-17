# Image Resizer

Utility for image resizing and file format conversion. It works with `jpeg` and `png` files out of the box, for additional formats install [corresponding libraries](https://pillow.readthedocs.io/en/5.2.x/installation.html#building-from-source).

## How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

## Usage

To resize image provide file name and one of the three possible parameters: `--width`, `--height` or `--scale`. You can also change resulting file name and destination with `--output` parameter. You can not specify both dimensional parameters and scale factor at the same time. Missing parameter will be calculated. If both `width` and `height` are specified and new aspect ratio differs from an old one, program will warn you and proceed.
```bash
$ python image_resize.py test.jpg --scale 0.5 # => test__200x300.jpg
$ python image_resize.py test.jpg --width 300 # => test__300x450.jpg
$ python image_resize.py test.jpg --height 240 # => test__160x240.jpg
$ python image_resize.py test.jpg --width 200 --height 200 # => test__200x200.jpg
New aspect ratio is different from the original one. Final image will be distorted.
```
To convert an image change the file extension to the file format you want to convert your image to.
```bash
$ python image_resize.py test.jpg -o test.png # => test__200x300.png
```

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
