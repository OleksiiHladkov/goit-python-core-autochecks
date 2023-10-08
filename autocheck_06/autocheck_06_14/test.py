import shutil


def unpack(archive_path:str, path_to_unpack:str) -> None:
    shutil.unpack_archive(archive_path, path_to_unpack, "zip")




if __name__ == "__main__":
    archive_path = "./backup_folder.zip"
    path_to_unpack = "./unpack_folder"
    unpack(archive_path, path_to_unpack)