from datetime import date


def get_days_in_month(month:int, year:int) -> int:
    first_date_current = date(year, month, 1)
    
    if month == 12:
        first_date_next = date(year + 1, 1, 1)
    else:
        first_date_next = date(year, month + 1, 1)
      
    delta = first_date_next - first_date_current
    
    return delta.days




if __name__ == "__main__":
    month = 12
    year = 2023
    print(get_days_in_month(month, year))