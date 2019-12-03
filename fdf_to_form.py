"""
This program dumps fdf data to form
"""
import os
import sys
import argparse

def final_step():
    """
    function to give the output file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_file", help="display a square of a given number",
                        type=str)
    parser.add_argument("fdf_file", help="display a square of a given number",
                        type=str)
    args = parser.parse_args()
    print("PDF File:" + args.pdf_file)
    print("FDF File:" + args.fdf_file)
    os.system('pdftk "' + args.pdf_file + '" fill_form "' + args.fdf_file +
              '" output "output.pdf" flatten')  #command give the output


def main():
    """
    calling the function
    """
    final_step()
    print("done")

if __name__ == '__main__':
    sys.exit(main())
