def is_valid(student, group, conflicts):
    """Check if a student can join the given group."""
    for member in group:
        if (student, member) in conflicts or (member, student) in conflicts:
            return False
    return True

def backtrack(students, groups, conflicts, index=0):
    """Backtracking function to assign students to valid groups."""
    if index == len(students):
        # All students successfully grouped
        return True  

    student = students[index]

    for group in groups:
        if len(group) < 3 and is_valid(student, group, conflicts):
            group.append(student)

            if backtrack(students, groups, conflicts, index + 1):
                return True  # Found a valid solution
            
            # Backtrack step — remove student and try the next option
            group.pop()

    return False  # No valid grouping found for this path

# Sample data
students = ['A', 'B', 'C', 'D', 'E', 'F']
conflicts = [('A', 'B'), ('C', 'D')]

# Initialize empty groups
groups = [[] for _ in range(len(students) // 3)]

# Run backtracking algorithm
if backtrack(students, groups, conflicts):
    print("Valid groups found:", groups)
else:
    print("No valid grouping possible.")
