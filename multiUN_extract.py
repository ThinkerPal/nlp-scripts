#!/usr/bin/env python2.6
'''
Filename: extract.py

Extracts available file list for certain language pairs or triples and so on

Usage:
  $ python extract.py lang1 lang2 lang3

For a detailed description of this corpus, please read:

  MultiUN: A Multilingual corpus from United Nation Documents,
  Andreas Eisele and Yu Chen, LREC 2010.

Please cite the paper, if you use this corpus in your work.

'''
import os, re, sys
from xml.sax import saxutils

OUTPUT_DIR = "./text"
XMLROOT = "./xml"


LANG_CODE = {
  'Chinese': "zh",
  'Arabic': "ar",
  'French': "fr",
  'Spanish': "es",
  'Russian': "ru",
  'English': "en",
  'Other': "de",
  'German': "de"
}

LANG_NAME = {
  "zh": 'Chinese',
  "ar": 'Arabic',
  "fr": 'French',
  "es": 'Spanish',
  "ru": 'Russian',
  "en": 'English',
  "de": 'Other'
}


HELP_MESSAGE = '''Usage:\n\tpython extract.py lang1 lang2 lang3...\n\n''' \
  '''Languages: Arabic (ar), Chinese (zh), English (en), French (fr), ''' \
  '''German (de), Spanish (es), Russian (ru)'''


def warning(message):
    """Prints a warning message to stderr."""
    print >> sys.stderr, message
    sys.exit()


STAG = re.compile(r"^[ \t]*<s n=\"\d+\">[ \t]*(.*)[ \t]*</s>[ \t]*$")
TAG = re.compile(r"<[^>]*>")

# PyLint warnings:
# W: 61,27:extract_text: Unused argument 'lang'
def extract_text(filename, lang="en"):
    """Extracts available file list for the given language."""
    handle = open(filename, 'r')

    text = ""
    for line in handle:
        line = line.strip()

        if line.find("<s") >= 0:
            sentence = STAG.search(line).groups()[0] + "\n"

            if not len(sentence.strip()):
                continue

            tagged = re.findall(r"<[^>]*>[^<]*</[^>]*>", sentence)
            tag_dict = {}

            if len(tagged):
                for pos in range(len(tagged)):
                    line = tagged[pos]
                    tag_type = line.lstrip("<").split(">")[0].upper()
                    tag_type += " - " + str(pos)
                    tag_value = line.lstrip("<").split(">")[1].split("<")[0]
                    tag_dict[tag_type] = tag_value
                    sentence = sentence.replace(line, tag_type, 1)

            tok_sent = sentence.strip()

            if len(tagged):
                # PyLint warnings:
                # C: 90,20:extract_text: Invalid name "t"
                # C: 90,23:extract_text: Invalid name "l"
                # (should match [a-z_][a-z0-9_]{2,30}$)
                for t, l in tag_dict.items():
                    tok_sent = tok_sent.replace(t, l)

            text += tok_sent.strip() + "\n"

        if line.find("</p") >= 0:
            text += "\n"
    handle.close()
    return saxutils.unescape(text.strip(), {'&quot;': '"', "&apos;": "'"})


if __name__ == "__main__":
    if len(sys.argv) < 2:
        warning(HELP_MESSAGE)

    if sys.argv[1].startswith("-"):
        if sys.argv[1] == "-t":
            OUTPUT_DIR += "-test/"
            XMLROOT += "-test/"
            LANGS = sys.argv[2:]
        else:
            warning("ERROR: Unsupported option.\n" + HELP_MESSAGE)
    else:
        OUTPUT_DIR += "/"
        XMLROOT += "/"
        LANGS = sys.argv[1:]


    if len(LANGS) == 0:
        warning(HELP_MESSAGE)
    elif len(LANGS)< 2:
        warning("Indicate at least two languages!\n" + HELP_MESSAGE)


    for pos, key in enumerate(LANGS):
        if LANG_CODE.has_key(key):
            LANGS[pos] = LANG_CODE[key]
        elif not LANG_NAME.has_key(key):
            warning("%s files not found.\n" % key + HELP_MESSAGE)

    COUNT = 0
    TEXTDIR = OUTPUT_DIR + "-".join(LANGS)

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    if not os.path.exists(TEXTDIR):
        os.mkdir(TEXTDIR)

    for y in range(2000, 2100):
        year = str(y)

        if not os.path.exists(XMLROOT + "%s/%s" % (LANGS[0], year)):
            continue

        targetdir = TEXTDIR + "/" + year + '/'

        if not os.path.exists(targetdir):
            os.mkdir(targetdir)

        for _filename in os.listdir(XMLROOT + "%s/%s/" % (LANGS[0], year)):
            docid = _filename.split("/")[-1].rsplit('-', 1)[0]
            parallel = True

            for _lang in LANGS[1:]:
                altFile = XMLROOT + _lang + "/" + year + '/' + docid + "-" \
                  + _lang + ".xml"

                if not os.path.exists(altFile):
                    parallel = False
                    continue

            if not parallel:
                continue

            # sys.stderr.write(docid+"\n")
            COUNT += 1
            # extract the texts and write to new files to be aligned
            for _lang in LANGS:
                orgfile = XMLROOT + _lang + "/" + year + '/' + docid + "-" \
                  + _lang + ".xml"
                newfile = targetdir + docid + "_" + _lang + ".snt"
                nf = open(newfile, 'w')
                nf.write(extract_text(orgfile, _lang))
                nf.close()

    sys.stderr.write("%d documents in all languages.\n" % (COUNT))
