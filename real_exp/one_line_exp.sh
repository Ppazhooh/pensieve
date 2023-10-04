rm mmlogs/*
rm results/*
downlink="TMobile-UMTS-driving.down"
uplink="TMobile-UMTS-driving.up"
scheme="RL"
server_up_time=4000
client_up_time=320
constant=10
python real_world_run_video.py $scheme $server_up_time 1 &
sleep 5
mm-delay 5 mm-link ../mahimahi_traces/$uplink ../mahimahi_traces/$downlink --downlink-log=mmlogs/$downlink.log ~/anaconda3/envs/py2/bin/python2.7 ../client.py $client_up_time &
result=$((constant + client_up_time))
sleep $result
killall -9 mm-link
killall -9 python2.7
killall -9 chrome