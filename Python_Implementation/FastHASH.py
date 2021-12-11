# %%
# a function which can return consective k-mers of a string
def getK_mers(str: str, k: int) -> list:
    """
    str: a string from which k-mers have to be constructed
    k:   length of each k-mer
    """
    k_mers = []
    for i in range(len(str) - k + 1):
        k_mers.append(str[i: i + k])

    return k_mers


# %%
# loade the data from .fasta file
file = open("../Data/refgen.fasta", "r")
# reading the whole file
raw_data = file.read()

# doing data clean-up if needed
# if we find ">" at the start we need to remove this line
# this first line only for mata-data
if raw_data[0] == ">":
    # finding the end of first line by raw_data.find("\n")
    # returns the index of first match
    # keep all the string except first line
    data = raw_data[raw_data.find("\n"):]

# removing all the endline parameters from the string
# this will give a long complete string of given refrence genome
data = data.replace("\n", "")
