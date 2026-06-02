from collections import Counter
from pathlib import Path

log_file = Path("logs/app.log")
report_file = Path("logs/report.txt")

if not log_file.exists():
    print("Log file does not exist yet. Start the app and hit some endpoints first.")
    raise SystemExit(1)

counter = Counter()

with log_file.open("r") as f:
    for line in f:
        if "INFO" in line:
            counter["INFO"] += 1
        elif "WARNING" in line:
            counter["WARNING"] += 1
        elif "ERROR" in line:
            counter["ERROR"] += 1
        else:
            counter["OTHER"] += 1

report_lines = [
    "Log Summary Report",
    "==================",
    f"INFO: {counter['INFO']}",
    f"WARNING: {counter['WARNING']}",
    f"ERROR: {counter['ERROR']}",
    f"OTHER: {counter['OTHER']}",
]

report_text = "\n".join(report_lines)

print(report_text)
report_file.write_text(report_text)
print(f"\nReport written to {report_file}")