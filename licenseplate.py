"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #9 - License Plate (licenseplate.py)


Author: Wonjun Lee

Difficulty Level: 5/10

Prompt: Jon was speeding on the highway with his RACECAR, and the highway camera has taken a picture 
of the RACECAR’s number plate. However, some characters on the plate are blurry. Please write a function 
that returns the number of possible combinations of the number plate. The number plate for his RACECAR
consists of 7 distinct characters, starting with 3 distinct alphabets and ending with 4 distinct numbers. 
The input will be passed as a string and any blurred characters will be written as ‘.’

Test Cases: 
Input: “ABC123.” ; Output: 7
Input: “.ON1123” ; Output: 24
Input: “.BC.234” ; Output: 168
"""

class Solution:
    def licensePlate(self,str):
        # type str: string
        # return: int
        
        # TODO: Write code below to return an int with the solution to the prompt
        blurry_letters = []
        blurry_numbers = []
        to_ret = 1
        letter_count = 0
        number_count = 0
        letters = str[:3]
        numbers = str[3:]
        for letter in letters:
            if letter == ".":
                letter_count += 1
        for number in numbers:
            if number == ".":
                number_count += 1
        for i in range(0, letter_count):
            blurry_letters.append(26 - (3 - letter_count) - (i))
        for i in range(0, number_count):
            blurry_numbers.append(10 - (4-number_count) - (i))
        if len(blurry_letters) == 0 and len(blurry_numbers) == 0:
            return 0
        else:
            for x in blurry_letters:
                to_ret *= x
            for x in blurry_numbers:
                to_ret *= x
            return to_ret

def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.licensePlate(string1)
    print(ans)

if __name__ == "__main__":
    main()