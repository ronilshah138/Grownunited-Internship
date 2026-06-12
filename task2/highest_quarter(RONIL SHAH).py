from pathlib import Path
import numpy as np

path = Path(__file__).parent / "sales.txt"
if not path.exists():
	print("sales.txt not found at", path)
	raise SystemExit(1)

sales = np.loadtxt(path)

q1 = sales[0:3].sum()
q2 = sales[3:6].sum()
q3 = sales[6:9].sum()
q4 = sales[9:12].sum()

quarters = np.array([q1, q2, q3, q4])

highest_sales = quarters.max()
highest_quarter = int(quarters.argmax()) + 1

print("Quarter with Highest Sales:", highest_quarter)
print("Sales:", f"{highest_sales:.2f}")
