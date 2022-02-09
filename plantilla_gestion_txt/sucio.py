

array_comandos = ["no cdp run \n", "no service tcp-small-servers \n", "no ip name-server \n"]

string = ""

for x in array_comandos:

    string = string + x

print(string)