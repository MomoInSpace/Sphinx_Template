#!/bin/bash

tex_filepath=$1
rst_filepath=$2
file_folder=$3
pdf_filepath=$4

# cd ..
pwd
echo FilePath:
echo $pdf_filepath


# pandoc ==================================================
pandoc -s $tex_filepath -o $rst_filepath 

# make4ht ================================================
# mkdir .make4ht_tmp -p
# cd .make4ht_tmp
# cp ../.images ./ -r
# make4ht -u -x ../mytest.tex "mathml, mathjax"
# Doesn't work completley, need to debug.
# download_string = ":{download}: Download as PDF <$pdf_filepath"
base_name=$(basename ${pdf_filepath})

sed -i "5i:download:\`Download as PDF <./tex_pdf/$base_name>\`\n" $rst_filepath 
# sed -i "4a"$pdf_filepath $rst_filepath 
# bash _static/scripts/replace_regex.sh "\\(=\\+\\n\\)\\(\\n\\)" "\\1\\2\\2:{download}: Download as PDF <\\./output_pdf/NAME.pdf>" $rst_filepath 
bash _static/scripts/replace_regex.sh "\\\\mathopen{}\\\\mathclose\\\\bgroup" "" $rst_filepath 
bash _static/scripts/replace_regex.sh "\\\\aftergroup\\\\egroup" "" $rst_filepath
echo $pdf_filepath
# bash _static/scripts/replace_regex.sh "\(:Author: .*\)" "\1 \n\n :download:\`Download as PDF \<$pdf_filepath\>\`" $rst_filepath
# awk $rst_filepath "\(:Author: .*\)" "\1 \n\n :download:<$pdf_filepath>" $rst_filepath

if test "$file_folder/.images/"; then
    ebb -x $file_folder/.images/*.pdf
    ebb -x $file_dolder/./images/*.png
fi

