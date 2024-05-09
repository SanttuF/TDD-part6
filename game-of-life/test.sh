output="$(python app.py testpattern.rle 8)"

if [ "$output" = "bob\$2bo\$3o!" ]; then
  echo "test passed"
else
  echo "test failed"
  echo "$output"
fi