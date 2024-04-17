# Write a Python function to check if two given strings ("listen", "silent") are anagrams of each
# other (i.e., they contain the same characters but may be in a different order).

def anagrams(st,stt):
    st=st.lower()
    stt=stt.lower()
    st=sorted(st)
    stt=sorted(stt)
    if st==stt:
        print("Anagrams")
    else:
        print("Not Anagrams")     
anagrams('listen','silent')
