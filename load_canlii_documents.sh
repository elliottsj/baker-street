#!/usr/bin/env bash

for fixture_path in baker_street/fixtures/canlii_*; do
    fixture_filename=$(basename "$fixture_path")
    fixture_name=${fixture_filename%.*}
    echo "Loading fixture: $fixture_name"
    ./manage.py loaddata "$fixture_name"
done
