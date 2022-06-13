#! /bin/bash
function create(){
  cd /home/meiqiao/test/
  mkdir -p $DIR
  echo "creating $DIR"
  touch $DIR/README.md
  cd $DIR
  git init
  git add .
}
read -p "What's your repo name:" DIR
create $DIR
