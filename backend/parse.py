import pymupdf4llm
def parse_file(file_path):
    """Function to extract text from PDF and convert it to markdown using pymupdf4llm."""
    try:
        # Extract markdown formatted text from the PDF
        md = pymupdf4llm.to_markdown(file_path)
        return md
    except Exception as e:
        raise Exception(f"Error parsing the PDF: {str(e)}")