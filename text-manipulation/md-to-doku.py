#!/usr/bin/env python3

"""
This is a janky script to convert (my opinionated) Markdown to Dokuwiki syntax.
"""

import re
import subprocess
from sys import stdin

__VERSION__ = '1.0.0'


# how many spaces are in your indentations
INDENT_SPACE = 4

COMMENT_ESC = "<>>@@@<<>"
AST_ESC = "<>>|||<<>"
SLASH_ESC = "<>>~~~<<>"


class TextStash:
    def __init__(self):
        self.index = 0
        self.blocks = {}
    
    def freeze(self, block):
        block_name = f"<>>STASH{self.index}<<>"
        self.blocks[block_name] = block
        self.index += 1
        return block_name
    
    def thaw(self, txt):
        for key, value in self.blocks.items():
            txt = txt.replace(key, value)
        return txt

def pbcopy(txt):
    task = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE, close_fds=True)
    task.communicate(input=txt.encode('utf-8'))

def indent_size(spaces):
    indents = int(len(spaces) / INDENT_SPACE)
    doku_indent = '  ' * indents
    return doku_indent

def convert_header(match_obj):
    if len(match_obj.groups()) < 2: return None
    base_header = 7
    header_count = match_obj.group(1).strip()
    header_level = base_header - len(header_count)
    header = "=" * header_level
    return f"{header} {match_obj.group(2)} {header}"

def convert_code_block(match_obj):
    # def escape_pound(mo):
    #     # return mo.replace("#", "<.>>__<<.>")
    #     return COMMENT_ESC
    lang = match_obj.group(1)
    code = match_obj.group(2).strip()
    # 'escape' # comments so they don't get converted to Doku headers
    # code = re.sub(r"^#+", escape_pound, code, flags=re.M)
    # escape markdown in code blocks
    # code = code.replace('#', COMMENT_ESC)
    # code = code.replace('*', AST_ESC)
    # code = code.replace('/', SLASH_ESC)
    if lang:
        # return f"<code {lang}>\n{code}\n</code>"
        code_block = f"<code {lang}>\n{code}\n</code>"
    else:
        code_block = f"<code>\n{code}\n</code>"
    # return f"<code>\n{code}\n</code>"
    return TXT_STASH.freeze(code_block)

def convert_inline_code(match_obj):
    # this theoretically matches code block comments with in-line code.
    # i'm not sure this is needed now that i'm stashing code blocks. it
    # shouldn't hurt to keep, either.
    if match_obj.group(0).startswith(COMMENT_ESC):
        return match_obj.group(0)
    stash_name = TXT_STASH.freeze(match_obj.group(2))
    return f"{match_obj.group(1)} ''{stash_name}'' {match_obj.group(3)}"

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
    if list_str.strip().startswith('-'):
        list_str = list_str.replace('- ', '* ')
    doku_indent = indent_size(list_str.split('* ')[0])
    # indent_len = len(list_str.split('* ')[0])
    # space_count = int(indent_len / 4 * 2)
    # spaces = ' ' * space_count
    # return f"  {spaces}{list_str.strip()} "
    return f"  {doku_indent}{list_str.strip()} "

def convert_no_lists(match_obj):
    indent = match_obj.group(1)
    if not indent: return "  -"
    indent = indent.replace('\t', ' ' * INDENT_SPACE)
    doku_indent = indent_size(indent)
    return f"  {doku_indent}-"


TXT_STASH = TextStash()
MD_DOC = stdin.read()

#
# Most of these conversions are run in a specific order to prevent converting
# the wrong thing. e.g. i want to convert ***bold italic text*** before **bold
# text** before *italic text*.
#

# convert code blocks
MD_DOC = re.sub(r"```(\w*)((.|\n)+?)```", convert_code_block, MD_DOC, flags=re.M)

# convert headers
MD_DOC = re.sub(r"(^#+) (.+)", convert_header, MD_DOC, flags=re.M)

# horizontal breaks
MD_DOC = re.sub(r"^[- *]{3,}$", '----', MD_DOC, flags=re.M)

# convert inline code
MD_DOC = re.sub(r"(.*)`(.+?)`(.*)", convert_inline_code, MD_DOC)

# convert bold-italic
MD_DOC = re.sub(r"\*{3}(.+?)\*{3}", convert_bold_italic, MD_DOC, flags=re.M|re.S)

# escape bold
MD_DOC = re.sub(r"\*{2}(.+?)\*{2}", esc_bold, MD_DOC, flags=re.M|re.S)

# convert italics
MD_DOC = re.sub(r"\*{1}(.+?)\*{1}", convert_italic, MD_DOC, flags=re.M|re.S)

# convert links – [[link|text]]
MD_DOC = re.sub(r"\[(.+?)\]\((.+?)\)", convert_links, MD_DOC, flags=re.M)

# convert lists (- and *)
MD_DOC = re.sub(r"^ *- ", convert_lists, MD_DOC, flags=re.M)
MD_DOC = re.sub(r"^ *\* ", convert_lists, MD_DOC, flags=re.M)

# convert numbered lists ('0.')
MD_DOC = re.sub(r"^([\t ]*)(\d+\.)", convert_no_lists, MD_DOC, flags=re.M)

# convert escaped comment # back to #
MD_DOC = MD_DOC.replace(COMMENT_ESC, '#')

# unescape bold and italics
MD_DOC = MD_DOC.replace(AST_ESC, "*")
MD_DOC = MD_DOC.replace(SLASH_ESC, "/")

MD_DOC = TXT_STASH.thaw(MD_DOC)

pbcopy(MD_DOC)
