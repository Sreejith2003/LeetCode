# a-z 

def calculate_distance(s: str) -> int:
    if len(s) <= 1:
        return 0
    return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))

# Taking user input
user_input = input("Enter a string: ")
print(f"Output: {calculate_distance(user_input)}")

# Time Complexity is : O(n)
# Space Complexity is : O(1)