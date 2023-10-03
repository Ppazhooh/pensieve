rm mmlogs/*
rm results/*
downlink="TMobile-UMTS-driving.down"
uplink="TMobile-UMTS-driving.up"
scheme="RL"
python real_world_run_video.py $scheme 4000 1 &
sleep 5
mm-delay 5 mm-link ../mahimahi_traces/$uplink ../mahimahi_traces/$downlink --downlink-log=mmlogs/$downlink.log ~/anaconda3/envs/py2/bin/python2.7 ../client.py &
sleep 20
killall -9 mm-link
sleep 10
# Clean up
killall -9 python2.7
killall -9 chrome