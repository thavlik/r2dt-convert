#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p data/sequences data/predictions data/output || true
python3 ./gen_seq.py > ./data/sequences/test.fa
docker run \
    --rm \
    --gpus=all \
    -v ./data:/data \
    thavlik/mxfold2:latest \
        mxfold2 predict /data/sequences/test.fa > ./data/predictions/test.fa
sed -i 's/ .*//g' ./data/predictions/test.fa
docker run \
    --rm \
    -v ./data:/data \
    --entrypoint r2dt.py \
    rnacentral/r2dt:latest \
        draw -q /data/predictions/test.fa /data/output/test
docker run \
    --rm \
    -v ./data:/data \
    thavlik/r2dt-convert:latest \
        python /convert-json.py /data/output/test/results/json/random_sequence.colored.json > data/output/test/results/json/processed.txt
