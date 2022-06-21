def compress(str1):
  res = ''
  count = 1
   
  for i in range(1, len(str1)):
    if str1[i - 1] == str1[i]:
       count += 1
    else:
      if count > 1:
         res += str(count)
      res = res + str1[i - 1]
      count = 1
  if count > 1:
   res += str(count)
  res = res + str1[-1]

print(compress('ABBCCCDEEEEA'))
# exprect output: A2B3CD4EA

