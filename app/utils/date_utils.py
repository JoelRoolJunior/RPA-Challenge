from datetime import datetime

def get_current_timestamp():
    return datetime.now().strftime('%d-%m-%Y %H:%M:%S')

def convert_str_to_date(date_str, format='%d-%m-%Y'):
    return datetime.strptime(date_str, format)