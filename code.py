def are_valid_groups(student_numbers, groups):
    for group in groups:
        return all(number in group for number in student_numbers)
