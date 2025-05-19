import sys
import argparse
import markdown
from weasyprint import HTML


def convert_markdown_to_pdf(input_file, output_file):
    with open(input_file, "r") as f:
        markdown_content = f.read()

    html_content = markdown.markdown(markdown_content)

    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    HTML(string=full_html).write_pdf(output_file)


def main():
    parser = argparse.ArgumentParser(
        prog="md-pdf",
        description="Convert markdown files to PDFs."
    )
    parser.add_argument(
        "input",
        type=str,
        help="filepath of markdown file to convert"
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="specify the output path of the PDF file",
    )

    args = parser.parse_args()
    if not args.input:
        return

    if not args.output:
        output_file = f"{args.input[:-2]}pdf"
    else:
        output_file = args.output

    try:
        convert_markdown_to_pdf(args.input, output_file)
        print(f"Converted {args.input} to {output_file}")
    except Exception as e:
        print(f"Error converting markdown file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
