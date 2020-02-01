import shutil

for i in range(10):
    dst = "img" + str(i) + ".png"
    shutil.copy("image.png", dst)
