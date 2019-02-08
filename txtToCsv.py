import csv

 #设置文件路径
# txtDir = "C://Users//larid//Desktop//Study//NLP//语料//八大类语料，各1500篇//财经//"

txtDir = "C://Users//larid//Desktop//Study//NLP//语料//八大类语料，各1500篇//教育//"

csvName = "education_text_500" + ".csv"
#文件的起始与终结名，具体结合语料
start = 285461
end = 285959
i = 0
with open(csvName, 'a+', newline='', encoding="utf-8") as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    for j in range(start,end):
        filename = str(j)+".txt"
        file_desc = "".join([txtDir, filename])
        # 读要转换的txt文件
        with open(file_desc, 'r',encoding='utf-8') as filein:
            for line in filein:
                line_list =  line.strip('\n').split('\t')
                writeLine = [i,line_list[0]]
                spamwriter.writerow(writeLine)
                i = i + 1
            spamwriter.writerow([i,""])
            i = i + 1
        filein.close()

