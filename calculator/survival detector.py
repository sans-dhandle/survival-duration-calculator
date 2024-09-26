class SurvivalDurationCalculator:
    def __init__(self, age):
        self.age = age
        self.days_in_year = 365.25  # Average, accounting for leap years
        self.hours_in_day = 24
        self.minutes_in_hour = 60
        self.seconds_in_minute = 60

    def calculate_duration(self, unit):
        unit = unit.lower()
        if unit in ['months', 'm']:
            return self.age * 12
        elif unit in ['weeks', 'w']:
            return int((self.age * self.days_in_year) / 7)
        elif unit in ['days', 'd']:
            return int(self.age * self.days_in_year)
        elif unit in ['hours', 'h']:
            return int(self.age * self.days_in_year * self.hours_in_day)
        elif unit in ['minutes', 'min']:
            return int(self.age * self.days_in_year * self.hours_in_day * self.minutes_in_hour)
        elif unit in ['seconds', 's']:
            return int(self.age * self.days_in_year * self.hours_in_day * self.minutes_in_hour * self.seconds_in_minute)
        else:
            return "That's not a valid time unit. Try again."

def main():
    print("Enter The Value To Calculate How Long Time you've lived.")
    try:
        age = int(input("what's your age? "))
        time_unit = input("choose a time unit: months(m), weeks(w), days(d), hours(h), minutes(min), seconds(s).\n"
                          "or else just type first letter : ")
        calculator = SurvivalDurationCalculator(age)
        result = calculator.calculate_duration(time_unit)
        if isinstance(result, int):
            print(f"your survival is {result} {time_unit.capitalize() if len(time_unit) > 1 else 'Months' if time_unit == 'm' else ''}.")
        else:
            print(result)
    except ValueError:
        print("Error! , Enter the correct value For Age.")

if __name__ == "__main__":
    main()
