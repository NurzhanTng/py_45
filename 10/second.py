import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('10/Final_CFD2023.xlsx', sheet_name='файнал')

labels = "Сдали Пересдача Провалили".split()
scores_with_bonus = [len(df[df["Final"] >= 20]), len(df[(df["Final"] >= 10) & (df["Final"] < 20)]), len(df[df["Final"] < 10])]
scores_no_bonus = [len(df[df["Total"] >= 20]), len(df[(df["Total"] >= 10) & (df["Total"] < 20)]), len(df[df["Total"] < 10])]
print(scores_with_bonus)

fig, ax = plt.subplots(1, 2)

ax[0].pie(x=scores_no_bonus, labels=labels, autopct='%1.1f%%')
ax[0].set_title("без дополнительных баллов")

ax[1].pie(x=scores_with_bonus, labels=labels, autopct='%1.1f%%')
ax[1].set_title("с дополнительными баллами")

plt.tight_layout()
plt.show()