<details> 
	<summary> `getKmerConsSignalForSubRegion.sh` </summary> 
	
	```
	#!/bin/bash 
	set -beEuo pipefail
	
	# getKmerConsSignalForSubRegion.sh ${coordinates}
	
	coords=$1
	chrom=$(echo $coords | cut -d":" -f1)
	runID=241002
	
	windowSize=300
	windowSize1=50
	convertGenomePositionFormatToBEDformat.sh ${coords} | tail -n 1 > ${coords}.bed
	bedtools makewindows -b ${coords}.bed -w $windowSize | sort -k1,1 -k2,2n > ${coords}_${windowSize}bpWindows.bed
	bedtools makewindows -b ${coords}.bed -w $windowSize1 | sort -k1,1 -k2,2n > ${coords}_${windowSize1}bpWindows.bed
	
	indexesToQuery="15_MaturityGrpV_index-ANCHOREDTO-Gmax_Wm82a5softmasked_241002 17_MaturityGrpIII_index-ANCHOREDTO-Gmax_Wm82a5softmasked_241002 21_MaturityGrpIV_index-ANCHOREDTO-Gmax_Wm82a5softmasked_241002 4_MaturityGrpVIIandVIII_index-ANCHOREDTO-Gmax_Wm82a5softmasked_241002 5_MaturityGrpVI_index-ANCHOREDTO-Gmax_Wm82a5softmasked_241002 8_MaturityGrp0and00_index-ANCHOREDTO-Gmax_Wm82a5softmasked_241002 8_MaturityGrpIandII_index-ANCHOREDTO-Gmax_Wm82a5softmasked_241002"
	
	outfile=combinedRawSignal_${coords}.tsv
	outfileAveraged1=combinedRawSignal_${coords}_avgdOver${windowSize1}bpWindows.tsv
	outfileAveraged=combinedRawSignal_${coords}_avgdOver${windowSize}bpWindows.tsv
	
	rm -f $outfile
	rm -f $outfileAveraged1
	rm -f $outfileAveraged
	
	for i in $indexesToQuery; do
		id=$(echo $i | cut -d"_" -f1-2)
		intersectBed -a ${i}/${chrom}_${runID}.bdg -b ${coords}.bed | awk -v name=$id -F"\t" 'OFS="\t" {print $1, $2+1, $4, name "\n" $1, $3, $4, name}' >> $outfile
	
		intersectBed -wo -a ${i}/${chrom}_${runID}.bdg -b ${coords}_${windowSize}bpWindows.bed | awk -F"\t" 'OFS="\t" { print $5, $6, $7-1, $8, $4 * $8 }' | sort -k1,1 -k2,2n | mergeBed -i stdin -c 4,5 -o distinct,sum | awk -F"\t" -v name=$id 'OFS="\t" { print $1, $2, $5/($3-$2+1), name }' >> ${outfileAveraged}
	
		intersectBed -wo -a ${i}/${chrom}_${runID}.bdg -b ${coords}_${windowSize1}bpWindows.bed | awk -F"\t" 'OFS="\t" { print $5, $6, $7-1, $8, $4 * $8 }' | sort -k1,1 -k2,2n | mergeBed -i stdin -c 4,5 -o distinct,sum | awk -F"\t" -v name=$id 'OFS="\t" { print $1, $2, $5/($3-$2+1), name }' >> ${outfileAveraged1}
	
	done

	```

</details>

