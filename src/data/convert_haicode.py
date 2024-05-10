#これはnormal_xiangting,erase_one_xiangting(two,three)
#で使用してる入力手牌['m1','m1','m4','m7','p1','s2] -> "1147m12p"への変換

def convert_array_to_string(arr):
    # Dictionary to store numbers corresponding to each alphabet
    num_dict = {'m': [], 'p': [], 's': [], 'z': []}

    # Iterate over the array and populate the dictionary
    for item in arr:
        if item[0] in num_dict:
            num_dict[item[0]].append(item[1])

    # Create the string from the dictionary
    result = ''
    for key in ['m', 'p', 's', 'z']:
        if num_dict[key]:
            result += ''.join(num_dict[key]) + key

    return result

# Test the function with the provided array
test_array = ['m9','m9','p1','p4','p7','p8','p9','s1','s2','s3','s6','s6','z4','z5']
print(convert_array_to_string(test_array))
