Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def find_greatest_number(numbers):
...     if not numbers:
...         return None  # Return None if the list is empty
...     greatest = numbers[0]
...     for num in numbers[1:]:
...         if num > greatest:
...             greatest = num
...     return greatest
... 
... # Example usage
... number_list = [10, 45, 32, 67, 100, 21]
... greatest_number = find_greatest_number(number_list)
... 
