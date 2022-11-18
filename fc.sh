FOLDERLIST=$(python3 check_ignore.py)
LEDIT=$(stat -f %Z $FOLDERLIST)
while true
do
  FOLDERLIST=$(python3 check_ignore.py)
  CEDIT=$(stat -f %Z $FOLDERLIST)
  if [[ "$CEDIT" != "$LEDIT" ]]; then
    echo "===== RUN PYTHON COMMAND ====="
    python3 test.py
    LEDIT=$CEDIT
  fi
  sleep 0.5
done