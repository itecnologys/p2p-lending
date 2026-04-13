import os
import markdown
import glob

# Template for Word-compatible HTML
html_template = """<html xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns="http://www.w3.org/TR/REC-html40">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <!--[if gte mso 9]>
    <xml>
        <w:WordDocument>
            <w:View>Print</w:View>
            <w:Zoom>100</w:Zoom>
            <w:DoNotOptimizeForBrowser/>
        </w:WordDocument>
    </xml>
    <![endif]-->
    <style>
        body {{
            font-family: Calibri, Arial, sans-serif;
            font-size: 12pt;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
{body}
</body>
</html>
"""

def convert_md_to_doc():
    md_files = glob.glob('*.md')
    if not md_files:
        print("No MD files found.")
        return

    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Convert markdown to html (including tables and extra features)
        html_body = markdown.markdown(text, extensions=['tables', 'fenced_code'])
        
        doc_filename = os.path.splitext(md_file)[0] + '.doc'
        
        final_html = html_template.format(title=os.path.basename(md_file), body=html_body)
        
        with open(doc_filename, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"Converted {md_file} to {doc_filename}")

if __name__ == '__main__':
    convert_md_to_doc()
