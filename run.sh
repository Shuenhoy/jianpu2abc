set -e
input=$1
name=$(basename $input .txt)

mkdir -p tmp out

jianpu-ly < in/$name.txt > tmp/$name.ly
lilypond -o out tmp/$name.ly || true
python remove_midi.py tmp/$name.ly tmp/$name.ly
lilypond -o out tmp/$name.ly || true
python remove_jianpu.py tmp/$name.ly tmp/$name.s.ly
python ly2abc/ly2abc.py tmp/$name.s.ly > out/$name.abc