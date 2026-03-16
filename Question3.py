
def group_numbers(nums: list) -> dict:
    numbers_by_signs = {
        "positive": [] ,
        "negative": [],
        "zero": []
    }
    for num in nums:
        if num > 0:
            numbers_by_signs["positive"].append(num)
        elif num < 0:
            numbers_by_signs["negative"].append(num)
        else:
            numbers_by_signs["zero"].append(num)
    return numbers_by_signs

nums = [4, -2, 0, 7, -5, 3]
print(group_numbers(nums))

