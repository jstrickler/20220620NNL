#!/usr/bin/env python
import sqlite3

with sqlite3.connect("../DATA/presidents.db") as conn:  # <1>

    cursor = conn.cursor()  # <2>

    # select first name, last name from all presidents
    cursor.execute('''
        select *
        from presidents
    ''')  # <3>

    # potus: potus_id, first_name, last_name, party_id
    # parties: party_id, party_name
    # cursor.execute("""select po.first_name, po.last_name, pa.party_name from potus po join parties pa on po.party_id = pa.party_id and po.other_field = pa.other_field ...

    print("Sqlite3 does not provide a row count\n")  # <4>

    for row in cursor.fetchall():  # <5>
        print(row)
#        print(' '.join(row))  # <6>

