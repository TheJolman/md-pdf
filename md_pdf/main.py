import sys
import argparse
from pathlib import Path
import markdown
from weasyprint import HTML, CSS


def md_pdf(md_path: Path, pdf_path: Path, css_path: Path | None = None) -> None:
    with open(md_path, "r") as f:
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

    styles: list = [CSS(filename=css_path)] if css_path else []

    HTML(string=full_html).write_pdf(pdf_path, stylesheets=styles)


def main():
    parser = argparse.ArgumentParser(
        prog="md-pdf", description="Convert markdown files to PDFs."
    )

    parser.add_argument("input", type=str, help="filepath of markdown file to convert")

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="specify the output path of the PDF file",
    )

    parser.add_argument(
        "-c", "--css", type=str, help="specify the path of a CSS file to use"
    )

    args = parser.parse_args()

    input_path = Path(args.input)

    if not args.output:
        output_path = input_path.with_suffix(".pdf")
    else:
        output_path = Path(args.output)

    css_path = Path(args.css) if args.css else None

    try:
        md_pdf(input_path, output_path, css_path)
        print(f"Converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting markdown file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
