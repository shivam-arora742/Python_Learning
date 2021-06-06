#
# Example file for working with conditional statements
#


def main():
    x, y = 10,100
    # x, y = 1000,100
    # x, y = 100,100

    # conditional flow uses if, elif, else
    if(x>y):
        result="x Greater than  y "
    elif(x<y):
        result="y Greater than  x"
    else:
        result="x equals to y"
    print(result)
    # conditional statements let you use "a if C else b"
    str="x is greater than y" if(x>y) else "x is not greater than y"
    print(str)
if __name__ == "__main__":
    main()
