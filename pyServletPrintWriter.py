import argparse


def main():
    parser = argparse.ArgumentParser(description="Spracuje html súbor do podoby využiteľnej v servletoch.\n"
                                                 "napr. out.println(\"<h1>Java PrintWriter</h1>\");")
    parser.add_argument("subor", metavar="subor", nargs=1, help="súbor, ktorého dáta sa majú spracovať")
    parser.add_argument("-w", dest="zapis")

    args = parser.parse_args()
    # ošetriť

    zapis = None

    subor = open(args.subor[0], encoding="utf8")

    if args.zapis is not None:
        zapis = open(args.zapis, "a", encoding="utf8")

    for line in enumerate(subor):
        line = line[1].rstrip()
        line = line.replace("\"", "\\\"")
        line = f"out.println(\"{line}\");"
        if zapis is not None:
            zapis.write(line + "\n")
        else:
            print(line)
    subor.close()

    if zapis is not None:
        zapis.close()


if __name__ == "__main__":
    main()
