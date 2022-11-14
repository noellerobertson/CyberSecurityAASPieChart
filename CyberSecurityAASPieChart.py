# CyberSecurityAASPieChart.py
# A program that outputs the credits in progress, completed, and unfulfilled in a pie chart.
# Based on my current progress in the PTCC Cyber Security AAS as of Fall 2022.
# By: Noelle Robertson

# Import matplotlib.
import matplotlib.pyplot as plt

# The numbers of credits in progress, completed and unfulfilled.
in_progress = 14
completed = 10
unfulfilled = 36

# Visual components: pie chart colors and labels.
labels = ['In Progress', 'Completed', 'Unfulfilled']
colors = ['#c500ff', '#47e7ff', '#ff00af']

# Build the pie chart and display it.
plt.pie([in_progress, completed, unfulfilled], labels=labels, colors=colors, autopct='%.0f %%', shadow=True)

plt.title('PTCC Cyber Security AAS Progress: Fall 2022')

plt.show()
