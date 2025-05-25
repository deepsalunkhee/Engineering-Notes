# Data Analytics with R - Comprehensive Course Notes

## 6.1 Exploring Basic Features of R

### Introduction to R
R is a powerful programming language and environment specifically designed for:
- Statistical computing
- Data manipulation
- Data analysis
- Graphical visualization

#### Why R?
- Open-source and free
- Large community support
- Extensive package ecosystem
- Powerful statistical capabilities
- Beautiful visualization options
- Integration with other tools

### R Development Environments

#### 1. RGUI (R Graphical User Interface)
```r
# Basic features of RGUI:
# - Simple console window
# - Basic script editor
# - Menu-driven interface
# - Package manager
```

Key Components:
- Console window for direct commands
- Script editor for saving code
- Graphics window for plots
- Package manager for extensions

#### 2. RStudio IDE
```r
# RStudio layout:
# - Top-left: Source Editor
# - Bottom-left: Console
# - Top-right: Environment/History
# - Bottom-right: Files/Plots/Packages/Help
```

Features:
1. Code completion
2. Syntax highlighting
3. Project management
4. Git integration
5. Package management
6. Interactive debugging

### Basic R Programming Elements

#### 1. Basic Expressions
```r
# Arithmetic Operations
10 + 5         # Addition: 15
20 - 8         # Subtraction: 12
4 * 6          # Multiplication: 24
15 / 3         # Division: 5
2 ^ 4          # Exponentiation: 16
17 %% 5        # Modulus: 2
7 %/% 3        # Integer Division: 2

# Logical Operations
TRUE & FALSE    # Logical AND: FALSE
TRUE | FALSE    # Logical OR: TRUE
!TRUE           # Logical NOT: FALSE

# Comparison Operations
5 > 3          # Greater than: TRUE
4 <= 4         # Less than or equal: TRUE
2 == 2         # Equal to: TRUE
3 != 4         # Not equal to: TRUE
```

#### 2. Variables in R
```r
# Variable Assignment
x <- 10                # Using arrow operator
y = "Hello"           # Using equals sign
z <- TRUE             # Boolean value

# Variable Naming Conventions
valid_name <- 1       # Use underscore
validName <- 2        # Use camelCase
.hidden <- 3          # Hidden variable
CONSTANT <- 4         # Convention for constants

# Variable Types
numeric_var <- 42.5   # Numeric
integer_var <- 42L    # Integer (note the L suffix)
character_var <- "R"  # Character
logical_var <- TRUE   # Logical
complex_var <- 3+2i   # Complex

# Checking Variable Types
class(numeric_var)    # "numeric"
typeof(integer_var)   # "integer"
str(character_var)    # chr "R"
```

#### 3. Working with Vectors
```r
# Creating Vectors
numbers <- c(1, 2, 3, 4, 5)
names <- c("John", "Jane", "Bob")
mixed <- c(1, "A", TRUE)  # Coerces to character

# Vector Operations
numbers * 2               # Multiply each element by 2
numbers + c(1, 1, 1, 1, 1) # Element-wise addition
numbers[numbers > 3]      # Conditional filtering

# Vector Functions
length(numbers)          # Length: 5
sum(numbers)            # Sum: 15
mean(numbers)           # Mean: 3
median(numbers)         # Median: 3
sd(numbers)             # Standard deviation

# Vector Indexing
numbers[1]              # First element
numbers[c(1,3,5)]      # Multiple elements
numbers[-2]            # All except second element
```

#### 4. Storing and Calculating Values
```r
# Basic Calculations
result <- (10 + 5) * 2
sqrt_value <- sqrt(16)
log_value <- log(10)

# Statistical Calculations
data <- c(15, 18, 22, 19, 21)
mean_value <- mean(data)
max_value <- max(data)
min_value <- min(data)
range_value <- range(data)

# Using Built-in Constants
pi_value <- pi
e_value <- exp(1)

# Rounding Functions
round_value <- round(3.14159, 2)
ceiling_value <- ceiling(3.14)
floor_value <- floor(3.14)
```

#### 5. Creating and Using Objects
```r
# Lists
my_list <- list(
  numbers = c(1, 2, 3),
  text = "Hello",
  logical = TRUE
)

# Data Frames
students <- data.frame(
  name = c("Alice", "Bob", "Charlie"),
  age = c(20, 22, 21),
  grade = c(85, 92, 78),
  stringsAsFactors = FALSE
)

# Matrices
my_matrix <- matrix(
  1:9,
  nrow = 3,
  ncol = 3,
  byrow = TRUE
)

# Factors
gender <- factor(c("M", "F", "F", "M"))
```

#### 6. Interacting with Users
```r
# Basic Input
name <- readline("Enter your name: ")
age <- as.numeric(readline("Enter your age: "))

# Conditional Messages
if (age >= 18) {
  message <- "You are an adult"
} else {
  message <- "You are a minor"
}

# Print Functions
print(paste("Hello,", name))
cat("Your age is:", age, "\n")
message(message)

# Warning and Error Messages
if (age < 0) {
  warning("Age cannot be negative")
}
if (is.na(age)) {
  stop("Invalid age entered")
}
```

