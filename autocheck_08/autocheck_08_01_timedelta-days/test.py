from datetime import datetime


def get_days_from_today(date:str) -> datetime:
    date_lst = date.split("-")
    date_current = datetime.now()
    delta = date_current - datetime(int(date_lst[0]), int(date_lst[1]), int(date_lst[2]))
    
    return delta.days





if __name__ == "__main__":
    date = "2021-10-09"
    print(get_days_from_today(date))