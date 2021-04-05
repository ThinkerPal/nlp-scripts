#!/bin/bash
echo -e "This requires:\n 1. Python 3 or greater\n 2.Cmake\n 3.Some brains that I do not have"
# ~/Desktop/project/data/scripts/multiunFOLDS.py

sudo chmod -R 777 ~/Desktop/project/data/act-multiun/results
echo -e "Now, we need to wait for you to check the files"
# timeout 120 /fast_align -i ~/Desktop/project/data/act-multiun/results/test_1.combined -d -o -v > ~/Desktop/project/data/act-multiun/results/train_1.align 2> ~/Desktop/project/logs/test1
# timeout 120 /fast_align -i ~/Desktop/project/data/act-multiun/results/test_2.combined -d -o -v > ~/Desktop/project/data/act-multiun/results/train_1.align 2> ~/Desktop/project/logs/test2
# timeout 120 /fast_align -i ~/Desktop/project/data/act-multiun/results/test_3.combined -d -o -v > ~/Desktop/project/data/act-multiun/results/train_1.align 2> ~/Desktop/project/logs/test3
# timeout 120 /fast_align -i ~/Desktop/project/data/act-multiun/results/test_4.combined -d -o -v > ~/Desktop/project/data/act-multiun/results/train_1.align 2> ~/Desktop/project/logs/test4
# timeout 120 /fast_align -i ~/Desktop/project/data/act-multiun/results/test_5.combined -d -o -v > ~/Desktop/project/data/act-multiun/results/train_1.align 2> ~/Desktop/project/logs/test5

echo -e "Do we continue? (Y/n)"
read -n 2 -s

# echo -e "Now, we combine the test files into a text file.\n Remember your 4 languages, src, trg, combined and reversed!\n"
# ~/Desktop/project/data/scripts/combine_into_train.py
sudo chmod -R 777 ~/Desktop/project

echo "I just realised that I need to use fast_align so imma do that real quick ok thank you"
#/fast_align -i ~/Desktop/project/data/act-multiun/results/train_1.combined -d -o -v > ~/Desktop/project/data/act-multiun/results/train_1.align 
#/fast_align -i ~/Desktop/project/data/act-multiun/results/train_1.reversed -d -o -v > ~/Desktop/project/data/act-multiun/results/train_1.revalign 
#/fast_align -i ~/Desktop/project/data/act-multiun/results/train_2.combined -d -o -v > ~/Desktop/project/data/act-multiun/results/train_2.align 
#/fast_align -i ~/Desktop/project/data/act-multiun/results/train_2.reversed -d -o -v  > ~/Desktop/project/data/act-multiun/results/train_2.revalign 
#/fast_align -i ~/Desktop/project/data/act-multiun/results/train_3.combined -d -o -v > ~/Desktop/project/data/act-multiun/results/train_3.align 
#/fast_align -i ~/Desktop/project/data/act-multiun/results/train_3.reversed -d -o -v  > ~/Desktop/project/data/act-multiun/results/train_3.revalign 
#/fast_align -i ~/Desktop/project/data/act-multiun/results/train_4.combined -d -o -v > ~/Desktop/project/data/act-multiun/results/train_4.align 
#/fast_align -i ~/Desktop/project/data/act-multiun/results/train_4.reversed -d -o -v  > ~/Desktop/project/data/act-multiun/results/train_4.revalign 
#/fast_align -i ~/Desktop/project/data/act-multiun/results/train_5.combined -d -o -v > ~/Desktop/project/data/act-multiun/results/train_5.align 
#/fast_align -i ~/Desktop/project/data/act-multiun/results/train_5.reversed -d -o -v  > ~/Desktop/project/data/act-multiun/results/train_5.revalign 


echo "First Fold"
~/Desktop/project/paper2/run_bi.sh 1 results/paper2/multiun/fold1 ~/Desktop/project/data/act-multiun/results/train_1 300 1 10 8 30
echo "Second Fold"
~/Desktop/project/paper2/run_bi.sh 0 results/paper2/multiun/fold2 ~/Desktop/project/data/act-multiun/results/train_2 300 1 10 8 30
echo "Third Fold"
~/Desktop/project/paper2/run_bi.sh 0 results/paper2/multiun/fold3 ~/Desktop/project/data/act-multiun/results/train_3 300 1 10 8 30
echo "Forth Fold"
~/Desktop/project/paper2/run_bi.sh 0 results/paper2/multiun/fold4 ~/Desktop/project/data/act-multiun/results/train_4 300 1 10 8 30
echo "Fifth Fold"
~/Desktop/project/paper2/run_bi.sh 0 results/paper2/multiun/fold5 ~/Desktop/project/data/act-multiun/results/train_5 300 1 10 8 30

echo -e "Reversing\n"
echo "First Fold"
~/Desktop/project/paper2/run_rev_bi.sh 0 results/paper2/multiun/fold1 ~/Desktop/project/data/act-multiun/results/train_1 300 1 10 8 30
echo "Second Fold"
~/Desktop/project/paper2/run_rev_bi.sh 0 results/paper2/multiun/fold2 ~/Desktop/project/data/act-multiun/results/train_2 300 1 10 8 30
echo "Third Fold"
~/Desktop/project/paper2/run_rev_bi.sh 0 results/paper2/multiun/fold3 ~/Desktop/project/data/act-multiun/results/train_3 300 1 10 8 30
echo "Forth Fold"
~/Desktop/project/paper2/run_rev_bi.sh 0 results/paper2/multiun/fold4 ~/Desktop/project/data/act-multiun/results/train_4 300 1 10 8 30
echo "Fifth Fold"
~/Desktop/project/paper2/run_rev_bi.sh 0 results/paper2/multiun/fold5 ~/Desktop/project/data/act-multiun/results/train_5 300 1 10 8 30

echo -e 'Bivec is now complete! Next, would be training for fastText\n\n\n\n'
# fasttext skipgram -input /project/data/europarl/results/train_1 -output /project/results/paper1/europarl/fold1
# fasttext skipgram -input /project/data/europarl/results/train_2 -output /project/results/paper1/europarl/fold2
# fasttext skipgram -input /project/data/europarl/results/train_3 -output /project/results/paper1/europarl/fold3
# fasttext skipgram -input /project/data/europarl/results/train_4 -output /project/results/paper1/europarl/fold4
# fasttext skipgram -input /project/data/europarl/results/train_5 -output /project/results/paper1/europarl/fold5
