import json

with open('meanAndStdev.csv', 'r') as infile:
    lines = infile.readlines()

with open('sdal.json', 'w') as outfile:
    data = []
    outfile.writelines("{\n")

    for line in lines:
        word, pleasure, activation, imagination, p_sdev, a_sdev, i_sdev = line.split(";")
        pleasure = str(round((float(pleasure) - 2),4))
        activation = str(round((float(activation) - 2),4))
        imagination = str(round((float(imagination) - 2),4))
        word, obj = word.split("_")
        word = str(word.rstrip())+":"+str({"obj":obj.rstrip(), "pleasure": pleasure.rstrip(), "activation": activation.rstrip(),"imagination": imagination.rstrip(),"p_sdev": p_sdev.rstrip(),"a_sdev": a_sdev.rstrip(),"i_sdev": i_sdev.rstrip() })+",\n"
        outfile.writelines(word)
    outfile.writelines("\n}")
