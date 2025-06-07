from itertools import groupby

def main():
    # Sample data: a list of tuples (category, item)
    data = [
        ('fruit', 'apple'),
        ('fruit', 'banana'),
        ('vegetable', 'carrot'),
        ('fruit', 'date'),
        ('vegetable', 'eggplant'),
        ('fruit', 'fig'),
    ]

    # Sort the data by category before grouping
    data.sort(key=lambda x: x[0])

    # Group by the first element of each tuple (the category)
    grouped_data = groupby(data, key=lambda x: x[0])

    # Print the grouped data
    for category, items in grouped_data:
        print(f"{category}: {[item for _, item in items]}")

if __name__ == "__main__":
    main()
# This code demonstrates how to use itertools.groupby to group data by a specific key.