import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

income = np.array([1000, 1200, 1100, 1300, 1400, 1500, 1600, 1700, 1800, 1900])

income_without_tax = income * 0.7

expenses = np.array([200, 350, 270, 380, 450, 430, 250, 900, 530, 600])

data = {
    'Income Without Tax': income_without_tax,
    'Expenses': expenses
}
df = pd.DataFrame(data)

savings = income_without_tax - expenses
df['Savings'] = savings

print("Complete DataFrame:")
print(df)

print("1st Quarter Data:")
print(df.iloc[:3])

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), income, marker='o', color='blue', label='Income')
plt.title('Income by Month')
plt.xlabel('Month')
plt.ylabel('Income')
plt.xticks(range(1, 11), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'])
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(range(1, 11), savings, color='green')
plt.title('Savings by Month')
plt.xlabel('Month')
plt.ylabel('Savings')
plt.xticks(range(1, 11), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'])
plt.grid()
plt.show()

total_savings = np.sum(savings)
plt.figure(figsize=(8, 8))
plt.pie(savings, labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Savings Distribution by Month')
plt.axis('equal') 
plt.show()

quarters = {
    "Quarter 1": income[:3],
    "Quarter 2": income[3:6],
    "Quarter 3": income[6:9],
    "Quarter 4": income[9:10]  # Only one month in the last quarter
}

average_incomes = {quarter: statistics.mean(income) for quarter, income in quarters.items()}

print("Average Income for each Quarter:")
for quarter, avg_income in average_incomes.items():
    print(f"{quarter}: {avg_income}")