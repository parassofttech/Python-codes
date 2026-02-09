with open("data.txt","r+") as file1:
    lines = file1.readLines()
    lines[0]= lines[0].replace("Amit","Amit Kumar")

    file1.seek(0)
    file1.writelines(lines)