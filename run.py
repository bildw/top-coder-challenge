import sys
from calculate import calculate


def main():
    if len(sys.argv) != 4:
        sys.stderr.write(
            "Usage: run.py <trip_duration_days> <miles_traveled> <total_receipts_amount>\n"
        )
        sys.exit(1)
    try:
        days = float(sys.argv[1])
        miles = float(sys.argv[2])
        receipts = float(sys.argv[3])
    except ValueError:
        sys.stderr.write("Error: all parameters must be numeric\n")
        sys.exit(1)

    result = calculate(days, miles, receipts)
    print(f"{result:.2f}")


if __name__ == "__main__":
    main()
