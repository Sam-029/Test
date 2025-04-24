'''
using simple logic fist sorted character & digits and than combining in sorted order
'''
def sort_letters_digits(i):
    letters = sorted([ch for ch in i if ch.isalpha()])
    digits = sorted([ch for ch in i if ch.isdigit()])
    return ''.join(letters + digits)

input = "B4A1D3"
print(sort_letters_digits(input)) 