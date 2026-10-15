#The purpose is for the user to identify a strand inside the uploaded file. 
#file is defined in main.py where the user selects the file and the path is passed to this script through file.
#DO NOT USE file for another variable name. 
def oppenFile(file):
    try:
        with open(file, 'r') as data:  # data is the name of the file variable for the reading process
            lineas = data.readlines()  # Readlines will read each line and will output an array with all the data.

            seq = "".join(lineas).replace("\n", "").upper()
            if seq.startswith(">"):
                seq = "".join(lineas[1:]).replace("\n", "").upper()
            else:
                seq = "".join(lineas).replace("\n", "").upper()
        return seq
    except Exception as e:
        return f"Error: {e}"

seqToSearch="AAATTT"

