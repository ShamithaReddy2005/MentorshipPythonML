# Write a python program that takes a list of numbers and returns their sum.
def sum_of_numbers(num_list):
    total_sum = 0
    for num in num_list:
        total_sum += num
    return total_sum

# Example usage:
numbers = [1, 2, 3, 4, 5]
print(f"The sum of numbers {numbers} is: {sum_of_numbers(numbers)}")

numbers2 = [10, 20, 30]
print(f"The sum of numbers {numbers2} is: {sum_of_numbers(numbers2)}")
