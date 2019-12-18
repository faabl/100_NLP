for i in `seq 1 $n`
do
    fname=`printf child_%02d.txt $i`
    fname_test=`printf child_test_%02d.txt $i`
    diff --report-identical-files $fname $fname_test
done