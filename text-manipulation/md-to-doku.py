#!/usr/bin/env python3

"""
This is a janky script to convert Markdown to Dokuwiki syntax.

TODO: convert numbered lists
"""

import re
import subprocess
from sys import stdin

COMMENT_ESC = "<.>>__<<.>"
AST_ESC = "<.>>|||<<.>"
SLASH_ESC = "<.>>~~~<<.>"


def pbcopy(txt):
    task = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE, close_fds=True)
    task.communicate(input=txt.encode('utf-8'))

def convert_header(match_obj):
    if len(match_obj.groups()) < 2: return None
    base_header = 7
    header_count = match_obj.group(1).strip()
    header_level = base_header - len(header_count)
    header = "=" * header_level
    return f"{header} {match_obj.group(2)} {header}"

def convert_code_block(match_obj):
    def escape_pound(mo):
        # return mo.replace("#", "<.>>__<<.>")
        return COMMENT_ESC
    lang = match_obj.group(1)
    code = match_obj.group(2).strip()
    # 'escape' # comments so they don't get converted to Doku headers
    code = re.sub(r"^#+", escape_pound, code, flags=re.M)
    if lang:
        return f"<code {lang}>\n{code}\n</code>"
    return f"<code>\n{code}\n</code>"

def convert_inline_code(match_obj):
    if match_obj.group(0).startswith(COMMENT_ESC):
        return match_obj.group(0)
    return f"''{match_obj.group(1)}''"

def convert_bold_italic(match_obj):
    return f"{AST_ESC}{AST_ESC}{SLASH_ESC}{SLASH_ESC}{match_obj.group(1)}{SLASH_ESC}{SLASH_ESC}{AST_ESC}{AST_ESC}"

def convert_italic(match_obj):
    return f"{SLASH_ESC}{SLASH_ESC}{match_obj.group(1)}{SLASH_ESC}{SLASH_ESC}"

def esc_bold(match_obj):
    return f"{AST_ESC}{AST_ESC}{match_obj.group(1)}{AST_ESC}{AST_ESC}"

def convert_links(match_obj):
    # [[link|text]]
    return f"[[{match_obj.group(2)}|{match_obj.group(1)}]]"

def convert_lists(match_obj):
    list_str = match_obj.group(0)
    print(list_str)
    if list_str.strip().startswith('-'):
        list_str = list_str.replace('- ', '* ')
    indent_len = len(list_str.split('* ')[0])
    space_count = int(indent_len / 4 * 2)
    spaces = ' ' * space_count
    return f"  {spaces}{list_str.strip()} "


MD_DOC = stdin.read()

# convert code blocks
MD_DOC = re.sub(r"```(\w*)((.|\n)+?)```", convert_code_block, MD_DOC, flags=re.M)

# convert headers
MD_DOC = re.sub(r"(^#+) (.+)", convert_header, MD_DOC, flags=re.M)

# convert inline code
MD_DOC = re.sub(r".*`(.+?)`.*", convert_inline_code, MD_DOC)

# convert escaped comment # back to #
MD_DOC = MD_DOC.replace(COMMENT_ESC, '#')

# convert bold-italic
MD_DOC = re.sub(r"\*{3}(.+?)\*{3}", convert_bold_italic, MD_DOC, flags=re.M|re.S)

# escape bold
MD_DOC = re.sub(r"\*{2}(.+?)\*{2}", esc_bold, MD_DOC, flags=re.M|re.S)

# convert italics
MD_DOC = re.sub(r"\*{2}(.+?)\*{2}", convert_italic, MD_DOC, flags=re.M|re.S)

# unescape bold and italics
MD_DOC = MD_DOC.replace(AST_ESC, "*")
MD_DOC = MD_DOC.replace(SLASH_ESC, "/")

# convert links – [[link|text]]
MD_DOC = re.sub(r"\[(.*)\]\((.*)\)", convert_links, MD_DOC, flags=re.M)

# convert lists (- and *)
MD_DOC = re.sub(r"^ *- ", convert_lists, MD_DOC, flags=re.M)

pbcopy(MD_DOC)
