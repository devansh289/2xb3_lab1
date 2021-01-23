# Function to check if each student number is in a group.
# Arg student_numbers is a list of strings.
# Arg groups is a list of list of strings.

# Example1: are_valid_groups([1,5], [[1,2,3], [3,4,5]]) returns False
# Example1: are_valid_groups([1,3,2], [[1,2,3], [3,4,5]]) returns True

def are_valid_groups(student_numbers, groups):

    # Checks if each group length is 3 or 4.
    for group in groups:
        if not (2 < len(group) < 5):
            return False

    # Checks if student_numbers has duplicates
    if len(student_numbers) != len(set(student_numbers)):
        return False

    # Checks if there exists a group with all of the student numbers.
    for group in groups:
        return all(number in group for number in student_numbers)