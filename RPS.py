import random

def get_sys_ch():
    sys_ch = random.choice(['rock', 'paper', 'scissors'])
    return sys_ch


def get_Winner(user_ch , system_ch):
    if user_ch == system_ch:
        return "\nIt's a tie"
    elif (user_ch == 'rock' and system_ch == 'scissors') or (user_ch == 'scissors' and system_ch == 'paper') or (user_ch == 'paper' and system_ch == 'rock'):
        return "\nYou win"
    else:
        return "\nYou lose"
    
def playGame():
    while True:
        print("\n\tChoose rock , paper or scissors or e to exit\n")
        user_ch = input().lower()

        if user_ch == 'e':
            print("\n\tThank you for Playing....")
            break

        elif user_ch not in ['rock', 'paper', 'scissors']:
            print("\tInvalid input! Enter valid inpiut : ")
            continue

        system_ch = get_sys_ch()
        print("System chose : ", system_ch)

        result = get_Winner( user_ch , system_ch )
        print(result)

        ans = input("\n\tDo you want to play again ? \n").lower()
        if ans == 'n':
            print("\n\tThank you for Playing....")
            break 

if __name__ == "__main__":
    playGame()