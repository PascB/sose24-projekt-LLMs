import PyPDF2


def extract_text_from_pdf(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]

                text = page.extract_text()

                if text:
                    txt_file.write(text)
                    txt_file.write("\n\n")


if __name__ == "__main__":
    pdf_path = "Code\\Monster_Manual.pdf"

    txt_path = "output.txt"

    extract_text_from_pdf(pdf_path, txt_path)
    print("pdf text has been extracted and saved")
