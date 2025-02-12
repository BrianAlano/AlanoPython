def translate_date(date_str):
    months = {
        '01': 'January', '02': 'February', '03': 'March', '04': 'April',
        '05': 'May', '06': 'June', '07': 'July', '08': 'August',
        '09': 'September', '10': 'October', '11': 'November', '12': 'December'
    }
    
    month, day, year = date_str.split('/')
    
    day = str(int(day))
    
    month_name = months[month]
    
    return f"{month_name} {day}, {year}"

def main():
    date_str = input("Enter the date (mm/dd/yyyy): ")
    translated_date = translate_date(date_str)
    print(f"Date Output: {translated_date}")

if __name__ == "__main__":
    main()