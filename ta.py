import fitz
import tabula
file="C:\\Users\\sheik jaheer\\Downloads\\Dr. Reddy’s Integrated Annual Report 2022-23_0.pdf"
# import fitz  # PyMuPDF

def extract_text_and_tables(pdf_path):
    doc = fitz.open(pdf_path)

    text_content = ""
    tables = []

    for page_num in range(doc.page_count):
        page = doc[page_num]

        # Extract text
        text_content += page.get_text()
        tables_from_page = tabula.read_pdf(pdf_path, pages=page_num + 1, multiple_tables=True, stream=True)
        tables.extend(tables_from_page)


        # # Extract images
        # for img_index, img in enumerate(page.get_images(full=True)):
        #     img_index = img_index + 1  # Image indices start from 1
        #     img_index_str = str(img_index)
        #     base_image = doc.extract_image(img[0])
        #     image_bytes = base_image["image"]

        #     image_filename = f"page_{page_num + 1}_image_{img_index_str}.png"
        #     with open(image_filename, "wb") as image_file:
        #         image_file.write(image_bytes)

        #     images.append(image_filename)

    doc.close()
    return text_content, tables

# Example usage

# text_content,tables = extract_text_and_tables(file)

# print("Text Content:", text_content)

# print("Extracted Images:", extracted_images)
from reportlab.pdfgen import canvas

def create_pdf_from_text_and_tables(text_content, output_pdf_path,tables):
    c = canvas.Canvas(output_pdf_path)

    # Set font and size
    c.setFont("Helvetica", 12)

    # Split text content into lines and add to PDF
    lines = text_content.split('\n')

    # Calculate the total number of pages needed
    # total_pages = (len(lines) + lines_per_page - 1) #lines_per_page

    # Add text to the new PDF
    c.drawString(50, c._pagesize[1] - 50, text_content)  # Adjust the coordinates as needed
    c.translate(0, -15)  # Adjust the vertical spacing as needed

    # Add tables to the new PDF
    for table_num, table in enumerate(tables):
        if table_num > 0:
            c.showPage()

        # Assume tables is a list of DataFrames from tabula-py
        for _, row in table.iterrows():
            for col_name, cell_value in row.iteritems():
                c.drawString(50, c._pagesize[1] - 50, f"{col_name}: {cell_value}")  # Adjust the coordinates as needed
                c.translate(0, -15)  # Adjust the vertical spacing as needed

    c.save()
    # c.save()

# Example usage
output_pdf_path = "C:\\Users\\sheik jaheer\\OneDrive\\Desktop\\TYNYBAY\\udbhata\\udbhata-poc-main\\op.pdf"
text_content, tables = extract_text_and_tables(file)
create_pdf_from_text_and_tables(text_content, tables, output_pdf_path)
