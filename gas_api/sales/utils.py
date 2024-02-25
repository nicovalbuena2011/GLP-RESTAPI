from datetime import datetime

def get_range_dates():

    current_date = datetime.now()
    current_month = current_date.month
    current_year = current_date.year
    # current_day = current_date.day

    # Crear objetos datetime.date para la primera fecha del mes actual y la fecha actual
    first_date = datetime(current_year, current_month, 1).date()
    current_date = current_date.date()

    return (first_date, current_date)