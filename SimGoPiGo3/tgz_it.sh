#!/bin/bash

fn="SimulatedGoPiGo3"
if test -f $fn.tgz; then
  rm $fn.tgz
fi
mkdir $fn
cp *.py $fn
cp README.md $fn
tar -zcvf $fn.tgz $fn
rm -r $fn
echo "done"
