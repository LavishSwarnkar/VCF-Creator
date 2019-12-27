f = open("nos.txt", "r")
nos = f.read().split(",")
vcard = "BEGIN:VCARD\nVERSION:2.1\nN:;%d;;;\nFN:%d\nTEL;CELL:%s\nEND:VCARD\n"
vcf = ""
count = 1
for no in nos:
    vcf = vcf + (vcard % (count, count, no))
    count += 1
with open("out.vcf", "w") as f:
    f.write(vcf)
print("VCF created!")
