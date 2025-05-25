import matplotlib.pyplot as plt  # importing the required libraries
from wordcloud import WordCloud


# Sample text data
text = "Python is a high-level programming language that is widely used for web development, data analysis, machine learning, artificial intelligence, and scientific computing. It was created by Guido van Rossum and first released in 1991. Python is known for its simplicity and ease of use, which has made it a popular choice for beginners and experienced programmers alike. Python is an interpreted language, which means that it is executed line by line, rather than being compiled before execution. This makes it a flexible and dynamic language, as changes can be made to the code on the fly. Python is also cross-platform, which means that it can be used on a wide range of operating systems, including Windows, Mac OS, and Linux. Python has a large and active community of developers, who have created a vast array of libraries and tools for the language. These libraries can be easily installed using Python's package manager, pip, and they provide additional functionality for tasks such as web scraping, data visualization, and machine learning. One of the most popular web frameworks for Python is Django, which provides a powerful and flexible platform for building web applications. Flask is another popular web framework for Python, which is lightweight and easy to use. Python is also widely used for scientific computing and data analysis, thanks to its libraries such as NumPy, Pandas, and SciPy. These libraries provide powerful tools for manipulating and analyzing data, and they are widely used in fields such as finance, economics, and biology."

# Generate word cloud with specified settings
wordcloud = WordCloud(width=800, height=800,
                      background_color='white', min_font_size=5).generate(text)

# Plot word cloud using matplotlib
# create a figure with specified size and facecolor
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)  # display the word cloud image
plt.axis("off")  # turn off the axis display
plt.tight_layout(pad=0)  # adjust the padding for the layout

plt.show()  # display the plot

# matplotlib.pyplot is a collection of functions that enable creating a variety of charts and plots in Python.

# wordcloud is a library that is specifically designed for generating word clouds, which are visual representations of text data where the size of each word is proportional to its frequency in the text.

# The code defines a string variable named text that contains sample text data about Python. This text data is used to generate a word cloud.

# The WordCloud object is created by passing in several parameters, including the width and height of the image, the background color, and the minimum font size. The generate method is called on the WordCloud object with the text variable as its argument. This generates the actual word cloud.