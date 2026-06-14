# BCP 210: Data Structures and Algorithms I
# Coursework Assignment 1: Arrays - Starter Template

def most_frequent(arr):
    """
    1. Most Frequent Registrant (8 Marks)
    Find and return the student ID (integer) that appears the most times in the array.
    """
    # TODO: Implement your solution here
    pass

def remove_duplicates(arr):
    """
    2. Ordered Deduplication (10 Marks)
    Remove duplicate student IDs from the array while preserving the order of first appearance.
    Return the deduplicated list.
    """
    # TODO: Implement your solution here
    pass

def first_non_repeated(arr):
    """
    3. First Unique Student (9 Marks)
    Find and return the first student ID in the list that appears exactly once.
    Return None if no such student exists.
    """
    # TODO: Implement your solution here
    pass

def has_target_sum(arr, target):
    """
    4. Contiguous Subarray Sum (10 Marks)
    Determine whether there exists a contiguous subarray whose sum equals the target value.
    Return True if it exists, otherwise False.
    """
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    # Test dataset from background context
    registrations = [1023, 1050, 1023, 1102, 1050, 1023, 1201, 1102, 1300, 1023]
    
    print("--- Testing Assignment 1: Arrays ---")
    print(f"Dataset: {registrations}")
    
    # 1. Test Most Frequent
    print(f"Most frequent student: {most_frequent(registrations)}")
    
    # 2. Test Deduplication
    print(f"Unique registrations: {remove_duplicates(registrations)}")
    
    # 3. Test First Non-Repeated
    print(f"First non-repeated student: {first_non_repeated(registrations)}")
    
    # 4. Test Subarray Sum
    target_sum = 2303 # Example target (1102 + 1201)
    print(f"Subarray with target sum {target_sum} exists: {has_target_sum(registrations, target_sum)}")
