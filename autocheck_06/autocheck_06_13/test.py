import shutil


def create_backup(path:str, file_name:str, employee_residence:dict[str,str]) -> str:
    file_data = ""
    for employee, residence in employee_residence.items():
        file_data += f"{employee} {residence}\n"
    
        file_data_byte = file_data.encode("utf-8")

        with open(path + "/" + file_name, "wb") as fh:
            fh.write(file_data_byte)

    return shutil.make_archive("backup_folder", "zip", path)




if __name__ == "__main__":
    path = "./test_folder"
    file_name = "test.bin"
    employee_residence = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
    print(create_backup(path, file_name, employee_residence))