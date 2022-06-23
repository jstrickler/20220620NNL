from pip._internal.commands.show import print_results

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

print("Guido's the godfather of Python")
print('Guido is the "godfather" of Python')
print("Guido is the \"godfather\" of Python")

print("""Guido's the "godfather" of Python""")

president_query = """
select pr.first_name, pr.last_name, p.party
from presidents pr
join parties p = pr.party_id
order by p.party, pr.last_name
"""

#  cur.execute(president_query)
#  data = cur.fetchall()

print(president_query)
print(repr(president_query))
print("s5: {}".format(s5))

