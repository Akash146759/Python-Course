
def add_numbers(num1, num2):
  sum_of_numbers = num1 + num2
  return sum_of_numbers

def sub_numbers(num1, num2):
  diff_of_numbers = num1 - num2
  return diff_of_numbers

number1 = int(input('enter first number'))
number2 = int(input('enter second number'))

result_add = add_numbers(number1, number2)
result_diff = sub_numbers(number1, number2)

print(f"The sum of {number1} and {number2} is: {result_add}") 
print(f"The diff of {number1} and {number2} is: {result_diff}") 