#### 7. Handling Data in R Workspace
```r
# Workspace Management
ls()                # List objects
rm(x)               # Remove object 'x'
rm(list = ls())     # Clear workspace

# Save and Load Workspace
save.image("workspace.RData")    # Save all objects
save(x, y, file = "data.RData")  # Save specific objects
load("workspace.RData")          # Load workspace

# Object Information
objects()           # List all objects
memory.size()       # Memory usage
object.size(x)      # Size of object 'x'
```

### 8. Creating Basic Plots
```r
# Simple Line Plot
x <- 1:10
y <- x^2
plot(x, y, type = "l",
     main = "Square Function",
     xlab = "X axis",
     ylab = "Y axis")

# Scatter Plot
plot(mtcars$wt, mtcars$mpg,
     main = "Weight vs MPG",
     xlab = "Weight",
     ylab = "Miles per Gallon",
     pch = 16)

# Histogram
hist(mtcars$mpg,
     main = "MPG Distribution",
     xlab = "Miles per Gallon",
     col = "lightblue",
     breaks = 10)

# Box Plot
boxplot(mpg ~ cyl, data = mtcars,
        main = "MPG by Cylinder",
        xlab = "Cylinders",
        ylab = "Miles per Gallon")
```

## 6.2 Advanced Data Operations

### Reading and Exporting Data
```r
# Reading Different File Types
csv_data <- read.csv("file.csv")
txt_data <- read.table("file.txt", header = TRUE)
excel_data <- readxl::read_excel("file.xlsx")

# Reading with Options
data <- read.csv("file.csv",
                 header = TRUE,
                 sep = ",",
                 stringsAsFactors = FALSE,
                 na.strings = c("NA", ""))

# Exporting Data
write.csv(data, "output.csv")
write.table(data, "output.txt")
saveRDS(data, "data.rds")
```

### Data Manipulation
```r
library(dplyr)

# Basic Operations
filtered <- mtcars %>%
  filter(mpg > 20) %>%
  select(mpg, wt, cyl) %>%
  arrange(desc(mpg))

# Creating New Variables
modified <- mtcars %>%
  mutate(
    weight_kg = wt * 453.592,
    efficiency = mpg/wt
  )

# Grouping and Summarizing
summary_stats <- mtcars %>%
  group_by(cyl) %>%
  summarise(
    avg_mpg = mean(mpg),
    sd_mpg = sd(mpg),
    count = n()
  )
```

### Built-in Functions
```r
# Statistical Functions
mean(mtcars$mpg)
median(mtcars$mpg)
var(mtcars$mpg)
sd(mtcars$mpg)
cor(mtcars$mpg, mtcars$wt)

# Data Structure Functions
head(mtcars)
tail(mtcars)
str(mtcars)
summary(mtcars)

# Applied Statistics
t.test(mtcars$mpg, mu = 20)
lm(mpg ~ wt, data = mtcars)
```

## 6.3 Data Visualization

### Basic Visualization Types
```r
# Base R Graphics
plot(pressure)
hist(rivers)
boxplot(OrchardSprays)
pie(rep(1, 24), col = rainbow(24))

# Advanced ggplot2 Graphics
library(ggplot2)

# Scatter Plot
ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  theme_minimal() +
  labs(title = "Weight vs MPG",
       x = "Weight (1000 lbs)",
       y = "Miles per Gallon")

# Bar Plot
ggplot(mtcars, aes(x = factor(cyl))) +
  geom_bar(fill = "steelblue") +
  theme_light() +
  labs(title = "Count of Cars by Cylinders",
       x = "Number of Cylinders",
       y = "Count")
```

### Advanced Visualization Applications
```r
# Time Series Plot
library(forecast)
data(AirPassengers)
autoplot(AirPassengers) +
  theme_minimal() +
  labs(title = "Air Passengers Over Time")

# Interactive Plot with plotly
library(plotly)
p <- plot_ly(mtcars, x = ~wt, y = ~mpg, 
             type = "scatter", mode = "markers")

# Faceted Plot
ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  facet_wrap(~cyl) +
  theme_bw() +
  labs(title = "Weight vs MPG by Cylinders")
```

### Documentation and Help
```r
# Accessing Help
?mean           # Help for mean function
help("plot")    # Help for plot function
example(lm)     # Examples of linear regression
help.search("correlation")  # Search help files

# Package Documentation
vignette("dplyr")    # dplyr package guide
browseVignettes()    # All available vignettes
```

### Best Practices
1. Code Organization
   - Use clear variable names
   - Comment your code
   - Break complex operations into steps
   - Use consistent formatting

2. Data Management
   - Always check data structure
   - Handle missing values explicitly
   - Document data transformations
   - Keep raw data separate from processed data

3. Visualization
   - Choose appropriate chart types
   - Use clear labels and titles
   - Consider color-blind friendly palettes
   - Include legends when necessary
