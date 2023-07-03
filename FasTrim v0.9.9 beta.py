import os
import string
import pathlib

print("=" * 30)
print("{:^30}".format("FasTrim v0.9.9 beta"))
print("{:^30}".format('Developed by Iann Monteiro'))
print("=" * 30)

wkpcluster = input('Defina o diretório dos arquivos R1 e R2 no cluster: ')
nthreads = input('Defina o número de threads: ').strip()
slidingwindow = input('Defina o SlidingWindow: ').strip()
leading = input('Defina o Leading: ').strip()
trailing = input('Defina o Trailing: ').strip()
minlen = input('Defina o Minlen: ').strip()
avgqual = input('Defina o AVGQUAL: ').strip()
headcrop = input('Defina o HeadCrop: ').strip()

texta = 'java -jar /bio/share_bio/softwares/Trimmomatic-0.32/Trimmomatic-0.38/trimmomatic-0.38.jar PE -threads {} '.format(nthreads)
textb = 'ILLUMINACLIP:/bio/share_bio/softwares/Trimmomatic-0.32/Trimmomatic-0.38/adapters/TruSeq3-PE-2.fa:2:30:10'
textc = 'SLIDINGWINDOW:{}'.format(slidingwindow)
textd = 'LEADING:{}'.format(leading)
texte = 'TRAILING:{}'.format(trailing)
textf = 'MINLEN:{}'.format(minlen)
textg = 'AVGQUAL:{}'.format(avgqual)
texth = 'HEADCROP:{}'.format(headcrop)
exte = '.fastq.gz'

input_file = input('Informe o arquivo de entrada: ')
output_file = input('Informe o arquivo de saída: ')

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for i in infile:
        sample = i.strip()
        outfile.write(texta + wkpcluster + sample + '{}'.format(exte) + ' ' +
                      wkpcluster + sample.replace("_R1_", "_R2_") + '{}'.format(exte) + ' {}.Ptrim.fq'.format(sample) +
                      ' {}.Utrim.fq'.format(sample) + ' {}.Ptrim.fq'.format(sample.replace("_R1_", "_R2_")) +
                      ' {}.Utrim.fq'.format(sample.replace("_R1_", "_R2_")) + ' ' +
                      textb + ' ' + textc + ' ' + textd + ' ' + texte + ' ' + textf + ' ' +
                      textg + ' ' + texth + '\n\n')

print("Arquivo gerado com sucesso, obrigado por ter utilizado Fastrim")