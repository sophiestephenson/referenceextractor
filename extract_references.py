import argparse
import os


def extract_references(filename):

    os.system("pdf2txt.py " + filename + " > content.txt")

    with open("content.txt", "r") as f:

        saveline = False

        references = []
        curr_reference = ""

        for line in f:

            if "Appendix" in line:
                saveline = False

            if saveline:
                if line.startswith("["):
                    if curr_reference != "":
                        references.append(curr_reference.strip("\n"))
                    curr_reference = line.strip()
                else:
                    curr_reference = curr_reference + " " + line.strip()

            if "References" in line:
                saveline = True

    with open("references.txt", "w") as out:
        for r in references:
            out.write("] ".join(r.split("] ")[1:]) + "\n")

    os.system("rm content.txt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str, required=True, help="filename")

    args = parser.parse_args()

    extract_references(args.f)
