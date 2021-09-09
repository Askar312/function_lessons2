a = input("")
def open_file(a):
    with open(f"{a}.py", 'w') as f:
        f.write(a)
open_file(a)
