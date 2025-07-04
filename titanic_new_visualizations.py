import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Titanic Dataset.xlsx", engine="openpyxl")

# Set seaborn style
sns.set(style="whitegrid")

# Pearson Correlation Heatmap
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5, ax=ax1)
ax1.set_title("Pearson Correlation Heatmap")

# Pairplot (Survived Hue)
pairplot_data = df.dropna(subset=["Age", "Fare", "Pclass", "Survived"])
sns.pairplot(pairplot_data, vars=["Age", "Fare", "Pclass"], hue="Survived")

# KDE Plot for Age
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.kdeplot(df["Age"].dropna(), shade=True, color="green", ax=ax3)
ax3.set_title("Age Distribution (KDE Plot)")
ax3.set_xlabel("Age")

# Boxplot of Age by Class
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.boxplot(x="Pclass", y="Age", data=df, ax=ax4)
ax4.set_title("Age Distribution by Passenger Class")

# Show all plots together
plt.show()
