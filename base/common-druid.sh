#!/bin/bash

druid_config_add(){
  echo -e -n "-D$1 "
}

echo -e -n "-server -Duser.timezone=UTC -Dfile.encoding=UTF-8 -Xmx$JAVA_MAX_HEAP -Xms$JAVA_MIN_HEAP -XX:MaxDirectMemorySize=$JAVA_MAX_DIRECT_MEMORY "

druid_config_add "druid.host=$(ip addr | grep 'eth0' | awk '{print $2}' | cut -f1  -d'/' | tail -1)"

druid_config_add "druid.port=$DRUID_PORT"

druid_config_add "druid.zk.service.host=$ZOOKEEPER_PORT_2181_TCP_ADDR"

druid_config_add "druid.metadata.storage.connector.connectURI=jdbc:postgresql://$POSTGRES_1_PORT_5432_TCP_ADDR:$POSTGRES_1_PORT_5432_TCP_PORT/druid"

