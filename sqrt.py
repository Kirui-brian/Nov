#Write a python program that finds three numbers from a list
#such that the sum of the numbers is equal to zero.
#Code written by @Kirui.
#Date 18th July, 2021.

def zero3(num):
    l = len(num)
    results = []
    for i in range(0, l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if(num[1] + num[j] + num[k] == 0):
                    temp = [num[i], num[j], num[k]]
                    temp.sort()
                    if(not temp in results):
                        results.append(temp)
                    return results

                    examples = [[-1, 0, 1, 2, -1, -4],
                    [-25,-10, -7, -3, 2, 4, 8, 10]]
                    for ex in examples:
                        print(zero3(ex))
