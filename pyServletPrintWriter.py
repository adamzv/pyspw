import argparse


def main():
    parser = argparse.ArgumentParser(description="Spracuje html súbor do podoby využiteľnej v servletoch.\n"
                                                 "napr. out.println(\"<h1>Java PrintWriter</h1>\");")
    parser.add_argument("subor", metavar="subor", nargs=1, help="súbor, ktorého dáta sa majú spracovať")

    args = parser.parse_args()
    # ošetriť
    subor = open(args.subor[0], encoding="utf8")

    for line in enumerate(subor):
        line = line[1].rstrip()
        line = f"out.println(\"{line}\");"
        # dočasne je možný len výpis do konzoly
        print(line)

    subor.close()


if __name__ == "__main__":
    main()
