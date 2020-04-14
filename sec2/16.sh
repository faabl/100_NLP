# 1行数の確認
#　各ユニットの行数

echo -n "n--> "
read n

# count=`wc -l hightemp.txt | cut -f 1 -d " "`　は何故かうまくいかない？
count=`cat hightemp.txt | wc -l`

#シェルは空白するかどうかは自由じゃない．代入とそれ以外で

unit=`expr $count / $n`
remainder=`expr $count % $n`


# 条件にて'>'は'-gt'，'<'は'-lt'
#また，条件文の最後はfiで
if [ $remainder -gt 0 ]; then
    unit=`expr $unit + 1`
fi

#split "-d"で数字の連番にする，"--additional-suffix="にて拡張子指定などできないから工夫が必要
#split --lines=$unit --numeric-suffixes=1 --additional-suffix=.txt hightemp.txt child_test_
split -l $unit  hightemp.txt child_test_

#生成ファイルの数に対するループの数
loop=0
#系列を生成する場合，{a..z}でもいけるよ.もしくは "$seq"でも可能
#　https://qiita.com/laikuaut/items/642aa329a8d214a2cccb
for i in {a..z}
do
    if test $loop -eq $n 
    then
        break
    else
        #四則演算(より一般的には算術式)は"$(( ~~_)) "の形で書かないといけないらしい
        tmp=$(($loop+1))
        echo "$tmp 回目"
        mv "child_test_a$i" "child_test_0$tmp.txt"
    fi
    #インクリーメントは'expr'より下のような書き方の方がいい．どうやら他のプロセスを立ち上げるかららしい．
    (( loop++ ))
done

#python版実行
python 16.py $n

# 検証

for i in `seq 1 $n`
do
    fname=`printf child_%02d.txt $i`
    fname_test=`printf child_test_%02d.txt $i`
    diff --report-identical-files $fname $fname_test
    
    
done

#ファイル削除
#"{}"はブレース展開というらしいが，どうやら変数をそのまま使うことはできない
#なので "eval" を使うらしい
eval rm child_0{1..$n}.txt
eval rm child_test_0{1..$n}.txt
