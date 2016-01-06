start = 13
end = 1000000
maxterms = 1
num_maxterms = 0
dict_terms = {}

for i in range(start, end+1):
    n = i
    terms = 1
    while n > 1:
        if n in dict_terms:
            terms += dict_terms[n]-1
            break
        if n%2==0:
            n //= 2
            #print(n)
        else:
            n = (3*n)+1
            #print(n)
        terms += 1
    dict_terms[i] = terms
    #print("start: {}, terms: {}".format(i, terms))
    if terms > maxterms:
        num_maxterms = i
        maxterms = terms
        
print("{} has the maximum of {} terms".format(num_maxterms, maxterms))
#print(dict_terms)