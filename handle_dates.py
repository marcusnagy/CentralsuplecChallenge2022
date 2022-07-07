
from dateutil.parser import parse
import pandas as pd


def handle_bad_format(date: str):
    print(f"Date prior: {date}")
    if '(GMT+' in date or '(GMT-' in date:
        print("ENTER")
        date = date.replace(date[-11:-1], '(GMT')
        print(date)
        return date
    return date


def main():
    dates_train = pd.read_csv('train.csv/train.csv').pop('date')
    dates_test = pd.read_csv('test.csv/test.csv').pop('date')
    dates_total = pd.concat([dates_train, dates_test])
    dates_total_copy = dates_total.copy()

    for idx, date in enumerate(dates_total):
        date_object = parse(handle_bad_format(date))
        hours = date_object.hour
        weekday = date_object.weekday()
        match weekday:
            case 0 | 1 | 2 | 3 | 4:  # Work day
                if hours in range(6, 19):
                    dates_total_copy[idx] = 1
                elif hours in range(19, 25):
                    dates_total_copy[idx] = 2
            case 5 | 6:  # Weekend
                if hours in range(6, 19):
                    dates_total_copy[idx] = 3
                elif hours in range(19, 25):
                    dates_total_copy[idx] = 4

    print(dates_total_copy)


if __name__ == "__main__":
    main()
