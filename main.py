#New Comment for SlopeStrikeApp

print ('Greetings user. Prepare to SlopeStrike!')

score = 0
lives = 3
while lives > 0:

    # Generate and print two random points, a target, Txy, and a Launch location, Lxy
    import random
    Tx = random.randint(1, 10)
    Ty = random.randint(1, 10)
    print(f'Target lock at coordinates ({Tx},{Ty}).')
    Lx = random.randint(0, 0)
    Ly = random.randint(0, 0)
    print(f'Launcher location: ({Lx},{Ly}).')

    # Prompts user for two inputs to form a ratio
    mrise = int(input("Enter the appropriate rise:"))
    mrun = int(input("Enter the approriate run:"))
    print(f'You entered {mrise}/{mrun}.')

    # Verifies if the inputted slope forms a line that intersects the Launch and Target locations
    if (Ty) - (Ly) == ((Tx) - (Lx)) * (mrise) / (mrun):
        print(f'HIT!')
        score = score + 10
        print(f'Current Score: {score}')
    else:
        print(f'MISS!')
        lives = lives - 1
        print(f'Current Score: {score}')

print(f'Game Over. Final Score: {score}')