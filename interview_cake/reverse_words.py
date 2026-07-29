import math

def reverse_words():
    # message = [ 'c', 'a', 'k', 'e', ' ',
    #     'p', 'o', 'u', 'n', 'd', ' ',
    #     's', 't', 'e', 'a', 'l' ]
    
    message = [ 't', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ',
  'h', 'a', 's', ' ', 'l', 'a', 'n', 'd', 'e', 'd' ]
    indices_map = {}
    count = 0
    for i in range(len(message)):
        if i == 0:
            indices_map[f"word{count}_start"] = 0
        if message[i] == " ":
            indices_map[f"word{count}_end"] = i - 1
            count += 1
            indices_map[f"word{count}_start"] = i + 1
        if i == len(message) - 1:
            indices_map[f"word{count}_end"] = i
    for i in range(count, -1, -1):
        start = indices_map[f"word{i}_start"]
        end = indices_map[f"word{i}_end"]
        times = math.ceil((end - start)/2)
        for time in range(times):
            tmp_start = message[start]
            tmp_end = message[end]
            message[start] = tmp_end
            message[end] = tmp_start
            start += 1
            end -= 1

    left_index = 0
    right_index = len(message) - 1

    while left_index < right_index:
        message[left_index], message[right_index] = message[right_index], message[left_index]
    
        left_index += 1
        right_index -= 1

    return message

if __name__ == "__main__":
    results = reverse_words()
    print(results)