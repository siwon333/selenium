import matplotlib.pyplot as plt

# Define your data as two lists, one for the years and one for the scores
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
scores = [75, 80, 85, 90, 95, 70, 65, 60, 55, 50, 45]

# Plot the data using the plot() function, with different styles for the data before and after a reference year
plt.plot(years[:6], scores[:6], 'b-o', label='Before 2016')
plt.plot(years[6:], scores[6:], 'r--s', label='After 2016')

# Add labels for the x and y axes
plt.xlabel('Year')
plt.ylabel('Score')

# Add a legend to the plot to distinguish between the two lines
plt.legend()

# Add an annotation to highlight the reference year
plt.annotate(xy=(2016, 90), text='Reference Year', ha='center', va='bottom', color='purple', fontsize=10)

# Show the plot
plt.show()