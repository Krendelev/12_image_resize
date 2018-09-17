import argparse
from PIL import Image


def change_ratio(orig_image, width, height):
    if args.width and args.height:
        orig_ratio = orig_image.size[0] / orig_image.size[1]
        new_ratio = args.width / args.height
        return new_ratio != orig_ratio
    return False


def resize_image(image, width, height, scale):
    if scale:
        width, height = (int(size * scale) for size in image.size)
    elif not height:
        height = int(image.size[1] * width / image.size[0])
    elif not width:
        width = int(image.size[0] * height / image.size[1])
    return image.resize((width, height))


def save_image(image, path_to_result):
    name, ext = path_to_result.split('.')
    path = '{0}__{i[0]}x{i[1]}.{1}'.format(name, ext, i=image.size)
    image.save(path)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('--width', type=int, nargs='?')
    parser.add_argument('--height', type=int, nargs='?')
    parser.add_argument('--scale', type=float, nargs='?')
    parser.add_argument('-o', '--output', nargs='?')
    arguments = parser.parse_args()
    if (arguments.width or arguments.height) and arguments.scale:
        raise parser.error('You can not specify both the dimensions \
                            and the scale factor.')
    if not any([arguments.width, arguments.height, arguments.scale]):
        arguments.scale = 1
    if not arguments.output:
        arguments.output = arguments.file
    return arguments


if __name__ == '__main__':
    args = get_args()
    try:
        orig_image = Image.open(args.file)
    except FileNotFoundError:
        print('File not found')
    if change_ratio(orig_image, args.width, args.height):
        print(
            'New aspect ratio is different from the original one.',
            'Final image will be distorted.'
            )
    res_image = resize_image(orig_image, args.width, args.height, args.scale)
    save_image(res_image, args.output)
