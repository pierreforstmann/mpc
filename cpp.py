#
"""
 cpp.py
 count pages in all PDF files in a given directory
 requires python 3
"""
import sys
import os
import logging
import argparse
import PyPDF2

#
def parse_arguments():
    """self explanatory"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="""directory name""")
    parser.add_argument("-v", "--verbose", action='store_true', \
                       help="""prints each PDF file name and number of pages""")
    return parser.parse_args()
#
def get_pdf_number_of_pages(filename):
    """ returns number of pages in PDF file """
    pdf_file_obj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    number_of_pages = pdf_reader.numPages
    if logging.getLogger().getEffectiveLevel() != logging.DEBUG:
        print(".", end="")
        sys.stdout.flush()
    logging.debug("{}: {} page(s)".format(filename, number_of_pages))
    pdf_file_obj.close()
    return number_of_pages
#
def count_books_and_pages():
    """ count number of PDF and number of pages for each PDF """
    args = parse_arguments()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    path = args.directory
    try:
        if path is None:
            raise Warning
        if not os.path.isdir(path):
            raise Warning
        total_pages = 0
        total_books = 0
        # dirs is the list of sub directories and is not needed in this function
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.lower().endswith("pdf"):
                    total_pages += \
                           get_pdf_number_of_pages(os.path.join(root, name))
                    total_books += 1
        print("")
        print("total number of books: {}".format(total_books))
        print("total number of pages: {}".format(total_pages))
    except Warning:
        logging.warning("You must indicate a valid directory !")


if __name__ == "__main__":
    count_books_and_pages()
