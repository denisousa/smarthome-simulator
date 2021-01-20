python ../new_application/run.py &
python ../new_environment/run.py &
python ../new_middleware/run.py &
sleep 2
/usr/bin/firefox --new-window http://localhost:5000