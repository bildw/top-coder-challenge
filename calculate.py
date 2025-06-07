def calculate(days: float, miles: float, receipts: float) -> float:
    """Compute the reimbursement amount."""
    BASE_PER_DIEM = 50.0
    RATE_FIRST_600 = 0.35
    RATE_AFTER_600 = 0.20
    RECEIPT_WEIGHT = 0.80

    mileage = RATE_FIRST_600 * min(miles, 600) + RATE_AFTER_600 * max(miles - 600, 0)
    amount = RECEIPT_WEIGHT * receipts + BASE_PER_DIEM * days + mileage
    return amount
