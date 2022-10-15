# mpc
## misceallaneous Python code


### How to compute size of Oracle database documentation

Setup python environment:

```
python3 -m pip install PyCryptodome --user
python3 -m pip install PyPDF2 --user
```

Download this git repository:

```
git clone https://github.com/pierreforstmann/mpc.git
```

Download Oracle Database 19 documentation set and unzip it:

```
wget https://docs.oracle.com/en/database/oracle/oracle-database/19/zip/oracle-database_19.zip
unzip oracle-database_19.zip
```

Run `cpp.py` to count number of PDF documents and total number of pages:
```
$ cd mpc
$ python3 cpp.py -d ../oracle-database_19_20210820
......................................................................................................................................................
total number of books: 150
total number of pages: 63437
```
