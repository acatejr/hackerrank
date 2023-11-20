def count_substring(string, sub_string):
    count = 0
    if (1 <= len(string) <= 200):
        for i in range(0, len(string)):
            if string[i:i+len(sub_string)] == sub_string:
                count += 1
                # print(i, len(sub_string), string, string[i:i+len(sub_string)])
        return count
    else:
        return

if __name__ == '__main__':
    string = "ABCDCDC" # input().strip()
    sub_string = "CDC" # input().strip()

    count = count_substring(string, sub_string)
    print(count)