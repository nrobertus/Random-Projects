facts = []
f = open('catfacts.txt', 'r')
for fact in f:
    fact = fact.translate(None, "\n")
    fact = fact.replace('"', "'")
    facts.append(fact)

r = open('output.txt', 'w')
r.write("facts = [")
for fact in facts:
    r.write("\"" + fact + "\"" + ",")
r.write("]")