output="$(python app.py testpattern.rle)"

if [ "$output" = "b2o\$2ob\$bob" ]; then
  echo "test passed"
else
  echo "test failed"
  echo "$output"
fi