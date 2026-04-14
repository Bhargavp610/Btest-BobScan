# App Folder

This folder contains a tiny customer order processing demo used for BobScan testing.

## What this folder is doing
- reads order data
- calculates totals and discounts
- writes events to a local log
- exposes a simple C++ helper used by the demo

## Files
- `order_processor.py` - main Python logic for loading and processing orders
- `auth_utils.py` - helper functions for token and password validation
- `report_builder.py` - builds a simple text report from processed orders
- `math_helper.cpp` - small C++ utility with intentionally weak logic checks
- `README.md` - explains this folder

## Why this repo exists
This is a dummy repo for scan testing. It contains a mix of:
- working code
- documentation drift
- security problems
- logical mistakes
- naming and professionalism issues

It is intentionally imperfect so the scanner can find issues and suggest fixes.