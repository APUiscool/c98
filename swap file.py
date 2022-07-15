def swapFileData():
  file1 = input("text1.docx")
  file2 = input("text2.docx")

  with open(filel, 'r') as a:
     data_a = a.read()
  with open(file2, 'r') as b:
     data_b = b.read()

  with open(filel, 'w+') as a:
     a.write(data_b)
  with open(file2, 'w+') as b: 
     b.write(data_a)

swapFileData()