mkdir output
pandoc main.md -o output/main.json
pandoc main.md -o output/main.filtered.json --filter demo_filter.py
pandoc main.md -o output/main.pdf
pandoc main.md -o output/main.filtered.pdf --filter demo_filter.py
python -m json.tool output/main.json > temp.json && mv temp.json output/main.json
python -m json.tool output/main.filtered.json > temp.json && mv temp.json output/main.filtered.json
