FROM banno/druid-base:latest

MAINTAINER Zach Cox zach.cox@banno.com

ENTRYPOINT exec java -Ddruid.coordinator.load.timeout=PT30S $(/common-druid.sh) -Ddruid.coordinator.startDelay=PT5S -cp "/usr/local/druid/config/_common:/usr/local/druid/lib/*" io.druid.cli.Main server coordinator
