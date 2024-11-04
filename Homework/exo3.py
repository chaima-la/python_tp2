import re
from datetime import datetime

def extract_date(text):
    matches = re.findall(r"(\d{2}\/\d{2}\/\d{4})|(\d{2}\.\d{2}\.\d{4})|(\d{4}\/\d{2}\/\d{2})|(\d{2}(?:st|nd|rd|th)? of (January|February|March|April|May|June|July|August|September|October|November|December)?, \d{4})", text)
    return [date for match in matches for date in match if date]

def transform_dates(dates):
    transformed_dates = []
    month_map = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04',
        'May': '05', 'June': '06', 'July': '07', 'August': '08',
        'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }

    for date in dates:
        if '/' in date: 
            if len(date.split('/')[0]) == 2:  
                day, month, year = date.split('/')
            else:  
                year, month, day = date.split('/')
        elif '.' in date: 
            day, month, year = date.split('.')
        elif ' of ' in date:  
            day, month_year = date.split(' of ')
            month, year = month_year.split(', ')
            day = day.rstrip('stndrdth') 
        else:
            continue 

        transformed_date = f"{year}-{month_map.get(month, month).zfill(2)}-{day.zfill(2)}"
        transformed_dates.append(transformed_date)

    return transformed_dates

# Example usage
text = "15/08/1980 10.12.2024 2019/11/29 Friday, the 31st of January, 2025 April 23rd, 2015"
dates = extract_date(text)
transformed = transform_dates(dates)
print(transformed)
