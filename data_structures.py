import random

def find_max(numbers: list) -> int:
    for i in numbers:
        if i in numbers > 4:
         return i
print(find_max)

def find_min(numbers: list) -> int:
      """Find the smallest(minimum) number in a list of numbers"""
      for i in numbers:
          if i in numbers < 2:
    return i
print(find_min)

# #def find_average(numbers: list) -> int:
#     """Find the average of a list of numbers int the list 'numbers' and return 
#     it as a float to one decimal point"""
    

# #def find_even_pairs(numbers: list) -> int:
#     """Find the neigbouring pairs of numbers that sum up to an even number and 
#     then return a list of tuples with the pairs' index numbers 
#     ie: [1,3,5] returns [(0,1)]
#     """



def find_number_of_even_numbers(numbers: list) -> int:
     """Find the total number of even numbers in the list 'numbers' and return 
     the number as an integer"""
     for n in numbers:
         if n % 2 == 0:
            return n 
print(find_number_of_even_numbers)




# #def draw_square(height: int) -> None:
#     """
#      Draws a square pattern of asterisks (*) with the given height.

#     Parameters:
#         height (int): The height of the square. Must be a positive integer.

#     Returns:
#         None: Prints the square pattern directly to console.

#     """


# #def reverse_sentence(text):
#     """
#     Reverse sentence
#     """


# def reverse_word(text):
#     """
#     Reverse each word in a sentence
#     """

# # ------------------- First write tests and the make the functions below pass those tests -----------------------
# def fibonacci(n):

#     """
#     Find the nth fibonacci number 
#     """
#     pass

# def primes(n):
#     """
#     Find the nth prime number
#     """
#     pass

# def factorial(n):
#     """
#     Find the factorial of n
#     """
#     pass

def count_vowels(text):
   
    count = 0
    for i in text:
        if i in "aeiouAEIOU":
            count = count+1
    return count

print(count_vowels("amawethu has red lips"))

# if "__name__" == "__main__":
#     pass
