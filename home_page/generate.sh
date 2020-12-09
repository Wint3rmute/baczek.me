#!/bin/bash

PAGE_FILES_DIR="./home_page/pages"
PAGE_FILES_GLOB="$PAGE_FILES_DIR/*.html"

TEMPLATES_FOLDER="./home_page/templates"
TEMPLATE_HEAD="$TEMPLATES_FOLDER/head.html"
TEMPLATE_TAIL="$TEMPLATES_FOLDER/tail.html"

for src_file in $PAGE_FILES_GLOB
do
    echo $src_file
    output_dir=$(basename $src_file)
    echo $output_dir

    cat $TEMPLATE_HEAD $src_file $TEMPLATE_TAIL | tidy \
        -indent \
        --indent-spaces 2 \
        -quiet \
        --tidy-mark no > $output_dir #\ 
        # $output_dir
done