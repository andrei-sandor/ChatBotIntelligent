import tabula
from tabulate import tabulate
import PyPDF2


def reader_schuedule(input_file, page_schedule, list_weeks):

    # reads table from pdf file
    df_schedule = tabula.read_pdf(input_file, page_schedule)  # address of pdf file

    result_string = ""

    for i in list_weeks:
        result_partial = "For week " + i + ", the topic is " + df_schedule["Topics"][i] + " presented by " + df_schedule["Presenter"][i] " and the tutorial is " +df_schedule["Tutorial"][i]
        result_string += result_partial + "\n"
    return result_string

#import camelot

#table = camelot.read_pdf("Outline.pdf")
#print(table[0].df)

# importing all the required modules

def give_page_from_info(message):
    page1 = ["Class Schedule", "Instructor", "TA's", "Course Calendar Information"]
    page2 = ["Evaluation and Assessment", "Suggested Readings"]
    page4 = ["Policies"]

    # creating a pdf reader object
    reader = PyPDF2.PdfReader('Outline.pdf')

# print the text of the first page
    if message.contains(page1):
        first_page = reader.pages[0]
        output1_pdf = PyPDF2.PdfWriter()
        output1_pdf.addPage(first_page)
        output1_pdf.write("p1Outline")
        return "p1"

    if message.contains(page2):
        second_page = reader.pages[1]
        output2_pdf = PyPDF2.PdfWriter()
        output2_pdf.addPage(second_page)
        output2_pdf.write("p2Outline")
        return "p2"

    if message.contains(page4):
        fourth_page = reader.pages[3]
        output4_pdf = PyPDF2.PdfWriter()
        output4_pdf.addPage(fourth_page)
        output4_pdf.write("p4Outline")
        return "p4"


def encrypted(admin_password):
    to_encrypt = PyPDF2.PdfWriter()
    to_encrypt.appendPagesFromReader("Outline.pdf")
    to_encrypt.encrypt(user_password=admin_password)

    to_encryptA1 = PyPDF2.PdfWriter()
    to_encryptA1.appendPagesFromReader("A1.pdf")
    to_encryptA1.encrypt(user_password=admin_password)

    to_encryptA2 = PyPDF2.PdfWriter()
    to_encryptA2.appendPagesFromReader("A2.pdf")
    to_encryptA2.encrypt(user_password=admin_password)
    return True
