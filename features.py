import sys
import os

import nltk
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords
ct = nltk.tokenize.casual_tokenize


def gen_ftr(input_loc="clean_enron", output_loc="stopwords.f"):
    def counter(text, auth, counts):
        tokens = ct(text ,preserve_case=False) # reduce_len = ?

        for token in tokens:
            try:
                counts[auth][token] += 1
            except:
                pass
        return counts

    def store(output_loc, labels, counts):
        formatted = ["%s, %s, %s\n" % labels,]
        for auth in counts.keys():
            for token in counts[auth].keys():
                count = counts[auth][token]
                formatted.append( "%s, %s, %s\n" % (auth, token, count) )
        
        out = open(output_loc, 'w')
        out.writelines(formatted)
        out.close()

    sw = stopwords.words('english')

    tree = os.walk(input_loc)
    dirs = next(tree)[1]
    # print(dirs)

    counts = {}
    for auth in dirs:
        if auth not in counts.keys():
            counts[auth] = dict( zip(sw, [0]*len(sw)) )

        subd = next(tree)
        root = subd[0]
        files = subd[2]
        for f in files:
            if f[0] == '.':
                continue

            mail = open("%s/%s" % (root, f), 'r', encoding='latin-1')
            
            text = mail.read()
            counts = counter(text, auth, counts)
            
            mail.close()
    
    store(output_loc, ('author', 'stopword', 'count'), counts)
    return counts

if __name__=="__main__":
    try:
        print(gen_ftr(sys.argv[1], sys.argv[2]))
    except:
        print(gen_ftr())
    exit()