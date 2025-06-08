#!/usr/bin/env python3
import sys

# Usage: python3 run.py <trip_duration_days> <miles_traveled> <total_receipts_amount>

def compute_reimbursement(days: float, miles: float, receipts: float) -> float:
    # Coefficients estimated from public data via least squares
    INTERCEPT = 249.85639405
    PER_DAY = 50.07448435
    RATE_FIRST_600 = 0.50617464
    RATE_AFTER_600 = 0.38310204
    RECEIPT_RATE = 0.38220469

    m1 = min(miles, 600)
    m2 = max(miles - 600, 0)
    reimbursement = (
        INTERCEPT
        + PER_DAY * days
        + RATE_FIRST_600 * m1
        + RATE_AFTER_600 * m2
        + RECEIPT_RATE * receipts
    )
    return round(reimbursement, 2)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("Usage: python3 run.py <trip_duration_days> <miles_traveled> <total_receipts_amount>")
    try:
        days = float(sys.argv[1])
        miles = float(sys.argv[2])
        receipts = float(sys.argv[3])
    except ValueError:
        raise SystemExit("All arguments must be numeric")

    result = compute_reimbursement(days, miles, receipts)
    # Print numeric result with two decimal places
    print(f"{result:.2f}")
