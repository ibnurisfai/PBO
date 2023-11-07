file1= open("umc.txt", "r")
teks="Latihan Python\n"

file2=open("umc.txt", "a")
file2.write(teks)
file2.close()

read_content=file1.read()
print(read_content)

file1.close()