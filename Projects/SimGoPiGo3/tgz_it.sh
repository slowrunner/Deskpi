#!/bin/bash

fn="SimGoPiGo3"
if test -f $fn.tgz; then
  rm $fn.tgz
fi
mkdir $fn
cp *.py $fn
cp README.md $fn
cp -r sim $fn
tar --exclude="__pycache__" -zcvf $fn.tgz  $fn
rm -r $fn
echo "done"
