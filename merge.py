import PyPDF2
import os
import sys


def merge_pdfs(output_filename="merged.pdf"):
    """Merge all PDF files in the current directory into a single PDF."""

    # Find all PDF files in the current directory
    pdf_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf') and f != output_filename]

    if not pdf_files:
        print("No PDF files found in the current directory.")
        sys.exit(1)

    print(f"Found {len(pdf_files)} PDF file(s):")
    for pdf in pdf_files:
        print(f"  - {pdf}")

    # Create PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Merge all PDFs
    for filename in sorted(pdf_files):
        try:
            with open(filename, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                total_pages = len(pdf_reader.pages)
                print(f"\nProcessing: {filename} ({total_pages} pages)")

                for page_num in range(total_pages):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)

                print(f"  ✓ Added {total_pages} pages")
        except Exception as e:
            print(f"  ✗ Error processing {filename}: {e}")
            continue

    # Write the merged PDF to output file
    try:
        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)
        print(f"\n✅ Successfully merged all PDFs into '{output_filename}'")
    except Exception as e:
        print(f"\n❌ Error writing output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    merge_pdfs()
