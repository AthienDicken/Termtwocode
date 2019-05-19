# Write the function between the START and END tags
# START

def IsPalindrome(tests):
 start = 1 #States which variable it starts at
 end = len(tests)-1
 while start < end:
    if tests[start] != tests[end]:
      return True
    start +=1
    end -=1
    return False
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))