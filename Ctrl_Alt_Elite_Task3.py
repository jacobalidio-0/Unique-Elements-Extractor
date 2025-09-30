def get_unique_elements(input_list):
    # Initialize a set to keep track of seen elements (for fast lookup)
    seen = set()
    # Initialize a list to store unique elements in order of appearance
    unique_list = []

    # Iterate through each item in the input list
    for item in input_list:
        # If the item is a string and has more than one character
        if isinstance(item, str) and len(item) > 1:
            # Break the string into individual characters
            for char in item:
                # Add character to unique_list if it hasn't been seen before
                if char not in seen:
                    seen.add(char)
                    unique_list.append(char)
        else:
            # For non-strings or single-character strings, check if seen
            if item not in seen:
                seen.add(item)
                unique_list.append(item)

    # Return the list of unique elements

    return unique_list

