#! /bin/bash
function create(){
  source .env 
  # set up the virtual environment
  pipenv install
  pipenv shell
  python main.py $DIR
  exit
  cd $FOLDERPATH
  mkdir -p $DIR
  echo "creating $DIR"
  touch $DIR/README.md
  cd $DIR
  git init
  git add .
  git commit -m "first commit"
  git remote add origin git@github.com:$USERNAME/$DIR.git
  git push -u origin master
}
read -p "What's your repo name:" DIR
create $DIR
