def lcd(a, b):
    big, sml = max(a, b), min(a, b)
    while big and sml:
        big, sml = sml, big % sml
    return a//big, b//big

if __name__ == "__main__":
    a, b = map(int, input().split(':'))
    print(':'.join(map(str, lcd(a, b))))