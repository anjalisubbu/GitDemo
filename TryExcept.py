


try:
    with open ("filelog.txt") as reader:
        reader.read()

except Exception as e:
    print(e)

#finally:
    #print("Remove junk data")
