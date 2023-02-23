#!/bin/bash

if [[ $# -eq 0 ]]
then
    echo "At least one argument required. Use 'serve' to run the server"
    exit 0
fi

mkdir build

echo "Importing config..."
cp accelerator-web-ui-template/config.toml build/baseconfig.toml
cp config.toml build/config.toml
cp -R content build/

echo "Importing themes..."
git submodule update --init --recursive
mkdir build/themes
cp -R accelerator-web-ui-template/themes/hugo-theme-learn build/themes/
cp -R accelerator-web-ui-template/layouts build/
cp -R accelerator-web-ui-template/static build/
cp -R accelerator-web-ui-template/data build/
cd build

echo "Creating Hugo site..."
HUGO_COMMAND="hugo"
if [ $1 = "serve" ]
then
    echo 'Will start Hugo server'
    HUGO_COMMAND="$HUGO_COMMAND server"
fi

if [ $# -eq 3 ]
then
$HUGO_COMMAND --config baseconfig.toml,config.toml --gc --minify -d ../public$2 -b $3
elif [ $# -eq 2 ]
then
$HUGO_COMMAND --config baseconfig.toml,config.toml --gc --minify -d ../public$2
else
$HUGO_COMMAND --config baseconfig.toml,config.toml --gc --minify -d ../public
fi
cd ..
rm -r build
