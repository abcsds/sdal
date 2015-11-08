import json

with open('meanAndStdev.csv', 'r') as infile:
    lines = infile.readlines()

with open('sdal.json', 'w') as outfile:
    data = []
    outfile.writelines("{\n")

    for line in lines:
        word, pleasure, activation, imagination, p_sdev, a_sdev, i_sdev = line.split(";")
        pleasure = str(float(pleasure) - 2)
        activation = str(float(activation) - 2)
        imagination = str(float(imagination) - 2)
        word, obj = word.split("_")
        word = str(word.rstrip())+":\n    "+str({"obj":obj.rstrip(), "pleasure": pleasure.rstrip(), "activation": activation.rstrip(),"imagination": imagination.rstrip(),"p_sdev": p_sdev.rstrip(),"a_sdev": a_sdev.rstrip(),"i_sdev": i_sdev.rstrip() })+",\n"
        outfile.writelines(word)

    # json.dump(data, outfile)
    outfile.writelines("\n}")
# and write everything back
#
