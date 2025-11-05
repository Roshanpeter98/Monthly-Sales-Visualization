import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel("sales.xlsx")

print(data.head())

plt.figure(figsize=(10, 6))
plt.plot(data['Month'], data['Sales'], marker='o', color='b', label='Sales')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()
