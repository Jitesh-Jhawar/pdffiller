
import sys
import json
import pprint
from fdfgen import forge_fdf
import PyPDF2
import argparse

def func2():
   
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_file", help="display a square of a given number",
                        type=str)
    parser.add_argument("json_file", help="display a square of a given number",
                        type=str)
    args = parser.parse_args()
    print("PDF File:" + args.pdf_file)
    print("JSON File:" + args.json_file)
    prettyp = pprint.PrettyPrinter(indent=4)
    r_json = json.loads(open(args.json_file).read())
    prettyp.pprint(r_json)  
    pdfread = PyPDF2.PdfFileReader(open(args.pdf_file, 'rb'), strict=False)  
    dictfields = pdfread.getFields()
    prettyp.pprint(dictfields)  
    r_list = list(dictfields.keys())  
    i = 0
    for value in r_list:
        print(str(i) + " " + value)
        i += 1

    i = 0
    for value in dictfields:
        dictfields[value]=r_list[i]
        i += 1
    print(dictfields)
    fields = [(dictfields['Your_Last_Name'], r_json['lastName']),
              (dictfields['Your_First_Name'], r_json['firstName']),
              (dictfields['Date'], r_json['date']),
              (dictfields['CheckBox1'], 'Yes'),
              (dictfields['CheckBox2'], 'Yes'),
              (dictfields['CheckBox3'], 'Yes'),
              (dictfields['CheckBox4'], 'Yes'),
              (dictfields['CheckBox5'], 'Yes'),
              ]  
    fdf = forge_fdf("", fields, [])  
    fdf_file = open("data.fdf", "wb")
    fdf_file.write(fdf)  
    fdf_file.close()


def main():
    func2()
    prettyp = pprint.PrettyPrinter(indent=4)
    prettyp.pprint("Created fdf file")

if __name__ == '__main__':
    sys.exit(main())
