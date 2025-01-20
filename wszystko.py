import subprocess


subprocess.run(['python', 'tabele.py']) #tworzenie pustych tabel
subprocess.run(['python', 'category_fill.py']) #wypełnanie tabeli kategorii
subprocess.run(['python', 'database_filler_template.py']) #wypełnianie pozostałych tabel

#kompilacja raportu
#try:
    #subprocess.run(['Rscript', '-e', 'rmarkdown::render("raport_team03.Rmd")'])
#except:
    #pass
