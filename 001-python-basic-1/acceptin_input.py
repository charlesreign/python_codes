# input() is used to accept user input
name = input("please enter your name ")
password = input("please enter your password ")

print(f"Hello {name} you password {('*' * len(password))} is of length {len(password)}")