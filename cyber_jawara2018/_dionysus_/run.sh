socat -s -d -d -d TCP-LISTEN:13342,reuseaddr,fork EXEC:'./dionysus_server'
