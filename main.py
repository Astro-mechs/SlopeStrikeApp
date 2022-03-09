# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print ('Greetings user. Prepare to SlopeStrike!')

import random
Tx = random.randint(-10, 10)
Ty = random.randint(-10, 10)
print(f'Target lock at coordinates ({Tx},{Ty}).')
Lx = random.randint(0, 0)
Ly = random.randint(0, 0)
print(f'Launcher location: ({Lx},{Ly}).')
mrise = int(input("Enter the appropriate rise:"))
mrun = int(input("Enter the approriate run:"))
print(f'You entered {mrise}/{mrun}.')
if (Ty) == (Tx) * (mrise) / (mrun):
    print(f'HIT!')
else:
    print(f'MISS!')
