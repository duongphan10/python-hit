A = ("An", "Binh", "Nam", "Long", "Ngoc", "Tu")
B = ("Binh", "Linh", "Nam", "Hai", "Long")
A = set(A)
B = set(B)
A.discard("Tu")
B.discard("Tu")
A.add("Cuong")
C = A.union(B)
D = A.intersection(B)
E = A.difference(B)
F = A.symmetric_difference(B)
