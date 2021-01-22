def are_valid_groups(student_numbers: list, groups: list) -> bool:
    for student in student_numbers:
        if student not in groups:
            return False
    return True
