### sanity check samples

```
snakemake --tibanna --use-conda --snakefile indexSnakefile \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-resources disk_mb=1000000 mem_mb=1000000 \
    --default-remote-prefix salk-tm-raw/reads \
    --configfile config/indexHap1and2andPcontigForVerification.json -p -j 1 -n


```


### Test (un)phased/(un)paired genome indexing
```
snakemake --tibanna --use-conda --snakefile Snakefile --tibanna-config root_ebs_size=16 log_bucket=salk-tm-logs --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes --configfile config/testPhased.json -p -j 1

snakemake --tibanna --use-conda --snakefile Snakefile --tibanna-config root_ebs_size=16 log_bucket=salk-tm-logs --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes --configfile config/testUnphased.json -p -j 1
```

```
(snake) [ hechen@10.7.30.227:/data1/hechen/workflows/pankmer/snakemake/soy_pangenome_operations ]$ snakemake --tibanna --use-conda --snakefile Snakefile --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes --configfile config/indexSCNphasedGenomes231120.json -p -j 1

(snake) [ hechen@10.7.30.227:/data1/hechen/workflows/pankmer/snakemake/soy_pangenome_operations ]$ snakemake --tibanna --use-conda --snakefile Snakefile --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes --configfile config/indexSCNgenomes231120.json -p -j 1

```

### test phased assembly naming convention
```
snakemake --tibanna --use-conda --snakefile indexSnakefile \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-resources disk_mb=1000000 mem_mb=500000 \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes \
    --configfile config/index_checkPhasedGenomeNamingIssue.json -p -j 1
```

### test subset
```
snakemake --tibanna --use-conda --snakefile subsetSnakefile --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes/pankmer --configfile config/testSubsetPhased.json -p -j 1

snakemake --tibanna --use-conda --snakefile subsetSnakefile \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-resources disk_mb=1000000 mem_mb=500000 \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes/pankmer -p -j 1 \
    --configfile config/testSubsetPhased2.json 

snakemake --tibanna --use-conda --snakefile subsetSnakefile \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-resources disk_mb=1000000 mem_mb=500000 \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes/pankmer -p -j 1 \
    --configfile config/subsetSCNinverseOfResistantGmax.json

```
