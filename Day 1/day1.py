with open("input.txt") as fp:
   lines_one = []
   lines_two = []
   line1 = int(fp.readline())
   line2 = int(fp.readline())
   line3 = int(fp.readline())
   line4 = int(fp.readline())

   lines_one = [line1, line2, line3]
   lines_two = [line2, line3, line4]

   line = int(fp.readline())
   num = 0
   while line:
      if sum(lines_two) > sum(lines_one):
         num += 1

      lines_one.pop(0)
      lines_one.append(lines_two[2])
      lines_two.pop(0)
      lines_two.append(line)

      line = fp.readline()

      if line != "":
         line = int(line)
      else:
         break

num += 1

print(num)