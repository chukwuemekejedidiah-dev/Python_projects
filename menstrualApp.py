from datetime import date, timedelta

def calculate_next_period(start_date, cycle_length):
    return start_date + timedelta(days=cycle_length)

def calculate_period_end(start_date, duration):
    return start_date + timedelta(days=duration)

def calculate_ovulation_date(next_period_date):
    return next_period_date - timedelta(days=14)

def predict_cycle(start_date, cycle_length, period_duration):
    next_period = calculate_next_period(start_date, cycle_length)
    end = calculate_period_end(next_period, period_duration)
    ovu = calculate_ovulation_date(next_period)
    fert_start = ovu - timedelta(days=5)

    print("\n--- Prediction ---")
    print("Next Period:", next_period.strftime("%d/%m/%Y"))
    print("Period End:", end.strftime("%d/%m/%Y"))
    print("Ovulation:", ovu.strftime("%d/%m/%Y"))
    print("Fertility Window:", fert_start.strftime("%d/%m/%Y"), "to", ovu.strftime("%d/%m/%Y"))
    print("------------------\n")

def get_valid_int(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"Value must be at least {min_val}. Try again.")
                continue
            if value > max_val:
                print(f"Value must not exceed {max_val}. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

while True:
    day = get_valid_int("Day (1-31): ", 1, 31)
    month = get_valid_int("Month (1-12): ", 1, 12)
    year = get_valid_int("Year (e.g., 2026): ", 1900, 2100)
    cycle = get_valid_int("Cycle Length (21-35 days): ", 15, 60)
    duration = get_valid_int("Period Duration (3-10 days): ", 1, 15)

    try:
        start_date = date(year, month, day)
        predict_cycle(start_date, cycle, duration)
    except ValueError:
        print("Invalid date entered. Please check the day, month, and year.")

    again = input("Do you want to make another prediction? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye! Stay healthy")
        break
