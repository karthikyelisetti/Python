def contains(big_string, little_string):
  if little_string in big_string:
    return True
  else:
    return False

print(contains("watermelon", "berry"))

def common_letters(string_one, string_two):
  lst = []
  for str1 in string_one:
    for str2 in string_two:
      if str2 == str1 and str2 not in lst:
        lst.append(str1)
  
  return lst

print(common_letters("banana", "cream"))