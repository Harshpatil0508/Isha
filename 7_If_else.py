age = int(input("Enter your age: "))

if age > 18:
    print("You are an adult.")
elif age == 18:
    print("You just became an adult.")
else:
    print("You are not an adult yet.")

x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(f"The number {x} is {result}.")

score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
else :
    grade = "D"

print(f"Your grade is: {grade}")


alphabet = input("Enter a alphabet : ").lower()
vowels = 'aeiou'
if alphabet in vowels:
    print(f"{alphabet} is a vowel.")
else:
    print(f"{alphabet} is a consonant.")

