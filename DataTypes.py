#predifined variables
i = 4
d = 4.0
s = "HackerRank"


# step_1: read the input from the suer
# Read and convert the input for each type
input_integer = int(input())
input_double = float(input())
input_string = input()


#step_2: perform operations
# 1. add the input int to the predifined int "i"
sum_integers = i + input_integer

#2. add the input double to the predefined double 'd', rounded to 1 decimal place
sum_doubles = d + input_double

#3. concatenate the predefined str "s" witn the input str
concatenated_string = s + input_string


# ste_3: print the results
print(sum_integers)
print(f"{sum_doubles:.1f}")
print(concatenated_string)