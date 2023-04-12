#https://www.codewars.com/kata/56676e8fabd2d1ff3000000c
def find_needle(haystack):
    # print(len(haystack))
    # needle = "needle"
    # i = 0
    # index = 0
    # for item in haystack:
    #     if item == needle:
    #         index = i
    #     i += 1
    # print(index)
    return(f'found the needle at position {haystack.index("needle")}')

print(find_needle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago']))