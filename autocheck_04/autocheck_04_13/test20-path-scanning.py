from pathlib import Path


def parse_folder(path: Path) -> tuple:
    files = []
    folders = []

    for i in path.iterdir():
        if i.is_dir():
            folders.append(i.name)
        else:
            files.append(i.name)

    return files, folders


if __name__ == '__main__':
    path = Path('C:\Games_Portable\Diablo 2 LoD')
    print(parse_folder(path))
