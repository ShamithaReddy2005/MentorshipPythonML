def are_anagrams(str1, str2):
    # Clean the strings by removing spaces and converting to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the lengths are different
    if len(str1) != len(str2):
        return False
    
    # Sort the strings and compare
    return sorted(str1) == sorted(str2)
