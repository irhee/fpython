#Dec2017

def main():
    file = open("SandP_Swap.txt","r")
    lines = file.readlines()

    writer = open("writer.txt","w")
    for line in lines:
        if 'K' in line:
            line = line.replace('K','')
            line = float(line) * 1000
        elif 'M' in line:
            line = line.replace('M','')
            line = float(line) * 1000000
        
        line = int(line)
        writer.write(str(line))
        writer.write('\n')

    file.close()
    writer.close()

    
main()
