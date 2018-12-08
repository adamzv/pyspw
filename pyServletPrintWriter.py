import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Spracuje html súbor do podoby využiteľnej v servletoch.\n"
                                                 "napr. out.println(\"<h1>Java PrintWriter</h1>\");")
    parser.add_argument("subor", metavar="subor", nargs=1, help="súbor, ktorého dáta sa majú spracovať")
    parser.add_argument("-w", dest="zapis")

    args = parser.parse_args()

    try:
        subor = open(args.subor[0], "r", encoding="utf8")
        zapis = open(args.zapis, "a", encoding="utf8")
    # Ak sa pri vstupe nezadá argument -w, tak hodnota atribútu args.zapis bude None
    except TypeError:
        zapis = None
    # Ak sa nenájde súbor z ktorého chceme čítať
    except FileNotFoundError:
        print("Súbor na čítanie sa nenašiel.")
        subor = None
    finally:
        # Ak sa súbor na čítanie nenašiel, ukonči program
        if subor is None:
            sys.exit(1)
        else:
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
