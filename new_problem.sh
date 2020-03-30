#!/bin/bash

set -e

if [ -z "$1" ]; then
    echo 'Argument is not exists.'
    exit 1
fi

branch=$(git rev-parse --abbrev-ref HEAD)

if [ "$branch" != "master" ]; then
    echo "Please checkout master branch."
    exit 1;
fi

program_name="$1"
git checkout -b "$program_name"
cp -pr template/ "$program_name"/
git add "$program_name"
git commit -m"$program_name initialize"
code "$program_name"
echo "if you want to test, run below command"
echo "$program_name/runtest"
