rm mmlogs/*
rm results/*
downlink=$2
uplink=$3
scheme=$1
server_up_time=4000
client_up_time=$4
constant=10
~/anaconda3/envs/py2/bin/python2.7  real_world_run_video.py $scheme $server_up_time 1 &
sleep 5
mm-delay $5 mm-link /d1/mahakcont/traces/$uplink /d1/mahakcont/traces/$downlink --downlink-log=mmlogs/$downlink.log --uplink-queue=droptail --uplink-queue-args="packets=$6" --downlink-queue=droptail --downlink-queue-args="packets=$6" ~/anaconda3/envs/py2/bin/python2.7 ../client.py $client_up_time $scheme &
result=$((constant + client_up_time))
sleep $result
killall -9 mm-link
killall -9 python2.7
killall -9 chrome