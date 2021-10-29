python = "python"
print("A python szó 1. karaktere:", python[0])
print("A python szó 5. karaktere:", python[5])
print("A python szó 5. karaktere:", python[-1])
print("A python szó 1. karaktere:", python[len(python)-1])

print("A python változóm 5-ször egymás után:", python * 5)

str2 = "hallgató"
str3 = "hiába a hegynyi anyag, a hallgató gyorsan halad"
print(str2 in str3)
print(python in str3)
print(python not in str3)
print(str3[0:5])
print(python + str2 + str3)
print(python, str2, str3)
str4 = "HALLGATÓ"
print(str4 in str3)