import modtest
from itsghosts.modtest import ValidateMe

print("+++++++++\n+Welcome+\n+++++++++\n")
name = input("Enter your name: ")

who0 = ValidateMe("IbrahimCPS")
who1 = ValidateMe("Ibrahim")
who2 = ValidateMe("CPS")
who3 = ValidateMe("Khan")

print("========= 00 =========")
who0.saymyname()
who0.doyouknowme()
print("========= 01 =========")
who1.saymyname()
who1.doyouknowme()
print("========= 02 =========")
who2.saymyname()
who2.doyouknowme()
print("========= 03 =========")
who3.saymyname()
who3.doyouknowme()
print("========= test =========")
