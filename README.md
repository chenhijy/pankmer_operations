
### subset
```
snakemake --tibanna --use-conda --snakefile subsetSnakefile \
    --tibanna-config root_ebs_size=32 log_bucket=salk-tm-logs \
    --default-remote-prefix salk-tm-dev/heidi/data1/hechen/MUsoyGenomes/pankmer \
    --configfile config/testSubsetPhased.json -p -j 1
```

### indexAndCharacterize
```
fList=Gcan_PI583945.a01.softmasked.fasta.gz,Gcyr_PI446944.a01.softmasked.fasta.gz,Gfal_PI612233.a01.softmasked.fasta.gz,Gfal_PI612234.a01.softmasked.fasta.gz,Gmax_FC32033.a01.softmasked.fasta.gz,Gmax_IA2021.a01.softmasked.fasta.gz,Gmax_IA3023.a01.softmasked.fasta.gz,Gmax_K17-6388.a01.softmasked.fasta.gz,Gmax_LD02-4485.a01.softmasked.fasta.gz,Gmax_M13-250056.a01.softmasked.fasta.gz,Gmax_MN0083.a01.softmasked.fasta.gz,Gmax_MN1511CN.a01.softmasked.fasta.gz,Gmax_PI209332.a01.softmasked.fasta.gz,Gmax_PI291293B.a01.softmasked.fasta.gz,Gmax_PI326580.a01.softmasked.fasta.gz,Gmax_PI398593.a01.softmasked.fasta.gz,Gmax_PI398595.a01.softmasked.fasta.gz,Gmax_PI398610.a01.softmasked.fasta.gz,Gmax_PI407729.a01.softmasked.fasta.gz,Gmax_PI407788A.a01.softmasked.fasta.gz,Gmax_PI408105A.a01.softmasked.fasta.gz,Gmax_PI416937.a01.softmasked.fasta.gz,Gmax_PI424078.a01.softmasked.fasta.gz,Gmax_PI437076.a01.softmasked.fasta.gz,Gmax_PI437112A.a01.softmasked.fasta.gz,Gmax_PI437654.a01.softmasked.fasta.gz,Gmax_PI438402.a01.softmasked.fasta.gz,Gmax_PI438471.a01.softmasked.fasta.gz,Gmax_PI438489B.a01.softmasked.fasta.gz,Gmax_PI438500.a01.softmasked.fasta.gz,Gmax_PI458020.a01.softmasked.fasta.gz,Gmax_PI471938.a01.softmasked.fasta.gz,Gmax_PI504288.a01.softmasked.fasta.gz,Gmax_PI518664.a01.softmasked.fasta.gz,Gmax_PI547570.a01.softmasked.fasta.gz,Gmax_PI547804.a01.softmasked.fasta.gz,Gmax_PI547830.a01.softmasked.fasta.gz,Gmax_PI548158.a01.softmasked.fasta.gz,Gmax_PI548200.a01.softmasked.fasta.gz,Gmax_PI548316.a01.softmasked.fasta.gz,Gmax_PI548359.a01.softmasked.fasta.gz,Gmax_PI548362.a01.softmasked.fasta.gz,Gmax_PI548402.a01.softmasked.fasta.gz,Gmax_PI548406.a01.softmasked.fasta.gz,Gmax_PI548445.a01.softmasked.fasta.gz,Gmax_PI548477.a01.softmasked.fasta.gz,Gmax_PI548488.a01.softmasked.fasta.gz,Gmax_PI548493.a01.softmasked.fasta.gz,Gmax_PI548542.a01.softmasked.fasta.gz,Gmax_PI548619.a01.softmasked.fasta.gz,Gmax_PI548655.a01.softmasked.fasta.gz,Gmax_PI548982.a01.softmasked.fasta.gz,Gmax_PI548986.a01.softmasked.fasta.gz,Gmax_PI549017.a01.softmasked.fasta.gz,Gmax_PI555396.a01.softmasked.fasta.gz,Gmax_PI555397.a01.softmasked.fasta.gz,Gmax_PI559932.a01.softmasked.fasta.gz,Gmax_PI561271.a01.softmasked.fasta.gz,Gmax_PI561350B.a01.softmasked.fasta.gz,Gmax_PI562374.a01.softmasked.fasta.gz,Gmax_PI567516C.a01.softmasked.fasta.gz,Gmax_PI567690.a01.softmasked.fasta.gz,Gmax_PI572239.a01.softmasked.fasta.gz,Gmax_PI578325.a01.softmasked.fasta.gz,Gmax_PI596541.a01.softmasked.fasta.gz,Gmax_PI599300.a01.softmasked.fasta.gz,Gmax_PI602492.a01.softmasked.fasta.gz,Gmax_PI602502B.a01.softmasked.fasta.gz,Gmax_PI603566.a01.softmasked.fasta.gz,Gmax_PI603713.a01.softmasked.fasta.gz,Gmax_PI612758A.a01.softmasked.fasta.gz,Gmax_PI619083.a01.softmasked.fasta.gz,Gmax_PI62202-2.a01.softmasked.fasta.gz,Gmax_PI633970.a01.softmasked.fasta.gz,Gmax_PI634193.a01.softmasked.fasta.gz,Gmax_PI639740.a01.softmasked.fasta.gz,Gmax_PI641156.a01.softmasked.fasta.gz,Gmax_PI648270.a01.softmasked.fasta.gz,Gmax_PI654356.a01.softmasked.fasta.gz,Gmax_PI667740.a01.softmasked.fasta.gz,Gmax_PI686349.a01.softmasked.fasta.gz,Gmax_PI698653.a01.softmasked.fasta.gz,Gmax_PI699632.a01.softmasked.fasta.gz,Gmax_PI699900.a01.softmasked.fasta.gz,Gmax_PI700010.a01.softmasked.fasta.gz,Gmax_PI88788.a01.softmasked.fasta.gz,Gmax_PI89772.a01.softmasked.fasta.gz,Gmax_PI90763.a01.softmasked.fasta.gz,Gmax_PI91346.a01.softmasked.fasta.gz,Gmax_U11-917032.a01.softmasked.fasta.gz,Gmax_U14-910097.a01.softmasked.fasta.gz,Gsoj_PI366122.a01.softmasked.fasta.gz,Gsoj_PI378690.a01.softmasked.fasta.gz,Gsoj_PI378695B.a01.softmasked.fasta.gz,Gsoj_PI407038.a01.softmasked.fasta.gz,Gsoj_PI407162.a01.softmasked.fasta.gz,Gsoj_PI407191.a01.softmasked.fasta.gz,Gsoj_PI407302.a01.softmasked.fasta.gz,Gsoj_PI424007.a01.softmasked.fasta.gz,Gsoj_PI424089.a01.softmasked.fasta.gz,Gsoj_PI468916.a01.softmasked.fasta.gz,Gsoj_PI479752.a01.softmasked.fasta.gz,Gsoj_PI483460B.a01.softmasked.fasta.gz,Gsoj_PI483463.a01.softmasked.fasta.gz,Gsoj_PI507580.a01.softmasked.fasta.gz,Gsoj_PI507662.a01.softmasked.fasta.gz,Gsoj_PI522226.a01.softmasked.fasta.gz,Gsoj_PI549047.a01.softmasked.fasta.gz,Gsoj_PI578337.a01.softmasked.fasta.gz,Gsoj_PI597458A.a01.softmasked.fasta.gz,Gsoj_PI597471D.a01.softmasked.fasta.gz,Gsoj_PI639590B.a01.softmasked.fasta.gz,Gsoj_PI639591.a01.softmasked.fasta.gz,Gsoj_PI639621.a01.softmasked.fasta.gz,Gste_PI546987.a01.softmasked.fasta.gz,Gste_PI547003.a01.softmasked.fasta.gz,Gsyn_PI441000.a01.softmasked.fasta.gz,Gtom_PI505203.a01.softmasked.fasta.gz,Gtom_PI505229.a01.softmasked.fasta.gz,otherAssembliesFinal/Gcyr_G1267a1.softmasked.fasta.gz,otherAssembliesFinal/Gdol_G1134a1.softmasked.fasta.gz,otherAssembliesFinal/Gfal_G1718a1.softmasked.fasta.gz,otherAssembliesFinal/Gmax_FiskebyIIIa1.softmasked.fasta.gz,otherAssembliesFinal/Gmax_KAS173-3L05a1.softmasked.fasta.gz,otherAssembliesFinal/Gmax_LeeA3.softmasked.fasta.gz,otherAssembliesFinal/Gmax_LincolnC10a1.softmasked.fasta.gz,otherAssembliesFinal/Gmax_Wm82_IGA1008.softmasked.fasta.gz,otherAssembliesFinal/Gmax_Wm82_NJAU.softmasked.fasta.gz,otherAssembliesFinal/Gmax_Wm82a5.softmasked.fasta.gz,otherAssembliesFinal/Gmax_ZH13.softmasked.fasta.gz,otherAssembliesFinal/Gsoj_W01a1.softmasked.fasta.gz,otherAssembliesFinal/Gsoj_W02a1.softmasked.fasta.gz,otherAssembliesFinal/Gsoj_W03a1.softmasked.fasta.gz,otherAssembliesFinal/Gste_G1974a1.softmasked.fasta.gz,otherAssembliesFinal/Gsyn_G1300a1.softmasked.fasta.gz,otherAssembliesFinal/Gtom_G1403a1.softmasked.fasta.gz,otherAssembliesFinal/Gmax_Wm82a6.softmasked.fasta.gz

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
