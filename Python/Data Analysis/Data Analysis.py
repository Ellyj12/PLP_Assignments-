
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

try:
    # Load Iris dataset directly from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to pandas DataFrame
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))  # add species names

    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Check structure (data types + missing values)
    print("\nDataset info:")
    print(df.info())

    print("\nMissing values per column:")
    print(df.isnull().sum())


    df = df.dropna()  # drop missing rows if any

except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print("An error occurred while loading the dataset:", str(e))

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Grouping by species and taking mean
group_means = df.groupby("species").mean(numeric_only=True)
print("\nMean values per species:")
print(group_means)

# Interesting findings
print("\nObservations:")
print("- Setosa tends to have the smallest sepal and petal measurements.")
print("- Virginica generally has the largest petals.")
print("- Versicolor lies between Setosa and Virginica in most measurements.")



sns.set(style="whitegrid")

# 1. Bar Chart (average petal length per species)
plt.figure(figsize=(7,5))
sns.barplot(x="species", y="petal length (cm)", data=df, estimator="mean")
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 2. Histogram (distribution of sepal width)
plt.figure(figsize=(7,5))
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title("Histogram: Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 3. Scatter Plot (sepal length vs. petal length)
plt.figure(figsize=(7,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="deep")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()