lines_maxlenth = 0
line_numbers = 1
cc_in = open("demo.py","r").readlines()
cc_out = open("demo_new.py","w")
for i in cc_in:
    if(lines_maxlenth<len(i)):
        lines_maxlenth = len(i)
for i in cc_in:
    i = i.ljust(lines_maxlenth+1).replace('\n',' ') + "#" + str(line_numbers) + "\n"
    line_numbers += 1
    cc_out.write(i)                  