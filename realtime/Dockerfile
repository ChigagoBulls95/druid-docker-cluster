FROM banno/druid-base:latest

MAINTAINER Zach Cox zach.cox@banno.com

ADD twitter_realtime.spec /usr/local/druid/realtime/

ENTRYPOINT exec java $(/common-druid.sh) -Ddruid.realtime.specFile=/usr/local/druid/realtime/twitter_realtime.spec -Ddruid.processing.buffer.sizeBytes=104857600 -cp "/usr/local/druid/config/_common:/usr/local/druid/lib/*" io.druid.cli.Main server realtime
