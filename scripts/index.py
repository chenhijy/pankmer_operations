import time
from pankmer import index_wrapper

start = time.time()
index_wrapper(snakemake.output.index,
    genomes_input=[snakemake.input.genomes],
    genomes_input_paired=[],
    split_memory=snakemake.params.mem_split,
    threads=snakemake.params.threads,
    index='',
    k=31,
    fraction=1.0,
    gzip_level=1)
stop = time.time()
print(f'Indexed in {(stop - start) / 60:.2f} minutes')
