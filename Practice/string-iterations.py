def letter_check(word, letter):
  counter = 0
  for chk in word:
    if letter == chk:
      counter += 1
  
  if counter > 0:
    return True
  else:
    return False

print(letter_check("codeacademy", "c"))
