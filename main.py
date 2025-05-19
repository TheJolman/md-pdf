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
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        type=str,
        default=None,
        help="filepath of markdown file to convert"
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="specify the output path of the PDF file",
    )

    args = parser.parse_args()
    if args.output:
        input_file = "test.md"
        convert_markdown_to_pdf(input_file, args.output)


if __name__ == "__main__":
    main()
    # argc = len(sys.argv)
    # if argc not in [2, 3]:
    #     print("Usage: ./compile input.md")
    #     print("Or:    ./compile input.md output.pdf")
    #     sys.exit(1)
    #
    # input_file = sys.argv[1]
    #
    # if len(input_file) < 4 or not input_file.endswith('.md'):
    #     print("Invalid markdown file name")
    #     sys.exit(1)
    #
    # if argc == 3:
    #     output_file = sys.argv[2]
    #     if len(output_file) < 5 or not output_file.endswith('.pdf'):
    #         print("Invalid pdf file name")
    #         sys.exit(1)
    # else:
    #     output_file = f"{input_file[:-2]}pdf"
    #
    # try:
    #     convert_markdown_to_pdf(input_file, output_file)
    #     print(f"Converted {input_file} to {output_file}")
    # except Exception as e:
    #     print(f"Error converting file: {str(e)}")
    #     sys.exit(1)
