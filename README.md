# pyspw [![Build Status](https://travis-ci.org/adamzv/pyspw.svg?branch=master)](https://travis-ci.org/adamzv/pyspw)

#### Použitie:
Výpis do konzoly:

```python pyServletPrintWriter.py <nazov_suboru>```

Výpis do súboru:

```python pyServletPrintWriter.py <nazov_suboru> -w <nazov_suboru_na_zapis>```

```python pyServletPrintWriter.py <nazov_suboru> -w``` vytvorí súbor tvaru `pyspw_<datum_cas>`


Výsledok:
```out.println("<!DOCTYPE html>");
out.println("<html lang=\"en\">");
out.println("<head>");
out.println("    <meta charset=\"UTF-8\">");
out.println("    <title>Title</title>");
out.println("</head>");
out.println("<body>");
out.println();
out.println("</body>");
out.println("</html>");
```
