class strandFormat:
    def format_forDNA(seq, rango, inicio, fin):
        count = 0
        vcount = 0
        finalArray = []  # this is the array that must contain the format.
        tempArray = []
        message = []
        lower = 0
        upper = 0
        try:
            inicio, fin = rango.split("-")
            inicio, fin = int(inicio), int(fin)

            strand = seq[inicio - 1: fin]

            for x in strand:
                count += 1
                vcount += 1
                tempArray.append(x)
                if count == 60 or vcount == len(strand):
                    count = 0
                    finalArray.append("".join(tempArray))
                    tempArray = []
                else:
                    continue

            for x in range(0, len(finalArray)):
                lower = upper + 1
                upper = upper + len(finalArray[x])
                if len(strand) > 60:
                    temp = f"{lower}-{strand[lower:upper+1]}-{upper}"
                    message.append(temp)

                elif len(strand) < 60:
                    temp = f"{lower}-{strand[lower:upper+1]}-{upper}"
                    message.append(temp)

                fmessage = "\n".join(message)
            lower = 0
            upper = 0
            return fmessage
        except:
            print("An error has occurred")
