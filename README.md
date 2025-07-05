# 📊 Titanic Dataset Visual Insights — Seaborn & Matplotlib Edition

## 🚀 Overview
This project explores the Titanic dataset through elegant, statistical visualizations using `Seaborn` and `Matplotlib`.  

The script `titanic_new_visualizations.py` produces insightful plots that reveal survival trends, class distributions, and age analytics.



## 📎 Script Reference
**Filename**: `titanic_new_visualizations.py`

## Libraries used:
- `pandas` 🐼
- `matplotlib` 📐
- `seaborn` 🌊

##Data source: 

`Titanic Dataset.xlsx` (loaded with `openpyxl` engine)

---

## 🖼️ Screenshots & Output

 Snapshots (`outputs/` folder)
Visualizations appear in order as:

#### 🧪 1. Pearson Correlation Heatmap
![Pearson Heatmap](outputs/Screenshot%20(351).png)
  
#### 🌈 2. Pairplot – Age, Fare, Class vs Survived
![Pairplot](outputs/Screenshot%20(352).png)

#### 📊 3. KDE Plot – Age Distribution
![KDE Plot](outputs/Screenshot%20(353).png)

#### 📦4. Boxplot – Age by Passenger Class
![Boxplot](outputs/Screenshot%20(354).png)  

---

## 🔍 Key Visuals

### 🔹 1. Pearson Correlation Heatmap
```python
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5)
```

🔹 2. Pairplot Colored by Survival Status
```python sns.pairplot(df.dropna(subset=["Age", "Fare", "Pclass", "Survived"]),
vars=["Age", "Fare", "Pclass"], hue="Survived")
```

🔹 3. KDE Plot — Age Distribution
```python
sns.kdeplot(df["Age"].dropna(), shade=True, color="green")
```

🔹 4. Boxplot — Age by Class
```python
sns.boxplot(x="Pclass", y="Age", data=df)
```


## 📦 Installation & Usage
💻 Dependencies
```bash
pip install pandas matplotlib seaborn openpyxl
```

## ▶️ Run Script

```bash
python titanic_new_visualizations.py
```

All visualizations will render consecutively for review or screenshot capture.

## 📜 License

This project is licensed under the MIT License. ©️
Feel free to fork, adapt, and share with credit to the author.

## 🙋‍♂️ Author

Gyanankur Baruah

@Gyanankur23

## 🔗 GitHub: 
```bash
github.com/Gyanankur23
```

📌 Proudly representing Thakur Shyamnarayan Degree College, Mumbai University

For collaboration, feedback, or to showcase your build using this template—reach out anytime!
