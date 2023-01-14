def romanToInt(s):
        # defines the dictionary to convert char to number
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        l = list(s)
        numbers = []
        count = 1
        sum = 0
        for n in l:
            # gets all the numbers in a list
            numbers.append(dic[n])
        for n in numbers:
            # evaluates if number needs to be subtracted
            if count < len(numbers):
                if n < numbers[count]:
                    sum -= n
                    count += 1
                else:
                    sum += n
                    count += 1
            else: 
                sum += n
        return sum

print(romanToInt("MMXXIII"))
