try:
    f = open("testFile",mode = "r")
    f.write("writing a  line here")
except:
    print("hey you have an error")
finally:
    print("executed!")
