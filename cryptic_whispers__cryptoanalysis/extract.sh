in=cattura.pcapng
out=dumps/dump
[ -d 'dumps' ] || mkdir dumps
for stream in $(tshark -nlr $in -Y tcp.flags.syn==1 -T fields -e tcp.stream | sort -n | uniq | sed 's/\r//')
do
        echo "Stream $stream: ${out}_${stream}"
            tshark -nlr $in -qz "follow,tcp,raw,$stream" | tail -n +7 | sed 's/^\s\+//g' | xxd -r -p > ${out}_${stream}
done
