from rembg import remove
from PIL import Image
from pathlib import Path


def remove_bg():
    list_of_ext = ['*.jpg', '*.png']
    all_files = []

    for ext in list_of_ext:
        all_files.extend(Path('/home/novikov/Python_projects/background_remover/input_img').glob(ext))

    for index, i in enumerate(all_files, start=1):
        input_path = Path(i)
        file_name = input_path.stem

        output_path = f'/home/novikov/Python_projects/background_remover/output_img/{file_name}_output.png'

        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)

        print(f'Completed: {index}/{len(all_files)}')


def main():
    remove_bg()


if __name__ == '__main__':
    main()
