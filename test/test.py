from termcolor import colored

def assertTest(result: bool) -> None:
    if result:
        print(colored("PASS", "green"))
    else:
        print(colored("FAIL", "red"))