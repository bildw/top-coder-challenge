#!/usr/bin/env bash
set -euo pipefail

# Usage: ./run.sh <trip_duration_days> <miles_traveled> <total_receipts_amount>
python3 run.py "$@"
