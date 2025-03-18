

def are_anagrams(s1,s2):


    a1="".join(sorted(s1))

    b2="".join(sorted(s2))

    if a1==b2:
        print("this is angram",s1,s2)
    else:
        print("this not a anagram",s1,s2)





are_anagrams("listen", "silent")  # Output: True
are_anagrams("hello", "world")
are_anagrams("hello","hey")