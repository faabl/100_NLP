if [ $# != 1 ]; then
    echo "ファイル名を引数に入力してください"
    exit 1
fi

file_name=$1

#
cut -f 1 -d "	" $file_name | sort    | uniq -c | sort -r 


# python 17.py | sort > ans2.txt
# diff --report-identical-files ans1.txt ans2.txt

# eval rm ans{1,2}.txt