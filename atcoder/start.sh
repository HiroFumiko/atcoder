#!/usr/bin/env zsh

# オプション解析
while getopts ":b:r:g:" opt; do
  case $opt in
    b)
      contest_type="abc"
      contest_num="$OPTARG"
      ;;
    r)
      contest_type="arc"
      contest_num="$OPTARG"
      ;;
    g)
      contest_type="agc"
      contest_num="$OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# 引数のチェック
if [[ -z "$contest_type" || -z "$contest_num" ]]; then
  echo "Usage: $0 -b <contest_num> or -r <contest_num> or -g <contest_num>" >&2
  exit 1
fi

# template/sample フォルダをcontents下にコピー
cp -r ./templates/sample "./contests"

# sample フォルダをリネーム
mv "./contests/sample" "./contests/${contest_type}${contest_num}"

echo "Created ./contests/${contest_type}${contest_num} successfully."
