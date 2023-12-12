def print_list_values(list):
    for item in list:
        print(item)

def add_to_list(list):
    list.append("the function added this")
    return list

def combine_list_elements(list):
    combined_string = ' '.join(list)
    return combined_string

fruit_list = ['apples', 'oranges', 'bananas']

# Step 1
print("Step 1:")
print_list_values(fruit_list)

# Step 2
print("\nStep 2:")
modified_list = add_to_list(fruit_list)
print(modified_list)

# Step 3
print("\nStep 3:")
combined_string = combine_list_elements(fruit_list)
print(combined_string)