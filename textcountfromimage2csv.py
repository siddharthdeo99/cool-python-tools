import csv
from collections import Counter
import pytesseract
from PIL import Image

# Load image
img = Image.open('example.png')

# Extract text using Pytesseract
text = pytesseract.image_to_string(img)

# Split text into individual words
words = text.split()

# Count occurrences of each word
word_counts = Counter(words)

# Save results to CSV file
with open('results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Word', 'Count'])
    for word, count in word_counts.items():
        writer.writerow([word, count])
