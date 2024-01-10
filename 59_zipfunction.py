fnames = ('Akshay', 'Chintan', 'Ashwin')
lnames = ('Patel', 'Goswami', 'Fofandi')

zipped = set(zip(fnames, lnames))

print(zipped)
# {('Akshay', 'Patel'), ('Chintan', 'Goswami'), ('Ashwin', 'Fofandi')}

for (a, b) in zipped:
    print(a, b)

# Akshay Patel
# Chintan Goswami
# Ashwin Fofandi
