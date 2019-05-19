# Write the function between the START and END tags
# START
def SortWordsAlphabetically(tests):
        jo = "-"  #To put the "-" back in later
        tests = tests.lower()
        word = tests.split("-")
        tests = word.sort()
        tests = jo.join(word)
        return tests



# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))