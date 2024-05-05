output="$(python app.py testinput)"

if [ "$output" = "testinput" ]; then
  echo "test passed"
else
  echo "test failed"
fi