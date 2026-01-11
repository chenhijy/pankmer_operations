def snakemain():
    chromSizeDict = snakemake.params["anchorChromSizeDict"]
    with open(snakemake.output[0], "w") as fout:
        for chrom in chromSizeDict:
            print(chrom + "\t" + str(chromSizeDict[chrom]), file=fout)

if(__name__ == "__main__"):
    snakemain()