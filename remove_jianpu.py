import sys

infile = sys.argv[1]
outfile = sys.argv[2]

begin_marker = "=== BEGIN JIANPU STAFF ==="
end_marker = "=== END JIANPU STAFF ==="

with open(infile, 'r') as f:
    lines = f.readlines()

with open(outfile, 'w') as f:
    skip = False
    for line in lines:
        if begin_marker in line:
            skip = True
        if not skip:
            f.write(line)
        if end_marker in line:
            skip = False

