#Rizwan's code
# def are_valid_groups(student_no, groups):
# 	return student_no in groups

def are_valid_groups(student_numbers, groups):
    for group in groups:
        print("I shall break your code :)")
        return all(number in group for number in student_numbers)

Devansh is a big boy now.