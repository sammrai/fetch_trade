#!/bin/bash

dockerbuildcmd="ionice -c 3 docker build"
function build_image(){
    imgname=$1
    $dockerbuildcmd --tag=$imgname .
    docker push $imgname
}

function err(){
  echo "#ERROR"
  exit
}

if [ "$1" = "test" ];then
  imgname=sammrai/fetch_trade:test
  $dockerbuildcmd --tag=$imgname .
  docker run --rm $imgname --exchanges liquid bitflyer coincheck gmocoin --symbols BTC/JPY --loop 5
  # docker run --rm -u$(id -u) -v $(pwd)/data:/data $imgname --exchanges liquid bitflyer coincheck gmocoin --symbols BTC/JPY --loop 5 --out /data
  exit
fi

if [ -z "$(git status --porcelain)" ]; then
  echo "ビルドを開始します。"
else
  git status
  echo "ビルドするためには変更点をコミットする必要があります。"
  exit 1
fi

tag=`git rev-parse --short HEAD`
build_image sammrai/fetch_trade:$tag
build_image sammrai/fetch_trade:latest