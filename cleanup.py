def cleanup():
    #newfile=open('raw_code.txt', 'w')
    count=0
    with open('raw_code_beauti_appendixB.txt', 'r+') as f:
        for line in f:
            count+=1
            # if count<3385:
            #     continue
            # tokens=line.split()
            # for token in tokens:
            #     if token.isdigit():
            #         print token
            #         print line

            #print line

            if line.strip().isdigit() or 'Appendix' in line or 'APPENDIX' in line:
                 print line
                 continue
            #newfile.write(line)



cleanup()