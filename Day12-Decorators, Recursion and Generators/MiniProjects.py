#. MINI PROJECT 3 — BANK TOKEN MACHINE (GENERATOR)

def token_machine(prefix):
    number = 1
    while True:
        yield f"{prefix}-{number}"
        number += 1


def run_token_machine():
    tokens = token_machine("A")
    print("=== Bank Token Machine ===")

    while True:
        choice = input("Press Enter for a token (q to quit): ")
        if choice.lower() == "q":
            print("Bye!")
            break
        print("Your token:", next(tokens))      
run_token_machine()




