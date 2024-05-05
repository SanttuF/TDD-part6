output="$(python app.py testpattern.rle)"

if [ "$output" = "b2o\$2ob\$bo!" ]; then
  echo "test passed"
else
  echo "test failed"
  echo "$output"
fi