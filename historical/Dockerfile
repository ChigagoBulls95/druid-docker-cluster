FROM banno/druid-base:latest

MAINTAINER Zach Cox zach.cox@banno.com

ENTRYPOINT exec java $(/common-druid.sh) -Ddruid.computation.buffer.size=67108864 -Ddruid.segmentCache.locations="[{\"path\":\"/var/tmp/druid/indexCache\",\"maxSize\":5000000000}]" -Ddruid.server.maxSize=5000000000 -cp "/usr/local/druid/config/_common:/usr/local/druid/lib/*" io.druid.cli.Main server historical
