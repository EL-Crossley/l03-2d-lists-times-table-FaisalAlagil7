# Put your function here
def timesTable(n):
    # Create a 2D list to hold the times table
    table = []
    
    # Generate the times table
    for i in range(1, n + 1):
        row = []  # Create a new row for each number
        for j in range(1, n + 1):
            row.append(i * j)  # Calculate the product and add it to the row
        table.append(row)  # Add the row to the table
    
    return table

# testing
nums = int(input())
print(timesTable(nums))
