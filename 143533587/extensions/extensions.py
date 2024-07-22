files = input("File name: ")
files = files.replace(" ","")
if files[-4:].lower() == ".jpg" or files[-5:].lower() == ".jpeg":
    print("image/jpeg")
elif files[-4:].lower() == ".gif":
    print("image/gif")
elif files[-4:].lower() == ".png":
    print("image/png")
elif files[-4:].lower() == ".pdf":
    print("application/pdf")
elif files[-4:].lower() == ".txt":
    print("text/plain")
elif files[-4:].lower() == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")