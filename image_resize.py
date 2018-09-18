import os
import argparse
from PIL import Image


def ratio_changed(original, width, height):
    return original[0] / original[1] != width / height


def compute_size(image_size, width, height, scale):
    if scale:
        width, height = (int(size * scale) for size in image_size)
    elif not height:
        height = int(image_size[1] * width / image_size[0])
    elif not width:
        width = int(image_size[0] * height / image_size[1])
    return width, height


def get_path(image_size, path_to_result):
    name, ext = os.path.splitext(path_to_result)
    path = '{0}__{i[0]}x{i[1]}.{1}'.format(name, ext, i=image_size)
    return path


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('--width', type=int, nargs='?')
    parser.add_argument('--height', type=int, nargs='?')
    parser.add_argument('--scale', type=float, nargs='?')
    parser.add_argument('-o', '--output', nargs='?')
    return parser


def validate_args(parser):
    arguments = parser.parse_args()
    parameters = (arguments.width, arguments.height, arguments.scale)
    parameter_exists = tuple(filter(None, parameters))
    if not any(parameter_exists):
        raise parser.error('You must specify at least one '
                           'parameter: width, height, scale')
    if any(filter(lambda x: x < 0, parameter_exists)):
        raise parser.error('Height, width and scale must be > 0')
    if (arguments.width or arguments.height) and arguments.scale:
        raise parser.error('You can not specify both the dimensions '
                           'and the scale factor')
    if arguments.output and not (os.path.splitext(arguments.output)[1]):
        raise parser.error('You must specify file extension')
    return arguments


if __name__ == '__main__':
    args = validate_args(get_args())
    try:
        orig_image = Image.open(args.file)
    except FileNotFoundError:
        exit('File not found')
    if (args.width and args.height and
            ratio_changed(orig_image.size, args.width, args.height)):
        print(
            'New aspect ratio is different from the original one. '
            'Final image will be distorted.'
            )
    new_width, new_height = compute_size(
        orig_image.size, args.width, args.height, args.scale
        )
    res_image = orig_image.resize((new_width, new_height))
    if not args.output:
        args.output = get_path(res_image.size, args.file)
    res_image.save(args.output)
