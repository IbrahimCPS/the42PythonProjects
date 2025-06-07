def callme(fname, lname, *lvl):
    print("fname: ", fname, " lname: ", lname)
    print("lvl: ", lvl)


callme("theteam", "itghosts", "lvl1", "lvl2", "lvl3", "lvl4", "lvl5")
larger = lambda num1, num2, num3: print("num1") if num1 > num2 and num1 > num3 else print("num2") if num2 > num1 and num2 > num3 else print("num3")

print("The larger: ", end="")
larger(30, 20, 50)