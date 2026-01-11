
### subset
```
snakemake --tibanna --use-conda --snakefile subsetSnakefile \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes/pankmer \
    --configfile config/testSubsetPhased.json -p -j 1
```

### indexAndCharacterize
```
snakemake --tibanna --use-conda --snakefile indexAndCharacterizeSnakefile \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-resources disk_mb=500000 mem_mb=1000000 \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes \
    --config \
        genomes=${fList} \
        outdir=pankmer/137panGlycine_k25_241002 \
        outputID=137panGlycine_k25 \
        k=25 \
        threads=128 \
        rounds=1 \
    -p -j 5 -k -n &>> logs/indexAndCharact137panGlycinek25.json

```

### anchorRegion
```
snakemake --tibanna --use-conda --snakefile anchorRegionSnakefile \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes \
    --default-resources disk_mb=100000 mem_mb=128000 \
    --configfile config/anchorMaturityGroups.json -p -j 100 &>> logs/anchorMatGroupsWm82a5
```
