# Data Analytics with R
## 6.1 Basic Features and Environment

### R and RStudio Overview
R is a programming language specifically designed for statistical computing and data analysis. RStudio is an Integrated Development Environment (IDE) that makes working with R more efficient.

#### RGUI vs RStudio
- **RGUI**: Basic interface for R
  - Simple console window
  - Limited features
  - Basic script editor

- **RStudio**: Advanced IDE with multiple panels
  - Console panel
  - Script editor
  - Environment/History panel
  - Files/Plots/Packages/Help panel

### Basic R Operations

#### 1. Handling Basic Expressions
```r
# Arithmetic operations
5 + 3    # Addition: 8
10 - 4   # Subtraction: 6
4 * 3    # Multiplication: 12
15 / 3   # Division: 5
2 ^ 3    # Exponentiation: 8
17 %% 5  # Modulus: 2
```

#### 2. Variables in R
```r
# Variable assignment
age <- 25              # Using arrow operator
name = "John"          # Using equals sign
salary <- 50000.50

# Variable types
class(age)     # "numeric"
class(name)    # "character"
class(salary)  # "numeric"
```

#### 3. Working with Vectors
```r
# Creating vectors
numbers <- c(1, 2, 3, 4, 5)
fruits <- c("apple", "banana", "orange")

# Vector operations
numbers * 2          # Multiplies each element by 2
numbers + c(1, 1, 1, 1, 1)  # Element-wise addition

# Vector functions
mean(numbers)    # Calculate average
sum(numbers)     # Sum all elements
length(numbers)  # Count elements
```

#### 4. Creating and Using Objects
```r
# Creating a data frame
student_data <- data.frame(
  name = c("Alice", "Bob", "Charlie"),
  age = c(20, 22, 21),
  grade = c(85, 92, 78)
)

# Accessing data
student_data$name     # Access column
student_data[1, ]     # First row
student_data[, 2]     # Second column
```

#### 5. Interacting with Users
```r
# Getting user input
user_name <- readline("Enter your name: ")
user_age <- as.numeric(readline("Enter your age: "))

# Displaying output
cat("Hello,", user_name, "!\n")
print(paste("You are", user_age, "years old"))
```

#### 6. Basic Plotting
```r
# Simple plot
x <- 1:10
y <- x^2
plot(x, y, type = "l", main = "Square Function",
     xlab = "X", ylab = "Y")

# Adding points
points(x, y, col = "red", pch = 16)
```

## 6.2 Data Management in R

### Reading and Exporting Data
```r
# Reading CSV file
data <- read.csv("example.csv")

# Reading Excel file (requires readxl package)
library(readxl)
excel_data <- read_excel("example.xlsx")

# Exporting data
write.csv(data, "output.csv")
```

### Data Manipulation
```r
# Using dplyr for data manipulation
library(dplyr)

# Filter rows
filtered_data <- data %>%
  filter(age > 25)

# Select columns
selected_data <- data %>%
  select(name, age)

# Create new columns
modified_data <- data %>%
  mutate(age_group = ifelse(age < 30, "Young", "Senior"))
```

### Built-in Functions
```r
# Statistical functions
mean_value <- mean(data$age)
median_value <- median(data$age)
sd_value <- sd(data$age)

# Data structure functions
head(data)        # First 6 rows
summary(data)     # Statistical summary
str(data)         # Structure of data
```

## 6.3 Data Visualization

### Types of Visualizations

#### 1. Basic Plots
```r
# Histogram
hist(data$age, 
     main = "Age Distribution",
     xlab = "Age",
     col = "lightblue")

# Scatter Plot
plot(data$height, data$weight,
     main = "Height vs Weight",
     xlab = "Height",
     ylab = "Weight")
```

#### 2. Advanced Visualization with ggplot2
```r
library(ggplot2)

# Bar Chart
ggplot(data, aes(x = category, fill = category)) +
  geom_bar() +
  theme_minimal() +
  labs(title = "Category Distribution")

# Box Plot
ggplot(data, aes(x = group, y = value)) +
  geom_boxplot() +
  theme_minimal() +
  labs(title = "Value Distribution by Group")
```

### Applications of Data Visualization

1. **Exploratory Data Analysis (EDA)**
   - Understanding data distribution
   - Identifying patterns and trends
   - Detecting outliers

2. **Presentation and Reporting**
   - Creating professional plots for reports
   - Interactive visualizations for presentations
   - Dashboard creation

3. **Decision Making**
   - Visualizing key metrics
   - Comparing different scenarios
   - Tracking changes over time

### Best Practices for Visualization

1. Choose appropriate chart types for your data
2. Use clear labels and titles
3. Maintain consistent color schemes
4. Avoid cluttering the visualization
5. Include proper legends and annotations
6. Consider your audience when designing

### Accessing Help and Documentation
```r
# Getting help for a function
?mean
help(plot)

# Examples for a function
example(hist)

# Search help for a topic
help.search("correlation")
```
