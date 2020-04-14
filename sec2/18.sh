if [ $# != 1 ]; then
    echo "ファイル名を引数に入力してください"
    exit 1
fi

file_name=$1


sort $file_name --key=3  --reverse > ans1.txt

python 18.py $file_name > ans2.txt

#同じ値があるため，比較しても異なる
diff --report-identical-files ans1.txt ans2.txt

eval rm ans{1,2}.txt