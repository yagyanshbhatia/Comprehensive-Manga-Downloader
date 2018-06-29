from os import listdir
from os.path import isfile, join
from fpdf import FPDF

mypath = "/home/yagyansh/Desktop/boruto"
onlyfiles = [(f) for f in listdir(mypath) if isfile(join(mypath, f))]

def natural_keys(text):
    c = text.split(".")[0];
    return int(c)

onlyfiles.sort(key=natural_keys)

pdf = FPDF()
for image in onlyfiles:
    pdf.add_page()
    pdf.image(mypath + '/'+ image,0,0,w=210,h=297)

pdf.output("boruto.pdf", "F")