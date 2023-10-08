from datetime import datetime


def get_str_date(date:str) -> str:
    date_datetime = datetime.fromisoformat(date.replace("Z", ""))
    
    return date_datetime.strftime("%A %d %B %Y")




if __name__ == "__main__":
    date = "2021-05-27 17:08:34.149Z"
    print(get_str_date(date))
