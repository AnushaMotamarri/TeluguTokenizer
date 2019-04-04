import sentencepiece as spm
import os
article=''
file=open('/home/anusha/pCloudDrive/thesis/dictionary/testset/03000351.txt','r',encoding='utf-8')
for line in file:
    article+=line
path1='/home/anusha/Documents/thesis/books-mag/'
x=os.listdir(path1)

for i in range(len(x)):
    x[i]=path1+x[i]

path2='/home/anusha/Documents/thesis/td/'
dirs=os.listdir(path2)  #gives years

files=[]
for dir in dirs:
    innerpath=path2+dir+'/' #creating path with years
    innerdirs=os.listdir(innerpath) #getting all sub directories in year directory
    for innerdir in innerdirs: #traversing sub dir
        npath=innerpath+innerdir+'/'
        files=os.listdir(npath)
        for i in range(len(files)):
            files[i]=npath+files[i]
        x+=files
print(len(x))
flist = ','.join(x)
spm.SentencePieceTrainer.Train(f'--input={flist} --model_prefix=Telugu_lmwholedata --vocab_size=10000')
sp=spm.SentencePieceProcessor()
sp.Load("Telugu_lmwholedata.model")
b=' '.join(sp.EncodeAsPieces(article))
print(b)
f=open('/home/anusha/pCloudDrive/thesis/tokenizer/tokenizedwholedata.txt','w+',encoding='utf-8')
f.write(b)
